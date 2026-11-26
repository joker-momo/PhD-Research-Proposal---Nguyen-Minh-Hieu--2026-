# BẢN TIẾNG VIỆT ĐỂ REVIEW — Hồ sơ Seed Grant AVSTC
*(Phiên bản 3 — đã co scope theo hướng **C + B** và **bổ sung 12 trích dẫn**. Bản nộp là tiếng Anh trong `proposal.tex` / `proposal.pdf`.)*

**Thay đổi so với bản 1:**
- **C** — Bỏ ROS/Gazebo khỏi phạm vi; dùng **NS-3 + độ trễ tính toán lấy từ đo đạc thật (trace-driven)**. Co-simulation đầy đủ để dành cho luận án năm 2.
- **B** — Cơ chế phục hồi hạ cấp từ "đã kiểm chứng" xuống **"trình diễn khả thi lần đầu" (proof of concept)**.
- Thêm hẳn một mục **"Phạm vi dự án"** nói rõ cái gì trong, cái gì ngoài — biến việc co scope thành điểm mạnh về tính thực tế thay vì điểm yếu.
- Bỏ mâu thuẫn "tháng 2 / tháng 8" trong phần rủi ro; thay bằng 2 rủi ro thật của phạm vi mới.
- **Thêm 12 trích dẫn** (lấy từ `references.bib` đã xác minh của luận án) + danh mục tài liệu tham khảo cuối Mục 5.

---

# MỤC 5 — PROJECT PROPOSAL (860/1000 từ, chưa tính danh mục TLTK)

**Tên đề tài:** Suy luận biên cộng tác bền vững trên bầy UAV: Tối ưu đồng thời tính toán–truyền thông và trình diễn đầu tiên về phục hồi giữa chừng suy luận

**Thời gian:** 01/11/2026 – 30/04/2027 (6 tháng)

## 5.1 Bối cảnh và động lực

Bầy UAV đang trở thành công cụ thiết yếu cho ứng phó thảm họa, tìm kiếm cứu nạn và kiểm tra hạ tầng — những nhiệm vụ có ý nghĩa quốc gia trực tiếp với Việt Nam, nơi bão lũ hằng năm thường xuyên làm tê liệt hạ tầng truyền thông mặt đất. Nhưng để UAV chạy AI nhận thức ngay trên không thì vấp phải mâu thuẫn cấu trúc: mạng nơ-ron sâu hiện đại vượt quá giới hạn Kích thước–Khối lượng–Năng lượng (SWaP) của bất kỳ UAV nhỏ nào, trong khi đẩy dữ liệu về đám mây lại giả định sẵn có kết nối — chính thứ vừa mất. Suy luận biên cộng tác (CEI) giải quyết bằng cách cắt mô hình chia cho cả bầy, để tập thể chạy được thứ không cá thể nào chạy nổi **[1]–[3]**.

Có hai trở ngại. **Thứ nhất**, ranh giới cắt quyết định kích thước tensor trung gian, mà tensor quyết định độ trễ truyền và năng lượng RF trên mạng bay FANET **[4], [5]**: chi phí tính toán và truyền thông dính chặt nhau, không tối ưu riêng rẽ được. **Thứ hai**, ít được nghiên cứu hơn: các hướng tiếp cận quan tâm độ tin cậy hoặc chọn sẵn cấu hình bền trước khi chạy **[6], [7]**, hoặc quyết định lại vị trí cho các tác vụ MỚI đến **[8]–[10]**. Hệ quả: khi một UAV rơi *giữa lúc đang suy luận*, request đang chạy dở không có đường phục hồi nào — nó ngầm định bị chạy lại từ tầng đầu, vứt bỏ phần đã tính đúng.

## 5.2 Phạm vi dự án *(mục mới)*

Dự án này là **một lát cắt 6 tháng có chủ đích** của một chương trình tiến sĩ lớn hơn. Nó nhắm vào lớp nền mà mọi thứ khác phụ thuộc vào: năng lực đánh giá dựa trên đo đạc thật, một bộ tối ưu đồng thời hoạt động được, và **một trình diễn khả thi đầu tiên** về phục hồi giữa chừng suy luận.

Hai thứ **cố ý để ngoài phạm vi**, dành cho giai đoạn sau của luận án: (a) đồng mô phỏng robotics đầy đủ với ROS/Gazebo — dự án này dùng NS-3 với độ trễ tính toán lấy từ đo đạc thật, đủ cho các câu hỏi đặt ra ở đây; và (b) một control plane trực tuyến đã kiểm chứng đầy đủ. **Việc nêu rõ ranh giới này là có chủ đích** — các sản phẩm giao nộp bên dưới được định cỡ đúng bằng những gì 6 tháng có thể tạo ra một cách vững chắc.

## 5.3 Mục tiêu

- **O1.** Thiết lập **hệ đánh giá dựa trên đo đạc**: đo chi phí tính toán và kích thước activation từng tầng trên nền tảng lớp Jetson, dùng số đo đó điều khiển mô phỏng FANET trong NS-3.
- **O2.** Xây dựng và giải bài toán tối ưu đồng thời cắt bounded-K + phân công UAV dưới ràng buộc SWaP–FANET, và đặc trưng hóa **bằng thực nghiệm** các vùng mà tăng K không còn bù nổi chi phí truyền thông.
- **O3.** **Trình diễn phục hồi giữa chừng ở mức proof-of-concept**: khi tiêm lỗi node, suy diễn lại ranh giới cắt trên topology còn sống và chạy tiếp từ activation cuối cùng đã giao, đo lượng tính toán tiết kiệm được so với chạy lại từ đầu.

## 5.4 Chương trình nghiên cứu

**Tháng 1–2 — Đo đạc và dựng hệ đánh giá.** Đo hồ sơ các mô hình phát hiện tiêu biểu (họ YOLO, họ ResNet) trên phần cứng lớp Jetson để lấy độ trễ suy luận, mức tiêu thụ năng lượng và kích thước tensor activation từng tầng. Dựng hệ đánh giá trong NS-3: topology FANET với các mô hình chuyển động hàng không chuẩn, biến động chất lượng liên kết, và độ trễ tính toán lấy từ số đo thật thay vì giả định tổng hợp. *Mốc:* hệ chạy được một pipeline suy luận end-to-end qua các UAV mô phỏng với chi phí từng tầng đo thật.

**Tháng 3–4 — Bộ tối ưu và đặc trưng hóa vùng hoạt động.** Hình thức hóa hàm mục tiêu L(x) + λE(x) trên các biến cắt và phân công, ràng buộc bởi giới hạn tính toán/bộ nhớ/năng lượng từng node, ràng buộc liên kết và thứ tự thực thi. Hiện thực liệt kê chính xác cho K nhỏ và heuristic tham lam cho quy mô lớn hơn; bài toán họ hàng đã được chứng minh NP-hard **[11]**, đó là lý do dùng giới hạn bounded-K. Quét K, số UAV và chất lượng liên kết để thu mặt đánh đổi độ trễ–năng lượng, so với baseline cắt-rồi-phân-công (đại diện cách làm tách rời hiện nay). *Mốc:* đặc trưng hóa thực nghiệm các vùng hoạt động của K, kèm so sánh định lượng với baseline tuần tự.

**Tháng 5–6 — Proof-of-concept phục hồi và phổ biến kết quả.** Bổ sung cơ chế tiêm lỗi vào hệ đánh giá, và hiện thực cơ chế phục hồi đầu tiên: phát hiện mất node đang giữ một đoạn đang chạy, suy diễn lại ranh giới cắt cho phần mô hình chưa xong trên topology còn sống, và chạy tiếp từ activation cuối cùng đã giao thành công. Đo khối lượng tính toán lặp lại, độ trễ phát sinh và tỷ lệ hoàn thành so với baseline chạy-lại-từ-đầu. Chuẩn bị một bài báo hội nghị cùng cộng tác viên Úc và công bố hệ đánh giá, bộ dữ liệu đo đạc và cấu hình kịch bản. *Mốc:* chứng minh định lượng rằng phục hồi tốt hơn chạy lại, kèm điều kiện biên mà điều đó đúng.

## 5.5 Kết quả kỳ vọng

1. **Bộ dữ liệu đo đạc mã nguồn mở**: chi phí tính toán, năng lượng và kích thước activation từng tầng cho các mô hình phát hiện tiêu biểu trên phần cứng hạn chế SWaP.
2. **Hệ đánh giá NS-3 mã nguồn mở** kèm cấu hình kịch bản tái lập được — tài sản dùng lại cho các đối tác AVSTC nghiên cứu trí tuệ biên trên không.
3. **Bộ tối ưu đồng thời bounded-K** kèm đặc trưng hóa thực nghiệm vai trò của K và so sánh định lượng với cách tối ưu tách rời.
4. **Cơ chế phục hồi mức proof-of-concept** với số đo đầu tiên về lượng tính toán tiết kiệm được so với chạy lại sau sự cố giữa chừng.
5. **Một bài báo hội nghị** đồng tác giả với cộng tác viên Úc, cùng báo cáo kỹ thuật và vật liệu demo cho đối tác công nghiệp.

## 5.6 Tác động và rủi ro

Dự án tạo nền cho ngữ nghĩa phục hồi trong suy luận phân tán trên mạng biến động: cơ chế lưu-điểm-rồi-chạy-tiếp là thường quy trong huấn luyện tại trung tâm dữ liệu nhưng vắng mặt trong pipeline suy luận trên mạng bay — nơi điểm quay lại là một activation nằm rải rác trên các node đang di chuyển, và việc lập lại kế hoạch tự nó là một bài toán tối ưu; một tổng quan hệ thống gần đây xác nhận rằng việc quản lý đồng thời tính toán và truyền thông khi offload trong bầy UAV vẫn còn bỏ ngỏ **[12]**. Về thực tiễn, Việt Nam đối mặt thiên tai lặp lại, trong đó hạ tầng mặt đất sập đúng lúc cần quan sát trên không nhất; một bầy UAV duy trì được nhận thức mà không cần hạ tầng bên ngoài, và sống sót khi mất từng máy bay, phục vụ trực tiếp nhu cầu đó. Công thức này cũng chuyển giao được sang đội robot mặt đất và phương tiện hàng hải.

**Hai rủi ro có phương án lùi cam kết trước.** Nếu việc mua phần cứng bị chậm, tháng 1–2 vẫn chạy bằng benchmark của nhà sản xuất và số liệu đã công bố, thay bằng số đo thật khi hàng về — thiết kế hệ đánh giá không đổi. Nếu cơ chế phục hồi không đạt ngân sách thời gian lập-lại-kế-hoạch trong kỳ hạn, sản phẩm giao nộp chuyển thành **đặc trưng hóa vùng thời gian lập kế hoạch khả thi** — vẫn thiết lập được tính khả thi và cung cấp đầu vào trực tiếp cho giai đoạn tiến sĩ kế tiếp.

## 5.7 Tài liệu tham khảo (12 mục — đều lấy từ `references.bib` đã xác minh của luận án)

| # | Nguồn | Dùng để chống đỡ điều gì |
|---|---|---|
| [1] | Kang et al., ASPLOS 2017 — Neurosurgeon | CEI khả thi, tồn tại điểm cắt tối ưu |
| [2] | Hu et al., INFOCOM 2019 — DADS | Cắt DNN thích ứng |
| [3] | Qu et al., IEEE Commun. Mag. 2024 | CEI cho bầy UAV |
| [4] | Amponis et al., J. Syst. Archit. 2021 | Định tuyến FANET, mạng bay biến động |
| [5] | Shao, Mao & Zhang, IEEE JSAC 2022 | Chi phí truyền thông gắn với tác vụ suy luận |
| [6] | Zhao et al., IWCMC 2022 | Lớp proactive — ràng buộc độ tin cậy |
| [7] | Dhuheir et al., WCNC 2023 — LLHR | Lớp proactive — phân rã tuần tự |
| [8] | Gao et al., IEEE IoT-J 2025 — P-MDP | Lớp per-task — quyết định lại theo slot |
| [9] | Meng et al., IEEE IoT-J 2026 | Lớp per-task — migration cân bằng tải |
| [10] | Kim et al., Applied Sciences 2024 — DRL-RLD | Lớp per-task — tái phân bổ khi UAV chết |
| [11] | Wang, Wang & Dai, ISPCE-ASIA 2024 — CDPO | **Chứng minh NP-hard** |
| [12] | Baktayan et al., EURASIP JWCN 2024 | Tổng quan hệ thống xác nhận gap còn mở |

---

# MỤC 6 — IMPACT AND COLLABORATION

## 6a. Lợi ích cho hợp tác chiến lược Việt–Úc (281/300 từ)

Dự án được thiết kế như **một sản phẩm chung**, không phải hai nỗ lực song song. Các đầu ra — bộ dữ liệu đo đạc, hệ đánh giá, bộ tối ưu và bản trình diễn phục hồi — đều nhằm để cả hai bên cùng tạo ra, cùng dùng, cùng công bố. Hệ đánh giá và bộ dữ liệu là kết quả bền vững nhất: một môi trường NS-3 có tài liệu, kèm số đo tính toán thật và cấu hình kịch bản tái lập được, lưu trữ công khai và duy trì sau khi hết tài trợ. Khi nó tồn tại, bất kỳ đối tác AVSTC nào cũng đánh giá được các đề xuất về trí tuệ biên trên không trên cùng một nền chung — hạ chi phí khởi động cho mọi hợp tác về sau.

Quan hệ đối tác khai thác **thế mạnh bổ sung**. Phía Úc đóng góp chiều sâu về mạng không dây, trí tuệ biên và phương pháp tối ưu; phía Việt Nam đóng góp hệ thống nhúng, nền tảng UAV, và — quan trọng nhất — bối cảnh vận hành sinh ra bài toán. Mùa bão lũ hằng năm ở Việt Nam cung cấp điều kiện sự cố thực tế mà phòng thí nghiệm ở nơi hạ tầng ổn định khó đặc tả được. Sự bất đối xứng này khiến hợp tác đi **hai chiều** thật sự.

Ba cơ chế đảm bảo tính liên tục được cài sẵn trong 6 tháng: bài báo hội nghị đồng tác giả; kho mã nguồn và dữ liệu chung dưới quản trị chung; và buổi demo kỹ thuật cho đối tác công nghiệp về mạng hàng không. Mỗi thứ tạo ra **bằng chứng của quan hệ đang vận hành**, không phải ý định hình thành quan hệ.

Chủ đề nằm đúng lĩnh vực ưu tiên của AVSTC — AI, robotics, kết nối thế hệ mới — và đúng chủ đề "khả năng chống chịu" của Giai đoạn II. Bước tiếp theo tự nhiên là một đề xuất song phương lớn hơn, **mở rộng từ nền tảng mô phỏng này sang đồng mô phỏng robotics đầy đủ và thử nghiệm thực địa**; grant này tạo nền kỹ thuật, hồ sơ công bố và quan hệ làm việc mà đề xuất đó đòi hỏi.

## 6b. Nghiên cứu quốc tế giúp gì cho sự nghiệp của tôi (193/200 từ)

Tôi đang là nghiên cứu sinh năm thứ nhất tại Trường Đại học Bách Khoa TP.HCM, vừa bảo vệ đề cương về điều phối thích ứng tính toán–truyền thông cho bầy UAV. Grant này định hình quỹ đạo đó theo ba cách.

**Thứ nhất**, nó biến một luận án đơn-cơ-sở thành công trình đồng tác giả quốc tế. Công bố cùng cộng tác viên Úc tại hội nghị quốc tế giúp thiết lập hồ sơ trong cộng đồng trí tuệ biên đúng giai đoạn hồ sơ đó có giá trị nhất.

**Thứ hai**, nó rèn năng lực mà chỉ làm luận án không đòi hỏi: xây dựng và phát hành phần mềm cùng dữ liệu nghiên cứu để người khác dùng lại, quản lý dự án có tài trợ theo sản phẩm giao nộp và lịch giải ngân, báo cáo trước hội đồng tài trợ. Đây là kỹ năng phân biệt người **thực hiện** dự án với người **dẫn dắt** được nhóm.

**Thứ ba**, nó thiết lập quan hệ làm việc với một nhóm nghiên cứu Úc đúng lĩnh vực. Hợp tác trực tiếp là con đường thực tế tới đồng hướng dẫn, cơ hội sau tiến sĩ, và vị thế tự chủ trì đề xuất song phương. Mục tiêu của tôi là tiếp tục nghiên cứu tại Việt Nam nhưng vận hành trong mạng lưới quốc tế — grant này là bước đi cụ thể đầu tiên.

---

# MỤC 8 — NGÂN SÁCH 6 THÁNG (AUD $15,000)

Toàn bộ là chi phí R&D phục vụ trực tiếp hoạt động ở Mục 5. Ngân sách sắp xếp để **hai đợt giải ngân khớp hai giai đoạn dự án**.

### Đợt 1 — sau khi ký hợp đồng (Tháng 1–4)

| Khoản mục | Diễn giải | AUD |
|---|---|---:|
| Phần cứng tính toán biên | 3 bộ kit lớp Jetson kèm bộ nhớ, nguồn, module không dây. **Toàn bộ phương pháp là trace-driven**: mọi độ trễ tính toán trong hệ đánh giá đều đến từ đo đạc trên phần cứng này — không có nó thì đánh giá dựa trên giả định thay vì dữ liệu. | 2.200 |
| Thiết bị đo công suất & vô tuyến | Module đo công suất, ăng-ten và phụ kiện vô tuyến để lấy mức tiêu thụ năng lượng từng tầng và hiệu chỉnh hành vi liên kết theo đo đạc thật thay vì tham số mặc định của bộ mô phỏng. | 1.200 |
| Hạ tầng tính toán mô phỏng | Nâng cấp workstation GPU / thuê compute đám mây cho các đợt quét tham số theo K, số UAV, độ cơ động, điều kiện liên kết (tháng 3–4). Đặc trưng hóa mặt đánh đổi cần hàng nghìn lượt chạy. | 3.000 |
| Trợ lý nghiên cứu | Sinh viên đại học/cao học bán thời gian 6 tháng: phát triển hệ đánh giá, viết kịch bản, tự động hóa thí nghiệm — giải phóng thời gian NCS cho phần xây dựng bài toán và phân tích. | 3.600 |
| **Cộng đợt 1 (hai phần ba)** | | **10.000** |

### Đợt 2 — sau khi nộp báo cáo cuối (Tháng 5–6)

| Khoản mục | Diễn giải | AUD |
|---|---|---:|
| Chi phí công bố | Phí đăng ký hội nghị và phí xuất bản truy cập mở cho bài báo đồng tác giả (Kết quả 5). Truy cập mở là cần thiết để đối tác AVSTC dùng được kết quả mà không vướng rào cản thuê bao. | 2.200 |
| Đi lại hợp tác | Một vé khứ hồi phổ thông và lưu trú cho chuyến làm việc hai tuần với cộng tác viên Úc: thiết kế thí nghiệm chung, bàn giao hệ đánh giá, chuẩn bị bài báo. | 2.400 |
| Phát hành dữ liệu & mã nguồn | Tài liệu hóa, lưu trữ dữ liệu kèm mã định danh vĩnh viễn, vật liệu demo cho đối tác công nghiệp (Kết quả 1, 2, 5). | 400 |
| **Cộng đợt 2 (một phần ba)** | | **5.000** |
| **TỔNG ĐỀ NGHỊ** | | **15.000** |

**Ghi chú.** (i) Không khoản nào trùng với hạ tầng sẵn có tại cơ sở chủ trì; phần cứng mang tính đặc thù cho đo hồ sơ đại diện SWaP và được giữ làm tài sản phòng thí nghiệm. (ii) Đợt 1 bao phủ mọi thứ cần để tạo ra hệ đánh giá, bộ tối ưu và phần đánh giá — chậm giải ngân đợt 2 không làm đình trệ phần kỹ thuật. (iii) Nếu khoản nào không hợp lệ, số tiền chuyển sang hạ tầng tính toán mô phỏng — làm sâu thêm khảo sát tham số mà không đổi sản phẩm giao nộp.

---

# ⚠️ ĐIỂM CẦN BẠN QUYẾT / KIỂM TRA

1. **Tên + tổ chức cộng tác viên Úc** — biến `\AusCollaborator` trong file LaTeX
2. **Ngày bắt đầu/kết thúc** — đang để 01/11/2026 – 30/04/2027; đối chiếu với lịch thực tế năm nhất của bạn
3. **Khoản "Trợ lý nghiên cứu" $3.600** — hỏi ban tổ chức xem chi phí nhân sự có hợp lệ không
4. **Giá phần cứng Jetson** — tra giá nhập tại VN thời điểm nộp
5. **Tên hội nghị mục tiêu** — nếu đã nhắm venue cụ thể thì ghi vào Kết quả 5
6. **Danh mục TLTK có tính vào 1000 từ không** — hỏi ban tổ chức; hiện Mục 5 là 860 từ chưa tính danh mục, còn dư 140 từ nên kể cả có tính vẫn an toàn
7. **Kiểm tra chồng chéo với luận án** — bản này giờ khớp với công việc năm nhất của bạn (dựng môi trường + bài toán bounded-K); phần recovery chỉ ở mức PoC, không đụng cam kết năm 3 trong đề cương
