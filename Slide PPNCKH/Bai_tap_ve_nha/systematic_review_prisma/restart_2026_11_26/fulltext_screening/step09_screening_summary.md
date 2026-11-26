# Bước 09 — Sàng lọc toàn văn theo P06

Hoàn tất đối chiếu lúc 2026-11-26T21:24:09+07:00 theo [kế hoạch đã duyệt](../approved_plan.md) và [tiêu chí P03/P06](../protocol_restart.md). Đầu vào là 44 PDF đã xác minh tại [bước 08](../fulltext_retrieval/fulltext_identity_index.csv). Bước 08 có 137 báo cáo cần tìm và 93 báo cáo chưa lấy được toàn văn. 93 hồ sơ đó vẫn ở bước truy xuất.

| Batch | Đã sàng lọc | INCLUDE | EXCLUDE | AWAITING_CLASSIFICATION | Nghiệm thu |
|---|---:|---:|---:|---:|---|
| 01 | 11 | 11 | 0 | 0 | [5/5 PASS](batch_01_review.md) |
| 02 | 11 | 9 | 2 | 0 | [5/5 PASS](batch_02_review.md) |
| 03 | 11 | 4 | 3 | 4 | [5/5 PASS](batch_03_review.md) |
| 04 | 11 | 1 | 8 | 2 | [5/5 PASS](batch_04_review.md) |
| Tổng | 44 | 25 | 13 | 6 | 4/4 đạt |

Đẳng thức hạch toán **44 = 25 + 13 + 6**. Đối chiếu 44/44 ID và SHA-256 với danh sách đã khóa. Mỗi báo cáo bị loại có đúng một lý do chính theo thứ tự P06. Các tiêu chí chưa xác minh được lưu kèm phần nguồn đã kiểm tra.

Gemini.app Task đánh giá toàn văn trong thư mục dự án. Codex kiểm lại bằng chứng, cách áp dụng tiêu chí và quyết định trước khi nhận từng batch. Đây là quy trình sàng lọc có AI hỗ trợ. Các số đếm ở đây là số báo cáo. Bước 10 mới đối chiếu phiên bản và xác định số nghiên cứu.

- [Quyết định, trang, mục và nguồn cho toàn bộ 44 báo cáo](fulltext_screening.csv)
- [Danh sách loại toàn văn, lý do chính và lý do phụ](exclusions.csv)
- [Các trường hợp chờ phân loại](awaiting_classification.csv)
