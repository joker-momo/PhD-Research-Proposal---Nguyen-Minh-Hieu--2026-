# Supplemental screening batch 01 — composite acceptance

The initial payload remains quarantined in [batch_01_review.md](batch_01_review.md). For the correction, native task `43a286ea-2e06-49cd-b30d-7e4c3671aab0` and context `a5b35e6a-1521-455b-a135-9da12527c3fc` were recovered after the original transport timeout. The full marked result was saved at 2026-11-27T10:21:36+07:00. No resend occurred.

| Check | Verdict | Evidence |
|---|---|---|
| A1. Coverage and identity | PASS | 8/8 report IDs and canonical SHA-256 matches. Exact DOI and zero duplicate DOI or normalized-title keys in this batch. Complete bibliographic join in batch_01_inputs.json. |
| A2. Protocol precedence | PASS | 8/8 application of P03/P06. Four all-true includes and four E3 exclusions, one primary reason each. |
| A3. Local evidence | PASS | The nine corrected physical-page passages match with ordinary line endings, typography and discretionary hyphen normalization. The three mismatches that persisted under broader normalization in the original payload were replaced with verified anchors. Scientific explanations were reduced to the eligibility judgment each source supports. |
| A3. Publication and review | PASS | IEEE Xplore directly gives 10 September 2026 for R0107. It supersedes the provider's explicitly unresolved E5. R0024 uses the DOI deposit and the technical-programme chair's report because the homepage returned HTTP 418. R0080 uses the IEEE final program pp1, 4 and 28. R0096 uses the Cloud2Things organizer CFP paired with the official UbiComp workshop listing and ACM paper. R0105 uses the conference site, DOI deposit and the organizer-linked submission portal. R0157 uses the organizer's submission guidelines and program. Correction observations that were unverifiable or unnecessary were not accepted as evidence. |
| A4. Isolation and output | PASS | 8/8 accepted records, no unresolved decision in this batch, zero worker claims. Two complete marked response receipts. Git scope contains only checkpoint artifacts; source PDFs are ignored. |
| Native chat cleanup | FAIL | The result was saved, but prepare-delete failed to activate the Gemini window. A repeat deletion confirmation was not attempted. |

`batch_01_accepted.json` preserves the composite judgments for 4 inclusions (R0014, R0036, R0080, R0107) and 4 exclusions for E3 (R0024, R0096, R0105, R0157). This is a screening checkpoint. Study-family linkage, extraction and appraisal precede the PRISMA and manuscript revision.
