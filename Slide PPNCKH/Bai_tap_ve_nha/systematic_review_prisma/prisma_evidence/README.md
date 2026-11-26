# Minh chứng PRISMA HK261

Mở mục của từng bước để xem bằng chứng gốc, biên bản nghiệm thu và tệp đầu ra đã đăng ký.
Các liên kết trỏ tới bản gốc trong dự án. PDF có giới hạn truy cập được truy vết từ sổ thu thập và chỉ mục nhận dạng ở bước 08.
Kết quả thô hoặc biên bản FAIL được lưu để truy vết. Chỉ biên bản nghiệm thu mới xác nhận bằng chứng được sử dụng.

Sổ tiến độ cập nhật lúc `2026-11-27T01:09:07+07:00`.

- [Kế hoạch 16 bước đã duyệt](../restart_2026_11_26/approved_plan.md)
- [Sổ tiến độ và các tiêu chí nghiệm thu](../restart_2026_11_26/progress.json)
- [Trạng thái dự án](../MUST_READ_AI_AGENT/current_state.json)
- [Nhật ký sự kiện theo thời gian](../MUST_READ_AI_AGENT/events.jsonl)
- [Cách kiểm tra và cập nhật thư mục](MAINTENANCE.md)

- [Bước 01](#buoc-01) · Kiểm kê dữ liệu đầu vào
- [Bước 02](#buoc-02) · Chốt protocol cho quy trình mới
- [Bước 03](#buoc-03) · Rà soát truy vấn đã thực sự chạy
- [Bước 04](#buoc-04) · Khóa phiên bản dữ liệu tìm kiếm
- [Bước 05](#buoc-05) · Chuẩn hóa metadata và provenance
- [Bước 06](#buoc-06) · Khử trùng lặp
- [Bước 07](#buoc-07) · Sàng lọc tiêu đề và abstract
- [Bước 08](#buoc-08) · Thu thập và xác minh toàn văn
- [Bước 09](#buoc-09) · Sàng lọc toàn văn mới
- [Bước 10](#buoc-10) · Liên kết report với study
- [Bước 11](#buoc-11) · Trích xuất dữ liệu mới
- [Bước 12](#buoc-12) · Đánh giá chất lượng và nguy cơ sai lệch
- [Bước 13](#buoc-13) · Hòa giải PRISMA
- [Bước 14](#buoc-14) · Tổng hợp theo câu hỏi nghiên cứu
- [Bước 15](#buoc-15) · Viết manuscript LaTeX SN Computer Science
- [Bước 16](#buoc-16) · Kiểm định và bàn giao

<a id="buoc-01"></a>
## Bước 01 · Kiểm kê dữ liệu đầu vào

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:09:24+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=5.

- [approved_plan.md](../restart_2026_11_26/approved_plan.md)
- [step01_inventory.json](../restart_2026_11_26/step01_inventory.json)
- [step01_inventory.md](../restart_2026_11_26/step01_inventory.md)
- [ieee_xplore_high_recall_export_2026-11-26.csv](../sources/raw/core_searches/ieee_xplore_high_recall_export_2026-11-26.csv)
- [ieee_xplore_complementary_export_2026-11-26.csv](../sources/raw/core_searches/ieee_xplore_complementary_export_2026-11-26.csv)
- [scopus_high_recall_export_2026-11-26.csv](../sources/raw/core_searches/scopus_high_recall_export_2026-11-26.csv)
- [scopus_complementary_export_2026-11-26.csv](../sources/raw/core_searches/scopus_complementary_export_2026-11-26.csv)
- [openalex_high_recall_2026-11-26_normalized.csv](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_normalized.csv)
- [openalex_complementary_2026-11-26_normalized.csv](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_complementary_2026-11-26_normalized.csv)
- [acm_all_records.csv](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_all_records.csv)
- [acm_basic_edition_recheck_2026-11-26.json](../sources/raw/core_searches/acm_basic_edition_recheck_2026-11-26.json)
- [acm_complementary_2026-11-26.json](../sources/raw/core_searches/acm_complementary_2026-11-26.json)
- [acm_high_recall_2026-11-26.json](../sources/raw/core_searches/acm_high_recall_2026-11-26.json)
- [ieee_xplore_complementary_2026-11-26.json](../sources/raw/core_searches/ieee_xplore_complementary_2026-11-26.json)
- [ieee_xplore_complementary_authenticated_2026-11-26.json](../sources/raw/core_searches/ieee_xplore_complementary_authenticated_2026-11-26.json)
- [ieee_xplore_high_recall_2026-11-26.json](../sources/raw/core_searches/ieee_xplore_high_recall_2026-11-26.json)
- [ieee_xplore_high_recall_authenticated_2026-11-26.json](../sources/raw/core_searches/ieee_xplore_high_recall_authenticated_2026-11-26.json)
- [scopus_access_attempt_2026-11-26.json](../sources/raw/core_searches/scopus_access_attempt_2026-11-26.json)
- [scopus_complementary_authenticated_2026-11-26.json](../sources/raw/core_searches/scopus_complementary_authenticated_2026-11-26.json)
- [scopus_high_recall_authenticated_2026-11-26.json](../sources/raw/core_searches/scopus_high_recall_authenticated_2026-11-26.json)
- [web_of_science_access_attempt_2026-11-26.json](../sources/raw/core_searches/web_of_science_access_attempt_2026-11-26.json)
- [web_of_science_free_view_recheck_2026-11-26.json](../sources/raw/core_searches/web_of_science_free_view_recheck_2026-11-26.json)
- [openalex_complementary_2026-11-26_checksums.sha256](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_complementary_2026-11-26_checksums.sha256)
- [openalex_complementary_2026-11-26_manifest.json](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_complementary_2026-11-26_manifest.json)
- [openalex_complementary_2026-11-26_raw.json](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_complementary_2026-11-26_raw.json)
- [openalex_high_recall_2026-11-26_checksums.sha256](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_checksums.sha256)
- [openalex_high_recall_2026-11-26_manifest.json](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_manifest.json)
- [openalex_high_recall_2026-11-26_raw.json](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_raw.json)
- [openalex_run_summary_2026-11-26.json](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_run_summary_2026-11-26.json)
- [browser_comp_startPage_10.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_10.json)
- [browser_comp_startPage_11.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_11.json)
- [browser_comp_startPage_12.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_12.json)
- [browser_comp_startPage_13.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_13.json)
- [browser_comp_startPage_14.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_14.json)
- [browser_comp_startPage_15.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_15.json)
- [browser_comp_startPage_16.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_16.json)
- [browser_comp_startPage_7.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_7.json)
- [browser_comp_startPage_8.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_8.json)
- [browser_comp_startPage_9.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_comp_startPage_9.json)
- [browser_high_startPage_0.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_high_startPage_0.json)
- [browser_high_startPage_1.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_high_startPage_1.json)
- [browser_high_startPage_2.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_high_startPage_2.json)
- [browser_high_startPage_3.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/browser_high_startPage_3.json)
- [complementary_page_01.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_01.json)
- [complementary_page_02.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_02.json)
- [complementary_page_03.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_03.json)
- [complementary_page_04.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_04.json)
- [complementary_page_05.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_05.json)
- [complementary_page_06.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_06.json)
- [complementary_page_07.json](../sources/raw/core_searches/acm_manual_capture_2026-11-26/complementary_page_07.json)
- [acm_complementary_records.json](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_complementary_records.json)
- [acm_high_recall_records.json](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_high_recall_records.json)
- [acm_capture_qa.json](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_capture_qa.json)
- [acm_capture_manifest.json](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_capture_manifest.json)

<a id="buoc-02"></a>
## Bước 02 · Chốt protocol cho quy trình mới

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:26:39+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=15.

- [protocol_restart.md](../restart_2026_11_26/protocol_restart.md)
- [step02_protocol_acceptance.md](../restart_2026_11_26/step02_protocol_acceptance.md)
- [step02_user_decision.md](../restart_2026_11_26/step02_user_decision.md)
- [step02_app_correction_raw.json](../restart_2026_11_26/step02_app_correction_raw.json)

<a id="buoc-03"></a>
## Bước 03 · Rà soát truy vấn đã thực sự chạy

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:41:53+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=6.

- [step03_query_audit_brief.md](../restart_2026_11_26/step03_query_audit_brief.md)
- [step03_query_audit_primary_raw.json](../restart_2026_11_26/step03_query_audit_primary_raw.json)
- [step03_query_audit_primary_review.md](../restart_2026_11_26/step03_query_audit_primary_review.md)
- [step03_query_audit_correction_brief.md](../restart_2026_11_26/step03_query_audit_correction_brief.md)
- [step03_query_audit_correction_01_raw.json](../restart_2026_11_26/step03_query_audit_correction_01_raw.json)
- [step03_query_audit_correction_01_review.md](../restart_2026_11_26/step03_query_audit_correction_01_review.md)
- [step03_query_audit_delimited_brief.md](../restart_2026_11_26/step03_query_audit_delimited_brief.md)
- [step03_query_audit_acceptance.md](../restart_2026_11_26/step03_query_audit_acceptance.md)
- [step03_query_audit_delimited_raw.json](../restart_2026_11_26/step03_query_audit_delimited_raw.json)
- [openalex_query_set_1.4_revised.json](../automation/search_configs/openalex_query_set_1.4_revised.json)
- [openalex_complementary_2026-11-26_manifest.json](../sources/raw/core_searches/openalex_complementary_revision_2026-11-26/openalex_complementary_2026-11-26_manifest.json)
- [openalex_run_summary_2026-11-26.json](../sources/raw/core_searches/openalex_complementary_revision_2026-11-26/openalex_run_summary_2026-11-26.json)

<a id="buoc-04"></a>
## Bước 04 · Khóa phiên bản dữ liệu tìm kiếm

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:42:41+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=4.

- [search_dataset_manifest.json](../restart_2026_11_26/search_dataset_manifest.json)
- [search_log.md](../restart_2026_11_26/search_log.md)
- [ieee_xplore_high_recall_export_2026-11-26.csv](../sources/raw/core_searches/ieee_xplore_high_recall_export_2026-11-26.csv)
- [ieee_xplore_complementary_export_2026-11-26.csv](../sources/raw/core_searches/ieee_xplore_complementary_export_2026-11-26.csv)
- [scopus_high_recall_export_2026-11-26.csv](../sources/raw/core_searches/scopus_high_recall_export_2026-11-26.csv)
- [scopus_complementary_export_2026-11-26.csv](../sources/raw/core_searches/scopus_complementary_export_2026-11-26.csv)
- [openalex_high_recall_2026-11-26_normalized.csv](../sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_normalized.csv)
- [openalex_complementary_2026-11-26_normalized.csv](../sources/raw/core_searches/openalex_complementary_revision_2026-11-26/openalex_complementary_2026-11-26_normalized.csv)
- [acm_all_records.csv](../sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_all_records.csv)

<a id="buoc-05"></a>
## Bước 05 · Chuẩn hóa metadata và provenance

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:47:38+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=5.

- [records_normalized.csv](../restart_2026_11_26/records_normalized.csv)
- [metadata_issue_log.json](../restart_2026_11_26/metadata_issue_log.json)
- [step05_metadata_brief.md](../restart_2026_11_26/step05_metadata_brief.md)
- [step05_metadata_raw.json](../restart_2026_11_26/step05_metadata_raw.json)
- [step05_metadata_review.md](../restart_2026_11_26/step05_metadata_review.md)

<a id="buoc-06"></a>
## Bước 06 · Khử trùng lặp

**Đã chốt theo sổ tiến độ** · `2026-11-26T18:49:12+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=4.

- [dedup_map.csv](../restart_2026_11_26/dedup_map.csv)
- [unique_record_queue.csv](../restart_2026_11_26/unique_record_queue.csv)
- [dedup_issues.json](../restart_2026_11_26/dedup_issues.json)
- [step06_dedup_review.md](../restart_2026_11_26/step06_dedup_review.md)

<a id="buoc-07"></a>
## Bước 07 · Sàng lọc tiêu đề và abstract

**Đã chốt theo sổ tiến độ** · `2026-11-26T19:28:28+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=12.

- [step07_batch01_brief.md](../restart_2026_11_26/step07_batch01_brief.md)
- [step07_batch01_primary_raw.json](../restart_2026_11_26/step07_batch01_primary_raw.json)
- [step07_batch01_primary_review.md](../restart_2026_11_26/step07_batch01_primary_review.md)
- [step07_batch01_correction_brief.md](../restart_2026_11_26/step07_batch01_correction_brief.md)
- [step07_batch01_correction_raw.json](../restart_2026_11_26/step07_batch01_correction_raw.json)
- [step07_batch01_accepted.csv](../restart_2026_11_26/step07_batch01_accepted.csv)
- [step07_batch01_acceptance.md](../restart_2026_11_26/step07_batch01_acceptance.md)
- [step07_batch02_brief.md](../restart_2026_11_26/step07_batch02_brief.md)
- [step07_batch02_raw.json](../restart_2026_11_26/step07_batch02_raw.json)
- [step07_batch02_accepted.csv](../restart_2026_11_26/step07_batch02_accepted.csv)
- [step07_batch02_acceptance.md](../restart_2026_11_26/step07_batch02_acceptance.md)
- [step07_batch03_brief.md](../restart_2026_11_26/step07_batch03_brief.md)
- [step07_batch03_primary_raw.json](../restart_2026_11_26/step07_batch03_primary_raw.json)
- [step07_batch03_primary_review.md](../restart_2026_11_26/step07_batch03_primary_review.md)
- [step07_batch03_fix_brief.md](../restart_2026_11_26/step07_batch03_fix_brief.md)
- [step07_batch03_raw.json](../restart_2026_11_26/step07_batch03_raw.json)
- [step07_batch03_accepted.csv](../restart_2026_11_26/step07_batch03_accepted.csv)
- [step07_batch03_acceptance.md](../restart_2026_11_26/step07_batch03_acceptance.md)
- [step07_batch04_brief.md](../restart_2026_11_26/step07_batch04_brief.md)
- [step07_batch04_read_shortfall_review.md](../restart_2026_11_26/step07_batch04_read_shortfall_review.md)
- [step07_batch04_read_shortfall_raw.json](../restart_2026_11_26/step07_batch04_read_shortfall_raw.json)
- [manifest.json](../restart_2026_11_26/screening_evidence/manifest.json)
- [step07_batch04_retry_brief.md](../restart_2026_11_26/step07_batch04_retry_brief.md)
- [step07_batch04_raw.json](../restart_2026_11_26/step07_batch04_raw.json)
- [step07_batch04_accepted.csv](../restart_2026_11_26/step07_batch04_accepted.csv)
- [step07_batch04_acceptance.md](../restart_2026_11_26/step07_batch04_acceptance.md)
- [step07_batch05_brief.md](../restart_2026_11_26/step07_batch05_brief.md)
- [step07_batch05_primary_raw.json](../restart_2026_11_26/step07_batch05_primary_raw.json)
- [step07_batch05_primary_review.md](../restart_2026_11_26/step07_batch05_primary_review.md)
- [step07_batch05_fix_brief.md](../restart_2026_11_26/step07_batch05_fix_brief.md)
- [step07_batch05_raw.json](../restart_2026_11_26/step07_batch05_raw.json)
- [step07_batch05_accepted.csv](../restart_2026_11_26/step07_batch05_accepted.csv)
- [step07_batch05_acceptance.md](../restart_2026_11_26/step07_batch05_acceptance.md)
- [step07_batch06_brief.md](../restart_2026_11_26/step07_batch06_brief.md)
- [step07_batch06_transport_failure.json](../restart_2026_11_26/step07_batch06_transport_failure.json)
- [step07_batch06_transport_review.md](../restart_2026_11_26/step07_batch06_transport_review.md)
- [step07_batch06_raw.json](../restart_2026_11_26/step07_batch06_raw.json)
- [step07_batch06_accepted.csv](../restart_2026_11_26/step07_batch06_accepted.csv)
- [step07_batch06_acceptance.md](../restart_2026_11_26/step07_batch06_acceptance.md)
- [step07_batch07_brief.md](../restart_2026_11_26/step07_batch07_brief.md)
- [step07_batch07_transport_failure.json](../restart_2026_11_26/step07_batch07_transport_failure.json)
- [step07_batch07_transport_review.md](../restart_2026_11_26/step07_batch07_transport_review.md)
- [step07_batch07_raw.json](../restart_2026_11_26/step07_batch07_raw.json)
- [step07_batch07_accepted.csv](../restart_2026_11_26/step07_batch07_accepted.csv)
- [step07_batch07_acceptance.md](../restart_2026_11_26/step07_batch07_acceptance.md)
- [title_abstract_screening.csv](../restart_2026_11_26/title_abstract_screening.csv)
- [step07_screening_summary.md](../restart_2026_11_26/step07_screening_summary.md)

<a id="buoc-08"></a>
## Bước 08 · Thu thập và xác minh toàn văn

**Đã chốt theo sổ tiến độ** · `2026-11-26T20:13:09+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=3.

- [input_manifest.json](../restart_2026_11_26/fulltext_retrieval/input_manifest.json)
- [batch_01.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_01.md)
- [batch_01.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_01.raw.json)
- [batch_01.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_01.lead_audit.json)
- [batch_01.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_01.leads.jsonl)
- [batch_01.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_01.csv)
- [batch_01.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_01.review.md)
- [batch_02.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_02.md)
- [batch_02.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_02.raw.json)
- [batch_02.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_02.lead_audit.json)
- [batch_02.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_02.leads.jsonl)
- [batch_02.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_02.csv)
- [batch_02.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_02.review.md)
- [batch_03.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_03.md)
- [batch_03.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_03.raw.json)
- [batch_03.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_03.lead_audit.json)
- [batch_03.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_03.leads.jsonl)
- [batch_03.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_03.csv)
- [batch_03.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_03.review.md)
- [batch_04.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_04.md)
- [batch_04.primary.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.primary.raw.json)
- [batch_04.primary.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.primary.lead_audit.json)
- [batch_04.primary_review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.primary_review.md)
- [batch_04_correction.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_04_correction.md)
- [batch_04.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.raw.json)
- [batch_04.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.lead_audit.json)
- [batch_04.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.leads.jsonl)
- [batch_04.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.csv)
- [batch_04.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_04.review.md)
- [batch_05.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_05.md)
- [batch_05.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_05.raw.json)
- [batch_05.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_05.lead_audit.json)
- [batch_05.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_05.leads.jsonl)
- [batch_05.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_05.csv)
- [batch_05.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_05.review.md)
- [batch_06.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_06.md)
- [batch_06.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_06.raw.json)
- [batch_06.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_06.lead_audit.json)
- [batch_06.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_06.leads.jsonl)
- [batch_06.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_06.csv)
- [batch_06.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_06.review.md)
- [batch_07.md](../restart_2026_11_26/fulltext_retrieval/briefs/batch_07.md)
- [batch_07.raw.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_07.raw.json)
- [batch_07.lead_audit.json](../restart_2026_11_26/fulltext_retrieval/batches/batch_07.lead_audit.json)
- [batch_07.leads.jsonl](../restart_2026_11_26/fulltext_retrieval/batches/batch_07.leads.jsonl)
- [batch_07.csv](../restart_2026_11_26/fulltext_retrieval/batches/batch_07.csv)
- [batch_07.review.md](../restart_2026_11_26/fulltext_retrieval/batches/batch_07.review.md)
- [retrieval_log.csv](../restart_2026_11_26/fulltext_retrieval/retrieval_log.csv)
- [fulltext_identity_index.csv](../restart_2026_11_26/fulltext_retrieval/fulltext_identity_index.csv)
- [missing_pdf.csv](../restart_2026_11_26/fulltext_retrieval/missing_pdf.csv)
- [step08_retrieval_summary.md](../restart_2026_11_26/fulltext_retrieval/step08_retrieval_summary.md)

<a id="buoc-09"></a>
## Bước 09 · Sàng lọc toàn văn mới

**Đã chốt theo sổ tiến độ** · `2026-11-26T21:24:09+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=4.

- [manifest.json](../restart_2026_11_26/fulltext_screening/manifest.json)
- [fulltext_identity_index.csv](../restart_2026_11_26/fulltext_retrieval/fulltext_identity_index.csv)
- [batch_01_brief.md](../restart_2026_11_26/fulltext_screening/batch_01_brief.md)
- [batch_02_brief.md](../restart_2026_11_26/fulltext_screening/batch_02_brief.md)
- [batch_03_brief.md](../restart_2026_11_26/fulltext_screening/batch_03_brief.md)
- [batch_04_brief.md](../restart_2026_11_26/fulltext_screening/batch_04_brief.md)
- [batch_01_raw.json](../restart_2026_11_26/fulltext_screening/batch_01_raw.json)
- [batch_01_primary_review.md](../restart_2026_11_26/fulltext_screening/batch_01_primary_review.md)
- [batch_01_correction01_brief.md](../restart_2026_11_26/fulltext_screening/batch_01_correction01_brief.md)
- [batch_01_correction01_raw.json](../restart_2026_11_26/fulltext_screening/batch_01_correction01_raw.json)
- [batch_01_correction01_review.md](../restart_2026_11_26/fulltext_screening/batch_01_correction01_review.md)
- [batch_01_correction02_brief.md](../restart_2026_11_26/fulltext_screening/batch_01_correction02_brief.md)
- [batch_01_correction02_raw.json](../restart_2026_11_26/fulltext_screening/batch_01_correction02_raw.json)
- [batch_01_accepted.csv](../restart_2026_11_26/fulltext_screening/batch_01_accepted.csv)
- [batch_01_review.md](../restart_2026_11_26/fulltext_screening/batch_01_review.md)
- [batch_02_transport01_raw.json](../restart_2026_11_26/fulltext_screening/batch_02_transport01_raw.json)
- [batch_02_transport01_review.md](../restart_2026_11_26/fulltext_screening/batch_02_transport01_review.md)
- [batch_02_retry01_brief.md](../restart_2026_11_26/fulltext_screening/batch_02_retry01_brief.md)
- [batch_02_retry01_raw.json](../restart_2026_11_26/fulltext_screening/batch_02_retry01_raw.json)
- [batch_02_retry01_review.md](../restart_2026_11_26/fulltext_screening/batch_02_retry01_review.md)
- [batch_02_correction01_brief.md](../restart_2026_11_26/fulltext_screening/batch_02_correction01_brief.md)
- [batch_02_retry01_transport_raw.json](../restart_2026_11_26/fulltext_screening/batch_02_retry01_transport_raw.json)
- [batch_02_correction01_raw.json](../restart_2026_11_26/fulltext_screening/batch_02_correction01_raw.json)
- [batch_02_accepted.csv](../restart_2026_11_26/fulltext_screening/batch_02_accepted.csv)
- [batch_02_review.md](../restart_2026_11_26/fulltext_screening/batch_02_review.md)
- [batch_03_review.md](../restart_2026_11_26/fulltext_screening/batch_03_review.md)
- [batch_03_correction01_brief.md](../restart_2026_11_26/fulltext_screening/batch_03_correction01_brief.md)
- [batch_03_raw.json](../restart_2026_11_26/fulltext_screening/batch_03_raw.json)
- [batch_03_transport_raw.json](../restart_2026_11_26/fulltext_screening/batch_03_transport_raw.json)
- [batch_03_accepted.csv](../restart_2026_11_26/fulltext_screening/batch_03_accepted.csv)
- [batch_03_correction01_raw.json](../restart_2026_11_26/fulltext_screening/batch_03_correction01_raw.json)
- [batch_03_primary_review.md](../restart_2026_11_26/fulltext_screening/batch_03_primary_review.md)
- [batch_04_review.md](../restart_2026_11_26/fulltext_screening/batch_04_review.md)
- [batch_04_correction01_brief.md](../restart_2026_11_26/fulltext_screening/batch_04_correction01_brief.md)
- [batch_04_raw.json](../restart_2026_11_26/fulltext_screening/batch_04_raw.json)
- [batch_04_transport_raw.json](../restart_2026_11_26/fulltext_screening/batch_04_transport_raw.json)
- [batch_04_correction01_review.md](../restart_2026_11_26/fulltext_screening/batch_04_correction01_review.md)
- [batch_04_correction02_brief.md](../restart_2026_11_26/fulltext_screening/batch_04_correction02_brief.md)
- [batch_04_correction01_raw.json](../restart_2026_11_26/fulltext_screening/batch_04_correction01_raw.json)
- [batch_04_accepted.csv](../restart_2026_11_26/fulltext_screening/batch_04_accepted.csv)
- [batch_04_correction02_raw.json](../restart_2026_11_26/fulltext_screening/batch_04_correction02_raw.json)
- [batch_04_primary_review.md](../restart_2026_11_26/fulltext_screening/batch_04_primary_review.md)
- [fulltext_screening.csv](../restart_2026_11_26/fulltext_screening/fulltext_screening.csv)
- [exclusions.csv](../restart_2026_11_26/fulltext_screening/exclusions.csv)
- [awaiting_classification.csv](../restart_2026_11_26/fulltext_screening/awaiting_classification.csv)
- [step09_screening_summary.md](../restart_2026_11_26/fulltext_screening/step09_screening_summary.md)

<a id="buoc-10"></a>
## Bước 10 · Liên kết report với study

**Đã chốt theo sổ tiến độ** · `2026-11-26T21:41:35+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: PASS=5.

- [manifest.json](../restart_2026_11_26/study_linkage/manifest.json)
- [batch_01_brief.md](../restart_2026_11_26/study_linkage/batch_01_brief.md)
- [batch_01_review.md](../restart_2026_11_26/study_linkage/batch_01_review.md)
- [batch_01_raw.json](../restart_2026_11_26/study_linkage/batch_01_raw.json)
- [batch_01_transport_raw.json](../restart_2026_11_26/study_linkage/batch_01_transport_raw.json)
- [batch_01_correction01_brief.md](../restart_2026_11_26/study_linkage/batch_01_correction01_brief.md)
- [batch_01_correction01_review.md](../restart_2026_11_26/study_linkage/batch_01_correction01_review.md)
- [batch_01_correction01_raw.json](../restart_2026_11_26/study_linkage/batch_01_correction01_raw.json)
- [report_study_map.csv](../restart_2026_11_26/study_linkage/report_study_map.csv)
- [pair_evidence.csv](../restart_2026_11_26/study_linkage/pair_evidence.csv)
- [unresolved_families.csv](../restart_2026_11_26/study_linkage/unresolved_families.csv)
- [step10_linkage_summary.md](../restart_2026_11_26/study_linkage/step10_linkage_summary.md)

<a id="buoc-11"></a>
## Bước 11 · Trích xuất dữ liệu mới

**Đã chốt theo sổ tiến độ** · `2026-11-27T00:33:28+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: FAIL=19, PASS=5.

- [manifest.json](../restart_2026_11_26/extraction/manifest.json)
- [batch_01_brief.md](../restart_2026_11_26/extraction/batch_01_brief.md)
- [batch_02_brief.md](../restart_2026_11_26/extraction/batch_02_brief.md)
- [batch_01_raw.json](../restart_2026_11_26/extraction/batch_01_raw.json)
- [batch_01_mechanical.json](../restart_2026_11_26/extraction/batch_01_mechanical.json)
- [batch_01_review.md](../restart_2026_11_26/extraction/batch_01_review.md)
- [batch_02_transport.json](../restart_2026_11_26/extraction/batch_02_transport.json)
- [batch_02_raw.json](../restart_2026_11_26/extraction/batch_02_raw.json)
- [batch_02_mechanical.json](../restart_2026_11_26/extraction/batch_02_mechanical.json)
- [batch_02_review.md](../restart_2026_11_26/extraction/batch_02_review.md)
- [batch_02_correction01_brief.md](../restart_2026_11_26/extraction/batch_02_correction01_brief.md)
- [batch_02_correction01_raw.json](../restart_2026_11_26/extraction/batch_02_correction01_raw.json)
- [batch_02_correction01_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction01_mechanical.json)
- [batch_02_correction01_review.md](../restart_2026_11_26/extraction/batch_02_correction01_review.md)
- [batch_02_correction02_brief.md](../restart_2026_11_26/extraction/batch_02_correction02_brief.md)
- [batch_02_correction02_raw.json](../restart_2026_11_26/extraction/batch_02_correction02_raw.json)
- [batch_02_correction02_transport.json](../restart_2026_11_26/extraction/batch_02_correction02_transport.json)
- [batch_02_correction02_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction02_mechanical.json)
- [batch_02_correction02_review.md](../restart_2026_11_26/extraction/batch_02_correction02_review.md)
- [batch_02_correction03_brief.md](../restart_2026_11_26/extraction/batch_02_correction03_brief.md)
- [batch_02_correction03_raw.json](../restart_2026_11_26/extraction/batch_02_correction03_raw.json)
- [batch_02_correction03_transport.json](../restart_2026_11_26/extraction/batch_02_correction03_transport.json)
- [batch_02_correction03_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction03_mechanical.json)
- [batch_02_correction03_review.md](../restart_2026_11_26/extraction/batch_02_correction03_review.md)
- [step11_chat_cleanup.jsonl](../restart_2026_11_26/extraction/step11_chat_cleanup.jsonl)
- [batch_02_correction04_brief.md](../restart_2026_11_26/extraction/batch_02_correction04_brief.md)
- [batch_02_correction04_raw.json](../restart_2026_11_26/extraction/batch_02_correction04_raw.json)
- [batch_02_correction04_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction04_mechanical.json)
- [batch_02_correction04_review.md](../restart_2026_11_26/extraction/batch_02_correction04_review.md)
- [batch_02_correction05_brief.md](../restart_2026_11_26/extraction/batch_02_correction05_brief.md)
- [batch_02_correction05_raw.json](../restart_2026_11_26/extraction/batch_02_correction05_raw.json)
- [batch_02_correction05_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction05_mechanical.json)
- [batch_02_correction05_review.md](../restart_2026_11_26/extraction/batch_02_correction05_review.md)
- [batch_01_preflight_brief.md](../restart_2026_11_26/extraction/batch_01_preflight_brief.md)
- [batch_01_preflight_review.md](../restart_2026_11_26/extraction/batch_01_preflight_review.md)
- [batch_01_preflight_raw.json](../restart_2026_11_26/extraction/batch_01_preflight_raw.json)
- [batch_01_preflight_mechanical.json](../restart_2026_11_26/extraction/batch_01_preflight_mechanical.json)
- [batch_01_extraction_new_brief.md](../restart_2026_11_26/extraction/batch_01_extraction_new_brief.md)
- [batch_01_extraction_new_review.md](../restart_2026_11_26/extraction/batch_01_extraction_new_review.md)
- [batch_01_extraction_new_raw.json](../restart_2026_11_26/extraction/batch_01_extraction_new_raw.json)
- [batch_01_extraction_new_transport.json](../restart_2026_11_26/extraction/batch_01_extraction_new_transport.json)
- [batch_01_extraction_new_mechanical.json](../restart_2026_11_26/extraction/batch_01_extraction_new_mechanical.json)
- [batch_02_correction06_brief.md](../restart_2026_11_26/extraction/batch_02_correction06_brief.md)
- [batch_02_correction06_review.md](../restart_2026_11_26/extraction/batch_02_correction06_review.md)
- [batch_02_correction06_raw.json](../restart_2026_11_26/extraction/batch_02_correction06_raw.json)
- [batch_02_correction06_mechanical.json](../restart_2026_11_26/extraction/batch_02_correction06_mechanical.json)
- [batch_01_targeted_correction_brief.md](../restart_2026_11_26/extraction/batch_01_targeted_correction_brief.md)
- [batch_01_targeted_correction_review.md](../restart_2026_11_26/extraction/batch_01_targeted_correction_review.md)
- [batch_01_targeted_correction_raw.json](../restart_2026_11_26/extraction/batch_01_targeted_correction_raw.json)
- [batch_01_targeted_correction_mechanical.json](../restart_2026_11_26/extraction/batch_01_targeted_correction_mechanical.json)
- [batch_02_three_field_correction_brief.md](../restart_2026_11_26/extraction/batch_02_three_field_correction_brief.md)
- [batch_02_three_field_correction_review.md](../restart_2026_11_26/extraction/batch_02_three_field_correction_review.md)
- [batch_01_direct_pdf_probe_brief.md](../restart_2026_11_26/extraction/batch_01_direct_pdf_probe_brief.md)
- [batch_01_direct_pdf_probe_review.md](../restart_2026_11_26/extraction/batch_01_direct_pdf_probe_review.md)
- [batch_01_verified_path_correction_brief.md](../restart_2026_11_26/extraction/batch_01_verified_path_correction_brief.md)
- [batch_01_verified_path_correction_review.md](../restart_2026_11_26/extraction/batch_01_verified_path_correction_review.md)
- [batch_02_r0062_precision_brief.md](../restart_2026_11_26/extraction/batch_02_r0062_precision_brief.md)
- [batch_02_r0062_precision_review.md](../restart_2026_11_26/extraction/batch_02_r0062_precision_review.md)
- [batch_01_parent_only_brief.md](../restart_2026_11_26/extraction/batch_01_parent_only_brief.md)
- [batch_01_parent_only_review.md](../restart_2026_11_26/extraction/batch_01_parent_only_review.md)
- [scoped_pdf_repairs_review.md](../restart_2026_11_26/extraction/scoped_pdf_repairs_review.md)
- [p08_reconciliation_review.md](../restart_2026_11_26/extraction/p08_reconciliation_review.md)
- [p08_integrated_candidate.json](../restart_2026_11_26/extraction/p08_integrated_candidate.json)
- [p08_source_inventory.json](../restart_2026_11_26/extraction/p08_source_inventory.json)
- [p08_batch_01_source_review.md](../restart_2026_11_26/extraction/p08_batch_01_source_review.md)
- [p08_batch_02_source_review.md](../restart_2026_11_26/extraction/p08_batch_02_source_review.md)
- [p08_source_assist_batch_01_raw.json](../restart_2026_11_26/extraction/p08_source_assist_batch_01_raw.json)
- [p08_source_assist_batch_01_review.md](../restart_2026_11_26/extraction/p08_source_assist_batch_01_review.md)
- [p08_extraction_table.json](../restart_2026_11_26/extraction/p08_extraction_table.json)
- [p08_quantitative_claim_source_matrix.csv](../restart_2026_11_26/extraction/p08_quantitative_claim_source_matrix.csv)
- [p08_extraction_lock.json](../restart_2026_11_26/extraction/p08_extraction_lock.json)
- [p08_source_assist_batch_01_brief.md](../restart_2026_11_26/extraction/p08_source_assist_batch_01_brief.md)

<a id="buoc-12"></a>
## Bước 12 · Đánh giá chất lượng và nguy cơ sai lệch

**Đang làm** · `2026-11-27T01:09:07+07:00`

Nghiệm thu cấp bước đã ghi trong sổ: FAIL=4, PASS=2.

- [manifest.json](../restart_2026_11_26/appraisal/manifest.json)
- [batch_01_brief.md](../restart_2026_11_26/appraisal/batch_01_brief.md)
- [batch_02_brief.md](../restart_2026_11_26/appraisal/batch_02_brief.md)
- [batch_03_brief.md](../restart_2026_11_26/appraisal/batch_03_brief.md)
- [batch_04_brief.md](../restart_2026_11_26/appraisal/batch_04_brief.md)
- [batch_05_brief.md](../restart_2026_11_26/appraisal/batch_05_brief.md)
- [batch_01_dispatch.json](../restart_2026_11_26/appraisal/batch_01_dispatch.json)
- [batch_01_raw.json](../restart_2026_11_26/appraisal/batch_01_raw.json)
- [batch_01_mechanical.json](../restart_2026_11_26/appraisal/batch_01_mechanical.json)
- [batch_01_research_review.md](../restart_2026_11_26/appraisal/batch_01_research_review.md)
- [chat_cleanup.jsonl](../restart_2026_11_26/appraisal/chat_cleanup.jsonl)
- [batch_01_access_preflight_brief.md](../restart_2026_11_26/appraisal/batch_01_access_preflight_brief.md)
- [batch_01_access_preflight_review.md](../restart_2026_11_26/appraisal/batch_01_access_preflight_review.md)
- [batch_01_parent_correction_brief.md](../restart_2026_11_26/appraisal/batch_01_parent_correction_brief.md)
- [batch_01_access_preflight_dispatch.json](../restart_2026_11_26/appraisal/batch_01_access_preflight_dispatch.json)
- [batch_01_access_preflight_mechanical.json](../restart_2026_11_26/appraisal/batch_01_access_preflight_mechanical.json)
- [batch_01_access_preflight_raw.json](../restart_2026_11_26/appraisal/batch_01_access_preflight_raw.json)
- [batch_01_parent_correction_review.md](../restart_2026_11_26/appraisal/batch_01_parent_correction_review.md)
- [batch_01_targeted_correction_brief.md](../restart_2026_11_26/appraisal/batch_01_targeted_correction_brief.md)
- [batch_01_parent_correction_dispatch.json](../restart_2026_11_26/appraisal/batch_01_parent_correction_dispatch.json)
- [batch_01_parent_correction_mechanical.json](../restart_2026_11_26/appraisal/batch_01_parent_correction_mechanical.json)
- [batch_01_parent_correction_raw.json](../restart_2026_11_26/appraisal/batch_01_parent_correction_raw.json)
- [batch_01_parent_correction_recovery.json](../restart_2026_11_26/appraisal/batch_01_parent_correction_recovery.json)
- [batch_01_parent_correction_transport_failure.json](../restart_2026_11_26/appraisal/batch_01_parent_correction_transport_failure.json)
- [batch_01_targeted_correction_raw.json](../restart_2026_11_26/appraisal/batch_01_targeted_correction_raw.json)
- [batch_01_targeted_correction_dispatch.json](../restart_2026_11_26/appraisal/batch_01_targeted_correction_dispatch.json)
- [batch_01_targeted_correction_mechanical.json](../restart_2026_11_26/appraisal/batch_01_targeted_correction_mechanical.json)
- [batch_01_targeted_correction_review.md](../restart_2026_11_26/appraisal/batch_01_targeted_correction_review.md)
- [batch_01_locator_repair_brief.md](../restart_2026_11_26/appraisal/batch_01_locator_repair_brief.md)
- [batch_01_locator_repair_raw.json](../restart_2026_11_26/appraisal/batch_01_locator_repair_raw.json)
- [batch_01_locator_repair_dispatch.json](../restart_2026_11_26/appraisal/batch_01_locator_repair_dispatch.json)
- [batch_01_locator_repair_mechanical.json](../restart_2026_11_26/appraisal/batch_01_locator_repair_mechanical.json)
- [batch_01_locator_repair_review.md](../restart_2026_11_26/appraisal/batch_01_locator_repair_review.md)
- [batch_01_accepted.json](../restart_2026_11_26/appraisal/batch_01_accepted.json)
- [batch_02_raw.json](../restart_2026_11_26/appraisal/batch_02_raw.json)
- [batch_02_dispatch.json](../restart_2026_11_26/appraisal/batch_02_dispatch.json)
- [batch_02_mechanical.json](../restart_2026_11_26/appraisal/batch_02_mechanical.json)
- [batch_02_review.md](../restart_2026_11_26/appraisal/batch_02_review.md)
- [batch_02_correction_brief.md](../restart_2026_11_26/appraisal/batch_02_correction_brief.md)

<a id="buoc-13"></a>
## Bước 13 · Hòa giải PRISMA

**Chưa bắt đầu** · `2026-11-26T18:07:38+07:00`

Chưa có tệp minh chứng được đăng ký cho bước này.

<a id="buoc-14"></a>
## Bước 14 · Tổng hợp theo câu hỏi nghiên cứu

**Chưa bắt đầu** · `2026-11-26T18:07:38+07:00`

Chưa có tệp minh chứng được đăng ký cho bước này.

<a id="buoc-15"></a>
## Bước 15 · Viết manuscript LaTeX SN Computer Science

**Chưa bắt đầu** · `2026-11-26T18:07:38+07:00`

Chưa có tệp minh chứng được đăng ký cho bước này.

<a id="buoc-16"></a>
## Bước 16 · Kiểm định và bàn giao

**Chưa bắt đầu** · `2026-11-26T18:07:38+07:00`

Chưa có tệp minh chứng được đăng ký cho bước này.
