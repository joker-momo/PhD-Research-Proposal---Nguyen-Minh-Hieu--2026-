# TASK
Correct exactly the 43 rejected P08 entries of Batch 01 task d9b919ae-f917-43ef-a656-9a8dbff893f6. Keep all other entries and locked metadata unchanged. This targeted follow-up addresses the path error logged under UUID 9739168f-ebd1-4da7-a576-38b39481648b and follows the successful direct project check 3b7f24df-853d-4b52-8dfd-9e3d1b3a4fda.

# REQUIRED WORK
1. Open only the listed reports, directly in attached project paths restart_2026_11_26/fulltext_retrieval/pdf/<report_id>.pdf. Start in the Task parent; resolve relative paths from the attached project folder, never an unmounted tool working directory. If lookup errors, open the same relative path anchored under the authorized attached host root below. Verify each PDF individually; a lookup error for one PDF is not an access disposition for other PDFs. Read each relevant body page. For each PDF give one short exact body quote, 1-based physical page and section or declare the file inaccessible with reason. If workers can demonstrably open the assigned files divide the 43 keys with no overlap; otherwise the parent reads sources directly. Return one consolidated reply and disclose actual worker usage.
2. Correct each F key according to the target list. "pN" in the list is the previous rejected locator, not a trusted page. Prefer a short self-contained statement bounded by its source. When the exact source does not support the prior suggestion, narrow the finding to what the named subtopic's source supports, or mark UNVERIFIED. Do not use the abstract or stitch text across pages or table cells.
3. For A2, set kind FIELD and keep the original subtopic. OBSERVED or NOT_REPORTED require one actual 1-based physical page, precise section/row locator and exact short contiguous quote. NOT_REPORTED requires a specific reason and a locator for the relevant material actually checked. UNVERIFIED is the honest choice when silence cannot be established. A2 uses quantitative:null. No numeric claims in FIELD text unless the same page explicitly supports the values as written, precision, metric context and units.
4. For A3, set kind NUMBER and keep the original metric name. Record a number only if printed in text, table or explicit figure label. Preserve approximation and units. Provide baseline, denominator, workload and conditions independently grounded in the report. No visual estimation or derived ratio. If unverified, keep quantitative:null and state why and where inspected. A missing original number does not authorize a substitute from another test.
5. Keep verified findings compact. No application or operational details beyond high-level academic characterization. Return each of 43 keys exactly once.

# REQUIRED OUTPUT
One P08_DELEGATION line followed by JSON {subagent_status,reason,assignments:[{worker,keys}]} where subagent_status is USED_CONFIRMED, UNAVAILABLE, or UNCONFIRMED. One P08_ACCESS line followed by compact JSON {reports:[{report_id,pdf_path,status,page,section,excerpt,reason}]}, exactly the 13 report IDs. Allowed access statuses OBSERVED and NOT_ACCESSIBLE. Section and excerpt must be from body. Use page:null for inaccessible. Contiguous excerpts, no ellipses.
One compact JSON object per key between standalone P08_FIX_BEGIN and P08_FIX_END; exactly 43 lines. Exact schema example (illustrative only):
{"key":"F00","report_id":"R0000","kind":"FIELD","label":"subtopic","status":"OBSERVED","finding":"one supported fact","page":5,"locator":"Results, paragraph 1","excerpt":"short exact continuous source fragment","quantitative":null,"reason":""}
Field statuses OBSERVED, NOT_REPORTED, UNVERIFIED, NOT_ACCESSIBLE. Number statuses OBSERVED, UNVERIFIED, NOT_ACCESSIBLE. For OBSERVED NUMBER, quantitative has exactly string fields {value,units,baseline,denominator,workload,conditions} and every field has a nonempty value. Preserve an approximation prefix on value when the source is approximate. For unresolved results use finding:"", reason specific and quantitative:null; give available inspected locator, or page:null and empty locator/excerpt for NOT_ACCESSIBLE. End with P08_SUMMARY JSON {returned_keys,unresolved_keys}, then standalone P08_COMPLETE.

# ACCEPTANCE CRITERIA
A1: 43 exact keys with original report and label, 35 FIELD and 8 NUMBER, 0 duplicates or additions. Keep original full label before the colon in the failure map. Use report metadata already locked in the manifest.
A2: 13/13 PDF access dispositions; every OBSERVED or NOT_REPORTED row has exact body source locator. Every adopted finding is supported by the original page. Abstract-only evidence=0.
A3: Every OBSERVED NUMBER verifies printed value, precision, units, baseline, denominator, workload and conditions. Unsupported claims=0.
A4: 43 independently parseable rows, allowable enums, reconciled returned/unresolved lists and all shortfalls explicit.
A5: One Task, one output, exactly 43 non-overlapping key assignments, only the 43 failed entries touched.

# BOUNDARIES
No editing files, web search, new reports, manuscript prose, read outside the named PDF scope, inventions, or restatement of valid keys. Use physical PDF pages, not printed journal pagination. Missing evidence stays explicit.

Authorized attached host root (direct attachment only): /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma

## Failure-key map
F01 | R0001 | A2 | decision_variables_objectives_constraints_and_solver/optimization_and_solver: locator/excerpt mismatch p2
F02 | R0001 | A2 | sensitivity_and_variability/alpha_sensitivity: locator/excerpt mismatch p3
F03 | R0002 | A2 | outcomes_latency_energy_communication_accuracy_reliability_and_scalability/success_cost_accuracy: locator/excerpt mismatch p8
F04 | R0003 | A2 | outcomes_latency_energy_communication_accuracy_reliability_and_scalability/latency_and_accuracy: locator/excerpt mismatch p6
F05 | R0006 | A2 | compute_and_radio/uav_compute_radio_params: locator/excerpt mismatch p6
F06 | R0006 | A2 | evaluation_platform_simulator_hardware_and_traces/simulation_trials: locator/excerpt mismatch p6
F07 | R0006 | A2 | baselines_and_workloads/baselines: locator/excerpt mismatch p6
F08 | R0009 | A2 | uav_architecture_role_and_topology/uav_assisted_mec: locator/excerpt mismatch p8
F09 | R0009 | A2 | partition_and_assignment/gu_uav_split: locator/excerpt mismatch p5
F10 | R0009 | A2 | compute_and_radio/compute_and_radio_params: locator/excerpt mismatch p8
F11 | R0009 | A2 | baselines_and_workloads/baselines_and_arrivals: locator/excerpt mismatch p8
F12 | R0009 | A2 | sensitivity_and_variability/radius_users_bandwidth: locator/excerpt mismatch p9
F13 | R0009 | A3 | total_energy_70_gus: missing quantitative components or quote/page mismatch
F14 | R0010 | A2 | inference_model_task_and_dataset/cnn_models: locator/excerpt mismatch p5
F15 | R0010 | A2 | decision_variables_objectives_constraints_and_solver/dqn_action_disassembly: locator/excerpt mismatch p4
F16 | R0010 | A2 | outcomes_latency_energy_communication_accuracy_reliability_and_scalability/latency_reduction: locator/excerpt mismatch p5
F17 | R0010 | A2 | funding_and_conflicts/funding: locator/excerpt mismatch p6
F18 | R0010 | A2 | funding_and_conflicts/conflicts: locator/excerpt mismatch p6
F19 | R0015 | A2 | mobility_channel_intermittency_failure_and_recovery/simplified_static_channel: locator/excerpt mismatch p6
F20 | R0015 | A2 | evaluation_platform_simulator_hardware_and_traces/simulation_platform: locator/excerpt mismatch p6
F21 | R0015 | A2 | outcomes_latency_energy_communication_accuracy_reliability_and_scalability/latency_and_runtime: locator/excerpt mismatch p6
F22 | R0015 | A3 | latency_reduction_alexnet_72mbps: missing quantitative components or quote/page mismatch
F23 | R0015 | A3 | latency_reduction_resnet152_72mbps: missing quantitative components or quote/page mismatch
F24 | R0015 | A3 | latency_reduction_vgg16_72mbps: missing quantitative components or quote/page mismatch
F25 | R0015 | A3 | eecia_runtime_vgg16_i5: missing quantitative components or quote/page mismatch
F26 | R0019 | A2 | uav_architecture_role_and_topology/centralized_rl_swarm: locator/excerpt mismatch p11
F27 | R0019 | A2 | inference_model_task_and_dataset/cnn_surveillance: locator/excerpt mismatch p11
F28 | R0022 | A2 | partition_and_assignment/exit_and_layer_partition: locator/excerpt mismatch p2
F29 | R0029 | A2 | compute_and_radio/compute_and_radio_params: locator/excerpt mismatch p5
F30 | R0044 | A2 | decision_variables_objectives_constraints_and_solver/cvar_bat_subgradient: locator/excerpt mismatch p6
F31 | R0044 | A2 | mobility_channel_intermittency_failure_and_recovery/fading_and_bs_fallback: locator/excerpt mismatch p3
F32 | R0044 | A2 | evaluation_platform_simulator_hardware_and_traces/simulation_area: locator/excerpt mismatch p6
F33 | R0044 | A2 | baselines_and_workloads/baselines: locator/excerpt mismatch p7
F34 | R0044 | A2 | sensitivity_and_variability/bw_reliability_psi1: locator/excerpt mismatch p7
F35 | R0045 | A2 | partition_and_assignment/two_part_split_and_migration: locator/excerpt mismatch p4
F36 | R0045 | A2 | decision_variables_objectives_constraints_and_solver/sac_per_cvx: locator/excerpt mismatch p6
F37 | R0045 | A2 | mobility_channel_intermittency_failure_and_recovery/threshold_migration_3d: locator/excerpt mismatch p9
F38 | R0045 | A2 | sensitivity_and_variability/seeds_and_thresholds: locator/excerpt mismatch p11
F39 | R0048 | A2 | decision_variables_objectives_constraints_and_solver/jdtso_and_mapdp: locator/excerpt mismatch p7
F40 | R0048 | A2 | baselines_and_workloads/baselines: locator/excerpt mismatch p10
F41 | R0048 | A3 | inference_latency_60_uavs_eff07: missing quantitative components or quote/page mismatch
F42 | R0048 | A3 | energy_consumption_60_uavs_eff07: missing quantitative components or quote/page mismatch
F43 | R0048 | A3 | throughput_60_uavs_eff07: missing quantitative components or quote/page mismatch
