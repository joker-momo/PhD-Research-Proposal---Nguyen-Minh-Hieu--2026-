# B04 Authenticated Resume Checkpoint Review

**Review timestamp:** 2026-11-26T14:18:09+07:00

**Query set:** 1.3

**Status:** `BLOCKED_WOS_CORE_AND_ACM_EXPORT_ACCESS`

This review supersedes the current-state conclusions of the earlier sign-in
checkpoint without deleting its evidence. Institutional access enabled complete
IEEE Xplore and Scopus exports. ACM Digital Library remained Basic Edition, and
the authenticated Clarivate session exposed Web of Science Free View rather
than the Web of Science Core Collection. B04 is therefore still incomplete.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| Eight exact query variants accounted for | PASS | Ledger contains high-recall and complementary rows for IEEE, ACM, Scopus and Web of Science. |
| Official-interface searches executed | FAIL | 6/8 executed: IEEE 2/2, ACM 2/2, Scopus 2/2, Web of Science 0/2. |
| Exact query retained for every executed run | PASS | Six executed runs point to query set 1.3; four new authenticated observation records repeat the exact IEEE/Scopus strings. |
| Search timestamp and filters retained | PASS | Four successful exports retain RFC 3339 times based on completed-export mtimes and record active year, type and language handling. |
| Reported totals recorded without inference | PASS | IEEE 42/21, ACM 79/325 and Scopus 77/33; Web of Science totals remain null. |
| Required IEEE content types applied | PASS | High-recall export has 26 conference + 16 journal records; complementary has 12 + 9. Early Access and Magazine records are excluded. |
| Record-level exports obtained and parsed | FAIL | 4/8 exports: IEEE 42 + 21 rows and Scopus 77 + 33 rows. ACM 0/2 and Web of Science 0/2. |
| Export count equals parsed data rows | PASS | 42=42, 21=21, 77=77 and 33=33. |
| Export-internal duplicate titles or non-empty DOIs | PASS | Zero duplicate titles and zero duplicate non-empty DOIs within each of the four exports. Cross-query deduplication is deferred to B05. |
| Raw evidence and checksum retained | PASS | Ten new raw artifacts plus the six earlier JSON records are covered by `sources/raw/core_searches/checksums.sha256`; 16/16 verify. |
| Unsupported quantitative claims | PASS | Zero; no Web of Science count is inferred and the 173 exported rows are not described as unique records. |
| B04 completion gate | FAIL | Licensed Web of Science Core Collection access and an ACM record-level export route remain unresolved. |

## Accepted outputs in this checkpoint

- IEEE Xplore high-recall: 42 reported and 42 exported.
- IEEE Xplore complementary: 21 reported and 21 exported.
- Scopus high-recall: 77 reported and 77 exported.
- Scopus complementary: 33 reported and 33 exported.
- Total exported rows before cross-platform and cross-query deduplication: 173.

## Blocking resume point

1. Obtain licensed Web of Science Core Collection access, then execute and
   export both version-1.3 queries with active editions, `CPCI-S`, document type,
   language, count and checksum recorded.
2. Obtain an ACM Premium/institutional record-level export or document an
   approved lawful alternative that produces complete records for the two
   already observed totals.
3. Re-run this acceptance table. B05 must not treat 173 rows as a deduplicated
   corpus and must not begin until the remaining access decision is resolved.
