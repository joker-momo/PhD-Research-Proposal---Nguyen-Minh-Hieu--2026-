# Mẫu Bài Tập Về Nhà / Báo Cáo Môn Học (PPNCKH Nâng cao - GK5007)

Thư mục này được thiết lập sẵn dành cho việc làm bài tập cá nhân, bài tập nhóm hoặc tiểu luận môn **Phương pháp Nghiên cứu Khoa học Nâng cao (GK5007)** - Trường Đại học Bách Khoa, ĐHQG-HCM.

---

## 1. Thông số định dạng chuẩn (Đã cấu hình sẵn)

| Tiêu chuẩn | Cấu hình trong LaTeX | Ghi chú |
| :--- | :--- | :--- |
| **Font chữ** | `Times New Roman` | Hỗ trợ cả **XeLaTeX** (`fontspec`) và **pdfLaTeX** (`times` + `T5`) |
| **Cỡ chữ (Font size)** | **13 pt** | Sử dụng `\usepackage{scrextend}` + `\changefontsizes{13pt}` |
| **Giãn dòng (Line spacing)** | **1.5 lines** | Sử dụng `\usepackage{setspace}` + `\setstretch{1.5}` |
| **Khổ giấy (Paper)** | A4 | `a4paper` |
| **Căn lề (Margins)** | Trái: 3.0 cm, Phải: 2.0 cm, Trên: 2.0 cm, Dưới: 2.0 cm | Chuẩn theo Nghị định 30/2020/NĐ-CP và quy định ĐHBK |
| **Thụt đầu dòng** | 1.0 cm (`\setlength{\parindent}{1.0cm}`) | Khoảng cách đoạn: `6pt` |

---

## 2. Cấu trúc thư mục

```text
Bai_tap_ve_nha/
├── main.tex                 # File LaTeX chính (preamble, trang bìa, mục lục, gọi các section)
├── main.pdf                 # File PDF đã biên dịch hoàn chỉnh
├── references.bib           # Danh mục tài liệu tham khảo (BibTeX chuẩn IEEE)
├── Makefile                 # Phím tắt biên dịch từ terminal (make, make xe, make clean)
├── .latexmkrc               # Cấu hình biên dịch tự động cho latexmk và VSCode
├── figures/                 # Thư mục chứa hình ảnh minh họa
│   └── HCMCUT-logo.png      # Logo Trường Đại học Bách Khoa - ĐHQG-HCM
└── sections/                # Các chương/phần nội dung tách rời
    ├── 01_tong_quan.tex     # Chương 1: Tổng quan và câu hỏi nghiên cứu
    ├── 02_phuong_phap.tex   # Chương 2: Phương pháp luận và mô hình toán
    ├── 03_thuc_nghiem.tex   # Chương 3: Kết quả thực nghiệm và thảo luận
    └── 04_ket_luan.tex      # Chương 4: Kết luận và hướng phát triển
```

---

## 3. Cách biên dịch file

### Cách 1: Dùng VSCode (Khuyên dùng)
- Mở thư mục bài tập trong VSCode.
- Mở file `main.tex`.
- Bấm tổ hợp phím:
  - `Ctrl + Alt + B` (Windows/Linux) hoặc `Cmd + Option + B` (macOS) để Build.
  - Hoặc click vào biểu tượng **TeX** ở thanh bên trái của VSCode và chọn **Build LaTeX project**.

### Cách 2: Dùng Terminal / dòng lệnh
- Biên dịch bằng `make`:
  ```bash
  make        # Biên dịch bằng pdflatex qua latexmk
  make xe     # Biên dịch bằng xelatex qua latexmk
  make clean  # Xóa các file phụ sinh ra (aux, log, toc, bbl, v.v.)
  ```
- Hoặc biên dịch trực tiếp bằng `latexmk`:
  ```bash
  latexmk -pdf main.tex      # Dùng pdflatex
  latexmk -xelatex main.tex  # Dùng xelatex
  ```

---

## 4. Các thành phần học thuật mẫu có sẵn trong `main.tex`

1. **Trang bìa trang trọng:** Logo Bách Khoa, Tên trường & Khoa KH&KT Máy tính, Tên môn học (GK5007), Thông tin NCS Nguyễn Minh Hiếu, Giảng viên phụ trách.
2. **Mục lục tự động:** Đánh số trang kiểu La Mã (`roman`) cho phần đầu và số tự nhiên (`arabic`) cho phần nội dung bài làm.
3. **Khung đề bài / câu hỏi nổi bật (`homeworkbox`):** Tạo khung viền xanh nhã nhặn để phân tách câu hỏi bài tập với câu trả lời.
4. **Công thức toán & Bảng ký hiệu:** Định dạng phương trình toán chuẩn học thuật (`amsmath`, `mathtools`) và bảng ký hiệu tham số (`tabularx`).
5. **Bảng kết quả thực nghiệm:** Trình bày bảng so sánh Baseline theo chuẩn `booktabs`.
6. **Trích dẫn khoa học:** Chuẩn trích dẫn IEEE (`ieeetr.bst`) tự động liên kết với `references.bib`.
