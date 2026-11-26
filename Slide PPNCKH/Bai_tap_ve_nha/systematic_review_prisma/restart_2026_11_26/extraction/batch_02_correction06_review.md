# Nghiệm thu P08 Batch 02, correction 06

UUID `432bbd73-3594-440b-a7a2-104f1804e2a3`, context `aedec5c1-d3fa-4e6a-8c1e-cf79afa5be61`. Gemini.app nhận một lần, lưu đủ đáp án rồi xóa chat. Bridge ghi New chat trống lúc 2026-11-26T23:22:19+07:00. Giữ raw nguyên vẹn; chỉ nối 3 dòng marker và payload khi phân tích cú pháp.

| Tiêu chí | Kết luận | Bằng chứng |
|---|---|---|
| A1 | PASS | 3/3 khóa, 3/3 báo cáo, 3/3 bằng chứng truy cập thân bài, 0 trùng hoặc ngoài phạm vi. |
| A2 | FAIL | 18/19 trích đoạn khớp trang. K02 có một trích đoạn bắt đầu cuối trang vật lý 16 và tiếp tục ở 17 nhưng khai toàn bộ là trang 17. |
| A3 | PASS | K01 loại đủ 3 tỷ lệ chỉ dẫn abstract; K02 ghi đúng phạm vi các phương pháp chạy được theo mục 4.2 và Figure 4; K03 tách 9 phát biểu có vị trí thân bài. Lỗi độ chính xác của giá trị K03 nằm ở A4. |
| A4 | FAIL | K03 có 1 trường số ghi giá trị chính xác trong khi nguồn trang vật lý 6 ghi xấp xỉ. |
| A5 | PASS | 3/3 dòng dữ liệu JSON đúng schema, marker và danh sách khóa khớp sau chuẩn hóa xuống dòng; 1 Task cha, 3/3 ID phân công một lần, 0 worker khai sử dụng. |

| Trường | Kết luận độc lập | Chi tiết |
|---|---|---|
| R0068 / K01 | PASS | 8/8 trích đoạn khớp trang; 3/3 tỷ lệ loại khỏi kết quả. Chỉ diễn giải “accuracy” ở VI-B.1 trong nghĩa tuân thủ ràng buộc theo trang 11. |
| R0074 / K02 | FAIL | Đọc trực quan Figure 4, trang 16, xác nhận các nhóm không chạy được. Trang 17 nêu các phương pháp phân tán chạy được. Cần trích riêng phần thực sự nằm trên trang 17. |
| R0121 / K03 | FAIL | 9/9 locator khớp văn bản, nhưng trường giá trị của kết quả xấp xỉ 40 lần làm mất mức chính xác được công bố. |

Toàn correction 06 giữ cách ly vì A2 và A4 FAIL. Chốt cấp Batch 02 vẫn FAIL, 0/12 báo cáo được nhận. Kiểm tra lại còn phát hiện trường kết quả kế thừa R0062 bỏ dấu xấp xỉ ở giai đoạn 2, mặc dù hai khóa số liệu correction 05 đã PASS. Trường kết quả R0062 không nằm trong ba trường được phép sửa ở lượt này. Không thay đổi các khóa đã PASS. Chưa thực hiện P09.
