# HK261 · Final integrity audit for the 46-study review

This audit covers the November 2026 HK261 coursework review prepared in the Springer Nature LaTeX format for SN Computer Science. The active evidence comes from the 25-study restart and the accepted supplemental full-text decisions. The canonical PDF and its supplements reflect this 46-study checkpoint. The active report-to-study map covers 46 unique reports and 46 unique studies.

| Criterion | Verdict | Verified evidence |
| --- | --- | --- |
| Current PRISMA reconciliation | PASS | 693 identified, 228 deduplicated away, 465 screened, 328 title/abstract exclusions, 137 sought, and 136 assessed. The assessed full texts comprise 87 exclusions, three awaiting classification and 46 included reports. The 46 reports represent 46 studies. Four reconciliation tests passed and all arithmetic differences equal zero. |
| Retrieval and unresolved cases | PASS | 44 original retrieved PDFs plus 92 newly recovered PDFs = 136 assessed reports. R0081 and R0082 await E7 resolution. R0132 awaits E2/E3 resolution. R0116 alone remains unretrieved. The Zenodo candidate contains a source-code ZIP and no article PDF. |
| Source verification | PASS | 47/47 source identities and source-bounded notice dispositions verified. The primary result failed, and its six supported rows were combined with 41/41 verified rows from the linked native correction. Raw receipts and matching chat cleanup were verified. |
| Registry and notice scope | PASS | Crossref returned all 46 recorded DOI works and 46 reverse update lookups. The dated checks found zero matching formal notices, including the exact DOI/title comparison against 74,131 Retraction Watch rows. R0113 matches the publisher and original PDF using title, authors, year and venue. Its incomplete DOI field leaves it at DOI_NOT_FOUND. Individual publisher notice coverage is non-exhaustive. |
| RQ1–RQ5 and quantitative integrity | PASS | Ten findings have 40 source traces and zero unsupported findings. The evidence retains 67 outcome measurements from 25 studies. Table 1 retains three within-study comparisons and conditions. R0092 Comm-Min is 64.4 ± 4.3% from Table V, physical p. 13. The scoped erratum corrects the prior transcription. |
| Data and appraisal | PASS | All 46 characteristics and report/study keys align. Records contain 460 engineering appraisal judgments across ten domains and 87 exclusions with one primary reason and decision locator each. Unverified, unreported and incommensurable outcomes remain explicit. |
| PRISMA 2020 reporting | PASS | All 27 numbered items have evidence or an explicit limitation, with physical final-PDF locators and 45 checked local links. The checklist records formal assessments that were not performed and disclosures pending author confirmation. |
| Springer Nature build | PASS | Tectonic 0.16.9 produced 13 pages, 47 resolved citation entries, 46 distinct outbound DOI URLs, zero unresolved citations or references, and zero overfull boxes. Underfull boxes and an included PDF version warning were observed. The included PRISMA figure renders legibly on physical p. 4. |
| Visual and rebuilt PDF | PASS | All 13 final rendered pages were inspected across steps 15–16. Twelve final renders match the inspected step 15 pages pixel for pixel. The final abstract page and PRISMA diagram were also inspected directly after the step 16 rebuild. An isolated extraction rebuild matches page text, page bounds and outbound DOI links on all 13 pages. |
| Handoff package | PASS | The ZIP includes compilable source, the final PDF, agreed derived data, PRISMA and audit, with per-member SHA-256 and ZIP CRC checks. The archive excludes restricted originals and raw research payloads. |
| Remaining confirmations | PASS | The limitations report preserves classification, retrieval, methodological and author/disclosure items. The workflow performed no journal submission or email. |

## Bibliographic exceptions

- R0006 keeps article-level pages 1–8 and the deposit's proceedings title. The primary audit flagged different numbering in the whole-conference table of contents. The exact-DOI Crossref work and original PDF identify the same report. [R0006 Crossref record](https://api.crossref.org/works/10.1109/icpads67057.2025.11322921)
- R0009 keeps the exact DOI deposit's last-author segmentation, Chee / Wei Tan, and January 2026 issue date. The PDF byline spells out Chee Wei Tan in the same sequence. [R0009 Crossref record](https://api.crossref.org/works/10.1109/tits.2025.3629117)
- R0058 cites the 2026 issue imprint and article 2644002 from original physical p. 1. The work was published online on 6 December 2025 according to the deposit and the PDF. [R0058 Crossref record](https://api.crossref.org/works/10.1142/s0218126626440020)
- R0113's article page and local physical PDF p. 1 agree on identity. The page's citation DOI field displays `10.64751/` without a suffix. The registry check retained `DOI_NOT_FOUND`. [R0113 publisher record](https://ajaccm.com/journal/index.php/ajaccm/article/view/771)

The applicable template and structured abstract were checked against the journal's author instructions. The finished abstract contains 174 words excluding labels. [SN Computer Science submission guidelines](https://link.springer.com/journal/42979/submission-guidelines), [Springer Nature LaTeX support](https://www.springernature.com/gp/authors/campaigns/latex-author-support)

The review uses a source-bounded notice check. A registry with no matching link cannot establish the absence of all possible notices. [Crossref Retraction Watch documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/), [Crossref Crossmark](https://www.crossref.org/crossmark/)

## Evidence

- [Final PDF and page verification](active_pdf_verification.json)
- [Final PRISMA checklist](../prisma/active_prisma_checklist.md) and [count ledger](../prisma/prisma_counts.json)
- [RQ1–RQ5 acceptance](../synthesis/active_rq_review.md) and [claim sources](../synthesis/active_claim_source_matrix.csv)
- [Independent registry evidence](active_independent_registry_evidence.json)
- [Primary native source audit](active_source_audit_primary_review.md) and [composite review](active_source_audit_composite_review.md)
- [Limitations and open confirmations](active_limitations.md)
