# Nghiệm thu P08 Batch 01, Task mới sau preflight

UUID `d9b919ae-f917-43ef-a656-9a8dbff893f6`, context `37102fe6-f984-4cd3-8fe0-1e06b0ac93fc`. Bridge hết 300 giây sau một lần gửi. Thu lại cùng UUID bằng hai snapshot chỉ đọc khớp đáp án 96.107 ký tự, 1 thư mục đính kèm. Giữ riêng receipt timeout và đáp án khôi phục. Sau khi lưu đáp án, helper Confirm một lần và xác minh New chat trống. Task cũ `45ae7459-5ef3-4d84-a315-7fecce8d3dfb` giữ nguyên.

| Tiêu chí | Kết luận | Bằng chứng |
|---|---|---|
| A1 | PASS | 13/13 ID và metadata khớp bảng khóa, 0 ID/DOI/tiêu đề trùng. |
| A2 | FAIL | 182/182 trường. 160/195 trường quan sát hoặc kiểm vắng có locator/trích đoạn khớp cơ học; 35 lỗi. |
| A3 | FAIL | 33 mục số liệu, 32 OBSERVED, 8/32 thiếu thành phần bắt buộc hoặc nguồn khớp. |
| A4 | FAIL | Cả 13/13 báo cáo có ít nhất một lỗi A2 hoặc A3; chưa hoàn tất xác minh ngữ nghĩa các mục khác. 0/13 báo cáo qua cổng. |
| A5 | PASS | 13/13 locator PDF đúng đường dẫn và trích đoạn khớp sau tiêu đề I. INTRODUCTION trên trang vật lý 1; 13/13 file SHA-256 khớp; 0 không đọc được; 13/13 ID được phân công đúng một lần; schema kết thúc và danh sách ID khớp. |

Việc truy cập đã được xác minh; tồn đọng là nghiệm thu nội dung trích xuất. Chi tiết 43 lỗi cơ học ghi theo ID và trường trong JSON nghiệm thu. Chỉ chuẩn bị đính chính đúng khóa lỗi sau công việc Batch 02 đã giao; giữ nguyên dữ liệu chưa nghiệm thu trong vùng cách ly.
