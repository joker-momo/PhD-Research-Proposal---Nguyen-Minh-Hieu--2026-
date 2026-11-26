# Final Planned Query Translations

**Version:** 1.2
**Adopted:** 2026-11-26 after S-01 query validation and Codex acceptance review
**Protocol alignment:** Amendments 001–004
**Execution status:** `UNEXECUTED` on all four core platforms
**Reported counts:** `COUNT_NOT_OBTAINED`

Every query requires at least one swarm-specific expression and an inference expression. Standalone `UAV` or `drone` is not sufficient. The complementary query adds DNN and partitioning/orchestration concepts. Eligibility is limited to English-language journal articles and full conference/proceedings papers published from 2021 through the final search date; the current execution window is 2021–2026.

## IEEE Xplore

Official syntax documentation: https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search

**Execution gate:** `BLOCKED_PENDING_AUTHENTICATED_UI_VERIFICATION`. Before either query is run, verify the exact Web Command Search behavior of the quoted `"All Metadata":` prefix, phrase quoting, wildcard limits, and the year, content-type, and English-language facets in the authenticated IEEE Xplore interface. The API documentation checked in S-01 does not establish those Web UI behaviors.

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

Planned interface filters, pending the same authenticated verification: year 2021–2026; content types `Journals` and `Conferences`; language `English`.

## ACM Digital Library

Official advanced search: https://dl.acm.org/search/advanced  
Official search guidance: https://libraries.acm.org/digital-library/search-and-browse

**Execution gate:** `BLOCKED_PENDING_AUTHENTICATED_UI_VERIFICATION`. Before either query is run, verify field/default-scope behavior, trailing wildcard support, the English-language facet, and the selected collection toggle in the authenticated ACM Digital Library interface.

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

Apply the date-published filter 2021–2026. Retain `Research Article` and `Short Paper` records for substantive eligibility screening; exclude `Demonstration`, `Extended abstract`, `Poster`, and `Work in Progress` records when those types do not provide the substantive method-and-results content required by Amendment 003. Record explicitly whether the run uses `Publications of the ACM and Affiliated Organizations` or `The ACM Guide to Computing Literature`; do not label either scope generically as `The ACM Digital Library` in the execution log.

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

Version 1.2 is prospective and has not been executed. IEEE and ACM runs remain prohibited until their authenticated-interface gates above are resolved and recorded. For each eventual run, record the exact pasted query, platform, collection, filters, local search date and time, reported result count, exported count, export format, raw file name, and any cap or failure. Do not replace an executed query silently; any change after the first formal run requires a dated protocol amendment and a rerun on every affected platform.

The seed matrix in `seed_query_coverage_matrix.csv` contains expected query sensitivity only. It is not evidence that any database search has been executed or that a seed record is indexed by a platform on the final search date.

