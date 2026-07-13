# Deep-Read: P-MDP & CDPO vs. gap "re-derive partition boundary"

**Ngày:** 2026-07-13 · **Mục đích:** Xác nhận 2 bài gần nhất (từ 3W scan) có/không giải quyết khả năng *re-derive lại ranh giới partition khi UAV chết giữa pipeline*, với communication cost là hàm nội sinh của quyết định partition.

**Lưu ý nguồn:** Cả 2 bài đều paywalled trên IEEE Xplore; phân tích dưới đây dựa trên abstract chính thức + metadata + snippet đã index. Các kết luận "KHÔNG làm X" được gắn mức tin cậy; nên tải bản full qua thư viện trường để xác nhận lần cuối trước khi sửa Literature Review.

---

## 1. P-MDP — "Cooperative DNN Partitioning in Energy-Harvesting and MEC-Enabled AAV Networks"

- **Nguồn:** IEEE (số hiệu tài liệu 10949590, ~2025). [IEEE Xplore](https://ieeexplore.ieee.org/document/10949590) · [ResearchGate](https://www.researchgate.net/publication/390506389_Cooperative_DNN_Partitioning_in_Energy-Harvesting_and_MEC-Enabled_UAV_Networks)

### Bài này LÀM gì
- Mô hình hóa DNN partitioning + edge offloading như **hybrid action decisions theo từng time slot** trong mạng AAV năng lượng thu hoạch (energy-harvesting), động.
- Điểm mới cốt lõi của họ: xử lý **khoảng trễ giữa lúc lấy mẫu trạng thái và lúc thực thi hành động** (state-sampling → action-execution gap) khi quỹ đạo không biết trước → **Predictive MDP (P-MDP)**.
- Giải bằng **TE-MHAPPO**: Transformer trích xuất đặc trưng chuyển động từ các time slot gần nhất + multi-agent hybrid-action PPO (kiến trúc actor–critic, federated/heterogeneous). Cải thiện ≥12.1% so với MHAPPO về reward (delay + energy).

### Bài này KHÔNG làm gì (đối chiếu gap)
| Tiêu chí gap | Kết luận | Tin cậy |
|---|---|---|
| Re-derive boundary khi node chết **giữa** pipeline đang chạy | Không có bằng chứng. Dynamics của họ là energy-harvesting + mobility; quyết định partition được đưa ra **per-slot cho tác vụ mới**, không phải phục hồi inference đang chạy dở | Trung bình–cao |
| Comm cost nội sinh trên **đa chặng FANET swarm-internal** | Kiến trúc là AAV↔MEC offloading (split device–server), không phải pipeline đa chặng nội bộ swarm | Trung bình |
| Phân tích cấu trúc/độ phức tạp (bounded-K, regime analysis) | Không — hướng tiếp cận là learned policy, không có kết quả giải tích | Cao |

**Điểm cần cẩn trọng khi viết lại novelty:** P-MDP *có* tính "online partition adaptation" theo nghĩa per-slot. Vậy KHÔNG được claim "chưa ai làm online re-optimization của partition" — phải thu hẹp thành: chưa ai làm **reactive re-derivation giữa chừng inference để bảo toàn service continuity**, phân biệt rõ với per-task/per-slot re-decision.

---

## 2. CDPO — "DNN-Based Task Partitioning and Offloading with Reliability Guarantees in Multi-UAV-Assisted MEC System"

- **Nguồn:** IEEE conference 2024 (số hiệu 10756252). [IEEE Xplore](https://ieeexplore.ieee.org/document/10756252/) · Bản mở rộng có vẻ tồn tại trên [OpenReview](https://openreview.net/pdf?id=EY3RuiblKo) ("Robust DNN Partitioning and Task Offloading in Multi-UAV...", bị chặn bot-check, chưa đọc được)

### Bài này LÀM gì
- Multi-UAV làm MEC server phục vụ mobile devices (UAV là hạ tầng tính toán, không phải nguồn tác vụ).
- **Reliability = robust transmission**: dùng **CVaR (conditional value-at-risk)** phân tích xác suất truyền thành công trong điều kiện kênh xấu nhất → chọn quyết định **chống chịu trước** (proactive), tại thời điểm quyết định.
- Formulate bài toán **CDPO (Collaborative DNN Partitioning and Offloading)** — **chứng minh NP-hard**.

### Bài này KHÔNG làm gì
| Tiêu chí gap | Kết luận | Tin cậy |
|---|---|---|
| Reactive re-derivation sau node failure | Không — reliability của họ là proactive (CVaR lúc ra quyết định), không có cơ chế phục hồi giữa chừng | Cao |
| Comm cost nội sinh đa chặng FANET | Kênh UAV–device, không phải pipeline swarm-internal | Trung bình–cao |
| Service continuity của inference đang chạy | Không có bằng chứng | Trung bình–cao |

### Giá trị sử dụng ngay
**Trích dẫn NP-hardness của CDPO làm mỏ neo cho complexity gap** (Roadmap item 1, R1-W1/DA-3): "bài toán joint partitioning+offloading lân cận đã được chứng minh NP-hard [CDPO]; do đó chúng tôi dùng bounded-K làm đòn bẩy tractability và phân tích cấu trúc theo K." → trả lời trực tiếp yêu cầu của Reviewer 1 về hardness citation.

---

## 3. Due diligence mở rộng (các bài "reliability + partitioning" sát gap nhất)

| Bài | Cơ chế reliability | Reactive re-derivation? |
|---|---|---|
| **Reliable DNN Partitioning for UAV Swarm** (Zhao et al., IWCMC 2022) — [IEEE](https://ieeexplore.ieee.org/document/9824945/) | Deep Q-learning chọn partition thỏa **ràng buộc reliability** (xác suất thành công dưới nguy cơ đứt link/chết node) — proactive, chọn trước phương án bền | Không có bằng chứng |
| **LLHR** (Dhuheir et al., WCNC 2023) — [arXiv 2305.15858](https://arxiv.org/abs/2305.15858) (đã đọc full abstract, open access) | Reliability qua **công suất phát tối ưu**; giải **tuần tự 3 bài con**: power → vị trí UAV → placement layer | Không. Đây còn là ví dụ điển hình của "sequential decomposition" mà đề tài phản biện — **ứng viên baseline tốt** cho R1-W2 |
| **Robust DNN Partitioning under Uncertain Inference Time** — [arXiv 2503.21476](https://arxiv.org/abs/2503.21476) | Chance-constrained programming — proactive | Không |
| Guardians of the Deep Fog (edge-to-cloud) | Xác suất sống sót của node → dự phòng/replication | Không (và không phải UAV/FANET) |

Ghi chú thêm: có survey mới **"DNN Partitioning for Cooperative Inference in Edge Intelligence"** (ACM Computing Surveys) — nên cân nhắc trích dẫn trong §3.

---

## 4. KẾT LUẬN: Gap SỐNG SÓT, và được mài sắc hơn

Toàn bộ các bài reliability-aware partitioning tìm được đều thuộc một trong hai lớp:

1. **Proactive robustness** — chọn partition "bền" ngay từ đầu (CVaR, chance constraints, reliability constraint, replication): CDPO, Reliable-DNN-IWCMC, robust-inference-time, Guardians.
2. **Per-task/per-slot re-decision** — quyết định lại cho tác vụ MỚI khi trạng thái đổi (P-MDP), hoặc phân rã tuần tự (LLHR).

**Chưa bài nào làm lớp thứ 3: REACTIVE mid-pipeline recovery** — khi 1 UAV chết giữa lúc inference đang chạy dở:
- tập ranh giới partition phải được **suy diễn lại** (không chỉ re-assign phần việc cũ),
- ranh giới mới → **tensor size mới** → comm cost mới trên topology FANET hiện tại (tính nội sinh),
- và phải quyết định **resume từ tensor trung gian nào** (activation đã có ở boundary trước điểm chết) thay vì chạy lại từ đầu.

Đây chính là "điểm nghẽn kỹ thuật chỉ xuất hiện ở giao điểm" mà Devil's Advocate (DA-1) đòi hỏi: các self-healing controller hiện có giả định task placement cố định, không mô hình hóa việc placement bị *ràng buộc bởi lựa chọn partition* — nên không thể "bolt DADS lên Pan et al." như DA thách thức.

## 5. Đề xuất bước tiếp theo (chưa sửa file)
1. Viết lại đoạn novelty trong Literature Review §7: thay lập luận conjunction bằng taxonomy **proactive / per-task online / reactive mid-pipeline** + nêu đích danh obstruction ở trên.
2. Thêm CDPO (NP-hard) vào §3 + Methodology "Computational Complexity"; thêm LLHR làm named baseline trong Objective 4; thêm EURASIP SLR củng cố gap (đã có từ 3W scan).
3. Sau khi thống nhất câu chữ → sửa .tex/.bib cùng lúc với các lỗi citation đã phát hiện (4 orphan refs, 8 thiếu DOI, 9 "and others", lỗi Shao & Zhang, bi2020lyapunov).

**Việc tồn đọng:** file `3W_Scan_Nearest_Neighbors.md` không có trong thư mục dự án (có thể phiên trước lưu ở scratchpad tạm) — các kết luận 3W hiện chỉ còn trong tóm tắt của bạn; file này bù lại phần P-MDP/CDPO.
