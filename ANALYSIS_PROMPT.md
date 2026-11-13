# Hướng dẫn phân tích hàng tuần (Claude đọc file này mỗi lần chạy)

## Đầu vào (chỉ đọc 2 file này, KHÔNG đọc data/papers.jsonl)
1. `research_profile.md` — hướng NCS và bối cảnh của Huy.
2. `digest/latest.md` — bảng số bài theo topic + top bài đã được lọc/chấm điểm sẵn bằng keyword.
   Kiểm tra dòng tiêu đề: nếu tuần trong digest cũ hơn tuần hiện tại > 1 tuần thì báo GitHub Action
   có thể đã lỗi, và vẫn phân tích digest đang có.

## Ngân sách (tiết kiệm quota)
- Không tìm kiếm web diện rộng. Chỉ được mở tối đa 3 trang arXiv (abs/HTML) cho những bài
  "Phải đọc" khi abstract không đủ để đánh giá.
- Điểm keyword chỉ là gợi ý sơ bộ; được phép hạ/nâng mức liên quan dựa trên hiểu nội dung.

## Đầu ra — báo cáo tiếng Việt, ngắn gọn, đọc trong 5 phút
1. **TL;DR** (3 dòng): tuần này có gì đáng chú ý nhất với Huy.
2. **Xu hướng** (3–5 gạch đầu dòng): dựa trên bảng số bài + nội dung top bài — chủ đề nào nóng lên,
   kỹ thuật nào lặp lại (VD: VLM cho localization, 3DGS-SLAM, scene graph…). Nói rõ khi số liệu
   còn quá ít tuần để kết luận.
3. **Phải đọc** (tối đa 3 bài): mỗi bài ghi — vì sao liên quan (gắn với trọng tâm nào trong profile),
   dùng được thế nào (baseline / dataset / trích dẫn / ý tưởng / đối thủ trùng hướng), có code không.
4. **Đáng lướt** (tối đa 5 bài): 1 dòng mỗi bài.
5. **Cảnh báo trùng hướng**: bài nào làm gần giống bài báo AprilTag+LiDAR, auto-tune Nav2, hoặc khung
   graph-SLAM + visual-language map — nếu không có thì ghi "Không có".
6. **Gợi ý hành động** (1–2 ý): VD thêm bài X vào related work, thử dataset Y, cân nhắc chỉnh đề cương.
Mỗi bài kèm link arXiv. Cuối báo cáo: một dòng gợi ý chỉnh `config.yaml` nếu thấy bộ lọc sót/nhiễu.
