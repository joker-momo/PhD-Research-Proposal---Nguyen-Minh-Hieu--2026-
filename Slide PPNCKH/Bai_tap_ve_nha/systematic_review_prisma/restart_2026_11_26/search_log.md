# Step 04 — Locked search dataset

Locked at 2026-11-26T18:42:41+07:00. The [search dataset manifest](search_dataset_manifest.json) identifies the exact query, source artifact, filters, timestamp basis, import file and SHA-256 for every selected run.

| Platform | Run | Version | Observed time or export timestamp | Rows |
|---|---|---|---|---:|
| IEEE Xplore | high_recall | 1.3 | 2026-11-26T14:13:05+07:00 | 42 |
| IEEE Xplore | complementary | 1.3 | 2026-11-26T14:15:41+07:00 | 21 |
| Scopus | high_recall | 1.3 | 2026-11-26T14:08:35+07:00 | 77 |
| Scopus | complementary | 1.3 | 2026-11-26T14:09:24+07:00 | 33 |
| OpenAlex | high_recall | 1.4-openalex-1 | 2026-11-26T14:54:14+07:00 | 85 |
| OpenAlex | complementary | 1.4-openalex-2 | 2026-11-26T18:41:10+07:00 | 31 |
| ACM Digital Library | high_recall | 1.3 | 2026-11-26T13:50:14+07:00 | 79 |
| ACM Digital Library | complementary | 1.3 | 2026-11-26T13:50:14+07:00 | 325 |

The locked dataset has 693 rows across seven import CSVs: IEEE Xplore 63, Scopus 110, ACM Digital Library 404, and OpenAlex 116. Unique records and included reports remain unknown. Academic eligibility and deduplication come later.

- ACM: 79 and 325 manually captured result positions are stored together in one CSV. The original browser runs produced zero native exports. Duplicate positions and incomplete metadata remain in the locked raw input. The month-level upper bound and language/type eligibility will be checked during the approved downstream stages.
- IEEE Xplore and Scopus: timestamp locators use local export modification time. IEEE's language eligibility remains a downstream check. Scopus applied an English filter.
- OpenAlex: the original high-recall export is retained alongside the revised complementary export. The old 26-row complementary export remains in the archive and contributes zero rows to this manifest. OpenAlex is a supplementary source.
- Web of Science Core Collection: unavailable and unsearched. The count is null.

The old 46-report collection contributed zero rows or screening decisions. The evidence archive has been preserved.
