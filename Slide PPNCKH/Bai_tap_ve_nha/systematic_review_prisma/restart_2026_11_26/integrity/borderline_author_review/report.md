# HK261 — Báo cáo thẩm định 5 hồ sơ biên

**Phạm vi.** Cả 5 hồ sơ hiện mang trạng thái đưa vào trong S2 và chưa có xác nhận của tác giả. Đợt này rà E2 (bối cảnh nhiều UAV được đánh giá), E3 (phân bổ, chuyển giao hoặc điều phối suy luận mạng nơ-ron), E4 (đánh giá phương pháp suy luận) và E7 (loại ấn phẩm, phản biện, phương pháp và kết quả). Áp dụng [§P03 của giao thức HK261](../../protocol_restart.md). Trang dưới đây là **số trang vật lý của PDF**, tính từ 1.

**Cách chốt.** Sau khi xem các trang gợi ý, ghi **Giữ**, **Loại — mã E…**, hoặc **Chờ — mã E…** cho từng mã bài. Bạn có thể đồng ý toàn bộ, hoặc sửa một số quyết định và nêu trang/lý do nếu có. Một lựa chọn **Chờ** ghi nhận việc tác giả đã xem hồ sơ và giữ quyết định mở. Xác nhận từ bạn là thẩm định của một tác giả có AI hỗ trợ. Chỉ tiêu hai người đọc độc lập được ghi riêng.

## Khuyến nghị để tác giả duyệt

| Mã | Gemini sau lượt sửa | Đề xuất để bạn chốt | Căn cứ quyết định |
|---|---|---|---|
| R0001 | Giữ | **Giữ** | Hai điểm cắt DNN. Thử nghiệm mô phỏng báo cáo phần thưởng. IEEE xác nhận track WIP và chính sách phản biện của kỳ đó. |
| R0113 | Chờ E3, E7. Gemini ghi nhận có đánh giá framework ở E4 | **Chờ E3** | Chưa nối được embedding giữa các UAV với một lần chạy suy luận đã đánh giá. Do đó E4 đối với suy luận hợp tác còn mở. E7 cũng cần làm rõ nếu E3 được xác lập. |
| R0145 | Giữ | **Giữ** | Có gán yêu cầu LLM tại UAV hoặc cloud theo kết nối và thí nghiệm cấp hệ thống trên 10 UAV. |
| R0223 | Giữ | **Giữ** | Có điều phối nhận diện tại UAV và suy luận phía máy chủ. Hình 7 và Bảng 2 nối kiến trúc với thí nghiệm. |
| R0292 | Chờ E7 | **Chờ E7** | Có chuyển giao công việc theo dõi bằng mạng nơ-ron và đánh giá handoff ở mức HIL. Còn thiếu minh chứng về cơ chế phản biện của track DroNet 2025. |

Mức ghi nhận tại thời điểm rà là **3/136 hồ sơ đã được tác giả xử lý, 0 hồ sơ có hai quyết định độc lập**. Audit S2 và PRISMA xác nhận **46 đưa vào, 89 loại, R0082 chờ E7**. Cả năm đề xuất trong bảng đang chờ quyết định của bạn.

## PDF gốc và căn cứ để quyết định

### R0001 — Phân chia DNN giữa UAV, edge và cloud

- **E2/E3.** Tr. 2 §II.A–B và tr. 3 §III.A. Hai điểm cắt xác định phần thực thi trên UAV, máy chủ biên và cloud. Mô phỏng nêu cấu hình 10 UAV, 4 máy chủ biên và 1 cloud. [PDF gốc R0001](../../fulltext_retrieval/pdf/R0001.pdf)
- **E4/E7.** Tr. 3 Hình 2–3 trình bày mức hội tụ của phần thưởng và phần thưởng theo trọng số độ trễ. Đây là số đo báo cáo trong điều kiện mô phỏng, nên chưa dùng để trích độ trễ hoặc năng lượng riêng. Tr. 2–3 có phương pháp phân chia và đánh giá. Chương trình IEEE ghi đúng bài ở mục WIP CWS_WIP_222. Hướng dẫn tác giả của cùng kỳ có quy định phản biện bản nộp và mức trang cho WIP. §P03 cho phép tác giả xét báo cáo ngắn có phương pháp và kết quả đủ nhận diện. [Chương trình ICWS](https://services.conferences.computer.org/2026/icws-program/) · [Hướng dẫn IEEE SERVICES 2026](https://services.conferences.computer.org/2026/info-for-authors/)

### R0113 — SNN, graph message passing và continual learning

- **E2.** Tr. 9, đầu mục “Implementation and Results”, mô tả mô phỏng nhóm 40 UAV và đề cập cả HIL. [PDF gốc R0113](../../fulltext_retrieval/pdf/R0113.pdf)
- **E3/E4.** Đọc tr. 7–9 trước, rồi các bảng và hình trong phần kết quả tr. 10–14. Tr. 7 mô tả các UAV trao đổi “compact navigation embeddings”; tr. 9 gắn GNN với liên lạc và SNN với xử lý ảnh theo sự kiện. Chưa truy được đường đi của embedding trong lần suy luận dùng để tạo một kết quả cụ thể. Bảng 4 ở tr. 13 có đối chiếu thêm thành phần Graph Coordination, song các chỉ số được báo cáo ở cấp điều hướng và phối hợp. Bảng chưa chỉ ra kết quả nào đo luồng suy luận qua nhiều UAV, hoặc kết quả nào chạy trong HIL.
- **E7.** Tr. 1 cung cấp lịch sử nhận/chấp nhận/xuất bản. §8 hướng dẫn của chính tạp chí công bố phản biện kín hai chiều. Đây là bằng chứng về chính sách. Thiếu DOI hoàn chỉnh và thời gian xử lý công bố ngắn tự chúng không xác định hồ sơ trượt E7. Giới hạn nội dung phương pháp/đánh giá vẫn cần xét cùng E3/E4. [Hướng dẫn tác giả AJACCM, §8](https://ajaccm.com/journal/index.php/ajaccm/author-guidelines) · [Hồ sơ bài trên tạp chí](https://ajaccm.com/journal/index.php/ajaccm/article/view/771)

### R0145 — Gán yêu cầu LLM theo kết nối UAV–cloud

- **E2/E3.** Tr. 6 §3.1/Hình 2. UAV có kết nối gửi quan sát lên LLM lớn trên cloud, còn UAV mất kết nối chạy LLM nhỏ tại chỗ. Đây là gán yêu cầu suy luận LLM cho cả một nút. §P03 cho phép gán như vậy ở hệ phân cấp UAV–cloud. [PDF gốc R0145](../../fulltext_retrieval/pdf/R0145.pdf)
- **E4.** Tr. 17–18 §6.2/Hình 7–10 so sánh cấu hình chỉ LLM nhỏ, chỉ LLM lớn và hỗn hợp trong kịch bản cố định 10 UAV. Phần này đo thời gian giao tiếp, thời gian suy luận và chi phí tính toán. Nó bổ sung thí nghiệm cấp hệ thống bên cạnh phép đo từng mô hình. Đây là điểm phải sửa so với nhận định sơ bộ rằng bài chỉ đo mô hình riêng lẻ.
- **E7.** PDF là bản ACM “Just Accepted” với lịch sử biên tập ở tr. 22. Metadata do ACM nộp xác nhận DOI và bản ghi bài báo tạp chí. [Bản ghi Crossref của ACM](https://api.crossref.org/works/10.1145/3774655) · [Chính sách ACM, “Categories of publications”](https://prod-www.acm.bloomreach.cloud/publications/policies/pre-publication-evaluation)

### R0223 — Điều phối LLM/VLM và nhận diện tại UAV

- **E2/E3.** Tr. 3–4 §3.2/Hình 3 và tr. 7 Hình 7. LLM phân tách lệnh thành phần nhận diện và lập đường cho từng UAV. Hình 7 cho thấy thay đổi đường gọi mô hình giữa các cấu hình, gồm Grounding DINO tại UAV và mô hình đa phương thức phía máy chủ ở cấu hình Master. Cuối tr. 3 mô tả dùng kết quả nhận diện làm đầu vào phản hồi cho LLM để cập nhật đồ thị tác vụ. Cấu hình minh họa ở tr. 4 sử dụng phản hồi từ UAV báo đầu tiên. Cơ sở E3 cần xét ở mức điều phối các phép suy luận dùng cho nhiệm vụ nhận diện, trong đó quy tắc chọn một phản hồi không chứng minh có hợp nhất tensor/đặc trưng. [PDF gốc R0223](../../fulltext_retrieval/pdf/R0223.pdf)
- **E4.** Tr. 5 §4.2 và tr. 7 Bảng 2 so sánh bốn cấu hình ở cấp hệ thống, theo tỷ lệ thành công, thời gian phản hồi lập kế hoạch và thời gian hoàn thành nhiệm vụ. Phần §4.1/Bảng 1 chỉ đối chiếu bộ lập đường PPO và không đủ nếu đứng riêng để xác lập E4 cho kiến trúc LLM/VLM.
- **E7.** Tr. 1 định danh đúng kỷ yếu ACAIB 2025. Mục công bố của thông báo chính kỳ 2025 nêu bản nộp được chuyên gia ban chương trình phản biện, bài được nhận xuất bản trong ACM ICPS. [Thông báo ACAIB 2025, mục công bố](https://www.ais.cn/attendees/index/FNJRAJ) · [Bản ghi Crossref của ACM](https://api.crossref.org/works/10.1145/3760269.3760299)

### R0292 — Chuyển trách nhiệm chạy bộ theo dõi giữa hai UAV

- **E2/E3.** Tr. 3 §4 và tr. 4 §4.1/Hình 3. Hai UAV có pipeline theo dõi dựa trên học sâu. D1 truyền dữ liệu theo dõi cho D2 qua Wi‑Fi để D2 tiếp quản nhiệm vụ. Tr. 3 §3.3 nêu ORB để so khớp mẫu giữa hai góc nhìn. Nếu áp dụng nhánh “chuyển giao yêu cầu suy luận” của E3, đối tượng chuyển giao là việc tiếp tục chạy bộ theo dõi mục tiêu, còn ORB là bước hỗ trợ nhận lại mục tiêu. [PDF gốc R0292](../../fulltext_retrieval/pdf/R0292.pdf)
- **E4.** Tr. 5 §5.2, Bảng 3 và Hình 5 có kết quả ghép mẫu D1–D2 và mô tả HIL bao gồm theo dõi ảnh, ghép đặc trưng và điều phối giữa UAV. Đây là bằng chứng thử nghiệm của hệ thống handoff ở mức HIL và trên dữ liệu ghi hình. Phép đo riêng trên bộ tracker ở §5.1 không tự xác lập E4 cho handoff. Cỡ padding ở đoạn mô tả tr. 5 và Bảng 3 có chênh lệch, nên không dùng số đó để chốt.
- **E7.** DOI tr. 1 và dữ liệu Crossref khớp. Macquarie giải thích hai biến thể “Tracking” và “Monitoring” của tiêu đề. Mục lục DBLP đặt bài dưới DroNet và MobiSys xác nhận DroNet là workshop chính thức của kỳ 2025. CFP giới thiệu quy trình nộp và thông báo quyết định, nhưng chưa xác lập quy tắc phản biện của bài hoặc track. Trang hạn nộp HotCRP nêu bài nộp đúng hạn mới được xem xét. Trang đó chưa mô tả cơ chế phản biện của track. Trạng thái chờ E7 có thể được chốt mà vẫn giữ ghi chú về phần phương pháp đã quan sát. [MobiSys 2025, mục DroNet](https://www.sigmobile.org/mobisys/2025/accepted_workshops/) · [Mục lục, mục DroNet](https://dblp.org/db/conf/mobisys/mobisys2025.html) · [DroNet 2025 CFP](https://sites.google.com/view/dronet2025/) · [Mốc nộp bài HotCRP](https://dronet25.hotcrp.com/deadlines) · [Hồ sơ Macquarie](https://researchers.mq.edu.au/en/publications/continuous-marine-monitoring-via-autonomous-uav-handoff/)


## Đối chiếu kết quả Gemini và lưu vết

Gemini.app trả nhận định cho năm hồ sơ rồi sửa theo phản hồi của Codex. Lượt sửa đầu bị mất quyền đọc PDF khi app chuyển sang worker. Lượt kiểm tra tiếp theo đối chiếu được năm đoạn thân bài với năm PDF. Lượt sửa cuối chạy trực tiếp trong một lượt Gemini. Kết quả từng lượt có trong [phản hồi gốc](gemini-initial-receipt.json), [lượt sửa bị lỗi truy cập](gemini-correction-receipt.json), [kiểm tra quyền đọc](access-review.md) và [phản hồi sửa cuối](gemini-parent-correction-receipt.json). [Manifest nguồn](manifest.json) ghi đường dẫn và SHA‑256 của bản PDF đã đối chiếu.

| Kiểm tra | Kết quả | Bằng chứng |
|---|---|---|
| Đủ mã, danh tính và tiêu chí | PASS | 5/5 mã như brief, 0 trùng mã, DOI hoặc tiêu đề chuẩn hoá. Bản gốc trả 20/20 ô. Lượt sửa cuối trả đủ 15/15 ô cần sửa với một dấu kết thúc. |
| Đọc PDF và truy vết các căn cứ trong báo cáo | PASS | 5/5 đoạn kiểm tra quyền đọc đối chiếu đúng PDF và trang. Các căn cứ dùng trong bảng khuyến nghị được đối chiếu theo PDF gốc hoặc nguồn xuất bản. Hình 2–3 của R0001, Hình 7–10 của R0145, Hình 7/Bảng 2 của R0223 và Bảng 3/Hình 5 của R0292 được xem trực tiếp trên trang PDF render bằng Apple PDFKit. |
| Nguyên văn và mức bằng chứng của toàn bộ phản hồi sửa | FAIL | Một số dẫn URL chung của ACM không tái lập được trực tiếp từ Codex. R0292 có trích đoạn ghép qua chỗ xuống dòng và cụm mã cấu hình chưa khớp nguyên văn. Không dùng số lượt nhận bài DroNet trong kết luận. R0113 có bảng đánh giá framework nhưng chưa truy được kết quả của luồng suy luận hợp tác. Các căn cứ trong bảng được đối chiếu lại từ nguồn gốc. |
| Số liệu đưa vào báo cáo | PASS | 0 điểm đọc ước lượng từ biểu đồ. Ba quy mô mô phỏng dùng trong báo cáo đối chiếu R0001 tr. 3, R0113 tr. 9 và R0145 tr. 17. |
| Hồ sơ còn mở và việc dùng worker | PASS | Lượt cuối báo 0 worker. R0113 còn mở ở E3, E4 liên quan và E7. R0292 còn mở ở E7. Ba bài còn lại khớp với đề xuất giữ của lượt Gemini cuối. |
| Lưu kết quả và dọn chat | FAIL | Phản hồi cuối được lưu và trả về trọn vẹn. Bridge ghi lỗi Missing AXGroup[0] khi xác minh dọn chat. Kiểm tra đọc sau đó thấy app ở Gemini — New chat, không có bản nháp, tệp gắn hay lượt đang chạy. Chưa kiểm chứng riêng việc xóa chat theo UUID. |

Điểm khác với phản hồi gốc là R0145 và R0223 có căn cứ giữ theo phạm vi E3 đã khóa, còn đề xuất loại R0292 theo E3 chuyển thành chờ E7. R0113 ghi nhận việc tạp chí công bố chính sách phản biện, song chưa có đủ căn cứ để khẳng định quy trình phản biện đối với hồ sơ này. Hai văn bản AJACCM dùng cả tên viết tắt của ấn phẩm khác và các cách mô tả số người phản biện khác nhau. Các tín hiệu đó giới hạn mức chắc chắn về chính sách áp dụng. [Hướng dẫn tác giả AJACCM](https://ajaccm.com/journal/index.php/ajaccm/author-guidelines) · [Chính sách tạp chí AJACCM](https://ajaccm.com/journal/index.php/ajaccm/policies)
