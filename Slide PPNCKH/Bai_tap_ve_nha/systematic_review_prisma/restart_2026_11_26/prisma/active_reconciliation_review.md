# HK261 · Active PRISMA reconciliation

The active checkpoint covers the accepted 26 November 2026 restart and its supplemental full-text recovery. Search runs, deduplication and title/abstract decisions carry forward from the baseline. The earlier reconciliation and checklist describe the 25-study manuscript revision. The 46-study working checklist records the evidence locators and reporting gaps. The previous selection counts and Figure 1 were checked on manuscript PDF page 6. This reconciliation projects current eligibility from S2 after validating the locked 46-report source corpus.

| Gate | Verdict | Evidence |
| --- | --- | --- |
| Record arithmetic | PASS | 693 identified − 228 duplicates = 465 screened. 465 screened − 328 excluded = 137 reports sought. |
| Retrieval and original identity | PASS | 92 of the 93 missing reports were recovered. Together with 44 prior PDFs, this gives 136 assessed reports. The intake and screening ledgers agree for all 92 supplemental IDs. All 136 report paths and original SHA-256 digests match the evidence catalog and local PDFs. |
| Eligibility and primary reasons | PASS | 136 assessed = 90 excluded + 0 awaiting classification + 46 included reports. All exclusion IDs have one primary code. E1 12, E2 29, E3 41, E4 1, E6 1 and E7 6. The author confirmed R0081 (E7), R0113 (E3) and R0132 (E3) on 27 November 2026. |
| Unresolved states | PASS | There are no reports awaiting classification. The author confirmed both the linked IEEE publication for R0082 and the ACM proceedings article R0292. R0292 has official DroNet programme and peer-review-policy evidence. The retained PDF is arXiv v1 and publisher-page comparison is unavailable locally. R0116 alone remains not retrieved. The intake record describes the Zenodo candidate as a source-code ZIP with no report PDF. |
| Linkage, extraction and appraisal | PASS | The locked P08/P09 source maps cover the previous 46 studies. The current eligibility ledger projects 45 one-report studies from that map and assigns R0082 a separate study ID, S047, based on its distinct DOI and title in the deduplication map. Reconciliation of downstream extraction, appraisal and synthesis is a separate checkpoint. |
| Reproducibility | PASS | Four focused tests passed. All four arithmetic differences are zero. The generated counts and LaTeX source reproduce byte for byte. The one-page compiled flow was inspected for labels, arrows and legibility. |
| Working checklist | PASS | 27/27 numbered items have a status, verified evidence locator and stated limitation. Checked 46 local evidence links and all named LaTeX labels. Item 16 was checked against the previous manuscript PDF page 6 and now points separately to current counts. |

- [Working checklist for 46 studies](active_prisma_checklist.md)
- [Count ledger by ID](prisma_counts.json)
- [PRISMA 2020 flow diagram](prisma_flow.pdf)
- [Supplemental screening and R0116 provenance](../supplemental_screening/manifest.json)
- [Active report-to-study map](../study_linkage/active_report_study_map.csv)
- [P08 extraction lock](../extraction/active_p08_extraction_lock.json)
- [P09 appraisal lock](../appraisal/active_p09_appraisal_lock.json)
