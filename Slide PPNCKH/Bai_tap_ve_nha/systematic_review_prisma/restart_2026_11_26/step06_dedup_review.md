# Step 06 — Deduplication

Verified at 2026-11-26T18:49:12+07:00. The 693 locked source rows reconcile to **465 screening records + 228 duplicate rows**. The deduplication map identifies every source row and its stable screening ID.

| Check | Verdict | Verified evidence |
|---|---|---|
| Raw rows accounted for | PASS | 693/693 source IDs, with exactly one mapping each. |
| DOI and title joins | PASS | 216 duplicate rows match both the normalized DOI and title of their representative. |
| ACM proceedings joins | PASS | 12 DOI-missing rows match a DOI-bearing ACM proceedings record on title, year and record type. Both source page/rank locators are retained. |
| Duplicate keys after deduplication | PASS | 0 repeated nonempty DOI or normalized title across the 465 screening records. |
| Conflicts preserved | PASS | 0 unresolved identity groups in the DOI and normalized-title comparison. 12 year disagreements across records sharing a DOI and title remain visible in the issues file. |
| Tests and boundaries | PASS | 4/4 normalization and deduplication tests. 0 legacy decisions imported or eligibility decisions performed. |

The matching rules use reported DOI and title identity. Similar titles by themselves cannot establish a match, and relationships between versions or studies remain for the study-family step. Number of included reports remains unknown.
