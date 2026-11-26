# Bước 09 – Nghiệm thu Batch 02

Codex kiểm tra lúc 2026-11-26T20:47:57+07:00. Gemini.app chế độ Task, đọc thư mục dự án trực tiếp. Task gốc `1e2f3174-da01-4b01-bc19-d65cda20ba4b`, context `44fa473d-f9ad-4c55-b5c3-db381bb01b3b`, bắt đầu 2026-11-26T13:34:27.970+00:00, kết thúc 2026-11-26T13:34:34.356+00:00. Task cuối `f46f6928-dcc7-4f5e-ad5e-72553b60bd67`, context `1086707b-3b0f-43a5-98b3-8ddacf623500`, bắt đầu 2026-11-26T13:43:01.656+00:00, kết thúc 2026-11-26T13:46:14.363+00:00. Trạng thái dọn chat `deleted`.

| Tiêu chí | Kết quả | Đối chiếu |
|---|---|---|
| A1 | PASS | 11/11 ID chính xác, 0 trùng và 0 ngoài danh sách. |
| A2 | PASS | 77/77 ô E1–E7. 2/2 quyết định loại có một mã lý do chính đúng thứ tự P06. |
| A3 | PASS | 77/77 trích đoạn được kiểm lại ở nguồn. 0 trích đoạn không khớp được nhận. |
| A4 | PASS | 11/11 báo cáo đã được Codex đối chiếu về ý nghĩa và quyết định. |
| A5 | PASS | 0 báo cáo có tiêu chí chưa rõ được ghi mã và lý do. 0 trường hợp đó được đưa vào INCLUDE. |

INCLUDE 9; EXCLUDE 2; AWAITING_CLASSIFICATION 0.

## Đối chiếu độc lập

- R0045 — PDF pp. 3–7 xác nhận phân hoạch và di chuyển tầng DNN; pp. 9–11 §IV mô phỏng nhiều UAV.
- R0047 — PDF pp. 3–5 định nghĩa tác vụ tổng quát; pp. 12–13 dùng DAG tổng hợp và GAT/DRL để tối ưu. Không có workload suy luận DNN được phân bổ; loại E3.
- R0048 — PDF pp. 3–7 §§III–VI dùng DAG phân hoạch cho phân tích video hợp tác; pp. 9–11 §VII đánh giá theo số UAV.
- R0054 — PDF p. 1 §II xác định mạng nhiều UAV và ngày xuất bản; p. 3 §II-B phân hoạch ML ba tầng; p. 4 §IV đánh giá mạng này.
- R0059 — PDF pp. 3–7 §§3–4 chuyển mô hình và thực thi CNN; pp. 8–10 §5 đánh giá nhiều UAV tác vụ/chuyển tiếp.
- R0061 — PDF pp. 7–10 cho thấy phân loại và phân đoạn tại từng UAV, hợp nhất cảm biến ngay trên từng UAV và chia sẻ cảnh báo/giám sát; loại E3.
- R0062 — PDF pp. 2–5 mô tả phân hoạch DNN; pp. 5–6 cho thấy prototype và tốc độ khung hình, Figs. 4–6.
- R0063 — PDF pp. 5, 8 §§4.1, 4.6 phân bổ suy luận giữa UAV và edge; pp. 11, 15+ §5 đánh giá mô phỏng nhiều UAV và inference.
- R0068 — PDF pp. 4–7 §§III–V mô tả gán tầng suy luận; pp. 10–12 §VI đánh giá nhiều UAV.
- R0071 — PDF pp. 2–4 §§II–III phân hoạch DNN giữa các UAV; p. 5 §IV mô phỏng so sánh nhiều UAV.
- R0073 — PDF pp. 3–8 §§2–4 gán tầng CNN; pp. 9–12 §5 đánh giá bao gồm UAV không hoạt động.
- Nguồn ngoài — IAJSE Review Policy xác nhận double-blind tại https://iaiest.com/iaj/index.php/IAJSE/ReviewPolicy.
- Nguồn ngoài — IEEE Communications Magazine policy và institutional record xác nhận review và loại bài R0062: https://www.comsoc.org/publications/magazines/ieee-communications-magazine/policies-guidelines ; https://researchportal.hkust.edu.hk/en/publications/elastic-collaborative-edge-intelligence-for-uav-swarm-architectur/.
- Nguồn ngoài — IEEE Conference Author Center xác nhận quy trình phản biện conference tại https://conferences.ieeeauthorcenter.ieee.org/understand-peer-review/.
