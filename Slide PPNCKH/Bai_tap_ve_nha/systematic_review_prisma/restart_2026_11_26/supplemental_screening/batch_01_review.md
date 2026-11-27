# Supplemental full-text screening batch 01

Reviewed 2026-11-27T10:14:45+07:00. Original transport timed out at 10:10:42 +07:00 with native Task generation still active. Bridge recovery of original UUID c3ab44ab-75fa-4f7b-a4d4-230860a6bcc5 and context 07bea6e9-3b38-4fff-96b8-d070bb869724 saved the same task's complete marked response at 10:13:14 +07:00 after two prior attempts found no complete result. No resend or changed task ID.

| Criterion | Verdict | Evidence |
|---|---|---|
| A1. Coverage and identity | PASS | Eight exact, distinct IDs and eight PDF SHA-256 matches. All 8/8 trusted bibliographic joins have title, authors, year, venue and DOI. |
| A2. Decision structure | PASS | Eight rows have all seven E states and compatible decision syntax. Four proposed exclusions have exactly one primary reason. This checks structure only. |
| A3. Exact PDF passages | FAIL | 49/58 PDF excerpts match the stated physical page under whitespace and ligature normalization. Nine require repair: R0024 E2/E6; R0080 E4; R0096 E1/E5; R0105 E3/E4/E6; R0157 E4. |
| A3. Official source and semantic evidence | FAIL | R0107 E5 can be resolved by matching IEEE metadata. R0024, R0080 and R0105 use download timestamps as date support; request applicable version dates. R0080 E7 cites a CFP invitation without evidence of peer review. R0105 E7 requires a source tied to the 2025 track. R0024 E7 cited URL returned 502 in independent check. |
| A4. Summary and isolation | PASS | One parseable end summary, eight IDs, one provider-reported uncertainty, no workers. Task receipt matches the authorized folder and no project file changes appeared in the scoped Git check. |
| Automatic chat cleanup | FAIL | Native result was saved. Prepare-delete could not activate the Gemini window; no deletion confirmation was repeated. |

Batch FAIL. Zero eligibility decisions adopted from this payload. The correction addresses six IDs while retaining the verified passages for review. Preserved exact evidence and compact amendment keys will be checked before adoption.
