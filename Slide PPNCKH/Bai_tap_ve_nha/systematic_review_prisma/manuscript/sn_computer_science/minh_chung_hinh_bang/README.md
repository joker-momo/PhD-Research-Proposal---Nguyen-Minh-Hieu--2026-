# Minh chứng hình, bảng và công thức HK261

Mở [chỉ mục theo từng mục trong PDF](ITEM_INDEX.md) để tra công thức, mã
LaTeX/TikZ, dữ liệu và vị trí nguồn gốc. Thư mục [sources](sources) giữ bản
sao đầu vào, mã và LaTeX đã sinh để biên dịch. Mở
[PDF đối chiếu](sources/manuscript/sn_computer_science/main.pdf)
để xem kết quả đã lưu. Các bản sao được đối chiếu với nguồn trên nhánh
HK261 bằng [package_evidence.py](package_evidence.py) và [SHA256SUMS](SHA256SUMS).

Tra các nhận định và các chỗ thiếu minh chứng trong [S4](../supplement_evidence_index.md).

## Đầu vào và cách tái tạo từng mục

| Mục | Đầu vào và quy tắc | Bước tái tạo |
| --- | --- | --- |
| Hình 1 · Lưu đồ PRISMA | [Số đếm và danh sách ID](sources/restart_2026_11_26/prisma/prisma_counts.json), [mẫu TikZ](sources/restart_2026_11_26/prisma/flow_template.tex), [nguồn TikZ đã điền số](sources/restart_2026_11_26/prisma/prisma_flow.tex). Công thức cân đối các bước nằm trong chỉ mục. | Bước 1 biên dịch nguồn TikZ đã đối soát. Bước 3 nhúng lưu đồ ở trang 7. |
| Hình 2 · Tổng quan tập nghiên cứu | [Mã hóa 46 nghiên cứu](sources/manuscript/sn_computer_science/technical_coding.psv), [đặc trưng](sources/restart_2026_11_26/synthesis/final_46/study_characteristics.csv), [BibTeX](sources/manuscript/sn_computer_science/references.bib) và [TikZ](sources/manuscript/sn_computer_science/technical_overview_figure.tex). Số đếm theo nhóm được đổi thành chiều cao hoặc chiều dài thanh. | Bước 2 sinh số đếm. Bước 3 vẽ bốn ô ở trang 8. |
| Hình 3 · Sơ đồ kiến trúc | Ba nhóm topology trong bảng mã hóa và [TikZ](sources/manuscript/sn_computer_science/technical_architecture_figure.tex). Mũi tên biểu diễn quan hệ logic. | Bước 3 vẽ sơ đồ ở trang 9. |
| Hình 4 · Cây phân loại | Bốn chiều phân loại trong bảng mã hóa và [TikZ](sources/manuscript/sn_computer_science/technical_taxonomy_figure.tex). Mỗi lá đếm các ID thuộc nhóm tương ứng. | Bước 2 sinh số đếm. Bước 3 vẽ cây ở trang 10. |
| Hình 5 · Biểu đồ thẩm định | [Tổng hợp 10 tiêu chí](sources/restart_2026_11_26/synthesis/final_46/appraisal_summary.csv) và [TikZ](sources/manuscript/sn_computer_science/technical_appraisal_figure.tex). Độ rộng mỗi đoạn là 100 × số nghiên cứu ở mức tương ứng / 46. | Bước 2 sinh đầu vào cho biểu đồ. Bước 3 vẽ thanh ở trang 23. |
| Bảng 1 · Khảo sát liên quan | [Các hàng LaTeX](sources/manuscript/sn_computer_science/main.tex#L33), BibTeX và [nguồn từng hàng](ITEM_INDEX.md#related-survey-matrix-source-locators). Ký hiệu từng ô dựa trên phạm vi thể hiện tại phần nguồn đã kiểm tra. | Bước 3 dàn bảng ở trang 2. |
| Bảng 3 · Kiến trúc | Bảng mã hóa, đặc trưng, [vị trí nguồn từng bài](sources/manuscript/sn_computer_science/s4_study_row_sources.csv) và [trích xuất R0082](sources/restart_2026_11_26/synthesis/final_46/r0082_evidence.json). Sắp theo topology, năm và ID. | Bước 2 sinh [LaTeX bảng](sources/manuscript/sn_computer_science/technical_architecture.tex). Bước 3 dàn bảng từ trang 12. |
| Bảng 4 · Đánh giá và khả năng phục hồi | Bảng mã hóa, đặc trưng, D09 trong tổng hợp 10 tiêu chí và vị trí nguồn theo ID. Có thể đối chiếu D09 với [mức thẩm định từng nghiên cứu](sources/restart_2026_11_26/synthesis/final_46/appraisal_table.csv). | Bước 2 sinh [LaTeX bảng](sources/manuscript/sn_computer_science/technical_evaluation.tex). Bước 3 dàn bảng từ trang 17. |
| Bảng 6 · Đối chiếu định lượng | [Sổ kết quả](sources/restart_2026_11_26/synthesis/final_46/contrast_evidence.csv), [đính chính R0092](sources/restart_2026_11_26/synthesis/active_rq_p08_erratum_R0092.json), [bản đồ 9 hàng](ITEM_INDEX.md#numerical-contrast-row-map) và [hàng LaTeX](sources/manuscript/sn_computer_science/main.tex#L260). Giữ số liệu, đơn vị, comparator và độ bất định như đã kiểm chứng. | Bước 3 dàn bảng ở trang 22. |
| Bảng 7 · Kết quả thẩm định | Tổng hợp 10 tiêu chí và [lý do theo nghiên cứu](sources/restart_2026_11_26/synthesis/final_46/appraisal_rationale.csv). Tỷ lệ Yes là 100 × số Yes / 46, làm tròn một chữ số thập phân. | Bước 2 sinh [hàng LaTeX](sources/manuscript/sn_computer_science/technical_appraisal.tex). Bước 3 dàn bảng ở trang 23. |
| Bảng 2 · Cơ chế × mức thực nghiệm | Đếm mỗi ID đúng một lần theo hai cột mã hóa trong [dữ liệu phân loại](sources/restart_2026_11_26/synthesis/final_46/mechanisms.csv). | Bước 2 sinh bảng, bước 3 dàn ở trang 7. |
| Bảng 5 · Độ phủ định lượng | Nối [dữ liệu theo nghiên cứu](sources/restart_2026_11_26/synthesis/final_46/report_coverage.csv) và [sổ kết quả](sources/restart_2026_11_26/synthesis/final_46/outcomes.csv) bằng report ID. Đếm số nghiên cứu theo trạng thái và cộng số mục matched và descriptive theo cơ chế. | Bước 2 sinh bảng, bước 3 dàn ở trang 21. |
| Bảng 8 · Kiểm toán S2 | [Sổ S2](sources/manuscript/sn_computer_science/human_adjudication_log.csv), [JSON](sources/manuscript/sn_computer_science/audit_summary.json), mã kiểm toán và [phép suy ra trong S4](../supplement_evidence_index.md#s2-audit-derivations). | Bước 2 chạy lại kiểm toán từ sổ S2, dữ liệu sàng lọc nền và PRISMA đã khóa. Bước 3 dùng [LaTeX đã sinh](sources/manuscript/sn_computer_science/adjudication_audit_table.tex) để dàn trang 25. |
| Công thức 1–3 | [LaTeX và phép suy ra](ITEM_INDEX.md#figures-tables-and-equations) cho hàm mục tiêu, độ trễ liên kết và thời gian phục hồi. | Bước 3 dàn công thức ở trang 11 và 24. |

## Các lệnh tái tạo

Chạy từ thư mục này. Dùng Python 3, pdfLaTeX và Tectonic. Lần đối chiếu dùng
Python 3.11.15, pdfTeX 1.40.27 (TeX Live 2025) và Tectonic 0.16.9. Tệp PDF
tạo lại có thể khác metadata. So sánh nội dung trang hoặc ảnh kết xuất.

```sh
shasum -a 256 -c SHA256SUMS

build_dir="$(mktemp -d)"
cp -R sources "$build_dir/"

# 1. Dựng lại Hình 1 từ nguồn TikZ đã điền số.
(
  cd "$build_dir/sources/restart_2026_11_26/prisma"
  pdflatex -interaction=nonstopmode -halt-on-error prisma_flow.tex
  cp prisma_flow.pdf ../../manuscript/sn_computer_science/prisma_flow.pdf
)

# 2–3. Sinh dữ liệu LaTeX rồi dựng bản thảo và toàn bộ hình, bảng.
(
  cd "$build_dir/sources/manuscript/sn_computer_science"
  python3 build_technical_survey.py
  python3 build_technical_survey.py --check
  python3 build_editorial_evidence.py tables
  python3 build_editorial_evidence.py check
  python3 audit_adjudication.py --frozen-prisma
  tectonic --keep-logs --keep-intermediates main.tex
  # Lượt thứ hai dùng tệp phụ đã lưu để ổn định bố cục các bảng nhiều trang.
  tectonic --only-cached --keep-logs --keep-intermediates main.tex
)
printf '%s\n' "$build_dir/sources/manuscript/sn_computer_science/main.pdf"
```

Tùy chọn `--frozen-prisma` dùng sổ PRISMA đã xác minh bằng SHA-256 trong gói. Để đối soát thêm từ hồ sơ sàng lọc của dự án, chạy lệnh dưới đây từ thư mục
này trong worktree. Lệnh kiểm tra lại cả số đếm lẫn nguồn TikZ của Hình 1.

```sh
python3 ../../../restart_2026_11_26/prisma/reconcile.py --check
python3 ../audit_adjudication.py --check
python3 ../../../restart_2026_11_26/synthesis/final_46/reconcile_inputs.py --check
```

Bỏ `--check` ở lệnh thứ hai để tái tạo Bảng 8 và JSON. Lệnh này dùng hồ sơ
sàng lọc gốc trong worktree và sổ quyết định tác giả đã chốt. Lệnh thứ ba kiểm tra dữ liệu của tập 46 bài dựa trên hồ sơ gốc, minh chứng R0082 và 12 quyết định của tác giả. Tra từng quyết định trong [S3](../supplement_s3.md#twelve-priority-decisions) và [dữ liệu áp dụng đã lưu](sources/restart_2026_11_26/synthesis/final_46/author_decision_application.json).

## Tra nguồn gốc và cập nhật

[Bản đồ ID và đường dẫn PDF gốc](sources/restart_2026_11_26/synthesis/final_46/synthesis_input_index.csv)
chỉ đến các tệp trong dự án HK261, kèm SHA-256. Các PDF nguồn và dữ liệu
tìm kiếm thô tra qua [S4 đầy đủ](../supplement_evidence_index.md) trong
worktree. Thư mục này chứa dữ liệu đã dùng để dựng hình, bảng và bản thảo.

Khi sửa nguồn chính, cập nhật S4, biên dịch và kiểm tra bản thảo trước.
Chạy `python3 package_evidence.py --refresh` rồi
`python3 package_evidence.py` từ thư mục này để cập nhật và kiểm tra
bản sao theo cùng phiên bản. Khi tháo thư mục khỏi worktree, dùng
`shasum -a 256 -c SHA256SUMS` để xác minh các tệp đã đóng gói.
