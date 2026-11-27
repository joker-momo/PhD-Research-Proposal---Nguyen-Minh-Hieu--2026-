# Truy hồi bổ sung ba hồ sơ ACM

Gemini.app trả về đủ 3 ID trong một tác vụ, báo không dùng worker và không xác minh được PDF nào. Codex kiểm tra độc lập Crossref, OpenAlex và URL PDF ACM cho cả ba. Tệp cấu hình đã được khôi phục với SHA-256 trùng bản gốc. Tác vụ chỉ ghi bằng chứng truy hồi, không cập nhật số liệu hoặc quyết định PRISMA.

| ID | Nguồn và kết quả đã kiểm | Phiên bản, số trang PDF, trang đầu |
|---|---|---|
| R0096 | URL PDF ACM trả HTTP 403. Crossref xác nhận DOI, tiêu đề, 5 tác giả, năm và kỷ yếu. OpenAlex ghi hybrid CC BY và không có URL PDF riêng. ResearchGate hiện không có toàn văn. Gemini báo REDI CEDIA hiện trạng thái hạn chế, còn lần kiểm độc lập REDI hết thời gian chờ. [ACM PDF](https://dl.acm.org/doi/pdf/10.1145/3714394.3756181) · [Crossref](https://api.crossref.org/works/10.1145/3714394.3756181) · [REDI CEDIA](https://redi.cedia.edu.ec/document/525712) · [ResearchGate](https://www.researchgate.net/publication/399171598_ARIES_Autonomous_Reconnaissance_Inspection_and_Exploration_System_for_Hybrid_Single_and_Multi-UAV_Building_Inspection_Approach_after_Disaster) | Chưa xác minh cả ba trường. |
| R0221 | URL PDF ACM trả HTTP 403. Crossref xác nhận DOI, tiêu đề, 3 tác giả, năm và kỷ yếu. OpenAlex ghi hybrid CC BY và không có URL PDF riêng. Trang RobCE dẫn kỷ yếu về ACM. ResearchGate hiện không có toàn văn. Gemini báo nhãn truy cập từ DBLP nhưng Codex chưa xác minh được nhãn đó. [ACM PDF](https://dl.acm.org/doi/pdf/10.1145/3820709.3820744) · [Crossref](https://api.crossref.org/works/10.1145/3820709.3820744) · [RobCE](https://www.robce.org/Publication.html) · [ResearchGate](https://www.researchgate.net/publication/410749149_MACE_A_Physics-Informed_Multi-modal_Large_Language_Model_for_Strategic_UAV_Swarm_Confrontation) | Chưa xác minh cả ba trường. |
| R0402 | URL PDF ACM trả HTTP 403. Crossref xác nhận DOI, tiêu đề, 3 tác giả, năm và kỷ yếu DronCom. OpenAlex ghi gold CC BY và chỉ trỏ về ACM. Gemini báo không thấy PDF độc lập trong các nguồn tác giả đã thử. Scilit không mở được trong lần kiểm độc lập, SciProfiles trả 403. [ACM PDF](https://dl.acm.org/doi/pdf/10.1145/3842435.3843964) · [Crossref](https://api.crossref.org/works/10.1145/3842435.3843964) · [OpenAlex](https://api.openalex.org/works/https://doi.org/10.1145/3842435.3843964) | Chưa xác minh cả ba trường. |

## Đối chiếu điều kiện chấp nhận

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| Đúng phạm vi và cấu trúc | PASS | 3/3 ID, 3/3 DOI đúng, 0 ID hoặc DOI trùng, 0 ngoài phạm vi, có dòng kết thúc, Gemini báo 0 worker. |
| Metadata hoặc thiếu hụt được khai báo | PASS | Gemini báo 3/3 lỗi mở Crossref/OpenAlex và để trống venue R0402. Codex kiểm tra độc lập 3/3 bản ghi Crossref với đủ tiêu đề, tác giả, năm, kỷ yếu và DOI. Dùng trường metadata của Crossref trong kết luận về định danh. |
| Truy hồi và định danh PDF hoặc lý do còn mở | PASS | 0 kết quả PDF được nhận là xác minh, 3/3 kết quả còn mở với 14 lượt thử do Gemini ghi. Codex tái hiện 3/3 lỗi 403 ở ACM và xác nhận OpenAlex trả pdf_url null cho cả ba. |
| Kiểm chứng các kết luận được sử dụng | PASS | 9/9 lượt kiểm tra HTTP độc lập có bản ghi và 3/3 DOI được đối chiếu. Không đưa trạng thái truy cập DBLP, thông tin REDI, Scilit hoặc SciProfiles chưa tái hiện vào kết luận truy hồi. Các lượt này được lưu như quan sát do Gemini báo. Dải trang trong Crossref không được dùng làm số trang PDF. |
| Giới hạn và bảo toàn hồ sơ | PASS | 0 PDF được tải, 0 liên hệ, 0 dấu hiệu vượt hạn chế trong các tuyến được ghi. Phạm vi file dự án được giới hạn ở hồ sơ tác vụ và trạng thái vận hành. |
| Dọn chat tự động | FAIL | Cầu nối lưu kết quả trước khi dọn chat, bước chuẩn bị xóa không thể kích hoạt cửa sổ Gemini. Lệnh khôi phục cầu nối chỉ xử lý tác vụ hết thời gian sau Send và không dọn lại chat của tác vụ đã hoàn tất. Giữ chat theo UUID trong biên nhận. |

Kết quả truy hồi được chấp nhận ở mức ghi nhận 3 hồ sơ còn mở. Không có bằng chứng từ trang đầu hoặc phiên bản PDF được đưa vào sử dụng. [Kết quả Gemini và các URL đã thử](gemini_result.jsonl) · [Đối chiếu độc lập](independent_sources.json) · [Biên nhận cầu nối](bridge_result.json)
