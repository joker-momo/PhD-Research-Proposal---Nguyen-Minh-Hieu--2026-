# Khóa đầu vào tìm kiếm PRISMA — phiên bản1

Thời điểm quyết định: **2026-11-26T16:02:08+07:00**.
Mã snapshot: `HK261-SEARCH-INPUT-20261126-v1`.

Chấp nhận khuyến nghị đã hiệu chỉnh từ Gemini.app Task sau kiểm tra10/10 tiêu chí. Khóa danh sách6 file CSV nhập liệu và dấu vết25 file bằng chứng bằng SHA-256 trong `search_dataset_lock_2026-11-26.json`. File gốc được giữ nguyên; không tuyên bố đã đặt quyền chỉ đọc của hệ điều hành. Amendment006 ghi nhận lúc2026-11-26T14:53:39+07:00 vẫn được giữ nguyên. Ghi chú này bổ sung quyết định hiện tại, không viết lại thời điểm hoặc lý do tìm kiếm trước đó.

| Nguồn | Dòng được nhận làm đầu vào | Cách hạch toán |
|---|---:|---|
| IEEE Xplore |63 |42+21; chưa khử trùng liên truy vấn/nguồn |
| Scopus |110 |77+33; chưa khử trùng liên truy vấn/nguồn |
| OpenAlex |111 |85+26; nguồn khám phá bổ sung, có9 ID trùng giữa2 truy vấn và102 ID hợp trong riêng OpenAlex |
| ACM Digital Library |0 |79 và325 là số hiển thị; tổng404 chưa biết trùng, không được cộng vào dòng nhập |
| Web of Science Core Collection |0 |Hai truy vấn chưa thực hiện được; số kết quả đều null, không phải0 kết quả |
| Research Horizon Navigator |0 |Chưa chạy; không phải nguồn kết quả của snapshot |

**Tổng284 dòng trước khử trùng**, không phải284 bài hoặc nghiên cứu duy nhất. Snapshot này chưa hợp nhất với46 báo cáo đã sàng lọc trước đó. Không cộng284 với46 để báo số nghiên cứu.

## Giới hạn phải giữ khi sử dụng

Khóa đầu vào cho phép bước chuẩn hóa và khử trùng có một phiên bản truy vết được. Việc này **không xác nhận tìm kiếm đã đầy đủ hoặc manuscript đã sẵn sàng nộp**. ACM chưa có record-level export; WoS Core chưa tìm kiếm được; chính sách/năng lực ACM tổng quát chưa kiểm chứng vì hai trang chính thức trả403. Không suy ra mọi cách thu thập hợp lệ khác đều bị cấm. OpenAlex không được đổi tên thành WoS Core hoặc coi là có độ phủ tương đương.

Giữ nguyên query gốc, thời điểm thực chạy, bộ lọc và mọi giới hạn của từng file bằng chứng: core query set1.3, OpenAlex1.4. Điều kiện ngày xuất bản chính xác, ngôn ngữ và loại bài phải tiếp tục được kiểm ở bước sàng lọc theo protocol; không suy ra mỗi dòng export đã đạt điều kiện. Giao diện ACM dùng mốc cuối tháng2026-11-30, được ghi rõ trong bằng chứng; không dùng mốc đó để nhận bài xuất bản sau ngày tìm kiếm.

## Bước kế tiếp

Chuẩn hóa6 CSV thành một bảng giữ source/query/file/row; khử trùng DOI/title với bảng ánh xạ từng dòng; sau đó đối chiếu với46 báo cáo hiện có để chỉ sàng lọc phần mới. Chưa có số unique cuối cùng. Nếu thu thêm nguồn, tạo snapshot phiên bản mới và giữ phiên bản này. Manuscript, submission và email nằm ngoài task này.

Nghiệm thu: `reviews/search_dataset_lock_app_correction_review.md`. Bằng chứng được chấp nhận: `results/search_dataset_lock_app_reconciled.json`.
