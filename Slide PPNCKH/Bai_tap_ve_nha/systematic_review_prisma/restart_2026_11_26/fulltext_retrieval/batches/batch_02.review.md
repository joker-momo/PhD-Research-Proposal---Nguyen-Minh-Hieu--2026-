# Step 08 batch 02 acceptance

Reviewed 2026-11-26T19:38:49+07:00. Gemini.app direct-project Task `4498de15-6ff5-414c-bfcc-a8c4c346cf34` and context `b862cedd-e0ff-45b0-a241-d6deaf801b8e`. Raw provider result is retained as research leads. The accepted CSV records Codex's separate observed checks. Provider observations do not establish access or availability.

| Criterion | Verdict | Evidence |
|---|---|---|
| T1 | PASS | 20/20 exact IDs. 0 missing, duplicates, or out-of-batch records. |
| T2 | PASS | 20/20 locked bibliographic joins. 19 DOI identities confirmed. Unconfirmed identities retained explicitly with attempt logs. |
| T3 | PASS | 13 parsed, identity- and version-checked PDFs; 0 verified HTML full texts. File hashes are recorded. Candidate outcomes verified separately. |
| T4 | PASS | 7 rows with no PDF have a reason and next route. 58 timestamped checks. 0 unresolved rows credited as retrieved and 0 eligibility decisions. |

PDFs reused from user/project copies: 12. The exact title and first-page evidence were verified against this independently discovered queue. Provider chat cleanup: deleted.

PDF shortfalls: {"NO_VERIFIED_PDF_FROM_CHECKED_ROUTES": 1, "PREPRINT_ONLY_TARGET_VERSION_UNVERIFIED": 1, "PUBLISHER_ANTI_BOT_CHALLENGE": 2, "PUBLISHER_OR_PDF_ACCESS_RESTRICTED": 1, "PUBLISHER_OR_PDF_AUTOMATED_ACCESS_UNAVAILABLE": 2}.
