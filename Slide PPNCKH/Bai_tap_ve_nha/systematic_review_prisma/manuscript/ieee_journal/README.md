# HK261 theo mẫu IEEE Journal

Bản định dạng hai cột dùng lớp IEEEtran journal V1.8b và kiểu thư mục IEEEtran 1.14 từ [gói IEEEtran](https://ctan.org/pkg/ieeetran). Nguồn nội dung là bản HK261 tại commit 8105b06. Mẫu dùng cho journal IEEE nói chung.

Biên dịch trong thư mục này với pdfLaTeX và BibTeX qua latexmk.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Hai bảng đặc tính của 46 nghiên cứu dùng hai trang mỗi bảng, với số bảng và tiêu đề cột lặp trên trang tiếp theo. Danh mục giữ 55 mục và các liên kết DOI. [Checklist PRISMA 2020](prisma_2020_checklist.md) trỏ đến các mục và trang của bản IEEE. Bộ hồ sơ IEEE gồm [S1 — Chiến lược tìm kiếm](../sn_computer_science/supplement_search_strategies.md), [S2 — Quyết định đủ điều kiện](../sn_computer_science/supplement_s2_adjudication.md), [S3 — Trích xuất và thẩm định](../sn_computer_science/supplement_s3.md) và [S4 — Chỉ mục minh chứng IEEE](supplement_s4.md). S4 đối chiếu số trang vật lý của PDF với mã LaTeX, dữ liệu và vị trí nguồn. Khi giải nén bộ phụ lục, mở README ở thư mục gốc để tra tệp và xác minh SHA-256.

Thông tin tác giả và các tuyên bố đang chờ xác nhận như trong bản nguồn.
