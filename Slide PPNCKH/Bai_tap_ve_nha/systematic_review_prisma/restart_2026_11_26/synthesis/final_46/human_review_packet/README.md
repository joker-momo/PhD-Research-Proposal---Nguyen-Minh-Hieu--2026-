# Phiếu thẩm định HK261

Tại lần xuất bản thảo gần nhất, tác giả đã xác nhận 8/136 quyết định toàn văn. Hai phiếu `screening.csv` vẫn để trống. Sổ S2 và PRISMA vẫn theo quyết định đã lưu (46 đưa vào, 90 loại, 0 chờ).

## Xác nhận hai phiếu đối chiếu nguồn

Ngày ghi nhận **2026-11-27**. Tác giả xác nhận trong chat HK261: “Điền R1 theo nhận định của tôi đồng ý với Codex và R2 theo ý kiến đồng nghiệp đồng ý với Gemini do tôi xác nhận lại. Giữ nguyên S2, PRISMA và bản thảo.”

- **R1** ghi nhận nhận định của tác giả sau khi xem và đồng ý với lượt Codex. [Phiếu R1](R1/source_verification.csv)
- **R2** ghi nhận ý kiến đồng nghiệp đồng ý với lượt Gemini, theo xác nhận lại của tác giả trong chat. [Phiếu R2](R2/source_verification.csv)

Hai xác nhận dựa trên kết quả hỗ trợ AI đã được xem. Hồ sơ ghi nhận xác nhận chung cho mỗi lượt. Cột `date` ghi ngày tiếp nhận xác nhận. Nguồn xác nhận R2 là lời tác giả. Bộ phiếu này cung cấp 0 cặp đánh giá độc lập hoặc làm mù và 0 cặp quyết định sàng lọc mới.

Mỗi phiếu có 887 khóa. R1 giữ 476 mục xác minh được, 332 mục một phần, 40 mục nguồn không báo cáo, 32 mục chưa giải quyết và 7 mục chênh lệch với dữ liệu đã lưu. R2 ghi 404 mục xác minh được, 403 mục một phần, 37 mục nguồn không báo cáo và 43 mục chưa giải quyết. R2 lấy lượt Gemini rà lại khi có. Mục một phần ghi phần kết luận được kiểm chứng và giới hạn tương ứng. Mục không qua kiểm tra nội dung hoặc vướng quyền truy cập giữ trạng thái chưa giải quyết. Với 38 khóa có giới hạn nguồn, R1 ghi trạng thái Codex ở mức tổng quát và R2 ghi giới hạn truy cập của Gemini.

Định vị từng mục bằng ba cột `packet_id`, `check_type`, `check_key` trong phiếu, tương ứng `packet_id`, `kind`, `key` trong bảng nguồn. Bảng nguồn lưu mã bài, hash PDF, trang vật lý đếm từ 1 và các kết quả kiểm tra trước khi điền phiếu. Ô đơn vị, điều kiện hoặc trang có thể để trống khi bảng nguồn chưa xác lập thông tin tương ứng ở mức có thể tách riêng. [Bảng nguồn](../../../integrity/source_review_887/source_review_887.csv) · [Báo cáo đối chiếu](../../../integrity/source_review_887/report.pdf)

Từ thư mục này, chạy `python3 -B record_source_endorsements.py 2026-11-27 --check` để kiểm tra hai phiếu đã lưu. Để tái tạo, dùng bản trắng của hai phiếu tại commit `1123203` trong một thư mục tạm rồi chạy lại lệnh với `--packet <thư_mục_tạm>` thay cho `--check`. SHA-256 của bảng nguồn là `8128156c04562d626965e38963bda056f034d517afcdd10a8343ce093b83ade1`.

Bản sao 136 PDF đã kiểm tra SHA-256 nằm trong [thư mục PDF cục bộ](../../../fulltext_retrieval/pdf/human_review_full_136/). PDF nguồn được lưu cục bộ theo điều kiện truy cập.

## Điều phối đánh giá độc lập

1. Tạo một thư mục PDF riêng trên máy bằng `python3.11 -B build_human_review_packet.py --materialize-pdfs /đường/dẫn/nội/bộ` từ thư mục cha của gói. Lệnh kiểm tra SHA-256 rồi sao chép 136 PDF dưới mã trung lập `HKF-001` đến `HKF-136`. Chỉ cung cấp bản PDF theo điều kiện truy cập của từng nguồn. R0082 trong tập này dùng bản arXiv đã lưu của bản ghi. Bản IEEE đã kiểm chứng có thể được đối chiếu riêng theo DOI và SHA-256 trong hồ sơ xuất bản.
2. Gửi mỗi người bộ PDF mã hoá và bản sao phiếu `screening.csv` của riêng họ. Người điều phối giữ `coordinator/key.csv`, `coordinator/exclusion_coverage.csv`, hồ sơ S2, bản thảo và kết quả AI cho đến khi nhận đủ hai phiếu sàng lọc. Hai người làm riêng và ghi mã người chấm, ngày ISO 8601, quyết định, lý do và trang vật lý. Lưu nguyên hai bản trước hoà giải. Ghi `INCLUDE`, `EXCLUDE` hoặc `AWAITING_CLASSIFICATION`; chọn một lý do E1–E7 theo thứ tự E5 → E6 → E1 → E7 → E2 → E3 → E4 của [giao thức](../../../protocol_restart.md#p06--selection-and-retrieval-steps0709) hoặc ghi bằng chứng cần bổ sung cho hồ sơ chờ.
3. Khi đã khoá hai phiếu, đối chiếu bằng mã đã cấp. Báo số cặp đủ dữ liệu, bảng chéo, tỷ lệ đồng thuận và Cohen's kappa khi xác định được. Báo tỷ lệ đồng thuận trên toàn bộ cặp đã hoàn tất, với mẫu số tối đa là 136. Có thể trình bày thêm theo nhóm quyết định và lý do loại đã lưu. Một người điều phối giải quyết bất đồng bằng nguyên văn, trang và lý do rồi trình tác giả xác nhận trước mọi cập nhật S2 hay PRISMA.
4. Sau khi khoá phiếu sàng lọc, giao phiếu `source_verification.csv` để đọc lại nguồn. Giữ nguyên kết quả sàng lọc độc lập dù phát hiện chênh lệch ở bước sau. Dùng sáu dòng kỹ thuật mỗi bài theo tiêu đề cột S4, từng dòng số liệu và phán định độ phủ, cùng mười tiêu chí của [khung thẩm định](../../../../manuscript/sn_computer_science/main.tex#L92). Trước khi so với kết quả đã trích, ghi giá trị hoặc phán định từ tài liệu, đơn vị, mẫu số hoặc điều kiện đo, trang vật lý và mục/bảng/hình. Nếu thiếu, dùng `NOT_REPORTED` hoặc `UNRESOLVED` kèm lý do. Với `report_coverage`, dùng `VERIFIED_EXACT`, `PLOT_ONLY` hoặc `PRINTED_UNRESOLVED` theo [quy tắc S3](../../../extraction/rq5_uniform/rule.md). Phiếu cung cấp vị trí đọc gợi ý. Ghi một kết quả theo mỗi hàng và nêu mọi chênh lệch trước khi đề nghị sửa sổ tổng hợp.

Bộ phiếu sàng lọc bao phủ 136/136 báo cáo đã đánh giá toàn văn, gồm 46 bài đưa vào và toàn bộ 90 bài loại theo quyết định đã lưu. Mã PDF và thứ tự từng phiếu lấy từ các thứ hạng SHA-256 khác nhau. Bộ mã `HKF-*` dành cho bản 136 hồ sơ, dùng cùng các phiếu mới. [Mã sinh gói](../build_human_review_packet.py) lưu seed và quy tắc. Có 887 dòng kiểm tra nguồn cho mỗi phiếu: 276 nhóm trường kỹ thuật, 105 mục số liệu gồm mục giữ và mục treo hoặc liên kết, 46 phán định độ phủ và 460 phán định thẩm định kỹ thuật. Nếu kết quả sàng lọc thay đổi tập chọn, lập bổ sung cho các nghiên cứu được xác nhận thêm.
