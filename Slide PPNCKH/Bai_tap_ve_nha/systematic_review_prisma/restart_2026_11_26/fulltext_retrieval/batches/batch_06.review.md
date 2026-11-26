# Step 08 batch 06 acceptance

Reviewed 2026-11-26T20:08:32+07:00. Gemini.app direct-project Task `7a419e99-4258-4dc8-ae9b-6d403d0c2fed` and context `5c77c75b-17dc-45cf-9416-60eb4a1c52fe`. Raw provider result is retained as research leads. Corrective task: not applicable. The accepted CSV records Codex's separate observed checks. Provider observations do not establish access or availability.

| Criterion | Verdict | Evidence |
|---|---|---|
| T1 | PASS | 20/20 exact IDs. 0 missing, duplicates, or out-of-batch records. |
| T2 | PASS | 20/20 locked bibliographic joins. 20 DOI identities confirmed. Unconfirmed identities retained explicitly with attempt logs. |
| T3 | PASS | 2 parsed, identity- and version-checked PDFs; 0 verified HTML full texts. File hashes are recorded. Candidate outcomes verified separately. |
| T4 | PASS | 18 rows with no PDF have a reason and next route. 112 timestamped checks. 0 unresolved rows credited as retrieved and 0 eligibility decisions. |

PDFs reused from user/project copies: 0. The exact title and first-page evidence were verified against this independently discovered queue. Provider chat cleanup: deleted.

For R0260, the supplied HTTP locator was normalized to the verified HTTPS author page. Its linked PDF returned 404. The raw provider URL is preserved.

PDF shortfalls: {"PDF_REPORT_VERSION_UNVERIFIED": 1, "PREPRINT_ONLY_TARGET_VERSION_UNVERIFIED": 1, "PUBLISHER_ANTI_BOT_CHALLENGE": 16}.
