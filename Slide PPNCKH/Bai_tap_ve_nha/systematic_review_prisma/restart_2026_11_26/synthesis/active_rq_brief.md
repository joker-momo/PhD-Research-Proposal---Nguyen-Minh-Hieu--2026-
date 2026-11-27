# TASK
Produce structured research notes for ten named HK261 RQ1–RQ5 comparisons. Work from the active 46-study checkpoint and its pinned evidence. Return research evidence only.

# REQUIRED WORK
1. Open the attached canonical HK261 project. Use restart_2026_11_26/protocol_restart.md P02 and P10, synthesis/active_synthesis_input_index.csv and synthesis/active_synthesis_input_manifest.json under restart_2026_11_26. Use only the accepted per-ID P08/P09 derivatives and PDF originals identified in that index. Match each report to the index. Bibliographic metadata and duplicates were verified upstream and need not be repeated.
2. Verify project and source accessibility before synthesis. Prefer local PyMuPDF or Poppler for PDF reading and local MinerU, then Marker, for layout problems if available. If only the approved client file viewer is available, use it and report that fact. Keep work in the parent task. Report inaccessible sources explicitly and give a body-page locator or exact locked field for each cited ID.
3. Return these exact ten comparisons in the assigned scope. All examples are bounded to the listed reports. Avoid corpus frequencies and claims of predominance.
   - RQ1-A R0001 and R0014. Distinguish infrastructure tiers and model segments from the two levels of airborne-cluster execution and intra-cluster spatial partition.
   - RQ1-B R0092 and R0118. Distinguish layer partition with a chosen peer from placement and selection of experts. Keep the assignment unit separate from topology.
   - RQ2-A R0006 and R0064. Identify optimized decisions and constraints. Keep conditions of the evaluation distinct from the decisions.
   - RQ2-B R0058 and R0080. Contrast whole-request assignment with confidence-triggered feature/raw handling and the targets of optimization.
   - RQ3-A R0014 and R0137. Distinguish indoor and outdoor evaluation in the first report. In the second, distinguish physical profiling and reported policy deployment from modeled communications. Cite P09 D07 to qualify the setting.
   - RQ3-B R0118 and R0125. Evaluate comparability from P09 D04. Check differences in model complexity for the common-planner experiment and changes in aggregate resource capacity for workstation scaling.
   - RQ4-A R0002 and R0092. Distinguish simulated UAV failure with migration from changing neighbors/link interruption with reassignment or local handling. Retain the exact simulated conditions.
   - RQ4-B R0038 and R0292. Differentiate tested software/node disconnection and restart from planned handoff with recorded footage and hardware-in-the-loop evidence.
   - RQ5-A R0080 only. Copy the two paired quantitative rows, accuracy and latency, with the exact same model pair and GSUP comparator. Retain the published uncertainty and no statistical separation inference.
   - RQ5-B R0092 only. Copy the deadline-satisfaction row from the verified quantitative rows. Include the tested model, comparator, episode basis and all-arrived-task denominator. Include a P09 appraisal locator that bounds the evidence.
4. Every factual clause needs an evidence field and locator. Prefer 2–3 evidence objects per conclusion. Original physical PDF pages begin at 1. Name the section/table plus exact locked field/value or a short contiguous PDF excerpt. Keep uncertainty, denominator, conditions and baseline verbatim for each quantitative row.

# REQUIRED OUTPUT
Exactly ten single-line JSON claim objects and one final summary. This illustrates the exact syntax, with example values:
{"claim_id":"RQ1-A","finding":"Scoped comparison","evidence":[{"report_id":"RTEST","source_path":"restart_2026_11_26/extraction/example.json","key":"partition_assignment","locator":"physical p. 3, §II","support":"Exact source field value or exact PDF phrase"}],"quantitative":[]}
For quantitative rows, copy the complete accepted P08 row object verbatim into the quantitative list. Use this exact summary shape, including field id:
{"id":"SUMMARY","claim_count":10,"tools_used":["tool actually used"],"workers_used":false,"limitations":{"RQ1":"...","RQ2":"...","RQ3":"...","RQ4":"...","RQ5":"..."},"unresolved":[]}
For an unresolved item replace its unsupported content with an explicit item key, status, reason and source checked in unresolved. End with standalone HK261_ACTIVE_RQ_COMPLETE.

# ACCEPTANCE CRITERIA
10/10 exact unique findings or documented shortfall. Five separate limitations. Every adopted assertion links to matching original PDF page/section and accepted evidence, independently checked by Codex. The three numerical rows preserve original values, units, baselines, denominators, workloads, conditions and locators. Zero unsupported numbers, unauthorized IDs, pooled effects, unverifiable claims presented as verified or duplicate claim IDs. Each named report has a source locator. Each RQ3 finding and RQ5-B has a source-located engineering appraisal judgment. The summary includes the tool actually used and explicit unresolved keys.

# BOUNDARIES
Only the attached canonical HK261 project and named sources. No internet, unrelated data, filesystem edits, uploads, worker dispatch, new model runs, old 46-report corpus, manuscript prose, statistical pooling, submission or email. R0081, R0082 and R0132 remain awaiting classification. R0116 remains unretrieved.

Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
