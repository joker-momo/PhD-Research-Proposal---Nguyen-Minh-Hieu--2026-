# Final integrity audit · HK261 restart

## Manuscript and evidence checks

| Criterion | Verdict | Verified evidence |
|---|---|---|
| Corpus and PRISMA arithmetic | PASS | 693 identified records − 228 duplicates = 465 screened; 465 − 328 excluded = 137 sought; 137 − 93 unavailable = 44 assessed; 44 = 13 excluded + 6 awaiting + 25 included. The 25 included reports map to 25 studies in the locked version ledger. Unexplained difference 0. |
| Appraisal and main figures | PASS | 25 × 10 = 250 judgments. All 10 manuscript appraisal rows match the P09 tally and sum to 25. Flow PDF and Figure 1 carry the reconciled counts. |
| Quantitative provenance | PASS | The two manuscript outcome examples match the accepted rows. R0054 PDF p. 4 §IV supplies conditions and p. 5 Table I supplies normalized cost and confidence-interval width. R0074 PDF pp. 15–17 §§4.1–4.2 and Fig. 4 establish the prefill metric, bandwidth, workload, comparator results and OOM categories. Unsupported values accepted: 0. The dossier retains 58 quantitative rows and excludes 11 withheld keys from synthesis. |
| Bibliographic identity | PASS | 26 distinct Crossref DOI records responded HTTP 200. Matching title, names and DOI were checked on page 1 of 25 locked PDFs. R0121 uses the registry's ASCII DOI because its original text contains a Cyrillic character and its PDF link is truncated. R0083's PDF and registry both include ShinYoung Cho; its manuscript citation now does too. |
| Date and edition | PASS | Issue-year bibliography retained. R0095 was available on 16 July 2026 per PDF p. 1, within the cutoff, and was assigned to the December 2026 issue. The issue date does not replace the online availability evidence used for eligibility. |
| Independent notice checks | PASS | 26/26 Crossref works checked for update metadata and matched by normalized DOI against both DOI fields of the 74,131-row Retraction Watch export. No formal correction, expression of concern or retraction was located in these registry checks. Coverage is source-bounded. |
| Citation integrity | PASS | 26 compiled bibliography entries, 26 distinct clickable DOI links, zero unresolved citations or cross-references. |
| Build and visual inspection | PASS | Approved Tectonic build succeeded. 10/10 PDF pages inspected, including the figure, appraisal table and references. The build reports non-blocking underfull vertical-box and embedded PDF-version warnings. No missing glyphs or overfull boxes were reported. |
| Reporting checklist | PASS | 27/27 numbered items have a disposition and a manuscript or dossier locator. Four assessments are outside the protocol and the two author declarations await confirmation. See the [PRISMA checklist](../prisma/prisma_checklist.md). |
| Reporting and authorship limits | PASS | Coverage, human-review and methodology limits are stated. Authorship and declarations await confirmations. No submission or email was performed. |

[Independent DOI and registry evidence](independent_registry_evidence.json) ·
[Limitations](limitations.md) ·
[Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) ·
[Retraction Watch dataset documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/) ·
[PRISMA 2020 checklist](https://www.prisma-statement.org/prisma-2020-checklist)

## Gemini.app evidence and disposition

The first 26-row response was quarantined for the failed fields documented
in the [initial review](source_audit_primary_review.md). The 21-row targeted
correction was checked against the actual local registry records. Only the
five source-resolved primary rows and 21 corrected rows contribute to the
composite. The independently observed registry results govern the manuscript.

| Targeted criterion | Verdict | Verified evidence |
|---|---|---|
| Exact correction coverage | PASS | 21/21 expected ID–DOI pairs, zero repeated IDs, normalized titles or DOIs, zero overlap with the five retained rows. |
| Identity and source locators | PASS | 21/21 corrected titles, publication years, venues and ordered bylines agree with the deposited metadata. The 40 search wrappers around the identity and notice links on 20 rows were unwrapped only when their embedded targets matched the exact Crossref work URLs in the independent HTTP 200 receipts. |
| Notice scope | PASS | 21/21 rows cite both checked registry sources and have no positive notice claim. This correction used supplied source snapshots. The provider explicitly reports that it did not independently browse the publisher pages for those 21 rows. |
| Output, provenance and completeness | PASS | 21/21 parseable rows with the required fields, zero unknown statuses, zero unresolved IDs, zero correction workers and completion marker. The placeholder link in the summary footer was not used. Locator coverage comes from the exact URLs in the rows and the independent receipts. |
| Composite coverage | PASS | 26/26 DOI audits have first-party identity and source-bounded notice disposition. Zero conflicting or out-of-bound discovery claims from the initial response were adopted. |

Primary UUID `f60d888e-ce8c-4895-a1de-2322204862d6` · payload saved, cleanup
**BLOCKED** by the persistent extra AX user row. Correct UUID, complete answer
and idle state were reverified after reopening. The native cleanup guard
refused the folder-detach prerequisite and no delete confirmation was sent.
Correction UUID `9694fcd8-81b9-48af-ad4a-5eb0b0604d12` · payload saved and
chat **DELETED**, with the empty new-chat postcondition verified. Duplicate
submissions and wrong-chat deletions observed: 0.

[Correction response](source_audit_correction_raw.json) ·
[Mechanical correction checks](source_audit_correction_checks.json) ·
[Initial chat cleanup receipt](source_audit_cleanup.json)

## Coursework package

Archive CRC checks and manifest SHA-256 checks passed. The extracted LaTeX
source was built independently from an empty temporary directory using the
bundled class, bibliography style, figure and sources. Original article
PDFs, search exports and the full Gemini bridge receipts remain in the
local evidence workspace. Some detailed locators refer to that workspace.


## Follow-up PRISMA reporting review

Checked at 2026-11-27T08:31:47+07:00. The earlier audit above records the original ten-page
build. The revised coursework PDF has eleven pages.

| Criterion | Verdict | Verified evidence |
|---|---|---|
| Checklist dispositions and locators | PASS | 27/27 entries checked against the revised PDF and bundled supplements. 12 reported, 9 partially reported, 4 not performed, 2 awaiting author confirmation. Items 10 and 18 are partial. |
| Evidence boundary | PASS | Six outcome groups, source units and conditions, narrative synthesis methods, report-ID joins, and documented restart changes were drawn from the locked protocol and derived tables. No screening decision, extracted measurement, study appraisal or citation was changed. |
| PDF and citations | PASS | Tectonic build passed, 11/11 pages visually inspected and 26 distinct DOI links verified. Figure 1 is on p. 5. No unresolved citation or cross-reference warnings, overfull boxes or missing characters. Vertical underfull-box and embedded PDF-version warnings remain. |
| Reporting gaps | OPEN | No formal reporting-bias or certainty assessment was performed. Engineering appraisal is distinct from study-level risk-of-bias assessment. Funding and other support, sponsor roles, competing interests, and any public sharing arrangements await author confirmation. The checklist records the remaining partial items. |

See the [revised PRISMA checklist](../prisma/prisma_checklist.md).
