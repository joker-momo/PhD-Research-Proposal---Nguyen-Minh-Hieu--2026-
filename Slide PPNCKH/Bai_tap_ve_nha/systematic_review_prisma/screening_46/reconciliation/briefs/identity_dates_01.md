# TASK
Resolve bibliographic identity, publication-date eligibility and source-version linkage for exactly ten reports: S19,S20,C03,C05,C09,C10,C13,C14,C19,C08. Return structured research evidence only. This does not request technical re-screening, final manuscript prose or file edits.

# REQUIRED WORK
1. Read the supplied accepted records and first-page/metadata portions of the ten local full texts. Preserve title/author discrepancies explicitly.
2. For each DOI-bearing record, inspect its official publisher/DOI record and Crossref works metadata. Report both attempts, actual access time and access outcome; if inaccessible do not pretend it was read. Supplementary discovery indexes may locate primary sources but cannot independently prove publication dates. For C08 inspect arXiv:2412.20860 version history/journal reference and verify candidate DOI 10.1016/j.future.2025.107874 against publisher/Crossref metadata.
3. Distinguish published-online, published-print/issue, conference publication, preprint version, accepted, received, Crossref created/deposited/indexed and file-download dates. Only publication or explicitly labelled preprint release evidence can resolve the relevant date. Keep partial dates at their true precision; do not invent a day. A 2026-only date straddles the fixed cutoff; a verified earlier month can resolve the interval. Current task access date does not move the cutoff 2026-11-25.
4. For each record return a source-bounded date-window verdict YES/NO/UNCERTAIN with exact evidence. For C08 additionally assess whether the supplied preprint is linked to the journal report using title, authors and explicit DOI/journal-reference evidence; separate identity linkage from full-text/numerical equivalence. If unique-recent-preprint eligibility is not established, state unresolved rather than assuming it.
5. Return bibliographic discrepancies, limitations and next evidence needed. No scientific study-family, extraction, integrity or scope decisions beyond these identity/date questions. Do not infer peer review from an acceptance banner or DOI existence alone; source the publication type.

# REQUIRED OUTPUT
One JSON object (no Markdown fences), with these fields:
- task: "identity_dates_01"
- window: {from:"2021-01-01",through:"2026-11-25"}
- records: exactly ten objects in requested order. Each object must have:
  id; title; authors (full ordered array); year (integer or null with unresolved reason); venue; doi (normalized string or DOI_NOT_FOUND); source_version; publication_type; identity_sources (array of source IDs); discrepancies (array); attempts (array of {url,accessed_at,outcome,observed_detail}); date_evidence (array of {date_value,date_precision:day|month|year,date_kind,source_id,field_or_locator}); date_window {status:YES|NO|UNCERTAIN,rationale,evidence_source_ids}; version_linkage {status:confirmed|unconfirmed|not_applicable,published_doi,source_ids,content_equivalence:verified|not_assumed,limitation}; proposed_working_decision:INCLUDE|EXCLUDE|UNCERTAIN; decision_basis (source IDs and applicable existing gates); unresolved (array).
- sources: array of {source_id,url_or_file,source_class:publisher|crossref|arxiv|supplied_full_text|discovery_only,accessed_at,locator,excerpt,metadata_fields}. For network sources accessed_at must be actual RFC3339 with timezone. Use exact short excerpts and preserve metadata keys/date-parts when relevant. Every source_id must resolve here. A failed fetch is an attempt, not substantive source evidence. Keep total prose excerpts per remote page at most 25 words; structured bibliographic facts/date fields may be returned as metadata_fields.
- c08_preprint_assessment: {published_identity_linkage,unique_recent_evidence:established|not_established,source_ids,reason,unresolved}; do not assess uniqueness by intuition.
- shortfall: array (empty if all records addressed; inaccessible sources go in attempts/unresolved)
- project_files_changed: 0
- final_prose_written: false

# ACCEPTANCE CRITERIA
A1. Exactly 10 unique requested IDs, 0 omissions and 0 extra records; all required fields present. Missing knowledge is represented explicitly, not by omission.
A2. Every scholarly record has title, ordered authors, year or documented unknown, venue, DOI/DOI_NOT_FOUND and at least one supplied/primary identity locator. Normalized DOI/title duplicates=0. Crossref and publisher attempts for all 10 records; C08 also has an arXiv attempt. Discrepancies retained, not silently repaired.
A3. Every factual date/version/identity claim resolves to an accessible source URL or supplied-file locator with an exact excerpt or metadata field; unsupported quantitative claims=0; nonexistent source references=0. All network attempts have valid observed timestamps and outcomes. Failed-access sources support only access limitations.
A4. Ten explicit date verdicts under the fixed 2021-01-01..2026-11-25 window; 0 acceptance/download/created dates substituted for publication; 0 fabricated day precision. Proposed decisions change only the relevant existing date/primary-report gate and preserve other accepted technical gates; unresolved or conflicting evidence stays UNCERTAIN.
A5. C08 has explicit title/author/DOI comparisons and version-linkage findings; confirmed identity does not imply numerical/content equivalence. Unique-recent eligibility established only with evidence or explicitly not_established. Exactly one C08 assessment; unresolved list present for every record.
A6. Project mutations=0; final prose=false; no unauthorized downloading, authentication bypass, contacts, submission or email. Return evidence only. Retain all unresolved issues; access failure is documented, never guessed away.

# BOUNDARIES
Read-only sources and network requests only. Do not save/edit project files, commit, download PDFs, access credentials/private communications, or write manuscript/report prose. Public abstracts support identity only. Do not call a preprint peer-reviewed. Do not rename reports or overwrite accepted results. Shared authors do not establish study identity. Use only the supplied ten reports and targeted bibliographic sources; no new corpus expansion or general literature search. HTTP403, missing metadata and genuine conflicts must remain unresolved. The request date is not the final search cutoff.

Canonical protocol: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/protocol.md; amendments 001/002 beside it. Accepted ledger: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/consolidated/decision_ledger.json.

Input records (metadata are accepted working inputs, not proof of publisher identity):

```json
[
  {
    "id": "S19",
    "title": "Adaptive Partition and Resource Allocation for Collaborative Inference Services in UAV Swarm",
    "authors": [
      "Ying Dong",
      "Jiebei Shi",
      "Songwei Li",
      "Yuzhou Gao",
      "Yeping Zhu",
      "Jianbing Zhang",
      "Jiwei Huang"
    ],
    "year": 2026,
    "venue": "2026 IEEE International Conference on Web Services (ICWS)",
    "doi": "10.1109/ICWS72778.2026.00154",
    "source_version": "publisher_pdf",
    "unresolved": [
      "Year-only 2026 venue/copyright metadata in the PDF without an explicit publisher publication date; IEEE Xplore download stamp (2026-11-24 UTC) suggests availability before 2026-11-25 but requires Crossref/IEEE Xplore date verification.",
      "Brief 3-page short conference paper (pp. 1222–1224) whose ICWS track/publication type is not explicitly labeled in the PDF and that omits specific DNN model architecture, input dimensions, and detailed simulation parameter tables; text inconsistently refers to the proposed method as CAPRI (pp. 1–2) and CAPRIC (p. 3).",
      "Collaboration is vertical across 10 UAVs, 4 edge servers, and 1 cloud server rather than peer-to-peer inter-UAV feature exchange; no physical multi-UAV flight or UAV failure-recovery evaluation is reported."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/S19.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/S19.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_04_accepted.json#/records/0"
  },
  {
    "id": "S20",
    "title": "Promise: Predictive and Cost-Optimal Migrations for Service-Continuous Edge Intelligence in Multi-UAV Networks",
    "authors": [
      "Jian Zhang",
      "Ming Tao",
      "Renping Xie",
      "Yin Zhang"
    ],
    "year": 2026,
    "venue": "2026 IEEE International Conference on Web Services (ICWS)",
    "doi": "10.1109/ICWS72778.2026.00067",
    "source_version": "publisher_pdf",
    "unresolved": [
      "Year-only 2026 venue/copyright metadata in the PDF without an explicit publisher publication date; IEEE Xplore download stamp (2026-11-25 01:42:27 UTC) indicates availability by the cutoff date but requires Crossref/IEEE Xplore date verification.",
      "Fig. 2(b) lists physical UAV hardware component specifications (e.g., S500 frame, Pixhawk6C, Orin Nano 4GB/8GB) used for parameterization, while actual evaluation is server-based simulation rather than physical flight or hardware-in-the-loop.",
      "Same conference venue (2026 IEEE ICWS) as S19, but distinct author teams, institutions, and systems."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/S20.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/S20.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_04_accepted.json#/records/1"
  },
  {
    "id": "C03",
    "title": "A LINK-LAYER MODEL OF A UAV SWARM MESH NETWORK WITH ENCAPSULATION OF INTERMEDIATE DEEP NEURAL NETWORK ACTIVATIONS: ANALYTICAL EVALUATION OF LATENCY AND TRAFFIC VOLUME",
    "authors": [
      "A. Kasianchuk",
      "H. Lastivka"
    ],
    "year": 2026,
    "venue": "Information and communication technologies, electronic engineering",
    "doi": "10.23939/ictee2026.02.144",
    "source_version": "publisher_pdf",
    "unresolved": [
      "Year-only 2026 publication evidence (Vol. 6, No. 2, 2026 on p. 2; Received 1 September 2026 on p. 1; references accessed 1 September 2026 on p. 10) without a dated publication record before 2026-11-25, requiring Crossref or publisher issue-date verification.",
      "Analytical and single-hop evaluation limitations for quality appraisal and bounded synthesis (not a multi_uav_evaluated eligibility barrier under Protocol Section 4.1(4)): numerical results cover single-hop link transmission and n = 6 independent binomial aggregator neighbors (pp. 6–8, Tables 2–3, Fig. 3), while Table 4 (p. 8) and Section 7 (pp. 8–9) disclose no NS-3/OMNeT++ simulation, high-density MAC collision modeling, correlated freezes/jamming, multi-hop route validation, IEEE 802.11 frame-aggregation modeling, or empirical DNN inference accuracy testing under degraded quorum (m < q).",
      "Page 1 lists author initials only ('A. Kasianchuk', 'H. Lastivka'; full Ukrainian names appear on p. 11 as 'Артем Касьянчук' and 'Галина Ластівка'), and the PDF text layer contains a Cyrillic 'с' homoglyph inside the DOI URL on p. 1."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C03.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C03.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_04_accepted.json#/records/4"
  },
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
    "doi": "10.1109/TCSVT.2026.3745821",
    "source_version": "author_manuscript",
    "unresolved": [
      "Exact publication date within 2026 is not printed on this IEEE Early Access author_manuscript PDF (only year-only 2026 copyright and acceptance notice).",
      "Physical testbed vs simulation boundary: physical DJI/Manifold and EC hardware measurements (Tables II-IV) parameterize offline 20,000-episode training/simulation, without reported multi-UAV flight trials or fault-injection experiments."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C05.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C05.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_05_accepted.json#/records/0"
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
    "doi": "10.1109/JIOT.2026.3755315",
    "source_version": "author_manuscript",
    "unresolved": [
      "Exact publication date within 2026 is not printed on this IEEE Early Access author_manuscript PDF (only year-only 2026 copyright and acceptance notice; IEEE Xplore download timestamp is November 25, 2026).",
      "Evaluation relies on discrete grid/FANET simulation and CIFAR-100 representative expert instantiation rather than physical multi-UAV flight hardware."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C09.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C09.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_05_accepted.json#/records/4"
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
    "doi": "10.1109/JIOT.2026.3740035",
    "source_version": "author_manuscript",
    "unresolved": [
      "Exact publication date within 2026 is not printed on this IEEE Early Access author_manuscript PDF (only year-only 2026 copyright and acceptance notice; IEEE Xplore download timestamp is November 25, 2026).",
      "Title discrepancy: supplied title_hint omits leading article 'A ' present in the supplied PDF title."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C10.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C10.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_05_accepted.json#/records/5"
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
    "doi": "10.1109/TVT.2026.3755123",
    "source_version": "author_manuscript",
    "unresolved": [
      "Date window unresolved: PDF shows VOL. XX, NO. XX, MONTH 2026, received 11 February 2026, acceptance notice, and 25 November 2026 download stamp, but no Date of publication record.",
      "Source version is an unedited accepted author manuscript (author_manuscript); final copy-edited Version of Record metadata and content equivalence require verification.",
      "Evaluated in discrete-event simulation only; real-hardware solver and failure-recovery latencies remain unmeasured (Section IV-E, Section VI)."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C13.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C13.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_06_accepted.json#/records/2"
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
    "doi": "10.1109/JIOT.2026.3746980",
    "source_version": "author_manuscript",
    "unresolved": [
      "Date window unresolved: PDF contains copyright year 2026, acceptance banner, and 25 November 2026 download stamp, but omits any Date of publication, received date, or acceptance date.",
      "Source version is an unedited accepted author manuscript (author_manuscript); final copy-edited Version of Record equivalence is unverified.",
      "Evaluation combines single-board Jetson TX2 compute profiling with simulated Rician-fading links rather than multi-UAV flight testing, and reported latency excludes input delivery, fusion, and routing-control overheads (Section IV-E)."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C14.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C14.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_06_accepted.json#/records/3"
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
    "doi": "10.1109/JIOT.2026.3755176",
    "source_version": "author_manuscript",
    "unresolved": [
      "Publication date unresolved: header states accepted for publication and content may change prior to final publication, with copyright 2026 and IEEE Xplore download stamp on 2026-11-25 but no formal publication date.",
      "NS-3 (10-50 worker UAVs) and PX4-Autopilot (2 nodes) evaluate authentication only; split-DNN inference is evaluated separately on a two-Raspberry-Pi-4 bench testbed with no real UAV flight experiments (deferred to future work).",
      "Author biography on p. 15 capitalizes 'YoungHo Park' whereas p. 1 byline uses 'Youngho Park'."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C19.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C19.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_07_accepted.json#/records/2"
  },
  {
    "id": "C08",
    "title": "Adaptive Heuristics for Scheduling DNN Inferencing on Edge and Cloud for Personalized UAV Fleets",
    "authors": [
      "Suman Raj",
      "Radhika Mittal",
      "Harshil Gupta",
      "Yogesh Simmhan"
    ],
    "year": 2025,
    "venue": "arXiv",
    "doi": "DOI_NOT_FOUND",
    "source_version": "preprint",
    "unresolved": [
      "Preprint eligibility and version linkage under protocol 4.1(7): supplied 50-page PDF is arXiv:2412.20860v2 [cs.DC] dated 24 Apr 2025 (non-peer-reviewed preprint) and lacks Future Generation Computer Systems journal metadata or DOI 10.1016/j.future.2025.107874; neither publication status, version equivalence between arXiv v2 and the unverified input journal DOI, nor whether this preprint qualifies as unique recent evidence is established by supplied evidence.",
      "Title discrepancy: supplied input title_hint ends in for UAVs whereas the supplied PDF title ends in for Personalized UAV Fleets (p. 1).",
      "Study-family linkage: extends prior conference paper cited as [22] (IEEE/ACM CCGrid 2023 on DEMS, pp. 6, 9, 41) and application platform [2] (CHI 2023 Extended Abstracts on Ocularone, pp. 9, 39), and cites companion preprints [55] (arXiv:2504.03709) and [56] (arXiv:2504.01988) on p. 43.",
      "Evaluation realism boundary: multi-drone evaluations up to 84 drones use VIoLET container emulation with Jetson Nano benchmarks, live AWS Lambda FaaS, and NS3/SUMO mobility traces (Secs. 8.1–8.6), Sec. 8.7 replaces DNN execution with sleep timers (p. 32), and Sec. 8.8 field validation uses a single DJI Tello drone with one Jetson Orin Nano edge (pp. 35–37) rather than a physical multi-UAV flight fleet."
    ],
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C08.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C08.txt",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_05_accepted.json#/records/3"
  }
]
```
