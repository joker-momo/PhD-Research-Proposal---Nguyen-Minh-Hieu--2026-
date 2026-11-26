# Bước 10 — Nghiệm thu batch_01

Đối chiếu lúc 2026-11-26T21:39:30+07:00. Gemini.app Task 3aa69dac-912e-434b-9299-081e633a2d05, context 3cca8a7e-0e00-46bf-846e-89be1826076c. Cầu nối bắt đầu 2026-11-26T14:26:35.667+00:00, kết thúc 2026-11-26T14:38:54.619+00:00.

| Tiêu chí | Kết quả | Bằng chứng kiểm tra |
|---|---|---|
| A1 | PASS | 25/25 ID và siêu dữ liệu khớp bảng P06, 0 ID/DOI/tiêu đề trùng. |
| A2 | FAIL | 25/25 trích đoạn định danh và 26/26 trích đoạn chính của 13 cặp khớp. Chỉ 3/4 trích đoạn bổ sung khớp. R0003–R0059 support_b không khớp ở trang 3 hoặc trang PDF nào. |
| A3 | PASS | Đủ 3/3 cặp ưu tiên, 13 cặp khác nhau, 0 đề xuất gộp. |
| A4 | PASS | 0 ca provider báo chưa phân giải hoặc thiếu nguồn; trạng thái 25/25 khớp với các cặp đã trả. Các thông tin ngoài quyết định liên kết chưa được đưa vào dữ liệu. |
| A5 | PASS | Receipt xác nhận Gemini.app Task dùng đúng thư mục gốc. Lấy lại kết quả từ cùng UUID, khớp hai lần đọc. 25/25 PDF khớp SHA-256, 0 thay đổi ngoài baseline. Việc xóa chat chưa xác nhận, đã xác nhận tháo thư mục. |

Cách ly kết quả trước khi sử dụng. Trích đoạn cần sửa thuộc R0059, trường support_b của cặp R0003–R0059, PDF trang 3 mục 2. Biên bản transport timeout và kết quả gốc khôi phục bằng đúng task ID được lưu riêng. Không có quyết định nào được nhập vào bảng chính ở checkpoint này.
