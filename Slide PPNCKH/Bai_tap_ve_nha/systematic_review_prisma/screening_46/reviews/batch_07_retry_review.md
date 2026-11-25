# Batch 07 retry — accepted working screening

Task ID: 01a21505-0273-79db-9709-79fcb61192f7
Context ID: 01a21505-0274-74ab-8804-1f315932a6f8
Parent task ID: 01a214fe-2fce-723a-a467-83943cc4d44b
Reviewer: Codex
Reviewed at: 2026-11-26T06:28:03+07:00
started_at: 2026-11-26T06:23:00+07:00
updated_at: 2026-11-26T06:28:03+07:00
completed_at: 2026-11-26T06:28:03+07:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| A1 record count | yes | PASS | Exactly 5 unique records C17–C21; shortfall 0 |
| A2 identity/reasons | yes | PASS | 5/5 complete identity fields and nonempty reasons; 27/27 author names and 5/5 DOI strings found on source first pages; normalized DOI/title and author-name duplicates 0 |
| A3 source/format | yes | PASS | 30/30 gates; 40/40 literal page quotes and permitted word lengths; mechanical errors 0; PDF checksums 5/5 |
| A4 eligibility | yes | PASS | 5/5 truth-table decisions; 3 INCLUDE, 1 EXCLUDE, 1 UNCERTAIN; C18 excludes generic DAG workloads, not merely lack of inter-UAV execution |
| A5 evaluation limits | yes | PASS | 5/5 located classifications; unsupported physical fleet/recovery/performance claims 0; no extracted percentage improvements |
| A6 uncertainty/ownership | yes | PASS | 5 explicit unresolved lists; C19 date remains UNCERTAIN; project_files_changed 0; final prose 0 |

Verdict: **ACCEPTED_WORKING_SCREENING**, derivative
`screening_46/results/batch_07_accepted.json`. Failed primary remains rejected
and immutable. Retry used the same committed brief; no quota fallback.

## Source review and interpretation limits

- C17, pp.1,3–5: dated 15 October 2026; explicit UAV/MEC/cloud DNN split,
  feature quantization and CPU allocation. Multi-UAV trajectory replay and
  pairwise separation substantiate multiple UAVs even though exact K is not
  stated. Outer GAT is the controller, not the only neural workload. Keep
  underlying model/dataset and K unresolved. Page 4 training transitions are
  60,000 per run (3,000 x 20); page 5 runtime measures 10,000 decisions per
  scheme (60,000 total). Do not conflate these with five-seed totals.
- C18, pp.1,3–4,12–13: neural inference appears in motivation/related work;
  evaluated workload is synthetic DAG nodes with sampled cycle/data sizes.
  Page 13 inference timing measures the GAT/DRL optimizer. The single assigned
  UAV per user is a system fact, not a new exclusion rule. Primary exclusion:
  no evaluated neural-inference workload under the fixed scope.
- C19, pp.1,10–12: NS-3 uses one coordinator and 10–50 workers for authentication;
  two Raspberry Pi 4 devices run CNN/MLP SplitNet with CIFAR-10; separate PX4
  nodes exchange authentication messages. None establishes physical multi-UAV
  inference flight. The date watermark is not publication evidence; UNCERTAIN.
  The benchmark timings in the quote are source values, not our measurements.
- C20, pp.1,4,8,10–11: dated 16 July 2026; single-host simulation, modeled
  macro-block loads, core controller plus four compute UAVs. Page 4 N-partition
  notation and page 8 total-N/core exclusion require explicit separation during
  extraction. Page 11 scale 2–8 changes workload proportionally. Controller
  overhead is excluded; p.8 failover is proposed, not evaluated. No accuracy or
  physical-flight claim is adopted.
- C21, pp.1,4,9–10: online 27 October 2025; simulated classifier-DAG partition
  and neighbor offloading with hardware profiles attributed to [41]. The source
  does not prove this study performed those original measurements. Counts 5–200
  describe simulation. Supplied text contains 4 NUL bytes; Gemini reports using
  the PDF directly, while normalized page quotes remain mechanically checkable.

Source-version/family, publisher metadata and retraction checks remain separate.
C17/C20 notation and evaluation limits must carry into extraction and appraisal.
No accepted screening artifact authorizes final synthesis without reconciliation.

## Working checkpoint

41/46 reports across batches 01–07: 28 INCLUDE, 2 EXCLUDE, 11 UNCERTAIN;
5 reports remain. Human adjudication and final study/PRISMA counts pending.
Manuscript and bibliography unchanged.
