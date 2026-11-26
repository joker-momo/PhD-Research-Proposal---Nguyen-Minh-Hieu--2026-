# TASK

Repair only six RQ1/RQ2/RQ4 claim keys and the summary in native Gemini Task 1b70c251-9b03-4336-adb7-b4fae5194d4d, context d2b31784-8402-409b-90fa-2f629637cef2.

# REQUIRED WORK

1. Use one parent Task reading the directly attached project read-only. Use the exact approved citation key, page and section tuples below, checked against the locked P08/P09 entries. Keep each finding narrow and qualitative. Do not include numerical values in the six corrected findings. Do not open other PDFs or claim exhaustive access.
2. Write `RQ1-A`: R0001 and R0054 both describe layer cuts across UAV, edge and cloud tiers. Do not add STAR-RIS or bitwidth claims. P08 locators: R0001 partition_and_assignment:1, 2, "II.A Inference Partitioning"; R0054 partition_and_assignment:1, 3, "Section II-B Three-tier DNN inference, Eq. (13) and (17e)".
3. Write `RQ1-B`: examples of sub-layer CNN tasks, row-wise feature-map partitioning and classifier-level DAG cuts. Keep taxonomy and omit extra topology, node-count and control details. P08 locators: R0015 partition_and_assignment:1, 3, "III.A System Model"; R0044 partition_and_assignment:1, 3, "II.C DNN Partitioning and Offloading"; R0048 partition_and_assignment:1, 7, "V.B Algorithm".
4. Write `RQ2-A`: the R0006 formulation optimizes horizontal UAV positions and layer assignment under memory, energy and coverage constraints, while the evaluation specifies compute, memory, power and coverage parameters. Cite P08 R0006 decision_variables_objectives_constraints_and_solver:1, 4, "III.B & IV"; compute_and_radio:1, 6, "V-A, UAV specifications and communication/energy parameter bullets". Omit R0045 and unsupported fixed settings.
5. Write `RQ2-B`: R0009 combines split/trajectory/power/resource decisions in its latency–energy formulation. In R0001 the formulation describes edge-server selection, while its policy uses the nearest edge server. P08 R0009 decision_variables_objectives_constraints_and_solver:1, 6, "IV.C Trajectory & Power"; P09 R0001 D02, 2, "II.E". Omit other R0001 decisions.
6. Write `RQ4-A`: R0048 assumes hovering and defers trajectories, R0003 uses trace-driven simulation, and R0045 simulates horizontal and altitude control with migration responding to energy or load thresholds. Do not attribute migration directly to trajectory or imply a flight trial. P08 R0048 mobility_channel_intermittency_failure_and_recovery:1, 12, "VIII. CONCLUSION"; R0003 evaluation_platform_simulator_hardware_and_traces:1, 5, "V.A Simulation Settings"; R0045 mobility_channel_intermittency_failure_and_recovery:1, 11, "IV-B.3 and IV-C, trajectory and migration trigger".
7. Write `RQ4-B`: R0063 evaluates cloud-link interruption and edge fallback. R0062 disables a node's communication program and checks redistribution and return on reconnection. R0002 separately simulates random UAV failures and migration. Do not characterize software disconnect as physical loss or cite unstructured FPS values. P08 R0063 mobility_channel_intermittency_failure_and_recovery:1, 16, "Section 5.3.3 and Table 9, pp. 16-17"; R0062 mobility_channel_intermittency_failure_and_recovery:1, 6, "Section EFFECT OF UAV UNAVAILABILITY"; R0002 mobility_channel_intermittency_failure_and_recovery:1, 7, "VII.A Experimental Settings".
8. Replace the summary with five scope limits, no counts. Keep original-viewer reading limits explicit, and distinguish those from the evidence base and from actual outcomes. Do not claim the quantitative matrix has 42 rows or that missing reporting constitutes absence.

# REQUIRED OUTPUT

JSONL one object per exact claim ID above. Example schema: {"rq":"RQ1","claim_id":"RQ1-A","finding":"Scoped comparison","citations":[{"report_id":"R0001","source":"P08","key":"partition_and_assignment:1","physical_page":2,"section":"II.A Inference Partitioning"}],"frequency":null,"quantitative":null}. Source enum P08 / P09, keep provided page and section labels exactly. Summary example: {"summary":true,"limitations":{"RQ1":"...","RQ2":"...","RQ3":"...","RQ4":"...","RQ5":"..."},"tools":[],"workers_used":false,"unresolved":[]}. Finish with `HK261_RESTART_14_CORRECTION_COMPLETE` alone.

# ACCEPTANCE CRITERIA

Six exact distinct claim IDs, one summary, zero malformed rows, zero numeric measurement or frequency claims in the replacements, all seven items have the required fields, 100% retained citations match files and scope, and no unreported shortfalls. Preserve all four accepted claim IDs unchanged.

# BOUNDARIES

No manuscript prose, edits, workers, external searches or new evidence. Do not reprint the four accepted claims. Keep units of analysis and classifications fixed. No access claim beyond the files actually read.
