# Đối chiếu phiếu R1 và R2 đã nhận

Ghép 136 mã HKF giữa hai phiếu gốc. Anh xác nhận đã duyệt R1 ngày 26/11/2026. Phiếu R2 được gửi trong chat ngày 28/11/2026. Cả 136 dòng của phiếu R2 ghi mã người chấm R2 và ngày 27/11/2026. Danh tính người điền, mức độ độc lập và quy trình đọc nguồn của R2 còn chờ xác nhận.

| R1 \ R2 | Đưa vào | Loại | Chờ | Tổng R1 |
| --- | ---: | ---: | ---: | ---: |
| Đưa vào | 5 | 2 | 26 | 33 |
| Loại | 0 | 29 | 58 | 87 |
| Chờ | 3 | 2 | 11 | 16 |
| Tổng R2 | 8 | 33 | 95 | 136 |

Hai phiếu trùng trạng thái ở 45/136 dòng (33,1%) và khác ở 91/136 dòng. Trong 29 dòng cả hai phiếu ghi Loại, 6 dòng chọn mã E chính khác nhau. Tỷ lệ này mô tả các trạng thái ghi trong hai tệp.

R2 có 95 dòng ghi Chờ. Trong đó, 90 dòng thiếu cả trang PDF lẫn mục/bảng/hình, đều ghi E7 và nêu giới hạn đọc văn bản trích xuất. Có thêm 2 dòng nhắc đến việc cắt văn bản và có điền cả hai trường định vị. Các ô có định vị cần được kiểm chứng với PDF gốc trước khi dùng làm căn cứ phân xử.

[Bảng đối chiếu theo mã HKF](r1_r2_comparison.csv) ghi số dòng ở mỗi phiếu, trạng thái, mã E và định vị đã nhập. Hai cột cờ dùng 1 cho có và 0 cho không. Tra lý do nguyên văn tại dòng tương ứng trong các phiếu gốc.

- [Phiếu R1 gốc](../R1/submitted/HK261_phieu_sang_loc_doc_lap_R1_136_filled.xlsx) · SHA-256 `621927bba73ecef6a539269cfb3b796fee43cf2a734c406d5d641d8e11be501a`
- [Phiếu R2 gốc](../R2/submitted/HK261_phieu_sang_loc_doc_lap_R2_136_filled.xlsx) · SHA-256 `740f71b9f55bfc145f7324812c7f60251ce7f8a439b68260a9477a9c740a4eb4`

S2 và kết quả PRISMA chính thức vẫn giữ 46 đưa vào, 90 loại, 0 chờ. Hồ sơ này mới ghi nhận và đối chiếu hai phiếu.
