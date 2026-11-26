# P08 batch 01 — kết quả cách ly

- Nghiệm thu lúc `2026-11-26T22:24:27+07:00`. Gemini.app Task `45ae7459-5ef3-4d84-a315-7fecce8d3dfb`, context `95008ecd-0b4a-40e7-81b8-9a2ea67a77e4`, message `hk261-restart-step11-p08-batch01-v1`.
- Trạng thái vận chuyển `TASK_STATE_COMPLETED` lúc `2026-11-26T15:23:40.460+00:00`. Backend dùng trực tiếp thư mục dự án. Ứng dụng chưa xác nhận xóa chat. Phạm vi direct_project không có checksum cho cả thư mục.
- Gemini báo client PDF tool ngừng khả dụng sau lượt đầu và worker không truy cập được thư mục Mac. 13 PDF vẫn có tại canonical workspace và 13/13 hash khớp khi Codex kiểm trước khi gửi. Đây là lỗi truy cập của phiên Gemini, không phải thiếu PDF trong dự án.

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 | PASS | 13/13 report/study ID và metadata khớp đầu vào. ID, DOI và tên trùng đều 0. |
| A2 | FAIL | 182/182 trường đúng cấu trúc nhưng toàn bộ `NOT_ACCESSIBLE`. Có 0/13 PDF được Gemini mở và 0 dữ kiện có trang/trích đoạn để kiểm. |
| A3 | PASS | 0 số liệu đề xuất, 0 số liệu thiếu đơn vị hoặc điều kiện được nhận. Không có bằng chứng định lượng để tổng hợp. |
| A4 | FAIL | Codex đối chiếu được bản PDF lưu của 13 báo cáo, song có 0 dữ kiện do Gemini trích để xác minh. Batch không cung cấp trích xuất toàn văn. |
| A5 | PASS | 13/13 nêu lý do truy cập; 0 trường biến lỗi truy cập thành `NOT_REPORTED`; 0 nhận định lấy từ abstract. |

**Kết quả: REJECTED.** Chấp nhận 0/13 báo cáo trích xuất. Giữ nguyên raw và task UUID. Theo chỉ đạo mới nhất, không gửi lại 13 ID này. Batch 02 chỉ bao gồm 12 ID chưa giao.
