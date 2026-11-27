# Kiểm tra hồ sơ minh chứng

Mở [mục lục 16 bước](README.md). Tại mỗi bước, đối chiếu tiêu chí trong [kế hoạch đã duyệt](../restart_2026_11_26/approved_plan.md) với biên bản PASS/FAIL. Từ kết luận, lần về dữ liệu gốc, DOI hoặc trang/đoạn cụ thể. Kiểm SHA-256 với manifest khi manifest đã lưu giá trị này. Khi cần xác nhận thời điểm, đối chiếu sự kiện và lịch sử Git của tệp. Danh sách này hỗ trợ kiểm toán. Từng nhận định vẫn cần được đối chiếu với nguồn.

Trong commit nghiệm thu, cập nhật trường `artifacts` của đúng bước trong [sổ tiến độ](../restart_2026_11_26/progress.json). Đăng ký đầu vào, đầu ra, manifest hoặc checksum, và biên bản nghiệm thu áp dụng cho bước đó. Với Gemini.app, đăng ký cả brief, receipt, kết quả thô, bảng PASS/FAIL và hồ sơ cách ly/sửa lỗi khi có. Lưu ID lần chạy và timestamp thực trong nhật ký sự kiện. Để báo cáo thiếu toàn văn, lưu DOI/link, kết quả truy cập và lý do trong sổ thu thập.

Giữ bộ hồ sơ trong workspace để các liên kết tương đối mở được. Tệp đặc thù của gói minh chứng có thể lưu trong thư mục này và đăng ký trong sổ tiến độ. Dữ liệu gốc và PDF tiếp tục dùng vị trí đã đăng ký trong dự án.

Tại thư mục `prisma_evidence`, chạy hai lệnh sau rồi stage mục lục đã tạo cùng commit nghiệm thu:

```bash
rtk proxy python3 build_index.py
rtk proxy python3 build_index.py --check
```

`--check` báo lỗi khi mục lục cũ hoặc khi đường dẫn minh chứng đã đăng ký không còn tệp. Cập nhật khi thay đổi phạm vi quyền truy cập hoặc khi phát hiện tệp thất lạc. Ghi rõ tình trạng thực và giữ lịch sử các lần nghiệm thu.

## Tiếp nhận PDF và minh chứng mới

1. **Xác định ID.** Tra ID trong [danh mục minh chứng theo ID](evidence_by_id.csv) và [hàng đợi hồ sơ](../restart_2026_11_26/unique_record_queue.csv). Đối chiếu DOI và tiêu đề với trang đầu hoặc trang thông tin xuất bản trong tệp gốc. Nếu không có DOI, kiểm đủ tiêu đề, tác giả, năm và nguồn xuất bản rồi ghi `DOI_NOT_FOUND`. Ghi trang vật lý của dấu nhận diện. DOI ngoài tệp hoặc tên tệp chỉ là đầu mối khi chưa xác minh được phiên bản.
2. **Chọn một bản chính.** Băm SHA-256 từng tệp trước khi sao chép. Cùng mã băm là bản sao theo byte. Khi tệp khác mã băm nhưng có cùng DOI, kiểm phiên bản, số trang và dấu xuất bản trước khi chọn. Ghi rõ bản nhà xuất bản, bản tác giả đã được chấp nhận, bản thảo chưa phản biện hoặc trạng thái chưa xác minh. Nếu cần giữ phiên bản khác làm bằng chứng đối chiếu, ghi quan hệ phiên bản trong hồ sơ và lưu riêng dưới `restart_2026_11_26/fulltext_retrieval/versions/RNNNN/<version>.pdf`. Khi hai báo cáo có DOI khác nhau, bảo toàn hai ID và ghi quan hệ nghiên cứu nếu có bằng chứng.
3. **Lưu PDF gốc.** Dùng `restart_2026_11_26/fulltext_retrieval/pdf/RNNNN.pdf`, ví dụ `R0007.pdf`. Giữ nguyên byte PDF. Sau khi chép, mở PDF, kiểm trang nhận diện, đếm trang vật lý và tính lại SHA-256. Ghi đường dẫn nguồn cung cấp và URL xuất bản khi có. Nếu URL chỉ xác nhận danh tính, ghi rõ vai trò đó. Ghi trạng thái truy cập và phiên bản còn chưa rõ trong sổ tiếp nhận.
4. **Lưu nguồn khác PDF.** Ghi ID, URL gốc, ngày giờ truy cập có múi giờ, loại tài liệu, phiên bản và mục liên quan. Khi có thể lưu tệp gốc hoặc ảnh chụp theo quyền truy cập, dùng `restart_2026_11_26/fulltext_retrieval/source_evidence/RNNNN/<nguon>.<ext>` và băm SHA-256. Nếu chỉ lưu được liên kết, dẫn về dòng nhật ký trong repo và ghi lý do. Dùng trang chính thức, mục hoặc tên trường để người sau tìm lại cùng căn cứ.
5. **Ghi danh mục và quyết định.** Mỗi dòng có ID, DOI hoặc định danh, loại minh chứng, trạng thái, nguồn, phiên bản nếu áp dụng, đường dẫn từ gốc repo, SHA-256 và số trang đối với PDF. Quyết định toàn văn dẫn trang vật lý 1-based và mục, bảng hoặc hình khi áp dụng. Giữ câu trích và lý do trong biên bản sàng lọc đã nghiệm thu. Hồ sơ thiếu toàn văn vẫn có một dòng trạng thái và căn cứ truy hồi.
6. **Kiểm chứng rồi commit.** Từ `prisma_evidence/`, chạy `rtk proxy python3 build_report_catalog.py` với PyMuPDF khả dụng. Stage PDF hoặc tệp nguồn theo đường dẫn cụ thể cùng sổ tiếp nhận, quyết định và dòng danh mục đã tạo. Chạy `rtk proxy python3 build_report_catalog.py --check` sau khi stage. Kiểm các tệp và dòng mới trong cùng commit. Tạo checkout sạch từ commit bằng `git worktree add --detach <thu-muc-kiem-tra> <commit>` rồi chạy lại chế độ `--check` trong checkout. Kiểm tệp PDF thật mở được, số trang và SHA-256 khớp. Nếu repo dùng Git LFS, tải đối tượng LFS trong checkout và xác minh tệp thật trước khi báo hoàn tất.

Mục lục 16 bước vẫn dẫn đến biên bản cấp bước, bản thảo và các báo cáo kiểm toán. Danh mục theo ID dẫn đến các bản nguồn và quyết định cho từng báo cáo. Tệp do người dùng cung cấp có thể có hạn chế phân phối. Ghi rõ nguồn chưa xác minh và giữ hồ sơ trong repo cục bộ nếu quyền đưa lên remote chưa được xác nhận.
