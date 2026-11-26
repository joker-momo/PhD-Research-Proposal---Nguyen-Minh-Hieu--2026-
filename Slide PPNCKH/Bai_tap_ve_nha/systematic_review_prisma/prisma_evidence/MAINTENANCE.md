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
