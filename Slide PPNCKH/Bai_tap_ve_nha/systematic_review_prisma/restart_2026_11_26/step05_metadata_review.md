# Step 05 — Normalization and metadata review

Reviewed at 2026-11-26T18:47:38+07:00. Native Gemini.app task 2f1423a8-3a09-41f8-8c86-c76a7f7c5e67 read the canonical HK261 folder with zero context copies. The raw provider receipt and original source field values were preserved.

| Criterion | Verdict | Evidence |
|---|---|---|
| N1 | PASS | 3/3 requested IDs; normalized title repeats 0; nonempty DOI repeats 0. |
| N2 | PASS | 3/3 field sets have permitted unknown markers; 3/3 IDs, record locators, titles and years match the locked CSVs. |
| N3 | PASS | 0 newly verified DOI or venue values asserted; all 3 gaps explicitly unresolved. Publisher, registry and repository evidence checked below. No non-authoritative lead ingested. |
| N4 | PASS | 0 eligibility decisions or new imports. All 7 locked CSV hashes unchanged. |
| P1 | PASS | 693/693 normalized rows and unique source-record positions; 2/2 regression tests PASS. |

| OpenAlex ID | Requested field | Verified disposition |
|---|---|---|
| W7217862547 | DOI | Keep missing. The [publisher](https://ajaccm.com/journal/index.php/ajaccm/article/view/771) confirms title/year and provides a prefix-only DOI. Its author order differs from the export. No DOI or change to author order imported. |
| W4415181609 | Venue | Keep missing. [Crossref](https://api.crossref.org/works/10.62311/nesx/rb978-81-981662-2-7) resolves the locked DOI and reports an empty container title. It gives National Education Services as publisher and reference-book as its type. The provider’s alternate identifier lead was not adopted. |
| W7200232308 | DOI | Keep missing. The [canonical repository URL](https://dspace.lib.cranfield.ac.uk/handle/1826/23982) returned 403. The [matching repository record](https://cran-test-dspace.koha-ptfs.co.uk/handle/1826/23982) has matching handle, title, author and year; its citation metadata exposes no DOI. |

There are 41 rows without a DOI, 239 without a venue, 215 without authors, 467 without language metadata and 520 without a full abstract in the locked exports. ACM snippets remain separate from full abstracts. Counts precede deduplication. Gaps may be resolved from another source during duplicate reconciliation and screening. No eligibility decisions were made.
