# Final Planned Query Translations

**Version:** 1.1  
**Locked:** 2026-11-24 after two Gemini research passes and Codex acceptance review  
**Protocol alignment:** Amendments 001 and 002  
**Execution status:** `UNEXECUTED` on all four core platforms  
**Reported counts:** `COUNT_NOT_OBTAINED`

Every query requires at least one swarm-specific expression and an inference expression. Standalone `UAV` or `drone` is not sufficient. The complementary query adds DNN and partitioning/orchestration concepts. Eligibility is limited to English-language journal articles and full conference/proceedings papers published from 2021 through the final search date; the current execution window is 2021–2026.

## IEEE Xplore

Official syntax documentation: https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search

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

Apply interface filters: year 2021–2026; content types `Journals` and `Conferences`; language `English`.

## ACM Digital Library

Official advanced search: https://dl.acm.org/search/advanced  
Official search guidance: https://libraries.acm.org/digital-library/search-and-browse

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

Apply interface filters: date published 2021–2026; content types `Research-Article` and `Conference-Paper`; search scope `The ACM Digital Library`. Do not include `Short-Paper`.

## Scopus

Official syntax documentation: https://service.elsevier.com/app/answers/detail/a_id/11236/supporthub/scopus/

### High-recall query

```text
TITLE-ABS-KEY(
  ("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
   OR "aerial network" OR FANET)
  AND
  ("distributed inference" OR "collaborative inference" OR "cooperative inference"
   OR "split inference" OR "split computing" OR "edge intelligence")
)
AND PUBYEAR > 2020 AND PUBYEAR < 2027
AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Complementary query

```text
TITLE-ABS-KEY(
  ("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
   OR "aerial network" OR FANET)
  AND (("deep neural network" OR DNN OR "deep learning") AND inference)
  AND (partition* OR offload* OR placement OR schedul* OR assign*
       OR "resource allocation")
)
AND PUBYEAR > 2020 AND PUBYEAR < 2027
AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

Apply the English-language refinement. The document-type expression must remain `(DOCTYPE(ar) OR DOCTYPE(cp))`, not `DOCTYPE(ar OR cp)`.

## Web of Science Core Collection

Official syntax documentation: https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html

### High-recall query

```text
TS=(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
     OR "aerial network" OR FANET)
    AND
    ("distributed inference" OR "collaborative inference" OR "cooperative inference"
     OR "split inference" OR "split computing" OR "edge intelligence"))
```

### Complementary query

```text
TS=(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs"
     OR "aerial network" OR FANET)
    AND (("deep neural network" OR DNN OR "deep learning") AND inference)
    AND (partition* OR offload* OR placement OR schedul* OR assign*
         OR "resource allocation"))
```

Apply interface refinements: publication years 2021–2026; document types `Article` and `Proceedings Paper`; language `English`; collection `Web of Science Core Collection`.

## Execution rule

For each of the eight runs, record the exact pasted query, platform, collection, filters, local search date and time, reported result count, exported count, export format, raw file name, and any cap or failure. Do not replace an executed query silently; any change after the first formal run requires a dated protocol amendment and a rerun on every affected platform.

The seed matrix in `seed_query_coverage_matrix.csv` contains expected query sensitivity only. It is not evidence that any database search has been executed or that a seed record is indexed by a platform on the final search date.

