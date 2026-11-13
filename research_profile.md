# Research profile — Huy (NCS Cơ điện tử, ĐH Bách khoa Hà Nội)

> Claude đọc file này mỗi tuần để đánh giá mức liên quan. Hướng nghiên cứu thay đổi thì sửa file này,
> không cần sửa scheduled task. Muốn đổi bộ lọc keyword thì sửa `config.yaml`.

## Hướng NCS (đang định hình, hạn nộp hồ sơ 30/11/2026)
- Khoảng trống tích hợp AI–robotics cho SLAM / localization / navigation trong nhà:
  dùng hiểu ngữ cảnh (semantic, vision-language) **hỗ trợ** stack cổ điển, không phải deep SLAM end-to-end.
- Ba trọng tâm: (1) semantic localization, (2) chẩn đoán & phục hồi lỗi (failure diagnosis/recovery,
  localization monitoring), (3) an toàn & đánh giá kiến trúc lai trên thiết bị edge.
- Ý tưởng khung: graph-SLAM nền Cartographer + visual-language map (kiểu VLMaps) →
  giám sát localization, debug navigation, lệnh ngôn ngữ tự do (cả tiếng Việt), vận hành dài hạn,
  sau đó thêm tay máy (mobile manipulation).
- Demo mục tiêu: lấy cốc ở lab mang tới phòng họp tầng khác, đi qua thang máy.
- Fallback: cobot → chỉ mobile; language actions → VLMaps tiếng Việt; môi trường động → tĩnh.

## Bài báo đang viết (đóng góp sẽ đưa vào luận án)
1. AprilTag + 2D LiDAR fusion: LiDAR hiệu chỉnh khoảng cách tag–camera khi tag ở xa (PnP sai lớn từ ~2 m),
   cung cấp ràng buộc landmark/fixed-pose cho SLAM. Có vấn đề phụ: PnP flip ambiguity ở tầm gần.
2. Auto-tune tham số Nav2 (costmap, controller, planner).

## Bối cảnh kỹ thuật
- Kinh nghiệm thực tế: AMR công nghiệp (Cartographer, ROS 2 Humble, nhà máy/kho), thấy mislocalization
  hiếm nhưng có trong vận hành dài hạn, tránh vật cản yếu, vấn đề tầng FMS.
- Không còn dữ liệu/môi trường thật của công ty → ưu tiên dataset/benchmark public, sim, và robot tự dựng.
- Phần cứng tầm trung (edge, Jetson/RPi) → quan tâm phương pháp chạy được on-device.

## Ưu tiên khi đánh giá
- Cao: bài có thể làm baseline / so sánh / trích dẫn trực tiếp; dataset hoặc benchmark dùng được;
  bài có code; bài trùng ý tưởng (cần biết sớm để định vị đóng góp).
- Thấp: xe tự lái ngoài trời, UAV, legged/humanoid, deep SLAM thuần không gắn stack cổ điển.
