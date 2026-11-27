# Đối chiếu R1/R2 để tác giả chốt

- [Báo cáo PDF](report.pdf) nêu quy mô và 12 mục nên đọc trước. Đây là bảy mục lệch dữ liệu đã lưu và năm mục R2 chưa qua đối chiếu nội dung.
- [Bảng cần chốt](muc_can_chot.csv) ghi mã bài, tên, DOI, tên tệp PDF, SHA-256, trang, nhận định, lý do và đề xuất trên mỗi dòng. Cột `tac_gia_chot` để trống.
- [Sổ quyết định của tác giả](author_decisions.csv) ghi từng xác nhận theo thứ tự. Các bảng sinh từ hai phiếu tiếp tục là ảnh chụp trước khi chốt.
- [Bảng toàn bộ 887 khóa](doi_chieu_887.csv) cho phép tìm lại mọi cặp R1/R2. [Tổng kiểm](summary.json) ghi các mẫu số và cờ.

## Cách đọc bảng

Số trang vật lý đếm từ 1. Đường dẫn PDF tính từ thư mục `systematic_review_prisma`. Với R0082, cột PDF IEEE chỉ áp dụng cho neo ghi rõ “IEEE publisher PDF” trong báo cáo nguồn. Các cột trạng thái và nhận định giữ đúng phiếu đã xác nhận.

`trang_khop_cum_trich` ghi trang có cụm trích khớp nguyên văn sau chuẩn hóa khoảng trắng và Unicode với PyMuPDF 1.26.7. `trang_doi_chieu_bang_hinh` lấy từ [biên bản kiểm tra trực quan](../primary_visual_checks.csv). `trang_doc_lai_theo_ngu_canh` ghi bốn khóa đã được định vị lại theo câu hoặc đề mục trên PDF. `trang_ung_vien` có trong PDF, dùng để tìm chỗ đọc tiếp. Một cụm trích khớp trang vẫn cần kiểm tra ý nghĩa, vị trí ô và phạm vi của kết luận. Mục giới hạn nguồn để trống trang thay vì suy đoán.

- `KHAC_TRANG_THAI` so sánh nhãn lưu trong phiếu. `KHAC_NHAN_GOC` so nhãn phán định D01–D10 hoặc độ phủ trong hai kết quả gốc trước khi hạ mức một mục ở R2. Các cờ này có thể cùng xuất hiện.
- `LECH_DU_LIEU_DA_LUU` ghi chênh lệch được lượt Codex phát hiện so với bản tổng hợp. `R2_KHONG_QUA_DOI_CHIEU` ghi kết quả Gemini chưa qua kiểm tra nội dung đã lưu.
- `RA_LAI_GIA_TRI_HAI_BEN` đánh dấu số thập phân hoặc phần trăm cần đọc lại khi so chuỗi đã chuẩn hóa. Đây là cờ sàng lọc. Viết khác đơn vị, thêm làm tròn hoặc biểu diễn khác có thể kích hoạt cờ.
- `GIOI_HAN_MINH_CHUNG` bao gồm xác minh một phần, nguồn chưa báo cáo, số chỉ hiện ở đồ thị, hoặc số in chưa giải quyết. `CHUA_GIAI_QUYET` giữ phần đang treo. `NGUON_GIOI_HAN` chỉ ghi giới hạn về phạm vi đối chiếu. Các dòng hoàn toàn không có cờ vẫn nằm trong bảng 887; quy tắc ghép không chứng nhận hai đoạn tường thuật có cùng ý nghĩa.

Tất cả mục cần chốt có đề xuất theo loại chứng cứ. Với 12 mục ưu tiên, đề xuất nêu cụ thể chỉ số hoặc phán định, phiên bản PDF và trang. Các mục còn lại dựa trên hai phiếu đã khóa, kiểm tra máy theo trang và biên bản đối chiếu gốc, với phạm vi được ghi theo từng hàng. Quyết định cập nhật trong sổ quyết định của tác giả. S2, PRISMA, bản thảo và hai bộ phiếu giữ nguyên.

## Tái tạo

Từ thư mục này, chạy `uv run --offline --no-project --with pymupdf==1.26.7 python -B build_reconciliation.py` để tạo CSV, JSON và dữ liệu LaTeX. Có thể truyền `--output <thư mục tạm>` để đối chiếu mà giữ bản đã lưu. Chạy `xelatex -interaction=nonstopmode -halt-on-error report.tex` hai lượt để dựng PDF.
