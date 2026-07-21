# Q&A Bank — Câu hỏi lớn & Điểm yếu của Proposal
*Cập nhật: 2026-07-13 · Nguồn: báo cáo 5-reviewer (7/7, 72.1/100 Minor Revision) + deep-read P-MDP/CDPO + đánh giá bổ sung. Lấy ra dùng khi luyện Q&A hoặc sửa proposal.*

---

## A. ĐIỂM YẾU — trạng thái hiện tại

### Đã vá (13/7) ✅
| # | Điểm yếu | Đã xử lý bằng |
|---|---|---|
| 1 | Novelty lập luận kiểu "conjunction" (chưa ai làm đủ 4 tiêu chí) — đòn nặng nhất của Devil's Advocate | Gap 3 viết lại: taxonomy proactive / per-task online / **reactive mid-inference** + obstruction có tên (re-derive boundary → tensor size mới → comm cost nội sinh + resume from activation) |
| 2 | Khẳng định NP-hard không có citation | Câu anchor CDPO (NP-hard) vào Gap 1 |
| 3 | K không được chặn | Quy tắc tạm K ≤ min(N, \|P\|), kỳ vọng K ≤ 8, tinh chỉnh = mục tiêu Objective 1 (Methodology) |
| 4 | Không có baseline cho claim "joint > sequential" | 3 baseline có tên trong Objective 4: (i) sequential partition-then-assign; (ii) static joint không re-derivation; (iii) full-restart |
| 5 | Ethics/dual-use chỉ 1 mệnh đề | Đoạn đầy đủ trong Risk Considerations (dân sự, không targeting/vũ khí hóa, theo hướng dẫn đạo đức của trường) |
| 6 | **6 reference ảo** (khan2022uavedge, chen2023edgeuav, zhou2023task, yang2024federateduav, kim2025faultaware, park2025marl) + sai tác giả wang2024ress | Gỡ sạch, thay bằng ref thật đã xác minh. **TUYỆT ĐỐI không thêm lại 6 key này** |

### Đã vá thêm (15/7) ✅
| # | Điểm yếu | Đã xử lý bằng |
|---|---|---|
| 7 | Lịch nộp 3 bài không chừa chu kỳ review IEEE (EIC-W2) | Câu làm rõ trong Timeline: milestone = ngày NỘP; bài 1–2 nhắm venue turnaround nhanh, bài 3 journal; phase sau chạy song song với review cycle của bài trước |
| 8 | Risk Considerations chung chung (EIC-W3) | Bảng trigger → fallback 4 hàng theo từng Objective (O1: hết đường giải tích ở M10 → exact small-K + empirical; O4: co-sim trượt M8 → network-only trước) |
| 9 | SWaP chưa lượng hóa (R1-W3) | Nêu reference class trong Methodology: Jetson-class companion computer 7–15W trên multirotor nhỏ |
| 12 | Transferability (R3-W2) | Đoạn cuối Expected Outcomes: 3-layer formulation áp dụng được cho ground robot fleet / maritime; UAV là instantiation khắc nghiệt nhất |

### Còn mở ⚠️
| # | Điểm yếu | Mức độ | Hướng xử lý |
|---|---|---|---|
| 10 | Hàm mục tiêu chỉ latency + energy, **vắng accuracy** — trong khi Fig 2 vẽ nén tensor (nén = mất chính xác) | Chưa reviewer nào nêu — tự phát hiện | Trả lời miệng (B7) — chủ đích để dạng ràng buộc cứng, không sửa văn bản trước 22/7 |
| 11 | **Control plane chạy ở đâu?** Bộ tối ưu tập trung trên 1 drone = single point of failure | Tự phát hiện | Trả lời miệng (B8) — leader election là extension của Phase 3, không sửa văn bản trước 22/7 |
| 13 | Kết luận "P-MDP/CDPO không làm X" mới ở mức abstract-level | Rủi ro thấp (đã giảm thêm 15/7: CDPO xác nhận dùng "backup reprocessing tại BS" = proactive redundancy; user không có tài khoản thư viện → full text lấy qua ResearchGate request / email tác giả / nhờ thầy) | Không chặn defense |
| ~~14~~ | ~~TODO citation~~ — **XONG 15/7 qua Crossref/Google**: CDPO = Wang, Ling; Wang, Junhua; Dai, Chen — ISPCE-ASIA 2024, DOI 10.1109/ISPCE-ASIA64773.2024.10756252 (lưu ý: venue tier khiêm tốn — nếu hội đồng soi thì đáp: "kết quả NP-hardness là chứng minh hình thức đã bình duyệt; độ khó của bài toán không phụ thuộc uy tín venue"). zhao2022reliable = Mingyue Zhao, Xing Zhang, Zezhao Meng, Xiangwang Hou (DOI 10.1109/IWCMC55113.2022.9824945). FANET survey: tác giả thật là **Amponis, Lagkas, Sarigiannidis, Vitsas, Fouliras, Wan** (bib cũ gán nhầm Rahmani!) — key đã đổi thành amponis2021fanet | Xong | — |

### ⚠️ HÀNG XÓM SÁT NHẤT — phát hiện 16/7, ĐÃ cite vào Gap 3 + bảng + slide 16
**Kim et al. 2024 (DRL-RLD)** — "End-to-End Latency Optimization for Resilient Distributed CNN Inference in Resource-Constrained UAV Swarms", *Applied Sciences* 14(23):10832, DOI 10.3390/app142310832. Swarm ad-hoc (U2U+U2G), DRL phân bổ layer, **tái phân bổ khi UAV chết** — sát Gap 3 hơn mọi bài trước. Đã đọc TOÀN VĂN (không chỉ abstract): (1) không có khái niệm resume/restart trong cả bài — request đang chạy dở ngầm định chạy lại; (2) reallocation = phương án mới cho request KẾ TIẾP theo time step; (3) DRL black-box, không phân tích cấu trúc/bounded-K/complexity; (4) mô phỏng 15 UAV, AlexNet/YOLO/VGG16. → Trả lời chuẩn: *"Kim et al. giữ cho MẠNG tiếp tục phục vụ; em cứu LƯỢT INFERENCE đang chạy — preserve activation, re-derive boundary, resume. Và em làm bằng công cụ giải tích thay vì black-box DRL."* Đây giờ là bài PHẢI thuộc trước khi vào phòng.

### Hàng xóm khác phát hiện 15/7 — biết để phòng khi hội đồng hỏi "đã đọc bài X chưa?"
1. **Meng et al. 2026** "DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted MEC" (IEEE IoT-J 13(13), 7/2026, DOI 10.1109/JIOT.2026.3685675) — chữ "migration" nghe sát Gap 3 nhưng đọc kỹ abstract: migration = CÂN BẰNG TẢI giữa UAV-server (device↔server, SAC-PER DRL, mục tiêu energy) — vẫn per-task/per-epoch, không failure-reactive, không resume mid-inference. ĐÃ đưa vào bảng so sánh với dấu †.
2. **Ren et al.** "Efficient Pipeline Collaborative DNN Inference in Resource-Constrained UAV Swarm" (WCNC 2024, DOI 10.1109/WCNC57260.2024.10570535) + bản BigCom 2023 — nhóm của Qu (đã cite qu2024elastic). Kiến trúc pipeline NỘI BỘ swarm — gần proposal nhất về kiến trúc; tập trung throughput/efficiency, chưa thấy failure recovery. Nếu bị hỏi: "họ tối ưu pipeline tĩnh cho throughput; tôi giải bài re-derive khi pipeline đứt giữa chừng — bổ sung chứ không trùng." Cân nhắc đọc kỹ + cite trong bản final thesis (không bắt buộc trước 22/7).

---

## B. CÂU HỎI DỰ KIẾN TỪ HỘI ĐỒNG — kèm gợi ý trả lời

**B1. "Chia nhỏ model AI có khả thi không? Ai làm được chưa?"**
→ *"Đã được kiểm chứng từ datacenter đến Raspberry Pi — Neurosurgeon chứng minh tồn tại điểm cắt tối ưu từ 2017, DeepThings chạy YOLOv2 trên cụm Pi thật. Đóng góp của tôi không phải chứng minh chia được, mà là chọn cách chia tối ưu và giữ dây chuyền sống sót trên mạng bay bất ổn."*

**B2. "K bằng bao nhiêu? Chọn thế nào?"**
→ *"K bị chặn bởi số UAV khả dụng và số điểm cắt hợp lệ của model — quy tắc tạm K ≤ min(N,|P|), thực tế kỳ vọng K ≤ 8. Quan trọng hơn con số là phân tích regime: vùng nào tăng K còn lời, vùng nào chi phí truyền nuốt hết lợi ích — đó chính là Contribution 2."* (Đã có trong Methodology.)

**B3. "Sao không bolt DADS (cắt model) lên Pan et al. (self-healing) là xong?"** — đòn của Devil's Advocate
→ *"Vì self-healing hiện có giả định task placement CỐ ĐỊNH. Khi placement bị ràng buộc bởi lựa chọn partition, node chết giữa pipeline buộc phải suy diễn lại ranh giới cắt — ranh giới mới sinh tensor size mới, tức chi phí truyền mới trên topology còn lại, và phải quyết định resume từ activation nào. Vòng phụ thuộc này không xuất hiện khi hai bài toán tách rời — đó chính là chỗ ghép không tự động."*

**B4. "Bài P-MDP 2025 đã làm online partition adaptation rồi mà?"**
→ *"Đúng, nhưng per-slot cho TÁC VỤ MỚI, trên kiến trúc AAV↔MEC server. Tôi giải ca khác: cứu lượt suy luận ĐANG CHẠY DỞ trong pipeline đa chặng nội bộ swarm — re-derive boundary + resume, không phải re-decide cho request kế tiếp."* (Bảng so sánh có footnote † đúng ý này.)

**B5. "Joint tốt hơn sequential — chứng minh đâu?"**
→ *"Không khẳng định suông — Objective 4 so trực tiếp với 3 baseline: sequential partition-then-assign (đại diện là LLHR-style decomposition), static joint, và full-restart. Nếu joint không thắng sequential có ý nghĩa thống kê thì luận điểm trung tâm sai và tôi sẽ biết sớm từ năm 1."*

**B6. "Mô phỏng thì tin được đến đâu? Sao không bay thật?"**
→ *"NS-3+ROS+Gazebo là combo chuẩn ngành cho claim mạng+robot. Luận án nhắm structural insight — cấu trúc trade-off và cơ chế thích ứng — không phải con số tuyệt đối của một platform cụ thể; sim-to-real gap được ghi nhận là limitation có chủ đích. Bay thật là hướng mở rộng sau tiến sĩ."*

**B7. "Nén tensor trước khi truyền thì mất accuracy — sao hàm mục tiêu không có accuracy?"** ⚠️ điểm yếu #10
→ *"Đúng — phiên bản hiện tại cố định mức nén bảo toàn (hoặc không nén), coi accuracy là ràng buộc cứng chứ không phải biến. Đưa accuracy vào thành chiều thứ ba của trade-off là mở rộng tự nhiên của Phase 2 và tôi đã dự phòng chỗ cho nó trong formulation."*

**B8. "Control plane chạy ở đâu? Nó chết thì sao?"** ⚠️ điểm yếu #11
→ *"Câu hỏi đúng trọng tâm Phase 3. Thiết kế cơ sở là orchestrator nhẹ trên một node + cơ chế bầu lại khi node đó mất (leader election — bài toán đã có lời giải chuẩn trong distributed systems); phương án phân tán hoàn toàn được xét như extension. Điểm mấu chốt: chi phí re-derive một lần re-optimization là nhỏ nhờ bounded-K, nên orchestrator không cần node mạnh."*

**B9. "3 bài báo trong 3 năm có thực tế không với chu kỳ review IEEE?"** ⚠️ điểm yếu #7 — CHƯA vá trong văn bản
→ Trả lời thẳng: *"Bài 1–2 nhắm venue chu kỳ nhanh (hội nghị/workshop tier tốt hoặc magazine), bài 3 nhắm journal; timeline tính mốc NỘP, không phải mốc chấp nhận, và các phase được thiết kế song song một phần để hấp thụ vòng revise."*

**B10. "Đề tài này khác gì đề tài thạc sĩ 'áp dụng AI cho drone'?"**
→ *"Ba chữ ký tiến sĩ: (1) formulation tối ưu tổ hợp mới với chứng cứ NP-hard và phân tích regime theo K; (2) obstruction lý thuyết chưa ai giải ở giao điểm partitioning–FANET–online; (3) chuẩn công bố quốc tế. Không phải áp dụng công cụ có sẵn — là xây công cụ."*

---

## C. CHECKLIST TRƯỚC BUỔI THUYẾT TRÌNH
- [ ] Tải bản full CDPO (IEEE doc 10756252) → điền tác giả/venue vào .bib (TODO trong file)
- [ ] Tải bản full P-MDP (10.1109/JIOT.2025.3558162) → xác nhận "không làm mid-inference recovery"
- [ ] Hoàn thiện author list rahmani2021fanet + zhao2022reliable
- [ ] Quyết định: vá tiếp điểm yếu #7 (timeline), #8 (risk table), #9 (platform), #12 (transferability)?
- [ ] Compile bản IEEEtran chuẩn trên máy (latexmk / Cursor)
- [ ] Đồng bộ slide với novelty mới (khi được yêu cầu)
- [ ] Luyện trả lời B1–B10 thành tiếng, mỗi câu ≤ 45 giây
