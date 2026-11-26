# Bước 01 — Kiểm kê đầu vào

Updated at: 2026-11-26T18:08:34+07:00

Đây là kiểm kê, chưa phải khóa dataset cuối hay kết quả sàng lọc.

| Nguồn | Hàng thô | File CSV |
|---|---:|---:|
| IEEE Xplore | 63 | 2 |
| Scopus | 110 | 2 |
| ACM Digital Library | 404 | 1 (2 truy vấn) |
| OpenAlex | 111 | 2 |
| Tổng | 688 | 7 |

7/7 CSV khớp số hàng và SHA256. Ledger evidence: 51/51 PASS (25 base +26 ACM). Unique records và included reports chưa biết. WoS không tìm do thiếu quyền; count=null. Không sử dụng bộ 46 cũ.

## Khoảng thiếu phải xử lý đúng bước

- I01: ACM authors missing215/404; abstract_snippet missing335/404; VENUE_NOT_FOUND238; DOI_NOT_FOUND39; URL_NOT_FOUND35. Metadata gap, not an exclusion decision. Locator: `sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_all_records.csv`.

- I02: OpenAlex normalized CSV has no abstract column; raw payload availability must be checked in step05. Two rows have missing DOI, one has missing venue. Locator: `sources/raw/core_searches/openalex_compensatory_2026-11-26/`.

- I03: ACM upper filter2026-11-30 exceeds actual search date2026-11-26; eligibility must use actual cutoff after query/protocol audit. Locator: `sources/raw/core_searches/acm_high_recall_2026-11-26.json#active_filters`.

- I04: Historical manifest contains superseded ACM count-only disposition and old46 linkage; use this inventory plus supplement for restart, not its old next_action. Locator: `corpus_expansion/search_dataset_lock_2026-11-26.json`.

- I05: IEEE/Scopus stored search times derive from export mtime; preserve basis, do not describe as independently logged live search timestamps. Locator: `sources/raw/core_searches/ieee_xplore_high_recall_authenticated_2026-11-26.json#timestamp_basis`.

## Nghiệm thu

| Criterion | Verdict | Evidence |
|---|---|---|
| All7 input CSVs exist and count/hash match | PASS | 7/7;688 total rows |
| All listed raw/capture evidence hashes match | PASS | 51/51 checks:base25+ACM26; these are ledger checks, not unique-file count |
| Every query variant has exact query/filter/time evidence | PASS | 8/8; timestamp basis preserved |
| Missing metadata and source shortfalls explicit | PASS | I01-I05; WoSnull; unique_countnull |
| No scientific decisions inherited or new screening performed | PASS | 0 old decision rows imported;0 newly screened; changes restricted to plan/inventory/state |
