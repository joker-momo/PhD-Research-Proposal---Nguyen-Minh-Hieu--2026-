# Step 08 batch 03 acceptance

Reviewed 2026-11-26T19:43:56+07:00. Gemini.app direct-project Task `d48af264-899f-45cc-9bed-3e49e3476fca` and context `265c8ee0-96de-4ded-8c72-138c1a773b43`. Raw provider result is retained as research leads. The accepted CSV records Codex's separate observed checks. Provider observations do not establish access or availability.

| Criterion | Verdict | Evidence |
|---|---|---|
| T1 | PASS | 20/20 exact IDs. 0 missing, duplicates, or out-of-batch records. |
| T2 | PASS | 20/20 locked bibliographic joins. 17 DOI identities confirmed. Unconfirmed identities retained explicitly with attempt logs. |
| T3 | PASS | 9 parsed, identity- and version-checked PDFs; 0 verified HTML full texts. File hashes are recorded. Candidate outcomes verified separately. |
| T4 | PASS | 11 rows with no PDF have a reason and next route. 73 timestamped checks. 0 unresolved rows credited as retrieved and 0 eligibility decisions. |

PDFs reused from user/project copies: 6. The exact title and first-page evidence were verified against this independently discovered queue. Provider chat cleanup: deleted.

PDF shortfalls: {"NO_VERIFIED_PDF_FROM_CHECKED_ROUTES": 3, "PREPRINT_ONLY_TARGET_VERSION_UNVERIFIED": 1, "PUBLISHER_ANTI_BOT_CHALLENGE": 2, "PUBLISHER_OR_PDF_AUTOMATED_ACCESS_UNAVAILABLE": 5}.
