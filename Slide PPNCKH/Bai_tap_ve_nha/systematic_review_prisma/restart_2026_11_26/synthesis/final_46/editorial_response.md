# Xử lý nhận xét biên tập HK261

Cơ sở đối chiếu là bản 29 trang tại commit `360d8d2`. Bản dựng hiện tại và bản gốc nằm cạnh [nguồn LaTeX](../../../manuscript/sn_computer_science/main.tex). PRISMA giữ 46 đưa vào, 90 loại, 0 chờ trong cả hai bản.

| Ý kiến biên tập | Xử lý và minh chứng |
| --- | --- |
| Bảng 8 cần phân biệt tác giả với hai người chấm | Tóm tắt và Bảng 8 ghi 8/136 quyết định tác giả xác nhận, 128 chưa có xác nhận, 0/0 quyết định từ hai người chấm độc lập, 0 cặp và kappa chưa xác định. [JSON kiểm toán](../../../manuscript/sn_computer_science/audit_summary.json). |
| Cần thực sự đọc toàn bộ bài chọn và mẫu phân tầng bài loại | Bộ phiếu ban đầu có 68 hồ sơ. Theo yêu cầu tiếp theo của tác giả, [hai bộ phiếu trắng](human_review_packet/README.md) hiện bao phủ 136 hồ sơ, gồm toàn bộ 46 bài chọn và 90 bài loại. Đã đối chiếu SHA-256 cho cả 136 PDF. Có 887 dòng đối chiếu nguồn cho mỗi người. Thẩm định sàng lọc và xác minh trích xuất của con người vẫn chưa được thực hiện. |
| R0145 và R0223 cần quyết định phạm vi và căn cứ | Giữ hai quyết định đưa vào đã được tác giả xác nhận theo E3 mức gán yêu cầu và E4 mức cấu hình. Xem căn cứ từng bài bên dưới và [quyết định S2](../../../manuscript/sn_computer_science/supplement_s2_adjudication.md). |
| Đối chiếu LLHR với IEEE chính thức | Bản IEEE do tác giả cung cấp xác nhận danh tính và DOI ở trang 1. [Kiểm tra](r0082_publisher_crosscheck.json) khớp 6/6 neo trích xuất, 10/10 neo thẩm định kỹ thuật và 4/4 chú thích hình ở cùng trang vật lý. Phần kết quả §IV, Hình 2–5 (tr. 5–6) vẫn là đồ thị. Không có số đọc ước lượng. S2 giữ nguyên bản ghi lúc tác giả chốt. [Hồ sơ và cách đối chiếu](r0082_review.md). |
| Hai hệ mã phân mảnh và đánh giá | [Một sổ mã](../../../manuscript/sn_computer_science/technical_coding.psv) áp dụng cho Bảng 2, 4, 5, Hình 2d và Hình 4 theo các chiều liên quan. Phân mảnh 17/8/6/6/9; modality 1 phân tích, 27 mô phỏng, 10 trace/profile, 7 bench và 1 outdoor. Bench có thể là đo thành phần. |
| §5.2 Level 2 dẫn nhầm Promise | Trích R0045 cho di trú theo ngưỡng (tr. 11, §IV.B.3–C) và R0292 cho HIL (tr. 4–5, §§4.1, 5.2). Promise (R0002) vẫn được dẫn tại Level 5 cho lỗi mô phỏng. |
| Bảng 5 cắt ngang Bảng 4 | Chặn float tại cuối Bảng 4 và sau Bảng 5. Xác minh bằng nhãn LaTeX và ảnh trang cuối Bảng 4, trang đầu Bảng 5. |
| Ký hiệu Bảng 1 và Bảng 8 | Đã mở rộng đệm Bảng 1 và xem dấu kiểm. Dòng Bảng 8 hiển thị cả chữ “kappa” và ký hiệu κ; phần trích văn bản có đủ hai thành phần. |
| Chữ, dấu câu và tràn cột trong §4.3, Bảng 3, 4 và 6 | Đã sửa cách in liên kết trong câu, tách năm khỏi số tham khảo chủ động, chuẩn hoá tên mạng đã gắn cờ và xử lý dòng hẹp Bảng 4. Bảng 6 giữ nguyên hai số và hiển thị dấu gạch chéo cùng cụm mean ± CI. |
| Tài liệu [6], [20], [49] | Đổi họ tác giả [20] về kiểu viết tên chuẩn. [6] và [49] được xác minh trong nguồn BibTeX, BBL và PDF đều có chữ Latin p. Các dải trang tương ứng là 1–6 và 1280–1285. |
| Tuyên bố và điều kiện nộp | Còn cần hai phiếu người chấm, bằng chứng kiểm tra trích xuất do người thực hiện và xác nhận các tuyên bố tác giả trước khi chuẩn bị hồ sơ nộp. |

## Hai ca biên

- **R0145 (Xiao và cộng sự).** [PDF](../../fulltext_retrieval/pdf/R0145.pdf), tr. 6, §3.1 và Hình 2 nêu gán yêu cầu LLM nhỏ tại UAV hoặc LLM lớn ở cloud theo kết nối. Tr. 17–18, §6.2 và Hình 7–10 đối chiếu ba chính sách dùng mô hình trong kịch bản 10 UAV. Bằng chứng hỗ trợ điều phối yêu cầu trong mô phỏng và so sánh cấu hình. Tác động riêng của quy tắc gán và khả năng vận hành ngoài thực địa chưa được xác lập.
- **R0223 (Wang và Deng).** [PDF](../../fulltext_retrieval/pdf/R0223.pdf), tr. 3–4, §3.2 và Hình 3 nêu cách phân vai LLM/VLM và phản hồi nhận diện cho đồ thị tác vụ. Tr. 5 §4.2 và tr. 7 Hình 7, Bảng 2 nối các vai suy luận với bốn cấu hình thử nghiệm. Mức chứng cứ là điều phối yêu cầu nhận diện và lập kế hoạch. Không có phép thử tách riêng tác động của cơ chế phân công, và việc dùng báo cáo đến đầu tiên không chứng minh hợp nhất đặc trưng.
- **Độ nhạy phạm vi.** Bỏ riêng từng bài còn 45 báo cáo và 96 mục giữ. Bỏ cả hai còn 44 báo cáo, 7 thay vì 9 bài dispatch, 34 thay vì 36 bài đóng góp số liệu và 94 thay vì 98 mục. Cả bốn kịch bản có 51 mục đối sánh. [Dữ liệu tính lại](scope_sensitivity.json) · [S3](../../../manuscript/sn_computer_science/supplement_s3.md).

Mức đánh giá thẩm định con người phụ thuộc vào hai bộ phiếu đã điền và hồ sơ đối chiếu do người thực hiện. Phần hồ sơ kỹ thuật có thể kiểm tra lại từ [S4](../../../manuscript/sn_computer_science/supplement_evidence_index.md) và [gói minh chứng](../../../manuscript/sn_computer_science/minh_chung_hinh_bang/README.md).

## Đối chiếu bản dựng

Bản PDF mới có 30 trang. Bảng 4 kết thúc ở trang 20; Bảng 5 bắt đầu ở trang 21; Bảng 8 ở trang 25. Đối chiếu PDF và mã phụ LaTeX xác nhận đủ 16 nhãn với vị trí đúng trong S4. Tám kiểm thử S2/PRISMA đều đạt. S4 kiểm tra 164 mục nhận định, 46 dòng nghiên cứu, chín đối chiếu định lượng và 49 mã băm PDF nguồn của tập hồ sơ trước khi bổ sung bản IEEE. Kiểm tra riêng bản IEEE dùng mã băm và 20 neo trong biên nhận. Bản dựng độc lập từ gói minh chứng khớp ảnh kết xuất trên cả 30 trang.
