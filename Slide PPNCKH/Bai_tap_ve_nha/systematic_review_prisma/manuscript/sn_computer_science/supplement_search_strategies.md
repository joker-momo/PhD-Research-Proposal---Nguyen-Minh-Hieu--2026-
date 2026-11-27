# Supplement S1. Executed search strategies

These are the recorded selected runs for the restart. Search dates are 26 November 2026 in the recorded timezone. The timestamp basis is shown for each run. ACM Digital Library used manual capture. The unavailable Web of Science Core Collection is outside the executed set.

## 1. IEEE — high_recall

Recorded time: 2026-11-26T14:13:05+07:00. Local filesystem modification time of the completed export.
Selected rows: 42. Query version: 1.3.

Filters: `{"publication_year": "2021-2026", "content_type": ["Conferences", "Journals"], "language": "facet_not_available_screen_downstream"}`.

```text
("All Metadata":"UAV swarm" OR "All Metadata":"drone swarm" OR "All Metadata":"multi-UAV" OR "All Metadata":"multiple UAVs" OR "All Metadata":"aerial network" OR "All Metadata":FANET) AND ("All Metadata":"distributed inference" OR "All Metadata":"collaborative inference" OR "All Metadata":"cooperative inference" OR "All Metadata":"split inference" OR "All Metadata":"split computing" OR "All Metadata":"edge intelligence")
```

Run evidence: `sources/raw/core_searches/ieee_xplore_high_recall_authenticated_2026-11-26.json`.

## 2. IEEE — complementary

Recorded time: 2026-11-26T14:15:41+07:00. Local filesystem modification time of the completed export.
Selected rows: 21. Query version: 1.3.

Filters: `{"publication_year": "2021-2026", "content_type": ["Conferences", "Journals"], "language": "facet_not_available_screen_downstream"}`.

```text
("All Metadata":"UAV swarm" OR "All Metadata":"drone swarm" OR "All Metadata":"multi-UAV" OR "All Metadata":"multiple UAVs" OR "All Metadata":"aerial network" OR "All Metadata":FANET) AND (("All Metadata":"deep neural network" OR "All Metadata":DNN OR "All Metadata":"deep learning") AND "All Metadata":inference) AND ("All Metadata":partition* OR "All Metadata":offload* OR "All Metadata":placement OR "All Metadata":schedul* OR "All Metadata":assign* OR "All Metadata":"resource allocation")
```

Run evidence: `sources/raw/core_searches/ieee_xplore_complementary_authenticated_2026-11-26.json`.

## 3. SCOPUS — high_recall

Recorded time: 2026-11-26T14:08:35+07:00. Local filesystem modification time of the completed export.
Selected rows: 77. Query version: 1.3.

Filters: `{"publication_year": "2021-2026", "document_type": ["Article", "Conference paper"], "language": "English"}`.

```text
TITLE-ABS-KEY(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND ("distributed inference" OR "collaborative inference" OR "cooperative inference" OR "split inference" OR "split computing" OR "edge intelligence")) AND PUBYEAR AFT 2020 AND PUBYEAR BEF 2027 AND (DOCTYPE(ar) OR DOCTYPE(cp)) AND LANGUAGE(english)
```

Run evidence: `sources/raw/core_searches/scopus_high_recall_authenticated_2026-11-26.json`.

## 4. SCOPUS — complementary

Recorded time: 2026-11-26T14:09:24+07:00. Local filesystem modification time of the completed export.
Selected rows: 33. Query version: 1.3.

Filters: `{"publication_year": "2021-2026", "document_type": ["Article", "Conference paper"], "language": "English"}`.

```text
TITLE-ABS-KEY(("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND (("deep neural network" OR DNN OR "deep learning") AND inference) AND (partition* OR offload* OR placement OR schedul* OR assign* OR "resource allocation")) AND PUBYEAR AFT 2020 AND PUBYEAR BEF 2027 AND (DOCTYPE(ar) OR DOCTYPE(cp)) AND LANGUAGE(english)
```

Run evidence: `sources/raw/core_searches/scopus_complementary_authenticated_2026-11-26.json`.

## 5. OPENALEX — high_recall

Recorded time: 2026-11-26T14:54:14+07:00. As recorded in source evidence; not a new search
Selected rows: 85. Query version: 1.4-openalex-1.

Filters: `"from_publication_date:2021-01-01,to_publication_date:2026-11-26,language:en"`.

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND ("distributed inference" OR "collaborative inference" OR "cooperative inference" OR "split inference" OR "split computing" OR "edge intelligence")
```

Run evidence: `sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_manifest.json`.

## 6. OPENALEX — complementary

Recorded time: 2026-11-26T18:41:10+07:00. Timestamp recorded for the actual revised API execution.
Selected rows: 31. Query version: 1.4-openalex-2.

Filters: `"from_publication_date:2021-01-01,to_publication_date:2026-11-26,language:en"`.

```text
("UAV swarm" OR "UAV swarms" OR "drone swarm" OR "drone swarms" OR "multi-UAV" OR "multi-UAVs" OR "multi UAV" OR "multiple UAVs" OR "multiple UAV" OR "aerial network" OR "aerial networks" OR FANET OR FANETs) AND (("deep neural network" OR "deep neural networks" OR DNN OR DNNs OR "deep learning") AND inference) AND (partition* OR offload* OR placement OR schedul* OR assign* OR "resource allocation")
```

Run evidence: `sources/raw/core_searches/openalex_complementary_revision_2026-11-26/openalex_complementary_2026-11-26_manifest.json`.

## 7. ACM — high_recall

Recorded time: 2026-11-26T13:50:14+07:00. As recorded in source evidence; not a new search
Selected rows: 79. Query version: 1.3.

Filters: `{"search_within": "Anywhere", "e_publication_date": "2021-01-01 through 2026-11-30", "content_type": "broad_full_text_collection", "language": "facet_not_available"}`.

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND ("distributed inference" OR "collaborative inference" OR "cooperative inference" OR "split inference" OR "split computing" OR "edge intelligence")
```

Run evidence: `sources/raw/core_searches/acm_high_recall_2026-11-26.json`.

## 8. ACM — complementary

Recorded time: 2026-11-26T13:50:14+07:00. As recorded in source evidence; not a new search
Selected rows: 325. Query version: 1.3.

Filters: `{"search_within": "Anywhere", "e_publication_date": "2021-01-01 through 2026-11-30", "content_type": "broad_full_text_collection", "language": "facet_not_available"}`.

```text
("UAV swarm" OR "drone swarm" OR "multi-UAV" OR "multiple UAVs" OR "aerial network" OR FANET) AND (("deep neural network" OR DNN OR "deep learning") AND inference) AND (partition* OR offload* OR placement OR schedul* OR assign* OR "resource allocation")
```

Run evidence: `sources/raw/core_searches/acm_complementary_2026-11-26.json`.


## Restart changes before screening

| Stage | Change and reason | Evidence in the project |
|---|---|---|
| Step 02, protocol definition | The publication-type decision resolved an open criterion. The restart admits peer-reviewed journal or conference reports with full text, substantive methods and evaluated results. This excludes preprints from the primary synthesis. Short papers are judged by their methods and results. | `restart_2026_11_26/protocol_restart.md`, P03/E7 and `restart_2026_11_26/step02_user_decision.md` |
| Step 03, query audit | Seven selected runs were retained. The supplementary OpenAlex complementary run was revised to preserve the intended terms, wildcards, OR tail and filters. The revised export replaced the earlier snapshot before dataset lock. | `restart_2026_11_26/step03_query_audit_acceptance.md` and `restart_2026_11_26/search_log.md` |
