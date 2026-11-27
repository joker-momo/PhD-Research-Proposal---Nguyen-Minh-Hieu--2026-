# HK261 theo mẫu IEEE Journal

Bản định dạng hai cột dùng lớp IEEEtran journal V1.8b và kiểu thư mục IEEEtran 1.14 từ [gói IEEEtran](https://ctan.org/pkg/ieeetran). Nguồn nội dung là bản HK261 tại commit 8105b06. Mẫu dùng cho journal IEEE nói chung.

Biên dịch trong thư mục này với pdfLaTeX và BibTeX qua latexmk.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Hai bảng đặc tính của 46 nghiên cứu dùng hai trang mỗi bảng, với số bảng và tiêu đề cột lặp trên trang tiếp theo. Danh mục giữ 55 mục và các liên kết DOI. [Checklist PRISMA 2020](prisma_2020_checklist.md) trỏ đến các mục và trang của bản IEEE. Hồ sơ S1–S4 tiếp tục được lưu cùng [bản nguồn HK261](../sn_computer_science/README.md).

Thông tin tác giả và các tuyên bố đang chờ xác nhận như trong bản nguồn.
