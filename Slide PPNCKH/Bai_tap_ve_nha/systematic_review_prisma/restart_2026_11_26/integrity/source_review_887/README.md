# HK261 · Đối chiếu nguồn cho 887 mục

Gói này kiểm tra các mục của phiếu nguồn bằng hai lượt hỗ trợ AI, riêng với phiếu người thẩm định. Khóa chính là mã HKF, loại mục và khóa trong phiếu. Mã R và hash PDF trong kết quả giúp mở đúng nguồn. Một trang luôn là chỉ số vật lý trong file, bắt đầu từ 1.

- `source_review_887.csv` gồm 887 dòng. Các cột `codex_*`, `gemini_*` và `correction_*` giữ riêng kết quả Codex, Gemini lượt đầu và lô Gemini rà lại, cùng trang, trích đoạn, ghi chú và kiểm tra neo nguồn.
- `source_review_summary.json` lưu số mục trả về, số mục thiếu, trạng thái của từng lô và tiêu chí để kiểm tra dữ liệu.
- `codex_pass.jsonl` lưu lượt Codex theo đúng khóa của phiếu. Thư mục `receipts/` lưu biên nhận và kết quả kiểm tra của Gemini. `primary_visual_checks.csv` ghi các ô bảng và nhãn hình đã đối chiếu trên ảnh render PDF gốc.
- `report.tex` và `report.pdf` tóm tắt các khác biệt đã phát hiện và cách đọc CSV.
- `phase_manifest.json` lưu chuỗi SHA-256 của từng PDF và từng file đầu vào thực tế. Bản PDF đã cung cấp riêng cho R0082 được nhận diện theo biên bản đối chiếu IEEE của gói tổng hợp.
- `correction_manifest.json` và `correction_targets.json` lưu khóa cần rà lại, lý do, hash tệp và ánh xạ trang của bộ đầu vào bổ sung. Bản gốc vẫn có thể truy vết từ manifest và CSV. Bộ đầu vào bổ sung chỉ tồn tại trong vùng tạm khi tạo và trong biên nhận bridge.

Các đoạn ngắn trong bảng dùng để kiểm chứng. `ANCHORS_MATCH` chỉ xác nhận nguyên văn trên trang, còn đối chiếu số liệu cần xác nhận đúng hàng, cột và điều kiện. `gemini_semantic` và cột giải thích đi kèm ghi kết quả kiểm tra nội dung riêng. Dùng `author_attention` để lọc các sai khác với dữ liệu hiện hành, các mục cần kiểm tra tiếp và các mục có phạm vi nguồn giới hạn. Khi hai lượt dùng cùng nhãn, đọc bằng chứng của từng lượt để xác định hai lập luận có tương đương hay không.

## Tái tạo

Chạy `python3 -B prepare.py /tmp/hk261-source-review` từ thư mục này với các PDF đã được gói thẩm định lưu cục bộ. Mã tái dựng văn bản theo trang vật lý bằng Apple PDFKit và kiểm tra lại manifest. Chạy `python3 -B review_sources.py /tmp/hk261-source-review` để tổng hợp các lượt đã lưu. Chuẩn bị mảng văn bản theo trang với `page.get_text(sort=False)` từ PyMuPDF 1.26.7 tại `/tmp/hk261-source-review/pymupdf/HKF-nnn.json` để tái tạo bước xác thực chuỗi mà PDFKit tách khác. Lệnh chỉ đọc phiếu R1/R2 và tạo kết quả trong thư mục báo cáo. Báo cáo tóm tắt biên dịch bằng `xelatex -interaction=nonstopmode -halt-on-error report.tex` hai lần.

Tái tạo đầu vào lô rà lại bằng `rtk uv run --offline --no-project --with pymupdf==1.26.7 python -B correction_packet.py correction_targets.json /tmp/hk261-correction/assets`. Đối chiếu hash trong `correction_manifest.json`. Công cụ trích các trang cần đọc, giữ bản đồ số trang gốc và chỉ chuyển sang văn bản hoặc ảnh khi cần giảm kích thước bộ đầu vào cho trình đọc.
