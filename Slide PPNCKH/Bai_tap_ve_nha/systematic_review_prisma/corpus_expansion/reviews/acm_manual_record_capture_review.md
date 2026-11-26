# ACM manual record-capture acceptance review

**Review timestamp:** 2026-11-26T17:47:48+07:00

**Status:** `ACCEPTED_COMPLETE_POSITION_LEVEL_CAPTURE`

| Criterion | Verdict | Objective evidence |
|---|---|---|
| Two accepted variants captured | PASS | High-recall and complementary outputs both exist. |
| Exact result positions | PASS | 79/79 plus 325/325 = 404/404 rows. |
| Rank integrity | PASS | Ranks are contiguous 1--79 and 1--325; duplicate ranks = 0/0. |
| Required bibliographic fields | PASS | Missing titles = 0; missing/out-of-range years = 0. |
| Explicit missing-data markers | PASS | DOI field empty = 0 and URL field empty = 0; 39 DOI and 35 URL not-found markers are explicit. |
| Provenance | PASS | Missing source-page URL/raw locator = 0; every raw/normalized artifact is listed in the manifest. |
| Duplicate disclosure | PASS | 1 high-recall and 11 complementary repeated identifiers are retained at distinct ranks and reported for deduplication. |
| Deterministic parser tests | PASS | 2/2 focused unit tests pass. |
| QA gate | PASS | `acm_capture_qa.json` reports `acceptance_pass: true`. |
| Integrity ledger | PASS | The checksum ledger covers 21 raw page files and 5 normalized/manifest files. |
| Unsupported claims | PASS | No relevance, unique-study, Web of Science, completeness or submission claim is made. |

The result is admitted as a supplement to snapshot `HK261-SEARCH-INPUT-20261126-v1`. The next task must account for 688 raw rows: 284 previously locked rows plus 404 ACM rows, before any cross-query or cross-platform deduplication.
