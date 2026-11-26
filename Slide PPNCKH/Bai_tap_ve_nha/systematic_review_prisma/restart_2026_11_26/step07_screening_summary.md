# Bước 07 – Sàng lọc tiêu đề và tóm tắt

Hoàn tất lúc 2026-11-26T19:28:28+07:00. Phạm vi là 465 bản ghi duy nhất từ tập dữ liệu được khóa theo lần làm lại.

| Batch | Khoảng ID | Đã nghiệm thu | Chuyển toàn văn | Chưa rõ | Loại ở bước 07 | Biên bản |
|---|---|---:|---:|---:|---:|---|
| 01 | R0001–R0030 | 30 | 11 | 5 | 14 | [PASS](step07_batch01_acceptance.md) |
| 02 | R0031–R0090 | 60 | 23 | 6 | 31 | [PASS](step07_batch02_acceptance.md) |
| 03 | R0091–R0165 | 75 | 8 | 23 | 44 | [PASS](step07_batch03_acceptance.md) |
| 04 | R0166–R0240 | 75 | 1 | 16 | 58 | [PASS](step07_batch04_acceptance.md) |
| 05 | R0241–R0315 | 75 | 0 | 28 | 47 | [PASS](step07_batch05_acceptance.md) |
| 06 | R0316–R0390 | 75 | 0 | 8 | 67 | [PASS](step07_batch06_acceptance.md) |
| 07 | R0391–R0465 | 75 | 1 | 7 | 67 | [PASS](step07_batch07_acceptance.md) |
| **Tổng** | **R0001–R0465** | **465** | **44** | **93** | **328** | |

- 693 bản ghi đầu vào − 228 bản ghi trùng = 465 bản ghi đã sàng lọc. Tổng ba trạng thái là 465.
- 465/465 ID có một quyết định, mã tiêu chí, lý do và trích đoạn khớp với bản ghi nguồn trong đúng nhóm khử trùng.
- 0 ID, DOI hoặc tiêu đề chuẩn hóa trùng. SHA-256 của 7 đầu vào đã khóa trùng với manifest. 0 quyết định kế thừa từ bộ cũ.
- Gemini.app sàng lọc trong Task mode bằng quyền đọc trực tiếp thư mục dự án. Chỉ mục bằng chứng của dự án chia dữ liệu thành các tệp nhỏ để khắc phục giới hạn đọc của ứng dụng. Không tạo bản sao ngữ cảnh riêng cho mỗi lượt.
- 137 bản ghi chuyển sang bước 08, gồm 44 chuyển toàn văn và 93 chưa rõ cần xác minh. Đây là số bản ghi cần truy xuất, trước bước sàng lọc toàn văn.

[Dữ liệu sàng lọc đã nghiệm thu](title_abstract_screening.csv) · [Kế hoạch đã duyệt](approved_plan.md)
