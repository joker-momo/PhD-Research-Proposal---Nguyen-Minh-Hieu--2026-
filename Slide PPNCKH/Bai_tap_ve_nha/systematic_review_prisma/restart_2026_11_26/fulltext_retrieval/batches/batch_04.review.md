# Step 08 batch 04 acceptance

Reviewed 2026-11-26T19:52:54+07:00. Gemini.app direct-project Task `a33d1ae9-0b17-40eb-a677-bef6dac9bc2e` and context `26547085-c23a-49d7-ad3f-f00e5d5b793f`. Raw provider result is retained as research leads. Corrective task: 3aa88422-5ce9-42a8-9eba-865a50d8b838. The accepted CSV records Codex's separate observed checks. Provider observations do not establish access or availability.

| Criterion | Verdict | Evidence |
|---|---|---|
| T1 | PASS | 20/20 exact IDs. 0 missing, duplicates, or out-of-batch records. |
| T2 | PASS | 20/20 locked bibliographic joins. 20 DOI identities confirmed. Unconfirmed identities retained explicitly with attempt logs. |
| T3 | PASS | 6 parsed, identity- and version-checked PDFs; 0 verified HTML full texts. File hashes are recorded. Candidate outcomes verified separately. |
| T4 | PASS | 14 rows with no PDF have a reason and next route. 95 timestamped checks. 0 unresolved rows credited as retrieved and 0 eligibility decisions. |

PDFs reused from user/project copies: 2. The exact title and first-page evidence were verified against this independently discovered queue. Provider chat cleanup: deleted.

PDF shortfalls: {"NO_VERIFIED_PDF_FROM_CHECKED_ROUTES": 2, "PDF_FAILED_IDENTITY_OR_READABILITY": 1, "PDF_REPORT_VERSION_UNVERIFIED": 1, "PREPRINT_ONLY_TARGET_VERSION_UNVERIFIED": 1, "PUBLISHER_ANTI_BOT_CHALLENGE": 7, "PUBLISHER_OR_PDF_AUTOMATED_ACCESS_UNAVAILABLE": 2}.
