# Final Planned Query Translations

**Version:** 1.3
**Adopted:** 2026-11-26 after S-01 validation and direct IEEE/ACM interface verification
**Protocol alignment:** Amendments 001–005
**Execution status:** 6/8 query variants executed on three core platforms; Web of Science Core Collection remains unavailable
**Reported counts:** IEEE Xplore 42/21 after required content-type filtering; ACM Digital Library 79/325 broad Full-Text results; Scopus 77/33; Web of Science `COUNT_NOT_OBTAINED`

Every query requires at least one swarm-specific expression and an inference expression. Standalone `UAV` or `drone` is not sufficient. The complementary query adds DNN and partitioning/orchestration concepts. Eligibility is limited to English-language journal articles and full conference/proceedings papers published from 2021 through the final search date; the current execution window is 2021–2026.

## IEEE Xplore

Official syntax documentation: https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search

**Execution gate:** `READY_FOR_S02_WITH_RESULTS_PAGE_FACET_CHECK`. Official help and the live Command Search interface verified the quoted `"All Metadata":` field syntax, exact phrases, Boolean grouping, the 25-term-per-clause ceiling, the 10-wildcard ceiling, and the three-character wildcard minimum. The complementary query uses four valid trailing wildcards. Results-page year, content-type and language facets must still be recorded during S-02.

### High-recall query

```text
("All Metadata":"UAV swarm" OR "All Metadata":"drone swarm"
 OR "All Metadata":"multi-UAV" OR "All Metadata":"multiple UAVs"
 OR "All Metadata":"aerial network" OR "All Metadata":FANET)
AND
("All Metadata":"distributed inference" OR "All Metadata":"collaborative inference"
 OR "All Metadata":"cooperative inference" OR "All Metadata":"split inference"
 OR "All Metadata":"split computing" OR "All Metadata":"edge intelligence")
```

### Complementary query

```text
("All Metadata":"UAV swarm" OR "All Metadata":"drone swarm"
 OR "All Metadata":"multi-UAV" OR "All Metadata":"multiple UAVs"
 OR "All Metadata":"aerial network" OR "All Metadata":FANET)
AND
(("All Metadata":"deep neural network" OR "All Metadata":DNN
  OR "All Metadata":"deep learning")
 AND "All Metadata":inference)
AND
("All Metadata":partition* OR "All Metadata":offload*
 OR "All Metadata":placement OR "All Metadata":schedul*
 OR "All Metadata":assign* OR "All Metadata":"resource allocation")
```

Planned result-page filters: year 2021–2026; content types `Journals` and `Conferences`; language `English`. If any facet is absent, export the broader permitted set, log the absent facet, and apply the corresponding eligibility rule during screening; do not infer a filtered count.

## ACM Digital Library

Official advanced search: https://dl.acm.org/search/advanced  
Official search guidance: https://libraries.acm.org/digital-library/search-and-browse

**Execution gate:** `READY_FOR_S03_WITH_LOGIN_EXPORT_CHECK`. The live Advanced Search page verified Boolean operators, exact phrases, trailing wildcards outside quoted phrases, `Search Within = Anywhere`, custom publication dates, and both collection labels. The observed session was Basic Edition, so sign-in/export capability and any results-page language/type facets must be recorded during S-03.

### High-recall query

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
 OR "aerial network" OR FANET)
AND
("distributed inference" OR "collaborative inference" OR "cooperative inference"
 OR "split inference" OR "split computing" OR "edge intelligence")
```

### Complementary query

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
 OR "aerial network" OR FANET)
AND
(("deep neural network" OR DNN OR "deep learning") AND inference)
AND
(partition* OR offload* OR placement OR schedul* OR assign*
 OR "resource allocation")
```

Use `The ACM Full-Text collection`, `Search Within = Anywhere`, and a custom date range from January 2021 through the month containing the search date. If the interface cannot express the exact search-day boundary, enforce it during screening. Retain `Research Article` and `Short Paper` records for substantive eligibility screening; exclude `Demonstration`, `Extended abstract`, `Poster`, and `Work in Progress` records when those types do not provide the substantive method-and-results content required by Amendment 003. If language or publication-type facets are absent, export the broader permitted set and enforce those criteria during screening. Any separate use of `The ACM Guide to Computing Literature` is supplementary and must be logged separately.

## Scopus

Official syntax documentation: https://service.elsevier.com/app/answers/detail/a_id/11236/supporthub/scopus/

### High-recall query

```text
TITLE-ABS-KEY(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND ("distributed inference" OR "collaborative inference" OR "cooperative inference" OR "split inference" OR "split computing" OR "edge intelligence")) AND PUBYEAR AFT 2020 AND PUBYEAR BEF 2027 AND (DOCTYPE(ar) OR DOCTYPE(cp)) AND LANGUAGE(english)
```

### Complementary query

```text
TITLE-ABS-KEY(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND (("deep neural network" OR DNN OR "deep learning") AND inference) AND (partition* OR offload* OR placement OR schedul* OR assign* OR "resource allocation")) AND PUBYEAR AFT 2020 AND PUBYEAR BEF 2027 AND (DOCTYPE(ar) OR DOCTYPE(cp)) AND LANGUAGE(english)
```

The English restriction is embedded in both queries. The document-type expression must remain `(DOCTYPE(ar) OR DOCTYPE(cp))`, not `DOCTYPE(ar OR cp)`. No separate Scopus sub-collection selector is required for this search scope.

## Web of Science Core Collection

Official syntax documentation: https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html

### High-recall query

```text
TS=(("UAV swarm" OR "UAV swarms" OR "drone swarm" OR "drone swarms" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR "aerial networks" OR FANET) AND ("distributed inference" OR "collaborative inference" OR "cooperative inference" OR "split inference" OR "split computing" OR "edge intelligence")) AND (PY=(2021-2025) OR PY=2026)
```

### Complementary query

```text
TS=(("UAV swarm" OR "UAV swarms" OR "drone swarm" OR "drone swarms" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR "aerial networks" OR FANET) AND (("deep neural network" OR "deep neural networks" OR DNN OR "deep learning") AND inference) AND (partition* OR offload* OR placement OR schedul* OR assign* OR "resource allocation")) AND (PY=(2021-2025) OR PY=2026)
```

Apply interface refinements: document types `Article` and `Proceedings Paper`; language `English`; collection `Web of Science Core Collection`. Record every active Core Collection edition, including whether `CPCI-S` is enabled, because edition coverage affects proceedings retrieval. The provisional 2021–2026 range is embedded in each query; do not add a conflicting year refinement.

## Execution rule

Version 1.3 has been executed for IEEE Xplore, ACM Digital Library, and Scopus. IEEE Xplore and Scopus produced four importable CSV exports; ACM returned two visible totals but Basic Edition did not provide record-level export; Web of Science personal sign-in exposed only Free View and did not permit either Core Collection query. The append-only ledger and raw records retain exact queries, filters, timestamps, totals, export formats, checksums, and blockers. A missing facet triggers broader export plus downstream screening, not an inferred count. Do not replace an executed query silently; any change after the first formal run requires a dated protocol amendment and a rerun on every affected platform.

The seed matrix in `seed_query_coverage_matrix.csv` contains expected query sensitivity only. It is not evidence that any database search has been executed or that a seed record is indexed by a platform on the final search date.

