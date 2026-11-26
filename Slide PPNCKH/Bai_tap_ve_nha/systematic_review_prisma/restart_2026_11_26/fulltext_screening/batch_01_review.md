# Bước 09 – Nghiệm thu Batch 01

Codex kiểm tra lúc 2026-11-26T20:34:08+07:00. Gemini.app chế độ Task, đọc thư mục dự án trực tiếp. Task gốc `2418e1e9-4e07-4a47-be11-8c7a4112bca2`, context `584bdcc4-936c-4210-972e-ee952e60bf5b`, bắt đầu 2026-11-26T13:18:43.969+00:00, kết thúc 2026-11-26T13:23:27.816+00:00. Task cuối `cbfc9595-a49c-4952-8abb-7ebde3dd614d`, context `3503a4f3-5aa1-4da6-8f07-0603f03a9b27`, bắt đầu 2026-11-26T13:29:38.218+00:00, kết thúc 2026-11-26T13:32:50.976+00:00. Trạng thái dọn chat `not_verified`.

| Tiêu chí | Kết quả | Đối chiếu |
|---|---|---|
| A1 | PASS | 11/11 ID chính xác, 0 trùng và 0 ngoài danh sách. |
| A2 | PASS | 77/77 ô E1–E7. 0/0 quyết định loại có một mã lý do chính đúng thứ tự P06. |
| A3 | PASS | 77/77 trích đoạn được kiểm lại ở nguồn. 0 trích đoạn không khớp được nhận. |
| A4 | PASS | 11/11 báo cáo đã được Codex đối chiếu về ý nghĩa và quyết định. |
| A5 | PASS | 0 báo cáo có tiêu chí chưa rõ được ghi mã và lý do. 0 trường hợp đó được đưa vào INCLUDE. |

INCLUDE 11; EXCLUDE 0; AWAITING_CLASSIFICATION 0.

## Đối chiếu độc lập

- R0001 — PDF pp.1–2 §II establishes English primary CAPRI partitioning over UAV, edge and cloud. PDF p.3 §III-A specifies a multi-UAV simulation with plotted reward results in Figs. 2–3. The official WIP track, review policy, complete method and results support E7. IEEE Xplore lists the exact version by the cutoff.
- R0002 — PDF pp.2–4 §§II–III defines the English primary inference module migration method. PDF pp.7–8 §VII shows evaluated ResNet-18 task modules and outcomes in multiple swarms. The regular-track program, IEEE peer-review policy and IEEE Xplore date support E5/E7.
- R0003 — English proceedings report, PDF p.1; pp.2–4 §§III–IV defines DMS and its partition branch; pp.4–6 §V establishes evaluated multi-UAV trace scenarios and reports results.
- R0006 — English original proceedings report, PDF p.1; pp.2–4 §§III–IV defines UAV placement and DNN partition; pp.6–7 §V evaluates multi-UAV cases and reports latency and coverage.
- R0009 — English IEEE journal article with submission and 2025 online dates at PDF p.1. PDF pp.3–5 §§III–IV describes inference partitioning between ground devices and UAV edge resources; pp.7–9 §V presents multi-UAV energy and latency evaluation.
- R0010 — English proceedings report, PDF p.1; pp.2–4 §§III–IV defines sequential DNN stages across UAVs; pp.4–5 §V specifies trace-based multi-UAV evaluation and reports results.
- R0015 — English proceedings report, PDF p.1; pp.2–4 §§III–IV establishes layer and intra-layer inference allocation; pp.5–7 §IV compares evaluated multi-UAV configurations and latency results.
- R0019 — English IEEE journal article with first publication and review history at PDF p.1. PDF pp.4–6 §III assigns CNN layers across UAVs; pp.10–15 §IV describes multi-UAV comparisons, including latency Fig. 9 on p.12.
- R0022 — English proceedings report, PDF p.1; pp.2–5 §§II–IV describes layer partition and early exit. PDF p.5 Table I and p.6 Fig. 6 establish evaluated multi-UAV cases and results.
- R0029 — English proceedings report, PDF p.1; pp.2–4 §§II–III defines DNN stages and replica placement among UAVs. PDF p.5 §IV specifies multi-UAV setting and benchmark comparisons.
- R0044 — English proceedings report, PDF p.1; pp.2–4 §§II–III models inference partitions offloaded to multiple UAVs; pp.6–8 §IV confirms multi-UAV evaluation and its delay and power outcomes.
- Nguồn ngoài — R0001 and R0002 exact DOI and Date Added fields: https://xplorestaging.ieee.org/document/11670054/ and https://ieeexplore.ieee.org/abstract/document/11670091/. Gemini used these as supplied evidence. ICWS exact track listings and published policy checked at https://services.conferences.computer.org/2026/icws-program/ and https://services.conferences.computer.org/2026/info-for-authors/.
- Nguồn ngoài — IEEE's publisher peer-review policy was checked for the IEEE proceedings reports at https://conferences.ieeeauthorcenter.ieee.org/understand-peer-review/. The publisher PDFs identify the proceedings manifestation and contain evaluated work.
