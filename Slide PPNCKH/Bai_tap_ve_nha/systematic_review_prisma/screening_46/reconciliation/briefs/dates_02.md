## TASK
Verify publication-date eligibility for exactly C05,C09,C10,C13,C14,C19. All currently have year-only2026 dates and UNCERTAIN date gates. Find authoritative publication-date evidence or document the remaining access/evidence gap; do not change scope or identities.

## REQUIRED WORK
1. Read the six accepted identity/date records and previous attempts below. Crossref originally supplied year-only dates and IEEE Xplore returned WAF HTTP202. Do not present these old attempts as new work.
2. For each ID make at most5 new targeted public-source attempts: publisher article metadata/official citation export, DOI-deposited publication fields, official journal issue records, or author/institutional repository records. Try at least2 distinct relevant source routes unless a verified publisher publication date resolves the record earlier. Use search only to locate sources; snippets/aggregator dates are discovery leads, not sufficient eligibility evidence. Record actual URL, response/access outcome and RFC3339 accessed_at. No login/challenge bypass or hidden endpoints; stop repeated identical WAF calls.
3. Identify the date label exactly: online publication/early-access publication, issue publication, acceptance, received, copyright, deposit/created/indexed, download, PDF creation, repository deposit. Only explicitly labeled publication evidence can resolve the date gate. Preserve date precision (day/month/year); do not convert YYYY to January1. Earliest verified publisher online-publication may establish eligibility even when a later issue date exists; record both and explain. Do not substitute administrative/download timestamps or infer date from DOI sequence.
4. Compare supported publication date/interval with inclusive2021-01-01..2026-11-25. Return YES only when verified publication evidence wholly establishes the within-window condition; NO only if authoritative earliest-publication evidence establishes outside-window; otherwise UNCERTAIN. A failed fetch does not prove absence. Preserve all other accepted gates and source-version limitations. No new study-family/quality/scope claim.
5. Return structured evidence with exact short excerpt <=25 words per remote source or exact metadata field/value. Each date assertion and eligibility rationale must reference a source ID. If authentication/manual browsing is needed, provide the exact URL, field label and smallest user action required, without asking for credentials. Do not write/save project or downloaded files; Codex will capture accepted sources.

## REQUIRED OUTPUT
One JSON object, no fences:
{"task":"dates_02","window":{"start":"2021-01-01","end":"2026-11-25"},"records":[{"id":string,"title":string,"authors":array,"year":integer,"venue":string,"doi":string,"prior_date_gate":"UNCERTAIN","date_gate":"YES|NO|UNCERTAIN","publication_dates":[{"value":string,"precision":"day|month|year","kind":string,"source_id":string,"field_or_locator":string}],"rationale":string,"source_ids":array,"attempts":[{"url":string,"accessed_at":RFC3339,"outcome":string,"source_class":string}],"unresolved":array,"manual_action":string|null}],"sources":[{"source_id":string,"record_id":string,"url_or_file":string,"source_class":string,"accessed_at":RFC3339,"field_or_locator":string,"excerpt_or_value":string,"evidence_kind":"publication|non_publication|access_failure"}],"shortfall":[],"project_files_changed":0,"final_prose_written":false}
Exactly6 records in requested order, even when evidence is inaccessible. For unresolved gates publication_dates may be empty; do not insert guessed dates. Sources must distinguish accepted prior local evidence from newly accessed remote evidence.

## ACCEPTANCE CRITERIA
D1: Exactly6 IDs in order, all identity fields equal supplied accepted records, DOI/title duplicates0. Each includes date_gate,attempts,unresolved,manual_action. No report silently dropped.
D2: Every factual/date assertion has a resolvable source ID and URL/file locator; all source IDs unique; each remote excerpt <=25 words; metadata values exact; unsupported quantitative claims0. At least1 source per record (prior local evidence permitted if labelled); new attempt count1–5 per record with early stop only on verified publisher success, otherwise at least2 distinct routes or documented access shortfall.
D3: Date kinds/precision correct;0 administrative/download/acceptance dates used as publication;0 padded day/month;0 snippet-only positive decisions; all6 cutoff decisions follow fixed window and preserve uncertainty.
D4: Every new attempt has actual RFC3339 timestamp with timezone and outcome; no fabricated fetches, HTTP statuses or successful access. All6 unresolved arrays present; access blockers have actionable exact URL/field description.
D5: 0 other-gate/identity/protocol/corpus edits, project_files_changed0, final_prose_writtenfalse, shortfall explicit. No file downloads/writes, credentials, unauthorized access, submission or messages. Transport completion remains unreviewed until Codex independently checks D1–D5.

## BOUNDARIES
Research/source verification only. Codex owns all final prose, project mutations, source snapshots and acceptance. Use only lawful public access; no challenge bypass. Prefer official primary sources. Do not fill research gaps by guessing. Missing publication date is uncertainty, not exclusion. Fixed cutoff2026-11-25; do not silently move it to current date. No secrets or personal account data.
Accepted prior evidence: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reconciliation/results/identity_dates_01_accepted.json
Prior source snapshots/review: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reconciliation/reviews/identity_dates_01_correction_review.md
Canonical local full texts: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/<ID>.txt
Input records and historical attempts:
[
  {
    "id": "C05",
    "title": "MARL-based Reliability-aware Video Analytics in Multi-UAV-Assisted MEC Systems",
    "authors": [
      "Hao Hao",
      "Changqiao Xu",
      "Wei Zhang",
      "Shujie Yang",
      "Xiaolong Wang",
      "Huiling Shi",
      "Gabriel-Miro Muntean"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Circuits and Systems for Video Technology",
    "doi": "10.1109/tcsvt.2026.3745821",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/TCSVT.2026.3745821",
        "accessed_at": "2026-11-26T06:55:38+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-10-23T19:14:19Z."
      },
      {
        "url": "https://doi.org/10.1109/TCSVT.2026.3745821",
        "accessed_at": "2026-11-26T06:55:39+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11745919/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  },
  {
    "id": "C09",
    "title": "NetMoE: Joint Trajectory Planning and Distributed Mixture-of-Experts Inference for UAV Swarms",
    "authors": [
      "HyungBin Park",
      "SuKyoung Lee"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3755315",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/JIOT.2026.3755315",
        "accessed_at": "2026-11-26T06:55:39+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-11-18T20:05:10Z."
      },
      {
        "url": "https://doi.org/10.1109/JIOT.2026.3755315",
        "accessed_at": "2026-11-26T06:55:40+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11804345/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  },
  {
    "id": "C10",
    "title": "A DRL-Assisted Decentralized Framework for UAV Swarm Collaborative Inference",
    "authors": [
      "Songwei Li",
      "Zhihan Wang",
      "Jiebei Shi",
      "Jiwei Huang"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3740035",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/JIOT.2026.3740035",
        "accessed_at": "2026-11-26T06:55:40+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-10-06T19:10:19Z."
      },
      {
        "url": "https://doi.org/10.1109/JIOT.2026.3740035",
        "accessed_at": "2026-11-26T06:55:41+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11719586/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  },
  {
    "id": "C13",
    "title": "RDI-LLM: A Resilient Distributed Inference Framework for LLMs in Resource-Constrained UAV Swarm",
    "authors": [
      "Shengjie Zhong",
      "Zhongliang Zhao",
      "Jingxuan Chen",
      "Xianbin Cao",
      "Zhiyi Liu",
      "Dapeng O. Wu",
      "Tony Q. S. Quek"
    ],
    "year": 2026,
    "venue": "IEEE Transactions on Vehicular Technology",
    "doi": "10.1109/tvt.2026.3755123",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/TVT.2026.3755123",
        "accessed_at": "2026-11-26T06:55:41+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-11-18T20:08:05Z."
      },
      {
        "url": "https://doi.org/10.1109/TVT.2026.3755123",
        "accessed_at": "2026-11-26T06:55:42+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11804735/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  },
  {
    "id": "C14",
    "title": "CIDER: Collaborative Inference with Distilled Early-Exit Routing for Multi-UAV Edge Networks",
    "authors": [
      "Lianming Xu",
      "Yixue Liang",
      "Lei Jin",
      "Li Wang",
      "Ying-Jun Angela Zhang",
      "Xiaoyu Zhao",
      "Aiguo Fei"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3746980",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/JIOT.2026.3746980",
        "accessed_at": "2026-11-26T06:55:42+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-10-26T19:34:17Z."
      },
      {
        "url": "https://doi.org/10.1109/JIOT.2026.3746980",
        "accessed_at": "2026-11-26T06:55:43+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11753908/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  },
  {
    "id": "C19",
    "title": "PUF-enabled Self-Certified Authentication Protocol for Secure Cooperative Inference in UAV-Assisted Internet of Vehicles Environments",
    "authors": [
      "DeokKyu Kwon",
      "Ashok Kumar Das",
      "Youngho Park"
    ],
    "year": 2026,
    "venue": "IEEE Internet of Things Journal",
    "doi": "10.1109/jiot.2026.3755176",
    "prior_attempts": [
      {
        "url": "https://api.crossref.org/works/10.1109/JIOT.2026.3755176",
        "accessed_at": "2026-11-26T06:55:43+07:00",
        "outcome": "HTTP 200 OK",
        "observed_detail": "Crossref JSON returned type=journal-article, published=[[2026]], created=2026-11-17T20:17:25Z."
      },
      {
        "url": "https://doi.org/10.1109/JIOT.2026.3755176",
        "accessed_at": "2026-11-26T06:55:44+07:00",
        "outcome": "HTTP 202 (inaccessible: AWS WAF JavaScript challenge)",
        "observed_detail": "Resolved to https://ieeexplore.ieee.org/document/11803260/ with AwsWafIntegration bot verification page; IEEE Xplore article metadata and online publication day could not be read."
      }
    ]
  }
]
