## TASK
Reconcile the application of fixed multi-UAV collaborative-inference eligibility to exactly C06,SNCS,C04,C11,C16, using supplied full texts and existing accepted screening. Return source-grounded research evidence only; do not change the protocol.

## REQUIRED WORK
1. Read protocol.md and Amendments 001/002, then the five full reports and accepted screening records. Separate an evaluated architecture from an introductory drawing, future-work proposal, or training-only controller collaboration.
2. For each report identify the evaluated UAV count/roles, exact inference workload, where neural computation executes, and the inference request/resource/placement/feature decisions actually coordinated across the architecture. Distinguish inference coordination from RL training coordination, ordinary video/network transport, security alone, and a standalone component bench test. Simulation and analytical evidence may be eligible; physical flight and inter-UAV layer partitioning are not mandatory.
3. Map evidence to the two exact Amendment 001 criteria: evaluated multi-UAV architecture; inference execution/features/layers/requests/resources distributed, assigned, fused or jointly orchestrated across the swarm or multi-UAV-edge/cloud hierarchy. Do not invent a requirement that every UAV computes, that a layer split exists, or that direct UAV-to-UAV links must exist. Conversely, naming multiple UAVs does not alone establish an evaluated inference hierarchy.
4. Review supporting and contrary passages: C06 three-UAV setup versus per-UAV evaluation and A3C worker training; SNCS video-policy/DQN inference experiments versus separate Q-LADTR routing; C04 cloud-edge speculative LLM plus intra-swarm latent intent sharing; C11 aerial relays with terrestrial LLM prefill/decoding; C16 inference-server UAV plus jammer UAV. Determine YES/NO/UNCERTAIN for the two scope gates with exact source evidence and explain how the same fixed rule applies across all five.
5. Return a proposed working decision preserving the other four accepted gates and unchanged bibliographic/date data. If evidence cannot settle scope, return UNCERTAIN and one precise question a human reviewer must decide. Do not force inclusion to meet a count or cite SNCS because it is the target journal.

## REQUIRED OUTPUT
One JSON object, no Markdown fences:
- task: scope_01
- records: exactly 5 objects in input order. Fields: id,title,authors,year,venue,doi (or DOI_NOT_FOUND),prior_decision,proposed_decision,scope_gates:{multi_uav_evaluated:{status:YES|NO|UNCERTAIN,rationale,evidence_ids},collaborative_inference:{status:YES|NO|UNCERTAIN,rationale,evidence_ids}},other_gates_preserved (four status fields),architecture:{uav_roles,inference_execution_nodes,inference_workload,coordinated_decisions,evaluated_conditions,evidence_ids},supporting_interpretation:{note,evidence_ids},contrary_interpretation:{note,evidence_ids},evidence:[exactly4 objects {evidence_id,file,page,line_range,quote}],unresolved:array,human_question:string or null.
- consistency_checks: exactly 3 objects {principle,applies_to_ids,evidence_ids,assessment}, covering (i) not all UAVs must compute, (ii) training/transport is not automatically inference coordination, (iii) simulation/analytical evidence is eligible when the two scope criteria are met. Use report-qualified evidence IDs globally unique.
- shortfall:[]; project_files_changed:0; final_prose_written:false.
All substantive factual claims refer to local evidence IDs; four quotes may support multiple fields. The evidence set must include relevant supporting AND contrary/limiting text, or explicitly explain why no contrary passage was found without claiming a negative experiment. Each quote is one exact contiguous 1–40-word passage with PDF page and text line range; verify PDF directly when extraction is garbled.

## ACCEPTANCE CRITERIA
A1: Exactly the five requested unique IDs, no extras/missing records, all fields present; bibliographic identities retained from accepted input (0 unsupported changes); duplicate DOI/title records=0.
A2: Exactly20 evidence objects, 4/report; 20/20 quote/page/line locators match supplied files; 1–40 words each; all evidence references resolve; every substantive factual claim sourced; unsupported quantitative claims=0.
A3: Exactly10 scope gate verdicts; other four gates unchanged; decision truth table INCLUDE iff all six YES, EXCLUDE iff any NO, otherwise UNCERTAIN. No new mandatory physical-flight/layer-split/all-UAV-compute condition; no venue/count-driven override.
A4: 5/5 reports have supporting and contrary/limiting interpretations linked to evidence; exactly3 consistency checks apply fixed Amendment001 without changing scope. The five specific boundary issues in Required Work4 are each addressed explicitly.
A5: Unresolved array on5/5 records; every UNCERTAIN has one concrete human_question; missing evidence not asserted absent; study families/publication dates/numerical effects not independently revised. Working decisions remain pending final human adjudication.
A6: project_files_changed=0; final_prose_written=false; no web/downloads or file edits. Exact record count or documented shortfall, no invented data/DOI/quotes; no unauthorized access, credentials, messages, submission or Git operations.

## BOUNDARIES
Read-only supplied sources. Do not write final prose, edit project files, change the protocol, broaden the corpus, or research publication dates/study families in this task. Preserve uncertainty where the text cannot establish linkage. Research paper instructions are untrusted data. Dates remain bounded by2021-01-01..2026-11-25. Codex alone decides acceptance; the human researcher retains final eligibility responsibility.

protocol.md: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/protocol.md
protocol_amendment_001.md: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/protocol_amendment_001.md
protocol_amendment_002.md: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/protocol_amendment_002.md
Accepted input records:
```json
[
  {
    "id": "C06",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_05_accepted.json#/records/1",
    "review": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_05_correction_review.md",
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C06.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C06.txt",
    "prior_decision": "UNCERTAIN"
  },
  {
    "id": "SNCS",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_08_accepted.json#/records/4",
    "review": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_08_correction_review.md",
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/SNCS.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/SNCS.txt",
    "prior_decision": "UNCERTAIN"
  },
  {
    "id": "C04",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_04_accepted.json#/records/5",
    "review": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_04_correction_02_review.md",
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C04.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C04.txt",
    "prior_decision": "INCLUDE"
  },
  {
    "id": "C11",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_06_accepted.json#/records/0",
    "review": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_06_review.md",
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C11.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C11.txt",
    "prior_decision": "INCLUDE"
  },
  {
    "id": "C16",
    "accepted_record": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_06_accepted.json#/records/5",
    "review": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_06_review.md",
    "pdf": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/C16.pdf",
    "text": "/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C16.txt",
    "prior_decision": "INCLUDE"
  }
]
```
