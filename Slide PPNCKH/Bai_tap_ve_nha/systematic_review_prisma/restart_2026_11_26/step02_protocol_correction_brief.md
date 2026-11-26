# TASK
Correct the rejected protocol audit for parent task fb0bd54c-1cbe-4c73-87f7-9e4703a07478 (context936b6a79-101a-4763-a4a8-89666aa9fe39): replace only T02, T03 and T12 using draft1.1 and the direct user publication-type decision. Return structured evidence only.

# REQUIRED WORK
1. Read the supplied updated protocol_restart.md, approved_plan.md, step01_inventory.md, step02_user_decision.md and original step02_app_result_quarantined.json.
2. Fix failed C2: T12/P12 quote used an ellipsis that does not occur verbatim. Supply exact contiguous excerpts with correct section locators; never join fragments as one quote.
3. Reassess T02: user explicitly selected peer-reviewed journal/conference full reports only, with substantive method/evaluation. Verify updated E7 implements that choice and short-report operational thresholds; do not ask the user again or introduce another publication class.
4. Reassess T03: draft now states date-interval and assessed-report-version rules. Check boundary uncertainty is explicit rather than guessed. Preprints are no longer eligible primary reports.
5. Return exactly3 replacement checks T02,T03,T12, preserving original check schema. Do not return or alter the other9 checks. List remaining unresolved issues explicitly, or an empty array if none within these3 topics.

# REQUIRED OUTPUT
One JSON object only: {"parent_task_id":"fb0bd54c-1cbe-4c73-87f7-9e4703a07478","replacement_checks":[{"id":"T02","status":"CONSISTENT|ISSUE|UNRESOLVED","locators":[{"file":"protocol_restart.md","section":"P03","quote":"exact contiguous excerpt"}],"finding":"bounded audit finding","required_correction":null,"requires_user_approval":false}],"unresolved_items":[],"scholarly_records":[],"scholarly_records_not_applicable":"Protocol consistency audit only","actions_taken":{"external_searches":0,"records_screened":0,"project_files_changed":0,"final_prose_written":false}}

# ACCEPTANCE CRITERIA
K1: Valid JSON; correct parent ID; exactly3 unique IDs T02,T03,T12; other check replacements=0.
K2: Every replacement has all fields; every quote matches a contiguous substring in the named supplied file and the named section; missing/invalid locators=0. Cross-document claims have both locators.
K3: T02 explicitly verifies userdecision and E7 peerreview/fullreport/method/evaluation restrictions. T03 verifies version/dateinterval uncertainty. T12 exact plan/protocol evidence supports sequence/integrity boundaries.
K4: Every factual claim supported; unsupported quantitative claims=0; old46 imports=0; newsearch/screening/project edits/finalprose=0; scholarlyrecords0 with explicitN/A; no duplicateIDs.
K5: ISSUE has atomic correction; UNRESOLVED listed; CONSISTENT correctionnull; no unapproved scope/sequence changes; sourcecontext unchanged.
K6: After replacing these3 checks, original C1–C9 must be satisfiable. Any further defect outside the3requested IDs must be reported as unresolved, not silently patched or fabricated.

# BOUNDARIES
Same step02 and nativeGemini.app only; read only attached files. No browsing, research discovery, screening, project/context edits, manuscript prose, portal/email, or secrets. Do not relaunch parenttask or claim its transport failure was fixed. Missing evidence remains explicit. Codex handles the reconciliation and independent acceptance review.
