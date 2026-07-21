# KỊCH BẢN NÓI — Bảo vệ đề cương, 13:00 thứ Tư 22/07/2026
*Bài nói ~13 phút (khung cho phép 10–15). Ngôn ngữ: tiếng Việt, thuật ngữ giữ tiếng Anh. Nếu hội đồng yêu cầu nói tiếng Anh: báo Claude dịch trong 1 buổi.*
*Quy ước: **NÓI** = lời thoại; **NHẤN** = chỗ dừng 1 nhịp, nói chậm; **CHUYỂN** = câu bắc cầu sang slide sau. Mốc thời gian là thời điểm PHẢI RỜI slide đó.*

---

## Slide 1 — Title 【rời lúc 0:30】
**NÓI:** Kính thưa hội đồng, em là Nguyễn Minh Hiếu. Đề cương của em có tên "Adaptive Joint Computation–Communication Orchestration for Collaborative Inference in UAV Swarms" — nghĩa là: điều phối một cách thích ứng, đồng thời cả tính toán lẫn truyền thông, để cả bầy UAV cùng nhau suy luận AI. Dưới sự hướng dẫn của TS. Nguyễn Thành Công và PGS. Phạm Hoàng Anh.

*Luyện phát âm tít — chia 3 hơi: [Adaptive Joint Computation–Communication Orchestration] // [for Collaborative Inference] // [in UAV Swarms]*

| Từ | Đọc (IN HOA = nhấn) | Bẫy |
|---|---|---|
| Adaptive | ơ-**ĐÉP**-tiv | không đọc "a-đáp-tài-vơ" |
| Joint | **giojnt** | bật đuôi **-nt** |
| Computation | kom-piu-**TÊY**-shân | nhấn TÊY |
| Communication | cơ-miu-ni-**KÊY**-shân | đừng líu với từ trên |
| Orchestration | o-**KÍT**-strêy-shân | "or-KÍT", KHÔNG phải "or-chét" |
| Collaborative | cơ-**LE**-bơ-rơ-tiv | nuốt nhẹ 2 âm cuối |
| Inference | **ÍN**-phơ-rân-s | nhấn ĐẦU |
| UAV | you-êy-**VI** | đọc từng chữ cái |
| Swarms | **s-wormz** | có /s/ đầu + đuôi /mz/ |

*Mẹo vần: TÊY-shân / KÊY-shân / STRÊY-shân — 3 từ dài cùng đuôi, luyện riêng cụm này 10 lần là cả câu trơn. Vấp thì bình thản đi tiếp sang phần dịch tiếng Việt, không đọc lại từ đầu.*

**CHUYỂN:** Em xin bắt đầu bằng bài toán thực tế.

## Slide 2 — Agenda 【0:50】
**NÓI:** Bài trình bày gồm 5 phần: bối cảnh, khoảng trống nghiên cứu, câu hỏi và đóng góp, phương pháp, và kế hoạch 3 năm. *(Không đọc từng mục — lướt 10 giây rồi đi tiếp.)*

## Slide 3 — Background & Motivation 【2:20】
**NÓI:** Bầy UAV nhỏ đang trở thành nền tảng cho các nhiệm vụ khẩn cấp: tìm kiếm cứu nạn, giám sát cháy rừng, kiểm tra hạ tầng. Muốn hữu ích, UAV phải chạy AI nhận diện ngay trên không. Nhưng ở đây có một mâu thuẫn cấu trúc: model AI càng ngày càng lớn, còn UAV nhỏ bị khóa chặt bởi SWaP — Size, Weight, Power. Chạy toàn bộ model trên một UAV thì không gánh nổi; đẩy dữ liệu về server thì phụ thuộc kết nối — mà vùng thiên tai thường mất sóng.

**NHẤN:** Hướng thứ ba — Collaborative Edge Inference: cắt model thành các phần, cả bầy cùng gánh — không phụ thuộc bất kỳ hạ tầng nào bên ngoài bầy. Giống một dây chuyền lắp ráp trên không.

**CHUYỂN:** Việc cắt-ghép model đã được thế giới chứng minh khả thi từ 2017. Vậy khoảng trống nằm ở đâu?

## Slide 4 — THE RESEARCH GAP ⭐ slide quan trọng nhất 【4:30】
**NÓI:** Khi khảo sát các công trình về độ tin cậy trong collaborative inference, em thấy toàn bộ literature rơi vào đúng hai lớp. Lớp một — *proactive robustness*: chọn sẵn một phương án cắt "bền" ngay từ đầu, bằng CVaR hay reliability constraints. Nhưng cấu hình bị đóng băng từ lúc phát lệnh — không phản ứng được giữa chừng. Lớp hai — *per-task online adaptation*: quyết định lại theo từng time slot, như bài P-MDP trên IoT Journal 2025, hay bài task migration IoT Journal tháng 7 năm 2026 — nghĩa là văn liệu mới cách đây hai tuần. Nhưng các phương pháp này chỉ giúp **tác vụ kế tiếp**, không cứu được tác vụ **đang chạy** khi một UAV rơi.

**NHẤN (nói chậm):** Lớp thứ ba — cứu lượt suy luận đang chạy dở — chưa ai làm. Và nó khó vì một lý do cụ thể: khi một UAV chết giữa pipeline, không thể chỉ giao lại việc cũ. Phải suy diễn lại ranh giới cắt; ranh giới mới sinh ra tensor trung gian kích thước khác; kích thước khác nghĩa là chi phí truyền khác trên topology còn lại; và phải tiếp tục từ activation đã có thay vì chạy lại từ đầu. Bốn mắt xích đó khóa vào nhau — đó chính là điểm nghẽn kỹ thuật mà luận án này giải.

**CHUYỂN:** Từ điểm nghẽn đó, em đặt hai câu hỏi nghiên cứu.

> **📖 GHI CHÚ thuật ngữ slide 4 — KHÔNG đọc trong bài, chỉ để hiểu sâu + trả lời khi bị hỏi:**
>
> **Reliability constraint** (cách của Zhao/IWCMC 2022): thêm ràng buộc *"xác suất inference thành công ≥ ngưỡng (vd 99%)"* vào bài toán tối ưu — mỗi node/link có xác suất hỏng ước lượng trước, solver chỉ được chọn phương án cắt/gán còn trên ngưỡng. Nôm na: *"chỉ được xây nhà kiểu chịu được bão cấp 12."*
>
> **CVaR — Conditional Value-at-Risk** (cách của Wang/CDPO 2024): thước đo rủi ro mượn từ tài chính. Thay vì tối ưu theo *kỳ vọng* (kỳ vọng che mất thảm họa hiếm), CVaR tối ưu theo *mức thiệt hại trung bình của x% tình huống xấu nhất* — CDPO dùng để đảm bảo truyền thành công ngay cả ở đuôi xấu của phân bố kênh.
>
> **Điểm chung — ý mà câu thoại cần truyền tải:** cả hai quyết định MỘT LẦN, TRƯỚC khi chạy, dựa trên xác suất; khi sự cố thật xảy ra giữa chừng thì không làm gì — phương án đã đóng băng. Ẩn dụ chốt: *"Họ mua bảo hiểm và xây nhà chống bão — em là đội cứu hộ khi nhà sập thật. Hai việc bổ sung nhau, nhưng literature mới chỉ có bảo hiểm, chưa có đội cứu hộ."* (Câu này đồng thời né đòn "vậy proactive vô dụng à?" — không: bổ sung, không thay thế.)
>
> **Nếu bị cắt ngang hỏi "CVaR là gì?" — trả lời 20 giây:** *"Dạ, thước đo rủi ro từ tài chính: thay vì tối ưu theo kỳ vọng, nó tối ưu theo thiệt hại trung bình của phần trăm tình huống xấu nhất — bài CDPO dùng nó để chọn phương án truyền vẫn thành công ngay cả khi kênh rơi vào đuôi xấu của phân bố."*

## Slide 5 — RQ & Contributions 【6:00】
**NÓI:** RQ1 — tối ưu đồng thời: cắt model tối đa K phần và gán cho UAV, tối thiểu hóa latency và energy dưới ràng buộc kép tính toán–truyền thông. Bài toán họ hàng gần nhất đã được chứng minh NP-hard năm 2024, nên em dùng bounded-K làm đòn bẩy tractability. RQ2 — thích ứng online: tái tối ưu khi topology đổi và UAV hỏng, bao gồm re-derive ranh giới cho inference đang chạy và resume từ activation cuối cùng đã giao.

Bốn đóng góp kỳ vọng: formulation tối ưu đồng thời; phân tích giải tích vai trò của K; mô hình chi phí truyền thông nội sinh; và cơ chế re-derivation phản ứng — cái thứ tư là phần chưa có tiền lệ.

**CHUYỂN:** Phương pháp gồm bốn phase.

## Slide 6 — Methodology overview 【6:40】
**NÓI:** Bốn phase nối tiếp: phân tích sơ bộ để lộ cấu trúc bài toán, formulation, giải bài toán joint cho RQ1, và cơ chế online cho RQ2. Em đi nhanh qua từng phase.

## Slide 7 — Phase 1: Preliminary Analysis 【7:30】
**NÓI:** Mô phỏng đơn giản hóa cho thấy ba regime rõ rệt trên mặt phẳng latency–energy: computation-dominant, communication-dominant, và vùng cân bằng — với một Pareto front thực sự. Không có cấu hình nào thắng cả hai mục tiêu. Điều này xác nhận: không thể tối ưu hai vế độc lập rồi ghép lại — phải giải chung.

## Slide 8 — Phase 2: Formulation 【8:40】
**NÓI:** Bài toán: minimize L(x) cộng λE(x) trên tập khả thi định bởi ràng buộc SWaP, truyền thông FANET, và thứ tự thực thi. Biến quyết định gồm lựa chọn điểm cắt và gán UAV. K bị chặn bởi min của số UAV và số điểm cắt hợp lệ — thực tế em kỳ vọng không quá 8; xác định chính xác ngưỡng lợi–hại của K là một mục tiêu phân tích của Objective 1.

## Slide 9 — Phase 3: Joint Optimization 【9:20】
**NÓI:** Phase 3 giải bài toán: phân tích cấu trúc phụ thuộc giữa cắt và gán, tìm substructure giải được và cơ hội xấp xỉ, đặc trưng hóa Pareto frontier theo K và điều kiện mạng.

## Slide 10 — Phase 4: Online Adaptation ⭐ 【10:50】
**NÓI:** Đây là phần trả lời RQ2. Control plane theo dõi telemetry — chất lượng link, pin, tải CPU. Khi một UAV rơi giữa pipeline, cơ chế của em làm ba việc: re-derive tập ranh giới cắt cho phần model chưa chạy xong; định tuyến lại tensor trên topology còn sống; và resume từ activation trung gian cuối cùng đã giao — không chạy lại từ đầu.

**NHẤN:** Các self-healing controller hiện có giả định task placement cố định. Ở đây placement bị ràng buộc bởi chính lựa chọn cắt — vì vậy không thể lắp ghép hai công cụ có sẵn mà thành.

**CHUYỂN:** Làm sao biết cơ chế này thực sự tốt hơn?

## Slide 11 — Expected Outcomes & Validation 【11:50】
**NÓI:** Kiểm chứng bằng co-simulation chuẩn ngành: NS-3 cho mạng, ROS/Gazebo cho chuyển động, dưới các kịch bản khắc nghiệt — node rơi, đứt link. Quan trọng nhất: so với ba baseline có tên — sequential partition-then-assign đại diện cho cách làm tách rời; static joint không có re-derivation để cô lập đóng góp của RQ2; và full-restart để cô lập giá trị của việc resume. Nếu joint không thắng sequential, luận điểm trung tâm sai — và em sẽ biết điều đó ngay từ năm nhất.

## Slide 12 — Timeline 【12:30】
**NÓI:** Ba năm, ba phase, ba bài báo — mốc là ngày nộp: bài 1 tháng 12 về joint optimization, bài 2 tháng 24 về communication-aware optimization, bài 3 tháng 30 về online re-optimization; hai bài đầu nhắm venue chu kỳ nhanh, bài ba nhắm journal. Sáu tháng cuối viết luận án.

## Slide 13 — Close 【13:00】
**NÓI:** Tóm lại một câu: luận án này dạy một bầy drone yếu cách cùng khiêng một bộ não AI lớn — biết khiêng kiểu nào đỡ tốn sức nhất, và biết đổi cách khiêng ngay giữa chừng khi một thành viên gục ngã, mà không phải đặt não xuống làm lại từ đầu. Em xin cảm ơn hội đồng và mong nhận được góp ý.

---

## Slide ẩn — chỉ mở khi Q&A (gõ số + Enter khi đang trình chiếu)
- **14** = 3 gaps chi tiết + "41 verified references"
- **15** = kiến trúc co-simulation (NS-3 / ROS / PyTorch)
- **16** = ⭐ bảng hàng xóm gần nhất (Wang/CDPO, Gao/P-MDP, Meng 2026) + "vì sao bolt A lên B thất bại" → rút ra khi bị hỏi câu B3/B4
- **17** = term card CVaR & reliability constraint + ẩn dụ "bảo hiểm vs đội cứu hộ" → mở khi bị hỏi "CVaR là gì / sao không chỉ cần plan robust từ đầu"

## Nếu cháy giờ (đang ở slide 8 mà đã quá phút 9)
1. Slide 9: chỉ nói 1 câu "Phase 3 giải bài toán này bằng phân tích cấu trúc và xấp xỉ" — tiết kiệm 30s.
2. Slide 7: bỏ giải thích 3 regime, chỉ nói "Pareto front sơ bộ xác nhận phải giải chung" — tiết kiệm 30s.
3. TUYỆT ĐỐI không cắt slide 4 và 10 — đó là toàn bộ novelty.

## Cheat sheet 1 dòng/slide (in ra cầm tay)
1. Chào + tên đề tài → 2. lướt agenda → 3. SWaP vs model lớn; CEI = dây chuyền → 4. ⭐ 2 lớp cũ / lớp 3 chưa ai làm / 4 mắt xích khóa nhau → 5. RQ1 NP-hard bounded-K; RQ2 re-derive+resume; 4 contributions → 6. 4 phase → 7. Pareto 3 regime → 8. min L+λE; K ≤ min(N,|P|), ≤8 → 9. cấu trúc + xấp xỉ → 10. ⭐ telemetry / re-derive / reroute / resume; placement ràng buộc bởi cắt → 11. NS-3+Gazebo; 3 baselines; "sai thì biết từ năm 1" → 12. 3 năm 3 bài; mốc = ngày nộp → 13. câu chốt bầy drone khiêng não.

## 3 câu trả lời phải thuộc lòng (từ QA Bank)
- **"K bằng mấy?"** → quy tắc min(N,|P|), thực tế ≤8, ngưỡng chính xác là mục tiêu phân tích của Objective 1 (Contribution 2).
- **"Bolt DADS lên Pan et al. là xong?"** → placement cố định vs placement ràng buộc bởi partition; 4 mắt xích (boundary→tensor→cost→resume) không xuất hiện khi hai bài toán tách rời. → mở slide 16.
- **"Bài P-MDP/Meng 2026 làm rồi mà?"** → per-slot/per-epoch cho tác vụ MỚI, kiến trúc device–server; em cứu tác vụ ĐANG CHẠY trong pipeline nội bộ swarm. → mở slide 16.

---

# SỔ CÂU HỎI Q&A — 26 câu có thể bị hỏi
*Trả lời chi tiết đầy đủ cho nhóm A ở `QA_Bank_Cau_Hoi_Lon_va_Diem_Yeu.md` phần B. Mỗi câu dưới đây: ý trả lời 1–2 dòng + slide ẩn cần mở (nếu có). Luyện: mỗi tối bốc 4 câu, trả lời to ≤45 giây.*

## A. Tính mới & định vị (dễ bị hỏi nhất)
1. **Chia nhỏ model AI có khả thi không, ai làm chưa?** → Đã kiểm chứng từ datacenter đến cụm Raspberry Pi (Neurosurgeon 2017, DeepThings chạy YOLOv2); em không chứng minh "chia được" mà giải "chia tối ưu + sống sót trên mạng bay". *(= B1)*
2. **Chia model trên multi-UAV CỤ THỂ như thế nào?** → DNN = chồng tầng tuần tự; giữa 2 tầng chỉ cần truyền 1 tensor → đó là chỗ cắt. Hai bước: (i) triển khai — chọn K−1 điểm cắt, xẻ weights thành K gói, nạp mỗi gói vào 1 drone (mỗi con chỉ chứa 1/K model → thắng SWaP); (ii) runtime — A chạy tầng 1–6 → tensor qua radio → B chạy 7–12 → C chạy nốt. Số minh họa (ResNet): tensor ở tầng nông ~800KB (to hơn ảnh gốc 150KB!), tầng sâu ~100KB, output 4KB → cắt sớm tốn radio, cắt sâu dồn tải lên 1 con → điểm cắt + gán là BIẾN tối ưu, không phải tham số chọn trước. Bonus: luồng ảnh liên tục → pipeline, throughput tăng ~K lần; họ thay thế: cắt theo không gian ảnh (DeepThings). → chỉ Figure 1 trong proposal khi trả lời.
3. **Điểm mới so với các bài 2024–2026 gần nhất?** → Taxonomy 3 lớp; hai lớp đầu đã có người làm, lớp reactive mid-inference chưa. → slide 16. *(= B3, B4)*
4. **Novelty là "ghép 3 mảng có sẵn" thôi?** → Không — nêu đích danh obstruction: placement ràng buộc bởi partition khiến self-healing và partitioning không lắp ghép được; 4 mắt xích khóa nhau. *(= B3)*
5. **Đề tài này khác gì luận văn thạc sĩ "áp dụng AI cho drone"?** → 3 chữ ký tiến sĩ: formulation mới + chứng cứ NP-hard; obstruction lý thuyết chưa ai giải; chuẩn công bố quốc tế. *(= B10)*
6. **Nếu tháng sau có bài giải đúng gap này thì sao?** → Gap đã soi đến literature 07/2026 (2 tuần trước); nếu xuất hiện, phạm vi co lại về phân tích K + formulation coupled — vẫn đủ 2 bài đầu; RQ2 chuyển thành so sánh/mở rộng cơ chế của họ.

27. **Tít đề tài nghĩa là gì? (hoặc: "tít nghe kêu quá")** → Không phải chuỗi từ khóa — mỗi chữ là một mảnh của luận án:

| Chữ trong tít | Nghĩa | Ứng với |
|---|---|---|
| Adaptive | thích ứng khi mạng đổi, UAV rơi | RQ2 |
| Joint | tối ưu *đồng thời*, không tách rời | RQ1 |
| Computation–Communication | cắt ở đâu quyết định truyền bao nhiêu | coupling — Gap 1 |
| Orchestration | có "nhạc trưởng" điều phối cả bầy | control plane — Phase 4 |
| Collaborative Inference | cả bầy cùng gánh một model | CEI — nền móng |
| UAV Swarms | trên mạng bay FANET biến động | bối cảnh — Gap 2 |

### 📌 Thẻ dẫn chứng định lượng cho câu 1–2 (số liệu ĐÃ XÁC MINH từ nguồn gốc — đọc đúng số, đừng làm tròn khác đi)

**1. Neurosurgeon — Kang et al., ASPLOS 2017** (DOI 10.1145/3037697.3037698 — có trong references.bib của đề cương, key `kang2017neurosurgeon`):
- Cắt DNN tự động theo tầng giữa thiết bị di động (Jetson TK1) và cloud, đo trên 8 ứng dụng DNN thật.
- **Latency: nhanh hơn trung bình 3.1×, tối đa 40.7×** so với đẩy hết lên cloud.
- **Năng lượng thiết bị: giảm trung bình 59.5%, tối đa 94.7%.**
- Ý nghĩa với đề cương: chứng minh tồn tại "điểm cắt vàng" và lợi ích đo được của việc chọn điểm cắt đúng — chính là tiền đề của RQ1.

**2. DeepThings — Zhao, Barijough & Gerstlauer, IEEE TCAD vol. 37 no. 11, 2018** (DOI 10.1109/TCAD.2018.2858384):
- Chạy **YOLOv2 thật trên cụm 2–6 thiết bị edge lớp Raspberry Pi 3** (mỗi thiết bị dưới 23MB bộ nhớ khả dụng cho inference).
- **Speedup 1.7×–3.5×** khi tăng từ 2 lên 6 thiết bị; **giảm >68% memory footprint** mỗi thiết bị nhờ Fused Tile Partitioning (họ cắt theo không gian ảnh — họ hàng của hướng cắt theo tầng).
- Ý nghĩa: model phát hiện vật thể — đúng loại tác vụ của UAV — đã chạy phân tán thành công trên phần cứng yếu hơn cả Jetson.
- Giao tiếp giữa các Pi: WiFi 802.11 qua **router trung tâm** (infrastructure, 1 hop, ~100Mbit ổn định), TCP socket, node gateway điều phối + work stealing. → Nếu bị hỏi "sao không dùng luôn cách này": mạng của họ là chế độ "dễ" — có hạ tầng, không ai chết; work stealing cân bằng tải cho các ô độc lập, không cứu được chuỗi tuần tự đứt mắt xích; gateway là SPOF không xử lý. Đúng chữ ký Gap 2 + Gap 3.

**3. Quy mô công nghiệp:** mọi LLM lớn (GPT, BLOOM 176B...) đều chạy bằng pipeline/tensor parallelism trên nhiều GPU — cắt model là chuẩn vận hành hằng ngày ở datacenter (GPipe, NeurIPS 2019; Megatron-LM). Dự án Petals (2022) còn chạy BLOOM-176B phân tán qua Internet công cộng.

**3b. Dẫn chứng MỚI NHẤT (2024) — EdgeShard, IEEE IoT Journal 2024** (arXiv 2405.14371): chạy **Llama2 phân tán trên testbed thật 15 thiết bị, gồm 12 Jetson AGX Orin** — đúng lớp chip tham chiếu của đề cương; **giảm đến 50% latency, tăng 2× throughput**; dùng dynamic programming chọn đồng thời thiết bị + điểm cắt. Câu dùng: *"2024 người ta đã cắt cả LLM trên đúng lớp chip Jetson em nhắm — trên bàn thí nghiệm đứng yên; em đưa nó lên trời."* Kèm: Ren et al. (IEEE WCNC 2024, DOI 10.1109/WCNC57260.2024.10570535) — pipeline inference trên chính UAV swarm, DRL, mô phỏng.

**3c. Hàng xóm sát nhất — Kim et al. 2024 DRL-RLD (Appl. Sci. 14(23):10832):** tái phân bổ layer khi UAV chết, swarm ad-hoc — ĐÃ cite trong Gap 3 + bảng so sánh + slide 16. Khác biệt phải nói đúng: họ phục vụ tiếp request MỚI (không resume, không phân tích cấu trúc); em cứu request ĐANG CHẠY. Chi tiết đầy đủ trong QA Bank.

**4. Con số tensor trong giải thích câu 2** (tự tính từ kiến trúc ResNet-18 chuẩn, activation FP32 — nói rõ nguồn nếu bị hỏi): boundary nông 56×56×64×4B ≈ 800KB; boundary sâu 7×7×512×4B ≈ 100KB; ảnh vào 224×224×3 uint8 ≈ 150KB; output ~4KB. Chênh nhau ~8 lần giữa hai điểm cắt → lý do "cắt ở đâu" là biến tối ưu.

**Cách dùng khi trả lời B1:** đọc đúng 3 con số — "Neurosurgeon: 3.1× latency, 59.5% năng lượng; DeepThings: YOLOv2 trên 6 con Raspberry Pi, speedup 3.5×" — rồi chốt: "em không chứng minh chia được; em chọn cách chia tối ưu và giữ dây chuyền sống trên mạng bay."

## B. Kỹ thuật — formulation
7. **K bằng mấy? Ai chọn K?** → thuộc lòng ở trên. *(= B2)*
8. **Vì sao tin bài toán NP-hard?** → Bài toán họ hàng (CDPO, Wang et al. 2024) đã chứng minh NP-hard — em cite chứ không tự claim; bounded-K là đòn bẩy tractability.
9. **λ chọn thế nào? Weighted-sum có quét đủ Pareto không?** → λ quét dải để dựng front; weighted-sum bỏ sót điểm non-convex — nếu quan trọng sẽ dùng ε-constraint bổ sung; Phase 1 mới là minh họa cấu trúc.
10. **Model có nhánh (ResNet skip, YOLO FPN) thì cắt sao?** → Tập điểm cắt hợp lệ P thu hẹp tại các điểm khớp nhánh; bounded-K trên tập ứng viên hữu hạn xử lý tự nhiên; cắt tại nhánh = truyền 2 luồng, đã nằm trong mô hình chi phí.
11. **Nén tensor thì mất accuracy — sao objective không có accuracy?** → Phiên bản hiện tại: accuracy là ràng buộc cứng (nén bảo toàn hoặc mức nén cố định); thêm chiều accuracy là mở rộng tự nhiên của Phase 2. *(= B7 — điểm yếu tự biết #10)*
12. **Inference đơn lẻ hay luồng liên tục? Latency hay throughput?** → Formulation gốc: latency của một inference; pipeline liên tục (throughput) là chế độ đánh giá bổ sung trong co-sim — cắt mịn có lợi hơn cho throughput, đây chính là một regime của phân tích K.

## C. Kỹ thuật — online & hệ thống
13. **Control plane chạy ở đâu? Nó chết thì sao?** → Orchestrator nhẹ + leader election khi mất node giữ vai trò; bounded-K giữ chi phí re-optimize nhỏ nên node nào cũng gánh được. *(= B8 — điểm yếu tự biết #11)*
14. **Re-optimize có kịp thời gian thực không?** → Vì K nhỏ nên không gian tìm kiếm hẹp; nếu vẫn vượt budget → fallback trong bảng risk: precompute contingency plans, online chỉ chuyển plan.
15. **Activation trung gian lưu ở đâu, node giữ nó cũng chết thì sao?** → Activation tại boundary được giữ ở node gửi cho đến khi có ACK của node sau; mất cả hai node liên tiếp → resume từ boundary trước đó; xác suất và chi phí thuộc phân tích Phase 3.
16. **2–3 UAV rơi cùng lúc thì sao?** → Cùng một cơ chế, feasible set co lại; nếu không còn cấu hình khả thi với K ≤ N còn lại → graceful degradation (model nhỏ hơn / báo mất dịch vụ) — trường hợp biên được ghi trong kịch bản stress test.
17. **Bảo mật/tấn công vào tensor truyền giữa UAV?** → Ngoài phạm vi luận án (đã khoanh vùng ở Risk Considerations); tầng mã hóa link-layer chuẩn dùng được vì cost model chỉ cần payload size — cộng thêm hằng số.
18. **Các phần đã cắt có bắt buộc TẤT CẢ phải chạy đúng không?** → Đúng — chuỗi K khúc là tuần tự bắt buộc, một khúc hỏng là cả inference đứng (chạy tiếp sức); độ tin cậy nhân theo chuỗi ~p^K → K lớn bị phạt kép: truyền nhiều hơn VÀ dễ đứt hơn — thêm một lý do độc lập cho bounded-K; và đây chính là lý do tồn tại của RQ2 (không cứu thì full-restart). Cửa thoát phụ: early-exit heads (SPINN) cho kết quả accuracy thấp từ phần đã chạy — nêu như extension.
19. **Scalability: 50–100 UAV thì sao?** → Bài toán tách theo cụm pipeline (mỗi inference dùng ≤K node); bầy lớn = nhiều pipeline song song + bài toán gán cụm — mở rộng tự nhiên, không đổi cấu trúc lõi.

## D. Đánh giá & kế hoạch
20. **Mô phỏng tin được đến đâu, sao không bay thật?** → Combo NS-3+ROS+Gazebo là chuẩn ngành cho claim mạng+robot; luận án nhắm structural insight; bay thật là hướng sau tiến sĩ. *(= B6)*
21. **Baseline nào chứng minh "joint > sequential"?** → 3 baseline có tên trong Objective 4: sequential (kiểu LLHR), static-joint, full-restart — cô lập từng đóng góp; thua baseline là biết từ năm 1. *(= B5)*
22. **Metric nào đo "service continuity"?** → Tỷ lệ inference hoàn thành khi có failure, thời gian gián đoạn trung bình, và % công việc phải tính lại — so trực tiếp với full-restart.
23. **3 bài IEEE trong 3 năm có thực tế không?** → Mốc = ngày NỘP; bài 1–2 venue chu kỳ nhanh, bài 3 journal; phase sau chạy song song vòng review của bài trước. *(= B9)*
24. **Em đã làm được gì rồi?** → Phân tích Pareto sơ bộ (slide 7); khảo sát 41 tài liệu đã xác minh đến 07/2026; formulation khung min L+λE; và bảng so sánh 4 chiều làm cơ sở falsifiable cho gap.
25. **NS-3 + Gazebo tích hợp nổi tiếng khó — trượt tiến độ thì sao?** → Có trong bảng risk trigger→fallback: nếu quá tháng 8 → chạy network-only (NS-3 + trace compute) để Phase 2 không bị chặn.

## E. Ứng dụng & đạo đức
26. **Đề tài phục vụ gì cho Việt Nam? Có nhạy cảm quân sự không?** → Ứng dụng dân sự cụ thể: cứu hộ bão lũ miền Trung, giám sát cháy rừng, kiểm tra hạ tầng điện — các kịch bản mất kết nối hạ tầng là thực tế ở VN; phạm vi đạo đức đã khoanh trong Risk Considerations: không targeting, không tracking người, không vũ khí hóa; nghiên cứu theo hướng dẫn đạo đức của trường.
