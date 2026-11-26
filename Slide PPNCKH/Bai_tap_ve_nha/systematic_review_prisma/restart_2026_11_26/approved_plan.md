# Kế hoạch đã duyệt — khởi động lại systematic review HK261

Plan ID: HK261-PRISMA-RESTART-20261126-v1
Recorded at: 2026-11-26T18:07:38+07:00
Approval: Người dùng đã yêu cầu lập lại kế hoạch, xác nhận ACM đã có dữ liệu, bỏ WoS do thiếu quyền; sau đó duyệt triển khai đúng từng bước và xác nhận đã chuyển High. Đây là bản lưu kế hoạch được duyệt, không phải phê chuẩn hồi tố kết quả cũ.

## Phạm vi và điều kiện không được thay đổi ngầm

- Bắt đầu từ dữ liệu tìm kiếm IEEE Xplore, Scopus, ACM Digital Library và OpenAlex. OpenAlex là nguồn bổ sung, không phải WoS. WoS không thực hiện, kết quả không biết (null), không báo zero hits.
- Bộ 46 cũ chỉ là lịch sử: không dùng làm candidate pool, seed để ép truy vấn, chỉ tiêu số bài, hàng đợi ưu tiên, nhãn sàng lọc, extraction hoặc appraisal cho quy trình mới. Không bắt buộc đối chiếu kết quả với 46. PDF sẵn có chỉ được tái dùng sau khi record được tìm độc lập trong nguồn mới và identity được xác minh.
- Không ấn định 20/30–35/36/46 included reports. Số lượng được suy ra từ tìm kiếm và các gate. Khoảng 20 bài là yêu cầu bài tập theo PDF, không phải cỡ mẫu để điều chỉnh sàng lọc.
- Đích là SN Computer Science, manuscript LaTeX theo template Springer Nature chính thức; không tạo Word. Phạm vi hiện tại không submit/email.
- Research/extraction/classification/structured synthesis giao đúng Gemini.app Task; Codex sở hữu writing/editing/code/acceptance/Git. Không thay bằng Gemini CLI hoặc model khác.
- Không nhảy bước, không kế thừa kết quả khoa học cũ, không bịa ngày/DOI/số liệu. Mọi thay đổi phạm vi so với kế hoạch này phải trình người dùng trước khi thực hiện.
- Mỗi phase: kiểm Git → công bố TASK/OWNER/OWNED_PATHS/BINARY_ACCEPTANCE/PRE_TASK_GIT_STATUS và CODE_FIRST_DECISION → thực hiện → kiểm từng tiêu chí → audit diff/cleanup → commit riêng → merge/verify/cleanup trước phase tiếp theo. Không tạo framework/hook quản trị mới nếu không có lỗi thật chặn công việc.
- Mỗi Gemini brief có TASK / REQUIRED WORK / REQUIRED OUTPUT / ACCEPTANCE CRITERIA / BOUNDARIES. Kết quả chưa nghiệm thu không được dùng. Sửa lỗi theo đúng criterion; lưu task/context ID, raw result và review.
- Timestamp dùng RFC3339 có timezone. Bản kế hoạch này là baseline; tiến độ và bằng chứng cập nhật trong progress.json, current_state.json và event log, không sửa lịch sử để che sai lệch.

## Phân biệt nguồn yêu cầu

PDF môn `Slide PPNCKH/HK261 - Bài tập lớn-Tiểu luận.pdf`: khoảng 20 bài journal/conference liên quan hướng NCS; đọc để đề xuất ý tưởng; viết thử bài với các phần tối thiểu; tải template tạp chí; quy trình môn cuối cùng gồm submit và bằng chứng; hạn trước ngày thi 3 ngày (chưa có lịch thì không đoán). PDF cho phép expected results khi hình thành ý tưởng; không cho phép giả số PRISMA hoặc gán kết quả chưa thực hiện là thật.

Yêu cầu bổ sung của người dùng: systematic review PRISMA 2020, từ năm 2021, LaTeX/SNCS, Gemini.app, bỏ WoS do quyền truy cập, xây corpus mới độc lập bộ 46, giữ kế hoạch/kiểm toán/Git/timestamp và hiện tại không submit/email. Các gate chi tiết dưới đây là cách vận hành kế hoạch đã duyệt; không tự nhận tất cả là nguyên văn yêu cầu môn hay PRISMA.

## 16 bước theo thứ tự

### Bước 01 — Kiểm kê dữ liệu đầu vào

- TASK_ID: restart-01
- OWNER: CODEX_WRITING
- Đầu vào: Các file tìm kiếm IEEE Xplore, Scopus, ACM và OpenAlex đã có.
- Thực hiện: Đọc file thực; đếm hàng; ghi định dạng, metadata thiếu, query/filter/time locator và SHA256; đối chiếu manifest. Chỉ kiểm kê, chưa chuẩn hóa, khử trùng hay sàng lọc.
- Đầu ra: step01_inventory.json; step01_inventory.md
- BINARY_ACCEPTANCE: 100% file đầu vào được kiểm tra tồn tại/hash/count; tổng hàng tính từ file; mọi khoảng thiếu ghi rõ.
- Phụ thuộc: không có bước trước

### Bước 02 — Chốt protocol cho quy trình mới

- TASK_ID: restart-02
- OWNER: CODEX_WRITING + GEMINI_RESEARCH
- Đầu vào: Yêu cầu môn; skill; protocol/amendment và kiểm kê bước 01.
- Thực hiện: Codex ghi protocol theo phạm vi đã duyệt; Gemini.app kiểm tra sự nhất quán của RQ, UAV–edge/collaborative DNN inference và tiêu chí. Ghi thời gian từ 2021 đến ngày tìm kiếm cuối thật; loại tài liệu/ngôn ngữ; xử lý thiếu abstract/toàn văn; vai trò người và AI. WoS không thực hiện do thiếu quyền.
- Đầu ra: protocol_restart.md; bảng kiểm protocol và brief/result/review
- BINARY_ACCEPTANCE: Mọi RQ có tiêu chí thao tác được; không số lượng included định trước; không kế thừa bộ 46; mọi quyết định ngoài kế hoạch phải xin duyệt.
- Phụ thuộc: bước 01 đã qua gate và commit

### Bước 03 — Rà soát truy vấn đã thực sự chạy

- TASK_ID: restart-03
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Protocol bước 02; exact query/filter/time và bằng chứng nền tảng.
- Thực hiện: Gemini.app đối chiếu cú pháp, trường tìm kiếm, bộ lọc và phạm vi trên từng nguồn; Codex nghiệm thu. Giữ hoặc sửa có lý do và bằng chứng; nếu cần chạy lại thì lưu phiên bản và raw export riêng. Không tối ưu truy vấn để tái tìm bộ 46 cũ.
- Đầu ra: query_audit; phiên bản query và raw export khi cần
- BINARY_ACCEPTANCE: 4/4 nguồn có kết luận và locator; mọi truy vấn tuyên bố đã chạy có bằng chứng thật; sửa/rerun được version hóa; không tự đổi phạm vi.
- Phụ thuộc: bước 02 đã qua gate và commit

### Bước 04 — Khóa phiên bản dữ liệu tìm kiếm

- TASK_ID: restart-04
- OWNER: CODEX_WRITING
- Đầu vào: Các phiên bản nguồn được nghiệm thu ở bước 03.
- Thực hiện: Chọn chính xác file/query/phiên bản; ghi hash/count và nguồn gốc; giữ nguyên raw; không cộng lại export trùng phiên bản. Ghi WoS unavailable/not searched với count null.
- Đầu ra: search_dataset_manifest.json; search_log
- BINARY_ACCEPTANCE: 100% file được chọn có SHA256/query/count/time; không đếm lặp export cùng lần chạy; không đổi WoS thành zero result.
- Phụ thuộc: bước 03 đã qua gate và commit

### Bước 05 — Chuẩn hóa metadata và provenance

- TASK_ID: restart-05
- OWNER: CODEX_WRITING + GEMINI_RESEARCH
- Đầu vào: Dataset đã khóa.
- Thực hiện: Code nhập metadata thống nhất và gắn ID hàng, source/query/file/row; giữ nguyên bản thô. Gemini.app chỉ xác minh/bổ sung factual metadata thiếu với nguồn; chưa biết phải giữ missing marker.
- Đầu ra: records_normalized; metadata_issue_log
- BINARY_ACCEPTANCE: 100% hàng thô được hạch toán; mọi hàng có provenance; không tự bịa DOI/abstract/year; không lọc nội dung ở bước này.
- Phụ thuộc: bước 04 đã qua gate và commit

### Bước 06 — Khử trùng lặp

- TASK_ID: restart-06
- OWNER: CODEX_WRITING + GEMINI_RESEARCH
- Đầu vào: Records chuẩn hóa.
- Thực hiện: Code so DOI/title chuẩn hóa; Gemini.app xử lý cặp mơ hồ; giữ mọi liên kết nguồn và quyết định gộp. Không gộp trường hợp chưa đủ bằng chứng, không xóa raw.
- Đầu ra: dedup_map; unique_record_queue; unresolved_pairs
- BINARY_ACCEPTANCE: Mọi hàng có một đường truy vết; mỗi merge có lý do; duplicate chắc chắn còn sót=0; cặp chưa giải quyết được liệt kê, không ngụy tạo unique count.
- Phụ thuộc: bước 05 đã qua gate và commit

### Bước 07 — Sàng lọc tiêu đề và abstract

- TASK_ID: restart-07
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Toàn bộ records sau dedup; protocol đã chốt.
- Thực hiện: Gemini.app đánh giá từng record: chuyển toàn văn/exclude/unclear với lý do và locator; Codex kiểm mọi tiêu chí nghiệm thu và yêu cầu sửa lỗi. Thiếu abstract không tự động exclude.
- Đầu ra: title_abstract_screening; acceptance_reviews
- BINARY_ACCEPTANCE: 100% record có quyết định hoặc unresolved rõ; mỗi exclude có lý do theo protocol; không dùng nhãn cũ.
- Phụ thuộc: bước 06 đã qua gate và commit

### Bước 08 — Thu thập và xác minh toàn văn

- TASK_ID: restart-08
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Danh sách chuyển toàn văn từ bước 07.
- Thực hiện: Tìm toàn văn hợp lệ; xác minh DOI/title/version và log truy cập. Chỉ tái dùng PDF sẵn có nếu record được tìm độc lập ở quy trình mới và identity khớp. Tách không lấy được toàn văn thành not retrieved.
- Đầu ra: retrieval_log; PDF/text identity index
- BINARY_ACCEPTANCE: 100% record cần toàn văn có retrieved/not retrieved và locator/lý do; không suy diễn toàn văn từ abstract.
- Phụ thuộc: bước 07 đã qua gate và commit

### Bước 09 — Sàng lọc toàn văn mới

- TASK_ID: restart-09
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Toàn văn đã xác minh và protocol.
- Thực hiện: Đánh giá mới từng report; include/exclude/awaiting classification; một lý do chính cho exclude; trích dẫn trang/đoạn hỗ trợ; Codex nghiệm thu. Không kế thừa quyết định 46 cũ.
- Đầu ra: fulltext_screening; exclusions; acceptance_reviews
- BINARY_ACCEPTANCE: 100% report được hạch toán; mỗi quyết định có evidence locator; mọi nghi vấn được giữ rõ; không ép số included.
- Phụ thuộc: bước 08 đã qua gate và commit

### Bước 10 — Liên kết report với study

- TASK_ID: restart-10
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Reports đã sàng lọc; thông tin phiên bản/nghiên cứu.
- Thực hiện: Kiểm tra các phiên bản và study family có tín hiệu; chỉ gộp khi có bằng chứng hai phía; giữ report ID và study ID riêng.
- Đầu ra: report_study_map; unresolved_families
- BINARY_ACCEPTANCE: 100% reports có mapping/status; merge thiếu bằng chứng=0; không gọi reports là unique studies khi chưa xác minh.
- Phụ thuộc: bước 09 đã qua gate và commit

### Bước 11 — Trích xuất dữ liệu mới

- TASK_ID: restart-11
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Toàn văn included của quy trình mới.
- Thực hiện: Trích xuất kiến trúc, số UAV, workload/DNN, phân hoạch/phân công, mạng, baseline, latency/energy/communication, điều kiện đánh giá và giới hạn; mỗi claim có locator/units/conditions. Không nhập extraction cũ.
- Đầu ra: extraction_table; quantitative_claim_source_matrix
- BINARY_ACCEPTANCE: 100% included reports có trường dữ liệu hoặc not reported; unsupported quantitative claims=0; không biến thiếu trích xuất thành not reported.
- Phụ thuộc: bước 10 đã qua gate và commit

### Bước 12 — Đánh giá chất lượng và nguy cơ sai lệch

- TASK_ID: restart-12
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Included full texts và extraction mới.
- Thực hiện: Dùng domain phù hợp nghiên cứu mô phỏng/hệ thống; ghi rationale/locator và trạng thái chưa đánh giá; phân biệt không báo cáo với bằng chứng âm; không loại bằng điểm tổng tùy tiện.
- Đầu ra: appraisal_table; rationale_source_matrix
- BINARY_ACCEPTANCE: 100% included reports có appraisal/status; mỗi judgment có rationale/locator; không giả vờ hai reviewer độc lập hoặc đánh giá đã hoàn tất.
- Phụ thuộc: bước 11 đã qua gate và commit

### Bước 13 — Hòa giải PRISMA

- TASK_ID: restart-13
- OWNER: CODEX_WRITING + GEMINI_RESEARCH
- Đầu vào: Search/dedup/screening/retrieval/report-study/extraction logs.
- Thực hiện: Đối chiếu đơn vị records/reports/studies; số loại trước và sau toàn văn; not retrieved/awaiting; dựng flow và checklist 27 mục; ghi limitation/deviation.
- Đầu ra: prisma_counts; flow; checklist
- BINARY_ACCEPTANCE: Unexplained arithmetic difference=0; từng số truy được ID; đủ 27 items có trạng thái/locator/limitation; số không lấy từ bộ 46 cũ.
- Phụ thuộc: bước 12 đã qua gate và commit

### Bước 14 — Tổng hợp theo câu hỏi nghiên cứu

- TASK_ID: restart-14
- OWNER: GEMINI_RESEARCH + CODEX_WRITING
- Đầu vào: Extraction/appraisal đã accepted và PRISMA đã reconcile.
- Thực hiện: Gemini.app trả structured synthesis theo RQ; Codex viết. Gắn claim với nguồn, tử số/mẫu số; tách điều kiện không so sánh được; không suy từ không tìm thấy sang không tồn tại.
- Đầu ra: RQ synthesis; claim-source matrix; publication tables
- BINARY_ACCEPTANCE: 100% claim có nguồn; số đếm có mẫu số; unsupported claims=0; không gộp kết quả khác điều kiện để tạo ưu thế giả.
- Phụ thuộc: bước 13 đã qua gate và commit

### Bước 15 — Viết manuscript LaTeX SN Computer Science

- TASK_ID: restart-15
- OWNER: CODEX_WRITING
- Đầu vào: Bằng chứng đã accepted; template Springer Nature chính thức; kết quả bước 13–14.
- Thực hiện: Viết Methods → Results → Discussion → Introduction rồi Title/Abstract/Conclusion; đồng bộ bảng/hình/references/supplements; công khai giới hạn và vai trò AI/người. Chỉ dùng số từ quy trình mới; không đoán metadata tác giả.
- Đầu ra: main.tex; references.bib; figures/tables/supplements; compiled PDF
- BINARY_ACCEPTANCE: Chỉ dùng evidence accepted; đúng template mục tiêu; citation/claim/count nhất quán; tác giả/declarations chưa xác nhận được ghi là chưa xác nhận, không bịa.
- Phụ thuộc: bước 14 đã qua gate và commit

### Bước 16 — Kiểm định và bàn giao

- TASK_ID: restart-16
- OWNER: CODEX_WRITING + GEMINI_RESEARCH
- Đầu vào: Bản LaTeX/PDF và toàn bộ audit artifacts.
- Thực hiện: Gemini.app xác minh nguồn/DOI/correction/retraction theo brief; Codex kiểm số liệu, citations, PRISMA, build và nhìn mọi trang PDF; sửa rồi kiểm lại; bàn giao LaTeX/PDF/data/audit. Không submit hoặc email.
- Đầu ra: final_integrity_audit; PDF/LaTeX/data bundle; limitations report
- BINARY_ACCEPTANCE: Build PASS; unresolved citations=0; fabricated values=0; mọi trang PDF được kiểm; mọi gate có PASS/FAIL; limitations rõ; commit/merge/cleanup đúng phạm vi.
- Phụ thuộc: bước 15 đã qua gate và commit

## Theo dõi và xử lý sai lệch

Mỗi bước có status, started_at, updated_at, completed_at khi kết thúc, artifacts và acceptance evidence. Bước chưa bắt đầu dùng null cho started_at/completed_at, không ghi thời gian giả. Thiếu dữ liệu thì lưu unresolved/blocker tại bước tương ứng; không nhảy sang viết báo để lấp thiếu bằng suy đoán. Bất kỳ đổi nguồn/phạm vi/tiêu chí ngoài kế hoạch phải có bản đề xuất và người dùng phê duyệt trước.
