# Nghiệm thu sửa đúng phạm vi P08 bằng PDF gốc

PyMuPDF 1.26.7 chạy trong môi trường cô lập. Đối chiếu 25/25 SHA-256 với manifest trước khi đọc. Trang trong bản ghi là trang vật lý 1-based. Tọa độ dùng point trong trang gốc. Khi đoạn văn chuyển cột, lưu các mảnh bằng chứng tương ứng trên cùng trang. Những hàng số của R0048 mà text layer bỏ qua được đọc trực quan từ Table III. Không ghi đè bản Gemini hoặc sửa các khóa đã PASS.

| Tiêu chí | Batch 01 | Batch 02 |
|---|---|---|
| A1. Phạm vi | PASS. 43/43 khóa F01–F43, 13/13 mã báo cáo, 0 khóa trùng. | PASS. Hai trường đích R0059 và R0062. Một trường R0059 được tách thành ba nhóm bằng chứng. |
| A2. Trang, mục và bằng chứng | PASS trong phạm vi sửa. 43/43 khóa có trang vật lý, mục và vùng bằng chứng. R0010 F18 được đánh dấu NOT_REPORTED sau khi kiểm sáu trang và mục Acknowledgement. | PASS trong phạm vi sửa. R0062 p6 giữ dấu xấp xỉ. R0059 có vị trí nguồn riêng ở p7, p8 và p10 cho overhead, model switching và model partitioning tương ứng. |
| A3. Số liệu và giới hạn | PASS trong phạm vi sửa. 8/8 khóa số liệu có giá trị, đơn vị, workload, điều kiện và mẫu số hoặc baseline phù hợp. F13 và F22–F24 tách đoạn theo cột. F25 và F41–F43 dẫn đúng ô, hàng và cột. Không mang cấu hình thử nghiệm khác vào các hàng bảng. | PASS trong phạm vi sửa. R0062 ghi khoảng 2 FPS khi một UAV không sẵn sàng. R0059 phân biệt số byte ước tính với hai phép so sánh latency, mỗi phép giữ baseline và điều kiện riêng. |
| A4. Tích hợp và nghiệm thu toàn batch | FAIL. Sổ sửa đủ 43 khóa nhưng chưa được áp vào bộ 13 báo cáo và chưa kiểm ngữ nghĩa tất cả dữ kiện còn lại của bản trích xuất ghép. 0/13 khóa ở cấp báo cáo. | FAIL. Hai trường lỗi đã có bản sửa, còn cần tích hợp vào bộ 12 báo cáo và kiểm ngữ nghĩa tập ghép. 0/12 khóa ở cấp báo cáo. |
| A5. Giữ bằng chứng và truy vết | PASS. Bản Gemini thô, receipt timeout, bản kiểm và nhật ký xóa chat vẫn còn. Các sửa đổi nguồn lưu riêng. | PASS. Giữ nguyên R0074, R0121, C04-06 và phát biểu định tính về phục hồi giai đoạn 3. Công việc sửa nguồn này thực hiện cục bộ, không phát sinh chat mới. |

Kết quả sửa theo khóa được lưu trong `scoped_pdf_repairs.json`. Đây là đầu vào cho lượt hợp nhất và nghiệm thu P08, chưa phải bảng trích xuất dùng cho tổng hợp. P09 chưa mở.
