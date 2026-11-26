# P08 batch 02 — kết quả cách ly và sửa có mục tiêu

- Nghiệm thu lúc `2026-11-26T22:33:12+07:00`. Gemini.app Task cha `e891c230-d182-4bfa-8068-1cba64226569`, context `4f40fa22-61e6-4859-bb80-5f1d80ae1d2b`. Bridge trả `TASK_STATE_FAILED` tại `2026-11-26T15:26:52.553+00:00` vì có hai cửa sổ. Một lần gửi được ghi trong nhật ký bridge.
- Hai lần đọc chỉ đọc từ đúng cửa sổ có UUID và đính kèm đúng tên dự án trả cùng một đáp án có cặp marker hoàn chỉnh. Bản thu riêng không thay thế trạng thái bridge. SHA-256 hai snapshot lần lượt `d66495395c9392385cd8ff98fcb77f7c97abdea4dcd4e925f32ccd61a6b537ff` và `d66495395c9392385cd8ff98fcb77f7c97abdea4dcd4e925f32ccd61a6b537ff`. Chưa xác nhận xóa chat.
- Gemini khai báo `UNCONFIRMED` cho truy cập của subagent và Task cha tự xử lý 12 ID. Đối chiếu phân công cho thấy 12/12 ID, trùng 0. Đây là tự khai của Gemini trong cùng một Task cha.

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 | FAIL | 11/12 JSON đọc được và khớp mã nghiên cứu/metadata. R0121 thiếu phần kết thúc đối tượng. 0 ID, DOI hoặc tiêu đề trùng trong 11 dòng. |
| A2 | FAIL | 154/154 khóa có mặt trong 11 dòng. 90/159 trích đoạn so khớp văn bản PDF trên trang khai báo. 69 mục chưa xác minh được về locator/trích đoạn. |
| A3 | FAIL | 29/31 số liệu đề xuất là OBSERVED. 8/29 thiếu thành phần bắt buộc hoặc chưa khớp locator/trích đoạn. Chưa đưa số liệu vào tổng hợp. |
| A4 | FAIL | Đã mở PDF để kiểm cơ học. Các trích đoạn chưa khớp và số liệu chưa đủ ngữ cảnh ngăn nghiệm thu toàn bộ. Chưa xác nhận ý nghĩa của các mục còn lại; kết quả so khớp chuỗi không thay thế kiểm ngữ nghĩa. |
| A5 | PASS | 12/12 ID trong phân công nội bộ; giao nhau 0. Task cha ghi rõ chưa xác nhận subagent. Không dùng nhận định abstract-only để nghiệm thu. |

**Kết quả: REJECTED.** Lưu raw và bằng chứng thu; chưa nhận báo cáo nào. Correction chỉ yêu cầu 69 locator, 8 mục định lượng và một dòng R0121 bị cắt. Không gửi lại batch 01.
