# Đối chiếu ngày công bố theo E5

Từ thư mục `dual_ai_full_136`, chạy `python3 -B check_e5.py --replay` để tái tạo `e5_date_check/results.csv` từ dữ liệu đã lưu. Bỏ `--replay` để truy vấn lại Crossref. Có thể thêm `--output /tmp/hk261-e5` khi truy vấn mới để lưu riêng kết quả.

Script lấy hợp các hồ sơ mà ít nhất một lượt rà AI gắn trạng thái chờ E5 trong `review_136.csv`. DOI lấy theo mã hồ sơ từ hai sổ sàng lọc. Cửa sổ E5 tính từ 01/01/2021 đến hết 26/11/2026, với ngày kết thúc lấy từ `retrieval_round_01/round_01_evidence.json`. Bài tạp chí ưu tiên ngày xuất bản online. Bài hội nghị ưu tiên ngày xuất bản kỷ yếu. Ngày chỉ có tháng hoặc năm được biểu diễn bằng cả khoảng. Một khoảng cắt qua ranh giới E5 cần thêm chứng cứ.

- `results.csv` ghi trường ngày được sử dụng, khoảng ngày, nguồn, vị trí dữ liệu và kết quả. Cả 11 hồ sơ có ngày hoặc khoảng nhóm ngày nằm trọn trong cửa sổ E5. Bốn hồ sơ có độ phân giải theo tháng.
- `crossref_receipts.json` giữ phản hồi Crossref của 11 DOI. Đây là nguồn ngày cho R0001, R0002, R0028, R0121 và R0125.
- `retrieval_round_01/round_01_evidence.json` giữ ngày IEEE Xplore đã kiểm tra ở vòng truy hồi cho R0075, R0092, R0110, R0118 và R0137.
- `publisher_lookup.json` giữ ngày 10/09/2026 cho R0107, đọc từ trường Date of Publication trong kết quả IEEE Xplore Early Access được lập chỉ mục. Kết quả có DOI trùng khớp.

Kết quả này dùng để đối chiếu riêng tiêu chí ngày E5. Quyết định của người rà và số đếm PRISMA nằm trong các hồ sơ sàng lọc chính thức.
