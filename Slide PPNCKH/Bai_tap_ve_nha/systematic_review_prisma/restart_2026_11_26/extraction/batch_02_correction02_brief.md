# TASK
Correct the remaining source and schema defects in P08 correction Task 9e1ac0d2-3423-44e9-b446-a38239ad7345, linked to original batch e891c230-d182-4bfa-8068-1cba64226569.

# REQUIRED WORK
1. Open only the named PDFs directly from the attached project and confirm access in the parent. Use internal workers only if attachment access is verified; allocate each ID once, then reconcile one answer. With no confirmed worker, process in the parent and use UNCONFIRMED or UNAVAILABLE, not not_used.
2. Return a replacement only for each listed key below. Verify the physical 1-based page and cite one exact contiguous excerpt, without ellipses or paraphrasing. Field statuses allowed: OBSERVED, NOT_REPORTED, NOT_YET_ASSESSED, NOT_ACCESSIBLE, UNVERIFIED. Mark absence only with the section inspected and a reason. Use NOT_YET_ASSESSED or UNVERIFIED when appropriate. A table value needs its printed precision and measurement context. Use NOT_APPLICABLE with a reason if baseline or denominator does not apply. Quantitative statuses: OBSERVED or UNVERIFIED.
3. Confirm schema corrections separately so Codex can apply mechanical changes without asking you to repeat already parsed values: REPORTED to OBSERVED and VERIFIED to OBSERVED, using the approved status enums; wrap every single evidence object for R0121 in a one-element array; render R0121 unresolved entries as objects with field, reason and checked source. Do not substitute a new fact when only the format needs correction.

# REQUIRED OUTPUT
One line P08_DELEGATION followed by a JSON object with subagent_status, reason and assignments (worker and report_ids). Then lines between P08_FIX_BEGIN and P08_FIX_END. Exactly 10 correction objects {key,report_id,replacement} plus one object with key SCHEMA and fields status_mapping, r0121_array_fields, r0121_unresolved. For fields, return {subtopic,status,finding,page,locator,excerpt,reason}. For metrics, return {metric,value,units,baseline,denominator,workload,conditions,page,locator,excerpt,status,reason}.

# ACCEPTANCE CRITERIA
A1: 10 exact source correction keys plus SCHEMA, with 0 duplicates or added keys and 4 distinct assigned IDs. Bibliographic identities come from the accepted index with title, authors, year, venue and DOI or DOI_NOT_FOUND.
A2: 100% of observed replacements have a matching exact quote, actual supplied PDF and 1-based locator.
A3: 100% of observed metrics have original value, unit, workload, measurement conditions and applicable baseline/denominator. 0 unsupported numbers.
A4: Codex checks source excerpts and semantics independently before any adoption; 0 unsupported, contradicted or unverifiable claims presented as verified.
A5: All statuses use the required enums, unresolved entries are explicit and structured, all 14 R0121 fields have array shape, and worker assignments have 0 overlap. No invented proof of subagent usage.

# BOUNDARIES
Use only P08 and the named PDFs, read-only. No edits, new papers, web search, review prose, unlisted fields or prior batch 01 IDs. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.

## Correction keys
- C01: R0054, mobility_channel_intermittency_failure_and_recovery/mobility_channel_intermittency_failure_and_recovery/failure_and_recovery. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`
- C02: R0054, Normalized cost (holdout). Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`
- C03: R0054, Active-queue admission. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`
- C04: R0054, User data rate. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`
- C05: R0062, Collaborative inference frame rate (4 UAVs, Stage 1). Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf`
- C06: R0095, sensitivity_and_variability/sensitivity_and_variability/coeff_scale_and_model_sweeps. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0095.pdf`
- C07: R0095, Average single decision time. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0095.pdf`
- C08: R0121, inference_model_task_and_dataset/. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf`
- C09: R0121, code_and_data/. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf`
- C10: R0121, funding_and_conflicts/. Source: `restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf`
