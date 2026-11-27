# Supplemental full-text screening batch 02 — first-pass review

Native Task `cffe09b2-be88-4cd5-a630-ae525e024b0c`, context `472de481-2a6a-4f1f-8162-445e182b2ee8`. The bridge hit its deadline at 10:31:05 +07:00. The matching open task had no complete marked output in the first two recovery attempts. It was recovered on the third attempt at 10:34:21 +07:00. The same task ID and direct HK261 folder were preserved.

| Criterion | Verdict | Evidence |
|---|---|---|
| A1. Coverage and identity | PASS | 8/8 distinct expected IDs, each with a checked hash and title, authors, year, venue and DOI from the input manifest. No missing record. |
| A2. Structure and precedence | FAIL | 8/8 rows and 56/56 E states parse, with one primary code each. R0091, R0122 and R0148 call generic offloading/resource evaluation E4 T despite the absence of evaluation of a proposed inference method. R0099, R0128 and R0148 have U states while the end summary reports no uncertainty. The primary reason may still be independently supported. |
| A3. Original-PDF passages | FAIL | 56/59 returned local passages matched under conventional text normalization. R0091 E2, R0099 E2, and R0148 E5 need exact replacements. |
| A3. Publisher evidence | FAIL | R0122 E5 uses DBLP's update date. The existing Crossref deposit shows published-online date 2026-11-22. R0122 E7 lacks verifiable workshop membership and applicable review policy. R0099's journal policy can be checked directly. R0148's DOI deposit has published-online date 2026-05-04. R0128's available authoritative field only had a year on inspection. Missing month/day remains an explicit E5 U unless independently verified. |
| A4. Isolation | PASS | The complete marked response was saved with the original UUID. The receipt has direct project scope. Zero workers reported. |
| Native chat cleanup | FAIL | Prepare-delete failed to activate the Gemini window. A repeat confirmation was not attempted. |

No batch 02 decision was accepted at this gate. The correction targets specific evidence defects and preserves already verified material.
