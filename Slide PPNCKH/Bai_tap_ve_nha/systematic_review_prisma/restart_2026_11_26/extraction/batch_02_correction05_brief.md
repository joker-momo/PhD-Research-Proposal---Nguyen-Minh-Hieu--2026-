# TASK
Correct only C04-05 and C04-06 for R0062, from Batch 02 original e891c230-d182-4bfa-8068-1cba64226569 and correction d7da77d3-c487-43a5-be60-42bb51b7efd0.

# REQUIRED WORK
1. Open only restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf from the attached live project. Verify one body quote and its physical PDF page. Report if unavailable. The parent should read this one PDF and report truthful worker status.
2. Read the physical page 6 paragraph under Effect of UAV Unavailability. C04-05 is the four-UAV Stage 1 frame rate; C04-06 is the Stage 2 frame rate when one UAV is unavailable. Inspect the rendered typography because PDF text extraction can drop a tilde. Keep both as approximate values if so printed. For Stage 1, use the short contiguous fragment that contains the speed and avoid transcribing the acronym before that fragment. For Stage 2, use the corresponding contiguous fragment including the approximation sign. Preserve degree of precision, FPS, stage workload/condition, and applicable denominator and baseline. Do not report the paper's application or any deployment details. Hardware status may be NOT_APPLICABLE for this focused correction, with an explanation that the previously verified hardware is outside the two keys being fixed.

# REQUIRED OUTPUT
One P08_DELEGATION JSON line with subagent_status USED_CONFIRMED, UNAVAILABLE or UNCONFIRMED, reason, assignments [{worker,report_ids}]. One P08_ACCESS JSON line with reports [{report_id,pdf_path,status,page,excerpt,reason}], status OBSERVED or NOT_ACCESSIBLE. Between standalone P08_FIX_BEGIN and P08_FIX_END return one compact JSON object per target key (C04-05 or C04-06). Required fields and types are shown in this exact example (fake key, do not emit it):
{"key":"EXAMPLE","report_id":"EXAMPLE","metric":"illustration","status":"UNVERIFIED","value":null,"units":null,"baseline":null,"denominator":null,"workload":null,"conditions":null,"hardware_status":"UNVERIFIED","sources":[{"file":"example.pdf","page":3,"section":"Results","locator":"Figure 2, caption","excerpt":"exact short body quote","supports":["inspection"]}],"reason":"No exact value was printed."}
The metric status enum is OBSERVED, UNVERIFIED, NOT_ACCESSIBLE. hardware_status enum is REPORTED, NOT_REPORTED, UNVERIFIED, NOT_APPLICABLE. All nonnull text is a JSON string, sources is a list and pages are positive integers. An OBSERVED row has a value (retain approximate notation as printed), units, baseline, denominator, workload and conditions. Use NOT_APPLICABLE or NOT_REPORTED with reason for a component when justified. Allowed supports values: value, units, baseline, denominator, workload, conditions, hardware, inspection. Exact continuous excerpts without invented punctuation or ellipses. UNVERIFIED uses value:null and inspection locators. NOT_ACCESSIBLE uses value:null and sources:[] with reason. End with P08_SUMMARY JSON of returned_keys and unresolved_keys arrays followed by P08_COMPLETE.

# ACCEPTANCE CRITERIA
A1: Exactly C04-05 and C04-06 once each, same R0062, both statuses explicit, one access record, 0 duplicates or extra IDs.
A2: 2/2 observed frame rates have exact body excerpts on physical page 6 with matching value, FPS, workload and stage conditions; 0 abstract anchors.
A3: Both approximate values preserve the printed approximation. Zero numerical precision or conditions inferred from the graph.
A4: Two parseable objects meeting schema and enums; key lists reconcile; unknowns explicit.
A5: One parent result, zero assignment overlap, no project edits.

# BOUNDARIES
R0062.pdf only. Do not alter files, search externally, resend any previous task, expand claims, infer statistics, repeat other keys or supply operational application details. Report evidence gaps explicitly instead of guessing.
