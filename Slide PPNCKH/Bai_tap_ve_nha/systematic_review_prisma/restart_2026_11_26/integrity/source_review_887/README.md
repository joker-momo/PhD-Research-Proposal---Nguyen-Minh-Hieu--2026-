# HK261 · Đối chiếu nguồn cho 887 mục

Gói này kiểm tra các mục của phiếu nguồn bằng hai lượt hỗ trợ AI, riêng với phiếu người thẩm định. Khóa chính là mã HKF, loại mục và khóa trong phiếu. Mã R và hash PDF trong kết quả giúp mở đúng nguồn. Một trang luôn là chỉ số vật lý trong file, bắt đầu từ 1.

- `source_review_887.csv` gồm 887 dòng, có hai ô kết quả riêng cho Codex và Gemini cùng trang, trích đoạn, ghi chú và kiểm tra neo nguồn.
- `source_review_summary.json` lưu số mục trả về, số mục thiếu, trạng thái của từng lô và tiêu chí để kiểm tra dữ liệu.
- `report.tex` và `report.pdf` tóm tắt các khác biệt đã phát hiện và cách đọc CSV.
- `phase_manifest.json` lưu chuỗi SHA-256 của từng PDF và từng file đầu vào thực tế. Bản PDF đã cung cấp riêng cho R0082 được nhận diện theo biên bản đối chiếu IEEE của gói tổng hợp.

Các đoạn ngắn trong bảng dùng để kiểm chứng. `ANCHORS_MATCH` chỉ xác nhận nguyên văn trên trang, còn đối chiếu số liệu cần xác nhận đúng hàng, cột và điều kiện. Riêng khám phá từ Gemini giữ trạng thái tham khảo khi chưa được đối chiếu ngữ nghĩa. Cột `comparison` dùng để ưu tiên đọc các mục thiếu, bất đồng nhãn hoặc có khác biệt đề xuất; nhãn giống nhau chưa đủ để kết luận hai lập luận tương đương.

## Tái tạo

Chạy `python3 -B prepare.py /tmp/hk261-source-review` từ thư mục này với các PDF đã được gói thẩm định lưu cục bộ. Mã tái dựng văn bản theo trang vật lý bằng Apple PDFKit và kiểm tra lại manifest. Bổ sung các tệp JSONL của Codex và biên nhận gốc Gemini trong các thư mục tương ứng, sau đó chạy `python3 -B review_sources.py /tmp/hk261-source-review`. Lệnh chỉ đọc phiếu R1/R2 và tạo kết quả trong thư mục báo cáo. Báo cáo tóm tắt biên dịch bằng `xelatex -interaction=nonstopmode -halt-on-error report.tex` hai lần.
