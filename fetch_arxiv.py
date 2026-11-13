#!/usr/bin/env python3
"""
slam-nav-arxiv — fetch bài mới từ arXiv theo topic, lọc trùng, chấm điểm liên quan,
xuất digest gọn cho LLM đọc. Toàn bộ khâu này chạy free trên GitHub Actions, không tốn quota LLM.

Output:
  data/papers.jsonl          kho tất cả bài đã thấy (khóa = arXiv id không version)
  data/weekly_stats.json     số bài/topic theo tuần (để nhận định xu hướng)
  digest/<YYYY-Www>.md       digest tuần (top N theo điểm) — Claude đọc file này
  digest/latest.md           bản sao digest tuần mới nhất
  digest/latest.json         toàn bộ bài mới tuần này (kèm điểm), để tra cứu
  README.md                  bảng tổng quan
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
GH_RE = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+", re.I)


# ---------------------------------------------------------------- fetch
def build_query(filters, categories, start, end):
    terms = [f'all:"{f}"' if " " in f or "-" in f else f"all:{f}" for f in filters]
    q = "(" + " OR ".join(terms) + ")"
    if categories:
        q += " AND (" + " OR ".join(f"cat:{c}" for c in categories) + ")"
    q += f" AND submittedDate:[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]"
    return q


def parse_feed(xml_text):
    root = ET.fromstring(xml_text)
    out = []
    for e in root.findall("a:entry", NS):
        raw_id = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1]
        if not raw_id:
            continue
        pid = re.sub(r"v\d+$", "", raw_id)
        title = " ".join(e.findtext("a:title", "", NS).split())
        abstract = " ".join(e.findtext("a:summary", "", NS).split())
        comment = " ".join((e.findtext("arxiv:comment", "", NS) or "").split())
        authors = [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)]
        cats = [c.get("term") for c in e.findall("a:category", NS)]
        code = GH_RE.findall(abstract + " " + comment)
        out.append({
            "id": pid,
            "title": title,
            "authors": authors,
            "published": e.findtext("a:published", "", NS)[:10],
            "updated": e.findtext("a:updated", "", NS)[:10],
            "abstract": abstract,
            "comment": comment,
            "categories": cats,
            "url": f"https://arxiv.org/abs/{pid}",
            "code": code[0].rstrip(".") if code else None,
        })
    return out


def fetch_topic(name, filters, categories, start, end, max_results, delay):
    query = build_query(filters, categories, start, end)
    papers, page = [], 100
    for offset in range(0, max_results, page):
        params = {"search_query": query, "start": offset, "max_results": page,
                  "sortBy": "submittedDate", "sortOrder": "descending"}
        for attempt in range(4):
            try:
                r = requests.get(API, params=params, timeout=60,
                                 headers={"User-Agent": "slam-nav-arxiv/1.0"})
                r.raise_for_status()
                batch = parse_feed(r.text)
                break
            except Exception as ex:  # arXiv thỉnh thoảng trả 503 / feed rỗng
                print(f"  [{name}] retry {attempt+1}: {ex}", file=sys.stderr)
                time.sleep(delay * (attempt + 2))
        else:
            batch = []
        papers += batch
        time.sleep(delay)
        if len(batch) < page:
            break
    print(f"  [{name}] {len(papers)} papers")
    return papers


# ---------------------------------------------------------------- score
def compile_scoring(cfg):
    rules = []
    for w, pats in cfg["scoring"].items():
        for p in pats:
            rules.append((float(w), p, re.compile(p, re.I)))
    return rules


def score_paper(p, rules, cfg):
    s, hits = 0.0, []
    for w, pat, rx in rules:
        m_t = rx.search(p["title"])
        m = m_t or rx.search(p["abstract"])
        if m:
            s += w * (cfg["title_multiplier"] if m_t and w > 0 else 1)
            label = m.group(0).lower()
            hits.append(label if w > 0 else f"-{label}")
    if p.get("code"):
        s += cfg["code_bonus"]
    ctx = cfg.get("context_required")
    if ctx and s > 0 and not re.search(ctx, p["title"] + " " + p["abstract"], re.I):
        s *= cfg.get("no_context_factor", 0.3)
        hits.append("-no-robot-context")
    return round(s, 1), hits


# ---------------------------------------------------------------- io
def load_db(path):
    db = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                p = json.loads(line)
                db[p["id"]] = p
    return db


def save_db(path, db):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(db.values(), key=lambda p: (p["published"], p["id"]), reverse=True)
    path.write_text("".join(json.dumps(p, ensure_ascii=False) + "\n" for p in rows), encoding="utf-8")


def iso_week(d):
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def trend_table(stats, week, topics):
    weeks = sorted(stats)
    prev = [w for w in weeks if w < week][-4:]
    lines = ["| Topic | Tuần này | TB 4 tuần trước | Δ |", "|---|---:|---:|---:|"]
    for t in topics:
        now = stats.get(week, {}).get(t, 0)
        avg = sum(stats[w].get(t, 0) for w in prev) / len(prev) if prev else None
        if avg is None:
            lines.append(f"| {t} | {now} | – | – |")
        else:
            d = (now - avg) / avg * 100 if avg else 0
            lines.append(f"| {t} | {now} | {avg:.1f} | {d:+.0f}% |")
    return "\n".join(lines), len(prev)


def write_digest(cfg, week, new, stats, topics, out_dir):
    ranked = sorted(new, key=lambda p: p["score"], reverse=True)
    top = [p for p in ranked if p["score"] >= cfg["digest_min_score"]][: cfg["digest_top_n"]]
    rest = [p for p in ranked if p not in top]
    table, nprev = trend_table(stats, week, topics)
    n = cfg["abstract_max_chars"]

    md = [f"# Digest arXiv SLAM/Navigation — {week}",
          f"_Tạo lúc {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC · {len(new)} bài mới · "
          f"{len(top)} bài điểm cao nhất bên dưới (ngưỡng ≥ {cfg['digest_min_score']})_", "",
          "## Số bài theo topic", table,
          "" if nprev else "_Chưa đủ lịch sử để so sánh (cần vài tuần chạy)._", "",
          "## Bài điểm cao (đọc kỹ)"]
    for i, p in enumerate(top, 1):
        ab = p["abstract"] if len(p["abstract"]) <= n else p["abstract"][:n].rsplit(" ", 1)[0] + " …"
        au = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        md += [f"### {i}. {p['title']}",
               f"- **{p['id']}** · {p['published']} · score {p['score']} · topics: {', '.join(p['topics'])}",
               f"- {au}",
               f"- match: {', '.join(p['hits'][:8])}",
               f"- {p['url']}" + (f" · code: {p['code']}" if p.get("code") else ""),
               *( [f"- comment: {p['comment'][:160]}"] if p.get("comment") else [] ),
               f"> {ab}", ""]
    md += ["## Các bài còn lại (chỉ tiêu đề)"]
    md += [f"- [{p['score']}] {p['title']} — {p['id']}" for p in rest[:150]]
    if len(rest) > 150:
        md.append(f"- … và {len(rest) - 150} bài khác (xem digest/latest.json)")

    out_dir.mkdir(parents=True, exist_ok=True)
    text = "\n".join(md) + "\n"
    (out_dir / f"{week}.md").write_text(text, encoding="utf-8")
    (out_dir / "latest.md").write_text(text, encoding="utf-8")
    (out_dir / "latest.json").write_text(json.dumps(
        {"week": week, "count": len(new), "papers": ranked}, ensure_ascii=False, indent=1), encoding="utf-8")
    return top, table


def write_readme(path, week, top, table, total):
    md = ["# slam-nav-arxiv", "",
          "Tự động cập nhật mỗi tuần các bài arXiv mới về SLAM / Localization / Navigation / Semantic maps, "
          "lọc và chấm điểm theo `research_profile.md` + `config.yaml`. Digest đầy đủ: "
          "[`digest/latest.md`](digest/latest.md).", "",
          f"**Cập nhật: {week}** · tổng số bài trong kho: {total}", "", "## Số bài theo topic", table, "",
          "## Top 15 tuần này", "| # | Score | Title | Code |", "|---:|---:|---|---|"]
    for i, p in enumerate(top[:15], 1):
        code = f"[link]({p['code']})" if p.get("code") else ""
        md.append(f"| {i} | {p['score']} | [{p['title'].replace('|', '/')}]({p['url']}) | {code} |")
    path.write_text("\n".join(md) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--date", help="ngày chạy giả lập YYYY-MM-DD (mặc định hôm nay UTC)")
    ap.add_argument("--offline", help="thư mục chứa <topic>.xml giả lập thay vì gọi arXiv (để test)")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    today = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(dt.timezone.utc).date()
    start = today - dt.timedelta(days=cfg["lookback_days"])
    week = iso_week(today)
    topics = list(cfg["topics"])
    print(f"Week {week}: {start} → {today}")

    db_path = ROOT / "data" / "papers.jsonl"
    db = load_db(db_path)
    rules = compile_scoring(cfg)

    fetched = {}
    for name, t in cfg["topics"].items():
        if args.offline:
            f = Path(args.offline) / f"{re.sub(r'[^A-Za-z]+', '_', name)}.xml"
            batch = parse_feed(f.read_text(encoding="utf-8")) if f.exists() else []
        else:
            batch = fetch_topic(name, t["filters"], t.get("categories", cfg.get("categories")),
                                start, today, cfg["max_results_per_topic"], cfg["request_delay_sec"])
        for p in batch:
            if p["id"] in fetched:
                fetched[p["id"]]["topics"].append(name)
            else:
                p["topics"] = [name]
                fetched[p["id"]] = p

    new = []
    for pid, p in fetched.items():
        if pid in db:
            db[pid]["topics"] = sorted(set(db[pid]["topics"]) | set(p["topics"]))
            continue
        p["score"], p["hits"] = score_paper(p, rules, cfg)
        p["first_seen"] = week
        db[pid] = p
        new.append(p)

    stats_path = ROOT / "data" / "weekly_stats.json"
    stats = json.loads(stats_path.read_text()) if stats_path.exists() else {}
    stats[week] = {t: sum(t in p["topics"] for p in new) for t in topics}
    stats[week]["_total_new"] = len(new)
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(json.dumps(stats, indent=1, sort_keys=True))

    save_db(db_path, db)
    top, table = write_digest(cfg, week, new, stats, topics, ROOT / "digest")
    write_readme(ROOT / "README.md", week, top, table, len(db))
    print(f"New: {len(new)} · in digest: {len(top)} · total db: {len(db)}")


if __name__ == "__main__":
    main()
