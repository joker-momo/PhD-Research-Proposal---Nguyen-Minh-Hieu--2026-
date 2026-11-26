# TASK

Resolve only six P09 Batch 01 keys still failing after Gemini.app Task 643cc6f4-a83e-4caa-b6bd-1ddb01c4fa4c (context 1f6efe91-50b6-456b-9fe8-a0f036f4d1ba).

# REQUIRED WORK

1. Use only the native parent Task, no workers. Read the authorized original project PDFs in `restart_2026_11_26/fulltext_retrieval/pdf/` and P09 in `restart_2026_11_26/protocol_restart.md`. R0001, R0002, R0003, R0006 and R0009 are the only allowed originals. The previously accepted five access probes are already recorded. If an original cannot be opened, name the file and reason. Read in-app or use local PDF tools if available, with original-page verification. Never upload PDFs to an external parser.
2. Recheck the following six keys on the original physical 1-based pages. Short quotes below were independently observed in the PDF source and are only locators, not preassigned judgments:
   - R0001/D02: p.2 §II.D “declares the range of the partition points”; §II.E “select the ES”. Check the text on limits, not whether solver implementation enforces them. Do not claim nonenforcement from Eq. 6 or §II.E without affirmative evidence. Judge documented modeling assumptions, decisions and constraints.
   - R0002/D03: p.7 §VII.A “trained on the CIFAR-10 dataset is adopted for”; “the real-world UAV platform and parameter”. Report a specific rerun gap demonstrable from §VII.A and Fig. 2(b) or §IV, without claiming that all thresholds or battery settings are absent.
   - R0002/D09: p.7 §VII.A “trained on the CIFAR-10 dataset is adopted for”. Inspect §VII.A and p.9 §VIII/end matter for any author release. Separate use of public data from a release by these authors. Record inspected sections explicitly.
   - R0003/D07: p.2 §III “trajectories, channel conditions,” or “and inference task distributions”; p.5 §V.A “based on the real-world trajectory traces obtained from”. Distinguish model/coordination assumptions, trace-driven simulation, and flight validation.
   - R0006/D08: p.6 §V.B “stabilizes at 87.0%, indicating that” and “complete monitoring coverage”. Compare only the observed coverage and the same paragraph's own wording. Use qualitative wording for the rationale; omit all latency reductions and all abstract quotations.
   - R0009/D05: p.4 §III Eq. 14 “weighted latency and”; p.8 §V.B Fig. 4 and p.9 §V.B Fig. 5 captions. Link energy and latency outcomes to the objective without asserting a reported effect size.
3. Return one rationale per key, at most 30 words. Use exact original contiguous quotes with original typography where practical, one physical page per locator. Use null quotes for inspected absence and retain its named section. A NOT_REPORTED judgment requires a description of what was looked for. Clearly flag inability to assess. No numerical conclusions lacking metric definition and conditions.

# REQUIRED OUTPUT

Six JSONL judgments or documented shortfalls. Example schema on one line:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"Setup names the workload, but repeats are not described.","locators":[{"page":4,"section":"Methods","quote":"short exact line from the PDF"},{"page":5,"section":"Setup","quote":null}]}
Use YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, or NOT_YET_ASSESSED. Report report/domain keys in one summary object with returned_keys, unresolved, workers_used=false, and tools. End with P09_B01_LOCATOR_REPAIR_COMPLETE on a line by itself. Bibliographic metadata is frozen in locked P08 and the Batch 01 brief.

# ACCEPTANCE CRITERIA

- Exact scope of six keys; 0 duplicate, extra, previously accepted or malformed keys. If shortened, name and explain every omitted key.
- All six judgments have verifiable original-PDF page and section evidence and all quoted excerpts match. Zero unsupported scope, missing-information, or numerical conclusions.
- One parent response, 0 workers or project mutations. Disclose actual PDF tools and any unresolved items.

# BOUNDARIES

Read only the named originals and P09. No files written, external discovery, literature screening, new extraction, edits, or reappraisal of any other key. Do not infer source access, solver behavior, measured effects or bias from silence.
