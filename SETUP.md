# Cài đặt slam-nav-arxiv

## Phân chia công việc (tiết kiệm quota)
| Khâu | Chạy ở đâu | Chi phí |
|---|---|---|
| Query arXiv theo 7 topic, phân trang, retry | GitHub Actions (`fetch_arxiv.py`) | Free |
| Lọc trùng giữa các topic và với các tuần trước | GitHub Actions | Free |
| Chấm điểm liên quan bằng regex theo `config.yaml` | GitHub Actions | Free |
| Thống kê số bài/topic, so với TB 4 tuần | GitHub Actions | Free |
| Cắt còn top 40 bài + abstract rút gọn → `digest/latest.md` | GitHub Actions | Free |
| Đọc digest, nhận định xu hướng, chọn bài phải đọc, cảnh báo trùng hướng | Claude (scheduled task, thứ Hai) | Quota LLM |

Claude chỉ đọc ~1 file digest (~10–15k token) mỗi tuần thay vì hàng trăm abstract.

## Lịch
- Chủ nhật 20:00 (giờ VN): GitHub Action fetch + build digest, commit vào repo.
- Thứ Hai 07:43: Claude phân tích và gửi báo cáo.

## Các bước
1. Tạo repo **public** `slam-nav-arxiv` trên GitHub (public để Claude đọc được không cần token,
   và Actions free không giới hạn phút).
2. Push toàn bộ thư mục này lên nhánh `main`.
3. Settings → Actions → General → Workflow permissions → chọn **Read and write permissions**.
4. Tab Actions → "Weekly arXiv SLAM/Nav digest" → **Run workflow** để chạy lần đầu, kiểm tra
   `digest/latest.md` được tạo.
5. Chỉnh `research_profile.md` khi hướng NCS thay đổi; chỉnh `config.yaml` để thêm/bớt keyword.

## Chạy local
```bash
pip install -r requirements.txt
python fetch_arxiv.py                 # gọi arXiv thật
python fetch_arxiv.py --date 2026-11-15   # giả lập ngày chạy
```
Lưu ý: `README.md` do script tự sinh mỗi tuần — ghi chú cài đặt để ở file này.
