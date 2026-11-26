## TASK
Correct the rejected dates_02 retry evidence for exactly C05, C09, C10, C13, C14 and C19 using fresh direct source observations. Parent fallback task: 01a215dc-cc27-73fb-8933-0a471cf3ac32; rejected D2/D3/D4. Return evidence only, never final prose.

## REQUIRED WORK
1. Preserve the six supplied scholarly identities exactly. Discard the rejected retry's alleged fresh access timestamps and unsupported aggregator dates. Do not recycle those assertions. The prior accepted identity source below remains historical evidence, not a new remote observation.
2. Use code/available read-only tools to attempt exactly two direct public URLs per record: https://api.crossref.org/works/<doi> and the supplied IEEE article URL. Make at most one request to each URL, a 25-second timeout, no repeated challenge requests, no cookies/credentials, no hidden endpoints or downloads. Sequential requests are sufficient. A documented unavailable tool/network route is a shortfall, not a fabricated request. No open-ended search is requested.
3. Capture started_at immediately before each fetch and completed_at immediately after it from the runtime clock, in RFC3339 with seconds and timezone; capture requested URL, final URL if observed, actual HTTP status if exposed, and tool/network exception if present. Never copy an old timestamp or guess wall time. If a tool exposes neither a clock nor a status, put null and an explicit limitation. Do not manufacture HTTP 200/202. A truthful unavailable-route audit can pass even if all six gates remain UNCERTAIN.
4. Return the actual Crossref response message.DOI, message.title, message.author, message.container-title and all present date fields published, published-online, published-print, issued, created, deposited, indexed, accepted. Missing fields are absent, not negative evidence. Preserve date-parts arrays unchanged. published=[[2026]] is PUBLICATION evidence of YEAR precision; it is not a non-publication date. Label created/deposited/indexed administrative, accepted acceptance, without substituting them for publication. For publisher HTML return only directly readable identity and explicitly labelled publication field/value, or a short access-block description. Remote textual quotes at most25 words total per original URL; structured metadata fields may be returned as data.
5. For inclusive window2021-01-01..2026-11-25, classify each record YES only if authoritative publication evidence establishes eligibility, NO only if authoritative earliest-publication evidence establishes ineligibility, otherwise UNCERTAIN. Year-only2026 spans the cutoff and therefore remains UNCERTAIN. Do not infer publication from DOI sequence, download stamps, copyright, acceptance, admin dates or search snippets. Record an exact URL and field for remaining manual checks. No scope/family/appraisal reassessment.
6. Return the complete six-record replacement JSON with structured fetch trace. All factual claims must cite source IDs or supplied-file locators. Explicitly state that quoted/parsed observations came from this task's tools; when no tool was available, report that limitation instead. Missing evidence is acceptable; fabricated evidence is not.

## REQUIRED OUTPUT
One JSON object, no fences:
{"task":"dates_02_evidence_correction","parent_task_id":"01a215dc-cc27-73fb-8933-0a471cf3ac32","window":{"start":"2021-01-01","end":"2026-11-25"},"records":[{"id":string,"title":string,"authors":array,"year":integer,"venue":string,"doi":string,"date_gate":"YES|NO|UNCERTAIN","publication_dates":[{"value":string,"precision":"day|month|year","kind":string,"source_id":string,"field_or_locator":string}],"rationale":string,"source_ids":array,"attempt_ids":array,"unresolved":array,"manual_action":{"url":string,"field":string,"action":string}|null}],"attempts":[{"attempt_id":string,"record_id":string,"route":"crossref|publisher","requested_url":string,"final_url":string|null,"started_at":RFC3339|null,"completed_at":RFC3339|null,"http_status":integer|null,"outcome":"readable|access_blocked|network_error|tool_unavailable","tool":string,"error_or_limitation":string|null,"source_ids":array}],"sources":[{"source_id":string,"record_id":string,"url_or_file":string,"attempt_id":string|null,"provenance":"fresh_remote|accepted_prior_local","evidence_kind":"publication|administrative|acceptance|identity|access_failure","field_or_locator":string,"observed_value":any}],"shortfall":array,"unresolved":array,"project_files_changed":0,"final_prose_written":false}
Exactly6 records ordered C05,C09,C10,C13,C14,C19; exactly12 attempt records (each actual request or explicit tool_unavailable). Return identity/date metadata as separate sources if they have different evidence_kind. Prior accepted local source must identify its record/field and have no fake attempt_id. Fields unavailable in a source must not be asserted as read.

## ACCEPTANCE CRITERIA
D1: Exactly6 identities match input; DOI/title duplicates0; all required record fields present, all source/attempt IDs unique and references resolve, no dropped record.
D2: Exactly12 attempt records,2 per ID,1 per route; each has exact requested URL, an observed outcome or documented tool shortfall. All factual claims have source URL/file locator and source ID; fresh sources link to a real attempt. Unsupported quantitative claims0, invented aggregator claims0, remote textual quotation<=25 words per URL. All6 unresolved/manual-action fields present.
D3: Publication/date kinds and precision correct; year-only published evidence labelled publication; administrative/acceptance/download substitutions0; padded day/month0; fixed cutoff unchanged; all6 decisions justified and uncertainty retained where warranted.
D4: Every actual fetch has runtime-captured start/end times, start<=end within this task's execution interval, or explicit unavailable-clock shortfall with null values; fabricated timestamps/statuses/access0. No claim of a fresh fetch without a corresponding actual tool observation. Partial observations remain labelled partial. An honest unavailable-tool record is acceptable evidence of a blocked route, not successful verification.
D5: project_files_changed0; final_prose_writtenfalse; other gates/identities/protocol unchanged; credentials/bypass/submission/messages/downloads/writes0; shortfall and unresolved arrays present. No scientific adoption before Codex's review.

## BOUNDARIES
Read-only research. Codex owns all files, final writing and acceptance. Fixed cutoff2026-11-25. Do not force a positive date result. Do not access unrelated private files, send private data, modify any file, or use paid/authenticated services. Only the two direct routes per record are requested; no aggregator/search-date claims. Tool failures must be reported, not concealed. The rejected parent remains quarantined.
Canonical accepted identities (historical evidence): /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reconciliation/results/identity_dates_01_accepted.json
Exact publisher URLs:
C05 https://ieeexplore.ieee.org/document/11745919/
C09 https://ieeexplore.ieee.org/document/11804345/
C10 https://ieeexplore.ieee.org/document/11719586/
C13 https://ieeexplore.ieee.org/document/11804735/
C14 https://ieeexplore.ieee.org/document/11753908/
C19 https://ieeexplore.ieee.org/document/11803260/
Input identities:
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
    "doi": "10.1109/tcsvt.2026.3745821"
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
    "doi": "10.1109/jiot.2026.3755315"
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
    "doi": "10.1109/jiot.2026.3740035"
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
    "doi": "10.1109/tvt.2026.3755123"
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
    "doi": "10.1109/jiot.2026.3746980"
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
    "doi": "10.1109/jiot.2026.3755176"
  }
]
