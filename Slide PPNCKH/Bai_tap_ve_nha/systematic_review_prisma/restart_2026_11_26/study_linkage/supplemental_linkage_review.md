# HK261 supplemental study linkage · Accepted

**46 eligible reports map to 46 distinct study IDs** under P07 at this checkpoint. The map preserves all 25 accepted report assignments and adds 21 IDs. Three pending reports and R0116 are outside this map.

[Active report–study map](active_report_study_map.csv) · [Two-sided candidate evidence](active_pair_evidence.csv) · [Accepted baseline linkage review](step10_linkage_summary.md)

## Candidate coverage

The initial 25 reports had 300 possible pairs and 13 full-text comparisons. The 21 added reports introduce 735 new pairs, for 1,035 possible pairs overall. An independent screen compared normalized DOI and title, surname plus given initial, title string similarity (threshold 0.70), and occurrences of the other report's title or DOI in the original PDFs. The title normalization strips punctuation and diacritics. The screen found 35 alerts. Eleven were included among the 15 supplemental full-text comparisons. For the other 24, 16 single-initial matches resolved to different full names and eight titles occurred as ordinary bibliographic references, without an identity-level signal. Four topic-based priority pairs warranted comparison even without an automated alert. The final two-sided ledger covers 28 pairs. It records 28 DISTINCT decisions, zero merges, and zero unresolved pairs. The count is bounded by the available included reports and linkage signals.

R0014 and R0062 share multiple authors and embedded hardware categories. The evaluated arrangements and purposes differ. ASAP describes indoor embedded and outdoor UAV evaluations (R0014 physical p. 10, Fig. 12 and §VIII.A). The eCoEI paper describes a separate four-UAV continuity experiment (R0062 physical pp. 5–6, Experiment Setup and results). R0110 cites R0074 and uses an Orion-derived comparator (R0110 pp. 10 and 16). R0074 reports its original Orion evaluation (§4.1, pp. 14–15). These relationships do not establish the same investigation.

R0058's p. 1 DOI and visual imprint confirm the PDF identity. Its first-publication date in the original differs from the printed 2026 imprint. R0077's p. 1 identifies arXiv:2503.16146v3 and the accepted-manuscript version, with the journal DOI checked separately. For R0292, the PDF uses *Tracking* and the publisher deposit uses *Monitoring*. Both use the same DOI and ordered byline. R0036 and R0048 use matching author initials for Wen Wu and Wenbo Wu respectively, as printed on p. 1. Their distinct methods and evaluations support the pair decision. [R0077 journal deposit](https://api.crossref.org/works/10.1016/j.sysarc.2026.103804) · [R0292 proceedings deposit](https://api.crossref.org/works/10.1145/3711875.3737661)

## Composite acceptance

| Criterion | Verdict | Evidence |
|---|---|---|
| Exact report coverage and identity | PASS | 46/46 eligible IDs mapped, including 21 added PDF identities verified on physical p. 1. No duplicate normalized title or DOI. R0113 has an explicit DOI_NOT_FOUND marker and an inspected title and byline. Original SHA-256 values matched. |
| Pair coverage and source support | PASS | All 11 original priority pairs, three additional provider candidates, and one supplemental planning pair checked. Each of the 15 supplemental comparisons has two exact original-page anchors and a source-bounded design comparison. The 13 prior comparisons are carried with their original evidence. |
| Merge or unresolved evidence | PASS | Zero merges, zero unresolved candidate pairs, 28 distinct decisions. No operational or performance measurement needed for a linkage decision. |
| Locator-only correction | PASS | One parseable object, all five expected keys, all seven original-PDF excerpts match. Three version/identity distinctions retained. Pair conclusions agree with independent review. No outcome measurements accepted. |
| Approved native route and cleanup | PASS | Three native tasks, one dispatch each. All three completed payloads were saved. The bridge verified the matching chat cleanup for all three. Earlier malformed or unsupported fields are quarantined. |

The [primary review](supplemental_linkage_primary_review.md) and [first targeted correction review](supplemental_linkage_correction_review.md) record the rejected fields. The final [locator repair receipt](supplemental_linkage_locator_repair_receipt.json) carries task UUID `491e8b9a-861c-4575-84d1-ce6bfdf60e37`.
