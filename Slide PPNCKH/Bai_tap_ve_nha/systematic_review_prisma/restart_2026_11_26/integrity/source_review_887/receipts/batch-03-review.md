# Gemini · Kiểm tra lô 03

Task `75ad9323-c83b-4789-811c-db233aa69cf2`, context `351798a4-24ea-4531-acbc-33be8e1e9f54`.
Trạng thái bridge `TASK_STATE_FAILED`. Bắt đầu 2026-11-27T13:44:05.084+00:00, kết thúc 2026-11-27T13:59:07.173+00:00.

| Tiêu chí | Kết quả | Minh chứng |
| --- | --- | --- |
| Hash đầu vào và đầu ra bridge | PASS | Đối chiếu manifest và biên nhận. |
| Neo kiểm tra đọc PDF | PASS | HKF-118, PDF tr. 2. |
| Khóa chính xác và dấu kết thúc | PASS | 112/112 dòng. 0 lỗi cấu trúc hoặc khóa. |
| Nhận diện thư mục học thuật | PASS | 6/6 dòng nhận diện, 0 DOI trùng, 0 tiêu đề trùng. |
| Neo nguồn hoặc khoảng trống rõ | FAIL | 92 neo khớp đủ; 0 ghi khoảng trống; 20 cần chỉnh. |
| Đủ căn cứ cho toàn bộ kết luận | FAIL | Qua 72, một phần 34, không qua 6, chưa kiểm 0. |

Kết quả lô giữ ở trạng thái tham khảo. Việc khớp neo chưa xác nhận nội dung của phán định.
