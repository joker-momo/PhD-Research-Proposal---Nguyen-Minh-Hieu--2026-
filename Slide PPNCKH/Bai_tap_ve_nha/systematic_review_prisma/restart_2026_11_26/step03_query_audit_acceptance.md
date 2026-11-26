# Step 03 — Query audit and acceptance

Reviewed at 2026-11-26T18:41:53+07:00. Native Gemini.app Task `8d95f3d2-10d1-43b9-9906-ef7c48614d55`, context `de08f9dd-412b-42ff-8c52-62f62fde2c4c`. The first two answers remain quarantined. The accepted answer used the canonical project folder directly. Bridge cleanup was verified. Direct access does not produce a whole-folder immutability receipt. The inventory inputs were checked separately.

| Criterion | Verdict | Verified evidence |
|---|---|---|
| D1 | PASS | 8/8 unique runs, 4/4 documentation entries, valid field counts and exact parent ID. |
| D2 | PASS | 8/8 locators, reported counts and archived timestamps matched. ACM 79 + 325 captured positions, 0 initial native exports. WoS count null. |
| D3 | PASS | 4/4 platforms supported by official documentation or labeled as local observations. ACM guide section independently located at slide 16. No cross-source causal claim accepted. |
| D4 | PASS | 7 RETAIN and 1 REVISE. OpenAlex kept all original terms, the four wildcards, the OR tail, dates and language. |
| D5 | PASS | Four zero action counters and 6 explicit limitations. Provider result has zero screened or discovered records and zero reported edits. All 51 original checksum checks and 7 CSV row counts match. |
| R1 | PASS | Codex rerun archived: API 31, CSV 31, 26 original IDs retained, 5 newly observed IDs. Raw/CSV hashes match. |

## Source decisions

| Source | Original counts, high recall / complementary | Decision and search evidence |
|---|---:|---|
| IEEE Xplore | 42 / 21 | Retain both. The [official command-search page](https://ieeexplore-custom.ieee.org/search/advanced/command?reload=true) describes uppercase Boolean operators and field prefixes. Recorded settings and counts come from the authenticated run artifacts. Timestamp is export mtime. |
| Scopus | 77 / 33 | Retain both. The [official advanced-search guide](https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search) documents TITLE-ABS-KEY, dates, document types and language. Timestamp is export mtime. |
| ACM Digital Library | 79 / 325 | Retain both manually captured search-result sets. The [official guide, Advanced Search](https://libraries.acm.org/binaries/content/assets/libraries/new_acm-digital-library-user-guide.pdf#page=16) shows Anywhere, the collection scope, Boolean operators and a month-level date filter. The raw provider answer cited pages 19–21 for the section, while Codex verified slide 16. On the observed ACM runs the upper bound was November 30. Apply the protocol’s November 26 cutoff, language and report type downstream. |
| OpenAlex | 85 / 26 | Retain high recall and use version 1.4-openalex-2 for the complementary run at 2026-11-26T18:41:10+07:00. The [official search guide](https://help.openalex.org/api/searching/) documents exact matching, wildcards and OR. The 31 exported rows contain all 26 original OpenAlex IDs and 5 additional IDs at these two snapshots. This measures overlap, not recall. Neither export includes abstracts. |
| Web of Science | null | Unsearched because access was unavailable. |

The 688 rows in the initial inventory describe the original snapshots. If step 04 selects the revised complementary run, the expected total is 693 source rows before deduplication. Do not sum the original 26 and the revised 31. Academic eligibility and unique count remain open. No historical screening decision was imported.
