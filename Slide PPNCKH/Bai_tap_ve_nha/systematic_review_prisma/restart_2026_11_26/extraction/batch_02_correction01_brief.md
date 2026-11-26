# TASK
Correct the 77 failed entries and the one truncated report in parent result `e891c230-d182-4bfa-8068-1cba64226569` for P08.

# REQUIRED WORK
1. Read the named PDFs in the attached project directory with the parent native reader. Use an internal worker only if it can directly open the assigned PDF. Keep one parent answer, assign each report once, and identify actual assignments. If workers cannot access the attachment, do the correction in the parent.
2. For each E item below, replace only the indicated evidence entry. Use one short, exact contiguous fragment as printed (ideally 5–12 words), no ellipses or combined spans, and verify the 1-based physical PDF page and locator. Make the finding no broader than the quoted source supports. Where two distinct fragments are indispensable they need separate entries. For absence identify the actual section checked and reason.
3. For each Q item below, replace only the indicated quantitative claim. Give the source value, original units, baseline and denominator or explicit NOT_APPLICABLE with a short reason when truly inapplicable, workload, conditions, physical page, precise table/figure/section and a short exact excerpt. Use UNVERIFIED if full support is unavailable. No approximations read from graphs.
4. Return a full compact P08 replacement only for R0121 because its JSON line was truncated. It must contain the same identity and 14 field keys as batch 02, one traceable object per field where possible. Reference only named PDFs. For R0063 omit operational/tactical details and retain bibliographic or benign aggregate evaluation evidence only.
5. Check JSON for balanced braces and all requested IDs/keys before final. Prioritize compact JSON with short excerpts and do not repeat complete original rows for the 11 already parsed IDs.

# REQUIRED OUTPUT
One P08_DELEGATION JSON line {subagent_status,reason,assignments:[{worker,report_ids}]}. Then use standalone P08_FIX_BEGIN and P08_FIX_END. In between, return one short JSON line per key below with {key,report_id,replacement}. E replacement fields are {subtopic,status,finding,page,locator,excerpt,reason}. Q replacement fields are {metric,value,units,baseline,denominator,workload,conditions,page,locator,excerpt,status,reason}. The exact allowed key and PDF are fixed by the list below. Use reason for every unresolved item and cite the source actually inspected. The one FULL-R0121 line has replacement {report_id,study_id,title,authors,year,venue,doi,pdf_path,fields,quantitative_claims,unresolved} and exactly 14 original named field keys. Do not add material beyond the failed keys. Do not use a code fence.

# ACCEPTANCE CRITERIA
A1: Exactly 78 correction keys, including one complete R0121 and 77 targeted entries; 0 duplicate or unknown keys. R0121 title/authors/year/venue/DOI or DOI_NOT_FOUND and study ID match the accepted index; no metadata duplication. Internal assignments have exactly the 12 allowed IDs once.
A2: 100% of observed replacement entries specify the actual named PDF, 1-based page, precise locator and contiguous verbatim evidence. 0 quote/page mismatches. Inaccessible or unfinished material remains explicit and outside adopted evidence.
A3: 100% of proposed quantitative claims have original value, units, workload, conditions, applicable denominator and baseline, and a source locator. No unsupported numbers.
A4: Codex opens the actual PDFs and checks 100% of evidence proposed for adoption, including identity, meaning, exact locators and values. No assertions without sufficient support.
A5: All unresolved fields have status and reason. No abstract substitutes; no missed or duplicated assignment IDs and no unsupported claim of using subagents.

# BOUNDARIES
Read only the below PDFs, P08 in `restart_2026_11_26/protocol_restart.md`, and the relevant locked metadata in `restart_2026_11_26/fulltext_retrieval/fulltext_identity_index.csv`, `restart_2026_11_26/study_linkage/report_study_map.csv`. Do not edit any project file, add sources, browse, produce manuscript prose or repeat the 13 Batch 01 reports. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.

## Allowed correction keys and source PDFs
P08 fields for FULL-R0121: identity, uav_architecture_role_and_topology, inference_model_task_and_dataset, partition_and_assignment, decision_variables_objectives_constraints_and_solver, compute_and_radio, mobility_channel_intermittency_failure_and_recovery, evaluation_platform_simulator_hardware_and_traces, baselines_and_workloads, outcomes_latency_energy_communication_accuracy_reliability_and_scalability, sensitivity_and_variability, code_and_data, funding_and_conflicts, reported_limitations.

### R0054 — `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`
- R0054-01 E `identity/bibliographic_identity`
- R0054-02 E `partition_and_assignment/split_points_and_bitwidth`
- R0054-03 E `compute_and_radio/compute_and_rf_model`
- R0054-04 E `mobility_channel_intermittency_failure_and_recovery/failure_and_recovery`
- R0054-05 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/holdout_performance`
- R0054-06 Q `Normalized cost (holdout)`
- R0054-07 Q `Active-queue admission`
- R0054-08 Q `User data rate`

### R0059 — `restart_2026_11_26/fulltext_retrieval/pdf/R0059.pdf`
- R0059-01 E `identity/bibliographic_identity`
- R0059-02 E `partition_and_assignment/switching_and_layer_partitioning`
- R0059-03 E `decision_variables_objectives_constraints_and_solver/minimization_and_two_step_solver`
- R0059-04 E `mobility_channel_intermittency_failure_and_recovery/predetermined_trajectory_mobility`
- R0059-05 E `baselines_and_workloads/switching_and_partitioning_baselines`
- R0059-06 E `sensitivity_and_variability/horizon_bandwidth_memory_compute_uavs`
- R0059-07 Q `AMSM horizon H=4..7 latency CV`

### R0062 — `restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf`
- R0062-01 E `identity/bibliographic_identity`
- R0062-02 E `decision_variables_objectives_constraints_and_solver/heuristic_ooda_scheduling`
- R0062-03 E `mobility_channel_intermittency_failure_and_recovery/single_point_failure_and_recovery`
- R0062-04 E `evaluation_platform_simulator_hardware_and_traces/hardware_testbed`
- R0062-05 E `baselines_and_workloads/baselines_and_video_workload`
- R0062-06 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/frame_rate_and_resilience`
- R0062-07 Q `Collaborative inference frame rate (4 UAVs, Stage 1)`

### R0063 — `restart_2026_11_26/fulltext_retrieval/pdf/R0063.pdf`
- R0063-01 E `identity/bibliographic_identity`
- R0063-02 E `partition_and_assignment/hierarchical_and_speculative_split`
- R0063-03 E `decision_variables_objectives_constraints_and_solver/pomg_and_role_decoupled_mappo`
- R0063-04 E `baselines_and_workloads/baselines_and_scenarios`
- R0063-05 E `sensitivity_and_variability/ablations_and_frequency_sweep`

### R0068 — `restart_2026_11_26/fulltext_retrieval/pdf/R0068.pdf`
- R0068-01 E `uav_architecture_role_and_topology/ad_hoc_swarm_layers`
- R0068-02 E `inference_model_task_and_dataset/cnn_models`
- R0068-03 E `partition_and_assignment/layer_wise_partitioning`
- R0068-04 E `decision_variables_objectives_constraints_and_solver/ldtp_and_marl_meta`
- R0068-05 E `compute_and_radio/compute_and_radio_params`
- R0068-06 E `mobility_channel_intermittency_failure_and_recovery/dynamic_swarm_membership_and_energy_return`

### R0071 — `restart_2026_11_26/fulltext_retrieval/pdf/R0071.pdf`
- R0071-01 E `identity/bibliographic_identity`
- R0071-02 E `partition_and_assignment/single_split_offloading`
- R0071-03 E `decision_variables_objectives_constraints_and_solver/p_mdp_and_le_mhappo`
- R0071-04 E `compute_and_radio/compute_solar_and_ofdm`
- R0071-05 E `mobility_channel_intermittency_failure_and_recovery/high_dynamic_mobility_and_energy_depletion`
- R0071-06 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/weighted_cost_and_degradation`
- R0071-07 Q `Performance degradation ratio vs MHAPPO as Delta T increases`

### R0073 — `restart_2026_11_26/fulltext_retrieval/pdf/R0073.pdf`
- R0073-01 E `identity/bibliographic_identity`
- R0073-02 E `uav_architecture_role_and_topology/ad_hoc_swarm_with_u2g`
- R0073-03 E `inference_model_task_and_dataset/cnn_models_and_datasets`
- R0073-04 E `partition_and_assignment/resilient_layer_distribution`
- R0073-05 E `decision_variables_objectives_constraints_and_solver/ilp_and_ppo_solver`
- R0073-06 E `mobility_channel_intermittency_failure_and_recovery/inoperable_uav_reallocation`
- R0073-07 E `reported_limitations/environment_doppler_battery`

### R0074 — `restart_2026_11_26/fulltext_retrieval/pdf/R0074.pdf`
- R0074-01 E `identity/bibliographic_identity`
- R0074-02 E `uav_architecture_role_and_topology/pure_edge_heterogeneous_pipeline`
- R0074-03 E `partition_and_assignment/layer_and_sequence_partitioning`
- R0074-04 E `mobility_channel_intermittency_failure_and_recovery/channel_and_compute_noise`
- R0074-05 E `baselines_and_workloads/five_baselines`
- R0074-06 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/prefill_latency_and_scalability`
- R0074-07 E `sensitivity_and_variability/ablations_breakeven_and_monte_carlo`
- R0074-08 E `funding_and_conflicts/funding_and_conflicts`
- R0074-09 E `reported_limitations/decoding_determinism_scale_and_sim`
- R0074-10 Q `Predictive decoding break-even accuracy threshold`

### R0083 — `restart_2026_11_26/fulltext_retrieval/pdf/R0083.pdf`
- R0083-01 E `identity/bibliographic_identity`
- R0083-02 E `uav_architecture_role_and_topology/center_requesting_worker_uavs`
- R0083-03 E `partition_and_assignment/containerized_partition_placement`
- R0083-04 E `baselines_and_workloads/baselines_and_requests`
- R0083-05 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/latency_energy_longevity`
- R0083-06 E `funding_and_conflicts/funding_and_conflicts`

### R0089 — `restart_2026_11_26/fulltext_retrieval/pdf/R0089.pdf`
- R0089-01 E `identity/bibliographic_identity`
- R0089-02 E `uav_architecture_role_and_topology/drone_terminals_and_aerial_servers`
- R0089-03 E `inference_model_task_and_dataset/branchy_resnet_cifar10`
- R0089-04 E `partition_and_assignment/hybrid_early_exit_and_offloading`
- R0089-05 E `decision_variables_objectives_constraints_and_solver/heuristic_priority_queues_and_balancing`
- R0089-06 E `compute_and_radio/compute_and_ofdma_params`
- R0089-07 E `sensitivity_and_variability/resource_and_load_sweeps`

### R0095 — `restart_2026_11_26/fulltext_retrieval/pdf/R0095.pdf`
- R0095-01 E `uav_architecture_role_and_topology/core_and_computing_uavs`
- R0095-02 E `inference_model_task_and_dataset/macro_block_dnn_models`
- R0095-03 E `decision_variables_objectives_constraints_and_solver/ppo_dmcp_and_cache`
- R0095-04 E `baselines_and_workloads/rl_and_partition_baselines`
- R0095-05 E `outcomes_latency_energy_communication_accuracy_reliability_and_scalability/completion_latency_and_decision_time`
- R0095-06 E `sensitivity_and_variability/coeff_scale_and_model_sweeps`
- R0095-07 Q `Average single decision time`

### R0121 — `restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf`
- FULL-R0121
