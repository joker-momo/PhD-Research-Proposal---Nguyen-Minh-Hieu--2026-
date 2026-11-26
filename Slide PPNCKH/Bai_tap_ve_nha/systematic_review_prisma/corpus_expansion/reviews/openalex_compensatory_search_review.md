# OpenAlex Compensatory Search Acceptance Review

**Review timestamp:** 2026-11-26T15:12:17+07:00
**Query set:** 1.4 / OpenAlex adapter 1
**Status:** `ACCEPTED_AS_SUPPLEMENTARY_COMPENSATORY_SEARCH`

This review accepts the two OpenAlex runs as reproducible supplementary search
evidence. It does not convert them into Web of Science Core Collection runs and
does not assert equivalent coverage.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| Two configured variants executed | PASS | High-recall and complementary manifests both exist and report one completed cursor page. |
| API total reconciles with exported rows | PASS | High-recall 85=85; complementary 26=26. |
| Exact query and OpenAlex interpretation retained | PASS | Both raw records and manifests contain the submitted Boolean string and `meta.x_query.oql`. |
| Date and language filters retained | PASS | Both manifests record 2021-01-01 through 2026-11-26 and `language:en`. |
| Wildcard mode is valid | PASS | Complementary search uses `search.title_and_abstract.exact`; the tested validator rejects wildcards in stemmed mode. |
| Raw and normalized records retained | PASS | Two raw JSON files contain 85 and 26 records; two normalized CSV files contain the same row counts. |
| Internal duplicate identities reported | PASS | Each variant has zero duplicate OpenAlex IDs, non-empty DOIs and normalized titles. |
| Cross-query overlap reported without false unique claim | PASS | Nine OpenAlex IDs overlap; the two variants contain 102 union IDs before cross-platform deduplication. |
| Checksums verify | PASS | Six variant raw/CSV/manifest files verify 6/6 against their local checksum files; all nine generated artifacts are covered by the parent checksum ledger. |
| Unsupported WoS claim | PASS | Source fields equal `OpenAlex`; manifests and summary explicitly state that this is not a WoS Core run. |
| Publication-type boundary retained | PASS | Type is exported broadly and deferred to protocol-based screening; no journal/conference-only count is inferred. |
| Unit tests | PASS | Ten OpenAlex search tests pass with zero failures or skips, including timestamp-zone and evidence-overwrite guards. |

## Accepted counts

- High-recall: 85 reported and 85 exported.
- Complementary: 26 reported and 26 exported.
- Cross-query overlap: 9 OpenAlex IDs.
- Cross-query union: 102 OpenAlex IDs before cross-platform deduplication.

## Remaining boundary

Web of Science Core Collection remains unavailable and both planned WoS counts
remain null. ACM still lacks record-level exports. These OpenAlex records may be
added to the deduplication queue only under Amendment 006 and must not be used to
claim that B04's original eight core-platform exports were completed.
