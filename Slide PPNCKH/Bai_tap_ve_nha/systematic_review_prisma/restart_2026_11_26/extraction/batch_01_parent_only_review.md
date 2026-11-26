# Nghiệm thu Batch 01 — sửa 43 khóa trong một Task cha

UUID `fa4c883e-442b-416a-8818-5f468013ec4c`, context `8e54a1f8-55cc-4cd6-ad5a-62e5cdbb27df`. Bridge hết thời gian chờ. Đã giữ receipt transport và thu lại 36.790 ký tự từ cùng UUID bằng hai snapshot chỉ đọc khớp SHA-256 `6e8b2297b801371cb8eec97dce23dbf2df879ff5886eedcfdd23c2c34e439263`. Nhật ký ghi đúng một lần gửi. Sau khi lưu kết quả, helper kiểm lại UUID và nội dung, Confirm một lần rồi xác minh New chat trống.

| Tiêu chí | Kết luận | Bằng chứng |
|---|---|---|
| A1 | PASS | 43/43 dòng đúng ID/nhãn, gồm 35 FIELD và 8 NUMBER, 0 khóa trùng hay ngoài phạm vi. |
| A2 | FAIL | 13/13 PDF được Gemini báo đã đọc. Cổng trích đoạn truy cập kèm đề mục đúng trang xác minh 2/13. Cổng so khớp trích đoạn các khóa xác minh 39/43; 4 lỗi tại F13, F22–F24. Các đoạn khác nhau hai cột có thể sai ở thứ tự trích văn bản, vì vậy số này chỉ là đo cơ học. |
| A3 | FAIL | 8/8 dòng NUMBER có trường số liệu. F41–F43 dẫn câu dẫn nhập Table III mà không trích hàng/ô số liệu. F13 và F22–F24 cần locator đúng chính xác theo nguồn. F25 dẫn câu giới thiệu bảng; trang 6 có ô 0.0090 theo VGG-16 với I=5, nhưng đoạn trả về chưa neo chính ô. |
| A4 | PASS | 43/43 dòng parse được và đúng schema, danh sách khóa nhất quán. Gemini báo 0 unresolved; Codex cách ly các điểm chưa xác minh, không nhập vào bảng P08. |
| A5 | PASS | 1 Task cha, 1 lần gửi, 43/43 khóa gán cho parent, 0 worker theo metadata tự khai, 0 đề xuất thay đổi khóa ngoài danh sách. |

Batch 01 chưa đạt. Kết quả mới cho bằng chứng có thể truy cập trong Task cha nhưng chưa qua cổng chính xác nguồn và độ hẹp của phát biểu. Giữ dữ kiện đã PASS từ trước. Không xem 39 so khớp cơ học là 39 khóa đã nghiệm thu khoa học. Có 0/13 báo cáo khóa vào bảng P08.
