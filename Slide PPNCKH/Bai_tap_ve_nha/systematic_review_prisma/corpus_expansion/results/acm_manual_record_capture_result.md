# ACM manual record-capture result

**Completed:** 2026-11-26T17:47:48+07:00

**Database:** ACM Digital Library, The ACM Full-Text Collection

**Access observed:** signed-in Basic Edition browser session

The two accepted searches now have complete position-level captures:

| Variant | Reported | Captured | Rank coverage | Repeated source identities |
|---|---:|---:|---|---:|
| High recall | 79 | 79 | 1--79 | 1 |
| Complementary | 325 | 325 | 1--325 | 11 |

All 404 rows have a non-empty title, a 2021--2026 year, query/page/rank provenance, and a DOI/URL value or explicit not-found marker. The complementary set contains 39 `DOI_NOT_FOUND` markers and 35 `URL_NOT_FOUND` markers. These are reported missing values, not inferred identifiers.

The 12 repeated identities are ACM source-result repetitions at distinct displayed ranks. They remain in the capture CSV so the next deterministic deduplication task can preserve complete provenance.

## Evidence

- Raw pages: `sources/raw/core_searches/acm_manual_capture_2026-11-26/`
- Normalized CSV: `sources/normalized/core_searches/acm_manual_capture_2026-11-26/acm_all_records.csv`
- Variant JSON: `acm_high_recall_records.json`, `acm_complementary_records.json`
- Manifest and QA: `acm_capture_manifest.json`, `acm_capture_qa.json`
- Checksums: `acm_capture_checksums.sha256`

This closes the ACM record-level shortfall only. Web of Science Core Collection remains unexecuted and search completeness is not claimed.
