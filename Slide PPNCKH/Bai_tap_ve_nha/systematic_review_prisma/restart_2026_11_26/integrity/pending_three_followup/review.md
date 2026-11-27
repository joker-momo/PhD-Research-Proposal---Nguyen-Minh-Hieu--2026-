# Minh chứng để tác giả chốt ba hồ sơ HK261

Áp dụng [giao thức HK261 §P03](../../protocol_restart.md). Các số trang PDF bên dưới tính từ trang đầu tệp. Đây là đề xuất. PRISMA tại thời điểm rà vẫn có 44 đưa vào, 89 loại và 3 chờ. Kết quả này chưa được ghi vào S2 hay dùng để thay đổi tập tổng hợp.

## R0082 — LLHR

**Đề xuất giữ chờ E7 vì chưa đối chiếu được toàn văn của bản IEEE.** Đã xác minh danh tính công bố và chính sách phản biện.

- Bản [PDF đang lưu](../../fulltext_retrieval/pdf/R0082.pdf) in dấu arXiv:2305.15858v1 ở trang 1. Trang 2 §I mô tả phân chia các lớp CNN giữa nhiều UAV. Trang 5 §IV báo cáo đánh giá mô phỏng với LeNet và AlexNet. Đây là các vị trí nên đối chiếu với bản IEEE khi mở được. [Bản ghi arXiv v1 và DOI liên kết](https://arxiv.org/abs/2305.15858v1)
- Mục **UAVS AND COMMS** của mục lục WCNC 2023 liệt kê đúng tiêu đề và ba tác giả. Bản ghi do IEEE nộp tại Crossref có DOI 10.1109/WCNC55385.2023.10118908 và loại tài liệu proceedings-article. Mục **About Conference Peer Review** của IEEE Author Center nêu yêu cầu phản biện bài hội nghị. Hồ sơ HBKU đánh dấu đúng bài này là peer-review. [Mục lục WCNC](https://www.proceedings.com/content/069/069069webtoc.pdf) · [Crossref](https://api.crossref.org/works/10.1109/WCNC55385.2023.10118908) · [Quy định IEEE](https://conferences.ieeeauthorcenter.ieee.org/understand-peer-review/) · [Hồ sơ HBKU](https://elmi.hbku.edu.qa/en/publications/llhr-low-latency-and-high-reliability-cnn-distributed-inference-f/)
- IEEE Xplore trả trang kiểm tra trình duyệt hoặc không trả PDF qua các đường toàn văn đã thử. Hồ sơ HBKU dẫn về DOI. OpenAlex chỉ liệt kê arXiv là đường toàn văn công khai. Chưa kiểm tra được các trang phương pháp và kết quả của bản xuất bản. [IEEE Xplore](https://ieeexplore.ieee.org/document/10118908) · [OpenAlex, locations](https://api.openalex.org/works/https://doi.org/10.1109/WCNC55385.2023.10118908)

## R0113 — Hemasri và Reddy

**Đề xuất giữ chờ E3.** E4 cho đúng luồng suy luận hợp tác và E7 còn mở.

- Trang 7 (trang in 454) mô tả trao đổi embedding và tổng hợp thông tin bằng graph message passing. Công thức trang 7 và chú giải trang 8 đưa thông tin phối hợp đồ thị vào biểu thức quyết định điều hướng. Sơ đồ trang 8 không mô tả phép toán mạng nơ-ron nhận embedding từ UAV khác. Trang 9 mô tả vai trò của GNN và các thí nghiệm ở cấp hệ thống. [PDF bài báo](../../fulltext_retrieval/pdf/R0113.pdf)
- Trang 12 (trang in 459) nhắc lại việc trao đổi embedding trong phần thí nghiệm khả năng mở rộng. Trang 13 (trang in 460), Bảng 4, có cấu hình thêm Graph Coordination nhưng báo cáo kết quả cấp điều hướng, năng lượng, học liên tục và phối hợp. Bài không chỉ ra kết quả nào đến từ một lần chạy suy luận với đường truyền embedding và phép toán nhận xác định. PDF được tải trực tiếp từ trang tạp chí và trùng SHA-256 với tệp dự án. Chưa thấy tài liệu bổ sung hoặc mã trên trang bài để nối hai phần này. [PDF trên AJACCM](https://ajaccm.com/journal/index.php/ajaccm/article/download/771/716) · [Trang bài 771](https://ajaccm.com/journal/index.php/ajaccm/article/view/771)
- AJACCM công bố quy trình phản biện kín hai chiều tại **Author Guidelines §8**. Trang **Policies → Peer Review Policy** mô tả quy trình chung và phần khác trên cùng trang dùng tên viết tắt AJMIMC. Trang bài cung cấp lịch sử nhận/chấp nhận/xuất bản trong PDF và metadata DOI thiếu hậu tố. Các điểm này chưa xác minh được quy trình áp dụng cho bài cụ thể. [Author Guidelines §8](https://ajaccm.com/journal/index.php/ajaccm/author-guidelines) · [Policies](https://ajaccm.com/journal/index.php/ajaccm/policies)

## R0292 — Kim và cộng sự

**Đề xuất đưa vào.** Minh chứng phản biện đến từ đúng kỳ DroNet 2025 và khớp với bài trong kỷ yếu.

- Trang **SUBMISSIONS** chính thức, đoạn đầu, nêu nguyên văn “DroNet follows a single-blinded review process.” Cùng đoạn đó mô tả các loại bài và giới hạn độ dài. **TECHNICAL PROGRAM → Session #3** liệt kê đúng bài *Continuous Marine Monitoring via Autonomous UAV Handoff* và bảy tác giả. Đây là quy trình áp dụng ở cấp workshop. [DroNet Submissions](https://sites.google.com/view/dronet2025/submissions) · [DroNet Program](https://sites.google.com/view/dronet2025/program) · [SIGMOBILE, Accepted Workshops](https://sigmobile.org/mobisys/2025/accepted_workshops/)
- DOI 10.1145/3711875.3737661 trên trang 1 PDF khớp bản ghi do ACM nộp tại Crossref, loại proceedings-article, trang kỷ yếu 711–716. Macquarie University xác nhận biến thể tiêu đề *Tracking* trong PDF, đánh dấu peer-review và liệt kê bản xuất bản tại mục **Access to Document**. [Crossref](https://api.crossref.org/works/10.1145/3711875.3737661) · [Macquarie](https://researchers.mq.edu.au/en/publications/continuous-marine-monitoring-via-autonomous-uav-handoff/)
- Trang 4 §4.1 và Hình 3 mô tả D2 tiếp nhận trách nhiệm theo dõi. Trang 5 §5.2, Bảng 3 và Hình 5 mô tả kết quả ghép mẫu và thử nghiệm hệ thống hardware-in-the-loop (HIL). [PDF bài báo](../../fulltext_retrieval/pdf/R0292.pdf)


## Kiểm tra phản hồi Gemini.app

Bản đầu và bản sửa đầu được lưu riêng để tra soát. Chúng không qua kiểm tra định dạng hoặc vị trí trích dẫn. Lần kiểm tra cuối ghi rõ Gemini không mở được hai trang chính thức DroNet. Codex mở trực tiếp cả hai trang và tự xác minh căn cứ R0292. Vì thế đề xuất cuối cho R0292 khác đề xuất dựa trên nguồn Gemini đọc được.

Task 6f08b491-4311-4d89-b6ed-85b440d1cba0, context 198f8cf4-10b2-44a0-996b-e59dba35ff92. Kết quả gốc và hai lượt trước có biên nhận riêng trong thư mục. Cầu nối xác nhận đã xóa đúng ba chat đã lưu kết quả. Lần thử đầu lỗi trước Send chưa tạo phản hồi.

| Kiểm tra lần cuối | Kết quả | Đối chiếu |
|---|---|---|
| Đúng khóa và JSONL | PASS | 4/4 khóa, không khóa trùng hay ngoài phạm vi, 5 dòng parse được. Footer có trường bổ sung mô tả phần thiếu. |
| Định danh các bài | PASS | 3/3 định danh ở các lượt phù hợp PDF và nguồn gốc, gồm hai DOI hoàn chỉnh và DOI_NOT_FOUND cho bài 771. Không trùng khóa hoặc DOI hoàn chỉnh. |
| Truy vết các trường Gemini đánh dấu VERIFIED | PASS | 2/2 trường đối chiếu được. R0082 Related DOI trên arXiv và R0113 DOI hiển thị cùng HTML citation_doi trên trang bài. |
| Gemini truy hồi hai trang DroNet | FAIL | 0/2 theo phản hồi. Cả hai ghi NOT_ACCESSIBLE, trích đoạn để trống. Codex độc lập nhận HTTP 200 và xác minh 2/2 trường ở đúng trang. |
| Giới hạn suy diễn và số liệu | PASS | 0 kết quả định lượng hoặc số lượt nhận bài dùng để chốt. Thiếu toàn văn R0082 và phần kỹ thuật R0113 được ghi riêng. |
| Báo cáo phần thiếu và worker | PASS | Footer báo thiếu hai trang DroNet đối với Gemini, trạng thái chưa hoàn tất và không có worker. Đề xuất E7 của Gemini đối với R0292 chỉ phản ánh khả năng truy cập của Gemini. |
| Bằng chứng đề xuất cho tác giả | PASS | Codex đối chiếu 3/3 kết luận với §P03, trang PDF gốc, các trường xuất bản và, với R0292, quy trình của chính DroNet 2025. Bảng 4 của R0113 và Hình 3, Bảng 3, Hình 5 của R0292 được xem trên trang PDF render bằng Apple PDFKit. |
| Bảo toàn đầu vào và hồ sơ | PASS | Ba PDF và giao thức khớp 4/4 SHA-256 trước/sau ở cả bản làm việc và thư mục nguồn. Phạm vi Git chỉ gồm nhật ký nghiên cứu, trạng thái công việc và hồ sơ minh chứng này. |

Kết luận để tác giả xác nhận lần lượt là **R0082 giữ chờ E7**, **R0113 giữ chờ E3** và **R0292 đưa vào**. Hai trang DroNet đã được kiểm chứng trực tiếp, nên không sử dụng đề xuất giữ chờ R0292 trong phản hồi Gemini.
