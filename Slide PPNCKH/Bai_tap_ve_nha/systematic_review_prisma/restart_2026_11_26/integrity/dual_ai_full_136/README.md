# HK261 · Hai lượt rà soát hỗ trợ bởi AI

Bản tham chiếu gồm 136 PDF mã HKF và quyết định đã khóa 46 đưa vào, 90 loại, 0 chờ. Hai phiếu của người chấm được lưu riêng trong [gói thẩm định](../../synthesis/final_46/human_review_packet/README.md). Nhật ký này lưu kết quả AI. Chỉ ghi quyết định dưới tên người thực sự đọc và xác nhận quyết định, tiêu chí, nguồn, trang và ngày.

- [Báo cáo PDF](report.pdf) và [bảng 136 hồ sơ](review_136.csv).
- [Bảng kiểm 887 mục trích xuất](extraction_locator_audit.csv) và [9 đối chiếu ảnh nguồn](visual_outcome_review.csv).
- [Đầu vào và SHA-256 từng PDF](phase_manifest.json), [gói ngữ cảnh Gemini](isolated_context_manifest.json), [yêu cầu Gemini](gemini_isolated_brief.md), [rà cửa chấp nhận Gemini](gemini_review.md) và [báo cáo máy đọc](review_summary.json).
- [Phiếu R1](../../synthesis/final_46/human_review_packet/R1/screening.csv), [phiếu R2](../../synthesis/final_46/human_review_packet/R2/screening.csv). Giữ bản gốc của từng phiếu trước hòa giải. Ghi rõ nếu người chấm đọc khuyến nghị AI khi ra quyết định.

## Tái tạo

Dùng Python 3, macOS PDFKit qua Swift, và XeLaTeX có Times New Roman. Chuẩn bị các PDF mã HKF bằng lệnh trong gói thẩm định; đối chiếu SHA-256 với manifest trước khi phân tích. PDF của nhà xuất bản lưu cục bộ theo quyền truy cập. Kết quả trích xuất PDFKit theo trang có thể tạo lại bằng mã trong thư mục này. Sau khi tái tạo ngữ cảnh ban đầu, dùng `prepare_gemini_correction.py` với `gemini_initial_review_summary.json` để tái tạo nhóm văn bản cho 101 hồ sơ cần rà bổ sung. Kiểm tra từng tham số bằng `--help`.

1. Chạy `python3 prepare_review_pages.py /tmp/hk261-pages --gemini-context /tmp/hk261-context`. Mã đối chiếu PDF, tạo JSON văn bản theo trang vật lý (bắt đầu từ 1) và kiểm tra SHA-256 các tập văn bản Gemini.
2. Chạy `audit_review_inputs.py` với thư mục JSON trang làm đầu vào để tạo `extraction_locator_audit.csv`. Kết quả trực quan nằm trong `visual_outcome_review.csv`. Mỗi dòng ghi trang, bảng hoặc hình và điều kiện.
3. Chạy `python3 assemble_review.py /tmp/hk261-pages codex_pass.jsonl gemini_receipt.json --gemini-correction gemini_correction_receipt.json --gemini-gate gemini_gate.json` để tái tạo hai tệp LaTeX sinh tự động, CSV 136 hồ sơ và JSON tổng hợp.
4. Chạy `xelatex -interaction=nonstopmode -halt-on-error report.tex` hai lần trong thư mục này để dựng báo cáo.

Phiếu Codex và Gemini áp dụng E1–E7 và thứ tự loại E5 → E6 → E1 → E7 → E2 → E3 → E4. Phép đối chiếu báo cáo số hồ sơ khác quyết định đã khóa trong 136, giao bảng ba quyết định nếu đủ hai lượt đạt cửa chấp nhận, và Cohen’s kappa theo công thức \((p_o - p_e)/(1-p_e)\), với \(p_o\) là tỷ lệ quyết định trùng và \(p_e\) là tổng tích tỷ lệ biên của ba quyết định.

## Hồ sơ có khác biệt về phiên bản

- R0082 (HKF-115). Xem [biên bản đối chiếu IEEE](../../synthesis/final_46/r0082_publisher_crosscheck.json). DOI 10.1109/WCNC55385.2023.10118908.
- R0077 (HKF-100). [Trang Elsevier](https://www.sciencedirect.com/science/article/abs/pii/S1383762126001220) ghi bài nghiên cứu, số tháng 7/2026, DOI 10.1016/j.sysarc.2026.103804. Codex dùng trang này để kiểm chứng thông tin xuất bản sau khi khóa lượt rà soát. Cần đối chiếu bản toàn văn chính thức để kiểm tra các vị trí trích từ arXiv.
- R0292 (HKF-109). [S2](../../../manuscript/sn_computer_science/supplement_s2_adjudication.md) ghi nguồn chính sách DroNet 2025, chương trình Session 3 và DOI ACM. Phiếu chấm mù chỉ thấy PDF.
