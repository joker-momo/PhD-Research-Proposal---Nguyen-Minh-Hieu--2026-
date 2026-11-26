# TRAO ĐỔI VỚI THẦY HƯỚNG DẪN — Cơ hội hợp tác lab UAV
*Chuẩn bị: 07/09/2026 · Dùng cho buổi gặp TS. Nguyễn Thành Công / PGS. Phạm Hoàng Anh*

---

## 1. Bối cảnh — nói trong 60 giây

Anh Nguyễn Hoàng Dũng, NCS ngành Quản lý xây dựng (đã trúng tuyển), đề tài giám sát an toàn lao động bằng drone + YOLO, có hậu thuẫn của Newtecons. Anh ấy mời em tham gia nhóm, **lab đã có drone và bay được ngay**.

Đề tài hai bên nằm ở hai tầng chồng lên nhau của cùng một hệ thống:
- **Anh Dũng — tầng nhiệm vụ:** drone nào bay tới vùng rủi ro nào (MPA–GWO), YOLO phát hiện hành vi không an toàn
- **Em — tầng thực thi:** chạy model đó thế nào trên phần cứng bị khóa SWaP, cắt ở đâu, cứu ra sao khi một drone hỏng

Đề cương của anh ấy viết *"triển khai YOLO trên Jetson Nano gắn trên drone"* như một bước kỹ thuật hiển nhiên — **đó chính là bài toán nghiên cứu của em**.

---

## 2. Ba lợi ích cụ thể cho luận án

### 2.1 Vá điểm yếu lớn nhất: sim-to-real
Đề cương hiện tại **thuần mô phỏng suốt 3 năm**, và đây là hạn chế em đã tự ghi nhận trong mục Risk Considerations. Có drone thật thì lần đầu tiên có đường kiểm chứng vật lý.

### 2.2 Vượt toàn bộ nhóm hàng xóm trên trục kiểm chứng
Bốn công trình gần đề tài em nhất **đều là mô phỏng**:

| Công trình | Kiểm chứng |
|---|---|
| Wang et al. (CDPO), ISPCE-ASIA 2024 | Mô phỏng |
| Gao et al. (P-MDP), IEEE IoT-J 2025 | Mô phỏng |
| Kim et al. (DRL-RLD), Appl. Sci. 2024 | Mô phỏng |
| Meng et al., IEEE IoT-J 07/2026 | Mô phỏng |

Nếu em làm được **tiêm lỗi thật — ngắt một drone giữa lúc pipeline suy luận đang chạy, rồi re-derive ranh giới cắt và resume trên phần cứng bay thật** — thì đó không phải cải thiện biên, mà là vượt cả nhóm trên tiêu chí đánh giá.

### 2.3 Nâng cấp hai phần đang yếu nhất trong RQ1
- **Số đo năng lượng trong điều kiện bay thật** (nhiệt, rung, chia nguồn với động cơ) — khác hẳn đo trên bàn
- **Đo chất lượng liên kết FANET thật theo khoảng cách và hướng** — hiện mô hình chi phí truyền thông của em hoàn toàn dựa trên tham số mô phỏng; đây là chỗ reviewer dễ bắt nhất

---

## 3. Ba rủi ro — và cách em định chặn

| Rủi ro | Cách chặn |
|---|---|
| **Thời gian năm nhất bị hút** — dự án doanh nghiệp luôn có việc gấp hơn luận án | Chặn trần số buổi/tuần ngay từ đầu, thỏa thuận bằng văn bản. Giữ nguyên khối thời gian cho phần nền (dựng testbed, formulation) |
| **Ranh giới đóng góp bị mờ** — khó trả lời "đâu là đóng góp riêng của anh" lúc bảo vệ | Viết ra rõ: phần nào thuộc luận án của em và không ai khác dùng làm đóng góp chính. Lõi trí tuệ (formulation, phân tích K, cơ chế phục hồi) vẫn là của em |
| **Lệch trọng tâm ngành** — luận án CS biến thành dự án ứng dụng xây dựng | Anh Dũng cung cấp *bài toán và dữ liệu*; phương pháp vẫn thuộc lãnh địa của thầy. RQ1/RQ2 giữ nguyên |

**Cần kiểm tra thêm:** giấy phép bay ngoài trời (lab đã có sẵn thủ tục chưa, hay chỉ bay trong khu vực đã xin phép?), và quyền sở hữu / quyền công bố kết quả khi có Newtecons tham gia.

---

## 4. Hai phương án bổ sung thực nghiệm vào timeline 3 năm — xin thầy chọn

### Phương án A — Bảo thủ: thực nghiệm là *bổ trợ*
Giữ nguyên khung 3 năm hiện tại. Thêm một hoạt động đo đạc ngắn (~4–6 tuần, đặt vào tháng 6–9 năm nhất): profiling per-layer trên Jetson thật + đo link FANET thật. Kết quả dùng làm **tham số đầu vào** cho mô phỏng.

- **Được:** vá sim-to-real ở mức tham số, rủi ro thời gian thấp, không đổi cấu trúc luận án
- **Mất:** không có demo vật lý; vẫn là luận án mô phỏng khi ra hội đồng

### Phương án B — Tham vọng: thực nghiệm là *một cấu phần đóng góp*
Nâng Objective 4 từ "co-simulation" thành "co-simulation **+ kiểm chứng vật lý quy mô nhỏ**". Đặt một đợt thí nghiệm bay 3 drone vào cuối năm 2 (sau khi bộ tối ưu và cơ chế phục hồi đã chạy được trong mô phỏng), chứng minh mid-inference recovery trên phần cứng thật.

- **Được:** đóng góp mạnh hơn hẳn, khác biệt rõ với mọi bài hàng xóm, bài báo có trọng lượng cao hơn
- **Mất:** thêm phạm vi, thêm rủi ro kỹ thuật (tích hợp phần cứng luôn tốn hơn dự kiến), cần thầy đồng ý điều chỉnh Objective 4

**Nghiêng của em:** Phương án B, nhưng chỉ khi mô phỏng đã chạy ổn định trước — tức quyết định cuối cùng để đến cuối năm nhất, khi đã biết testbed có về đích đúng hạn hay không.

---

## 5. Ba câu xin ý kiến thầy

1. **Thầy thấy em nên tham gia ở mức nào** — chỉ trao đổi dữ liệu/thiết bị, hay tham gia nhóm với vai trò rõ ràng?
2. **Chọn phương án A hay B** cho cấu phần thực nghiệm? Nếu B thì đặt vào cuối năm 2 có hợp lý không?
3. **Thầy muốn em báo cáo phần hợp tác này với tần suất nào, và quyết định nào em phải hỏi thầy trước?**

Em cũng muốn mời thầy đứng tên đồng tác giả bài báo chung nếu hướng này đi tiếp.

---

## 6. Điều em chưa biết — sẽ hỏi anh Dũng trong buổi làm việc kỹ thuật

- Anh ấy định mỗi drone chạy YOLO độc lập, hay cần nhiều drone cùng gánh một model? *(Câu này quyết định giao diện kỹ thuật sâu hay nông)*
- Jetson chính xác là dòng nào (Nano đời cũ hay Orin Nano)?
- Quy mô bầy dự kiến bao nhiêu drone?
- Dữ liệu công trường của Newtecons có được chia sẻ và công bố không?
- Lịch của anh ấy: Nội dung 2 (YOLO trên drone) rơi vào năm nào trong kế hoạch 4 năm?
