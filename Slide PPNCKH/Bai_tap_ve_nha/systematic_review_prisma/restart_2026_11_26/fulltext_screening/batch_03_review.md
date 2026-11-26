# Bước 09 – Nghiệm thu Batch 03

Codex đối chiếu lúc 2026-11-26T21:03:18+07:00. Gemini.app Task đọc thư mục dự án trực tiếp. Task gốc 9db9c066-41fa-40b3-8bc3-468274e9711d, context e5ac8613-f91a-4452-92dd-72bd85c2a6e9. Kết quả cuối ef92e6e4-bd09-4267-9a41-d54134d002a9, context 513d937c-065f-4e69-a79b-577731783f4f. Thời điểm bắt đầu 2026-11-26T13:59:54.072+00:00, kết thúc cầu nối 2026-11-26T14:02:42.389+00:00. Khôi phục giao diện nếu có: null.

| Tiêu chí | Kết quả | Đối chiếu |
|---|---|---|
| A1 | PASS | 11/11 ID khóa, 0 trùng, 0 ngoài danh sách. |
| A2 | PASS | 77/77 trường E1–E7. 3/3 bài loại có một lý do chính theo thứ tự P06. |
| A3 | PASS | 71/71 trích đoạn PDF khớp; 3/3 nguồn ngoài được đối chiếu; 3 trường U có giới hạn ghi rõ. |
| A4 | PASS | 11/11 quyết định được Codex đối chiếu với toàn văn và nguồn thích hợp. |
| A5 | PASS | 4 báo cáo chờ phân loại; 0 báo cáo chờ đưa vào INCLUDE. |

INCLUDE 4; EXCLUDE 3; AWAITING_CLASSIFICATION 4.

## Đối chiếu độc lập

- R0074 — PDF pp. 6–8 §3 map LLM layers to swarm devices. PDF pp. 14–19 §4 describes a simulation and reports results across inter-UAV conditions. PDF p. 1 gives publication history.
- R0075 — PDF pp. 4–7 §III gives multi-UAV collaborative inference and pp. 8–11 §IV give evaluation. PDF p. 1 is an IEEE accepted version. DOI resolves to IEEE Xplore document 11753908; the publisher date field could not be verified. The Crossref publication date gives only 2026 (DOI created timestamp is not the publication date).
- R0081 — PDF p. 2 §§2–3 describes model partition and prototype evaluation. ACM MobiSys 2022 lists IDEA under Accepted Demos. The demo submission policy specifies the extended abstract and interest-based selection; peer review of a qualifying full report remains unestablished. The decision uses E7 uncertainty.
- R0083 — PDF pp. 2–6 §§3–4 shows DNN partition across multiple UAVs. PDF pp. 6–8 §4 and Figs. 2–5 report simulation with latency and energy evidence. PDF p. 1 supplies publication history.
- R0089 — PDF pp. 3–7 §§3–4 specify the DNN head, edge completion and intermediate representations. PDF pp. 8–10 §5 evaluates those policies in a multi-UAV / edge scenario. PDF p. 1 supplies publication history.
- R0092 — PDF pp. 3–9 §§III–IV specifies decentralized DNN placement; pp. 10–14 §V evaluates the system. PDF p. 1 is an IEEE accepted version. IEEE Xplore 11719586 date could not be verified and the Crossref published date gives only 2026.
- R0095 — PDF pp. 3–7 §§3–4 specifies DNN macro-block scheduling among UAVs; pp. 8–10 §5 contains simulation comparisons. PDF p. 1 supplies publication history.
- R0108 — PDF pp. 4–5 §III describes model training and generic offloading. PDF pp. 6–7 §IV gives architecture-level comparisons, with no identified collaborative inference workload or inference-specific evaluation. Primary E3, secondary E4.
- R0110 — PDF pp. 3–8 §§III–IV gives LLM assignment across swarm nodes. PDF pp. 9–13 §V gives simulation and comparison. The IEEE accepted-version header on p. 1 and DOI target IEEE Xplore 11804735 do not independently establish the publication date; the date field was inaccessible and no Crossref publication date was returned.
- R0111 — PDF p. 3 §§4.4, 5.1 and p. 4 §§5–6 describe a planned experiment and results template. The report provides no completed evaluation results. Primary E7.
- R0117 — PDF pp. 16–18 §5 and p. 26 §9 explicitly establish a conceptual reference architecture based on literature synthesis. Primary E1.
- ACM publisher deposit via Crossref, message.published.date-parts is [2022,6,27]: https://api.crossref.org/works/10.1145/3498361.3538674.
- Exact demo submission policy independently verified and track assignment verified separately: https://www.sigmobile.org/mobisys/2022/demos.html and https://www.sigmobile.org/mobisys/2022/accepted-demos.html.
- Publisher Peer Review Policy exact external-review sentence verified in fetched page: https://ijesat.com/ppolicy.php?content_id=11.
