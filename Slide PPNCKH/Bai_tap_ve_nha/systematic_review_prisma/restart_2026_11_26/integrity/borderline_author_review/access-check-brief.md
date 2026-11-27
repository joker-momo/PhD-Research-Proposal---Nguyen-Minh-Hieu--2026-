# TASK
Verify native Gemini.app parent read access for the five authorized local PDFs after correction e8b6e8c4-3b18-4410-9c3a-aa4e19bbdcad lost local file access on worker wake-up turns.

# REQUIRED WORK
1. Work entirely in the current parent Mac-connected turn. Do not invoke subagents or conversation tools. Open each exact file under restart_2026_11_26/fulltext_retrieval/pdf/ using client:view_file as attached. R0001.pdf page 3; R0113.pdf page 7; R0145.pdf page 6; R0223.pdf page 5; R0292.pdf page 4.
2. Return an exact short contiguous body quotation for the indicated physical page. If an individual PDF or the tool is unavailable, record the precise error or limitation immediately.

# REQUIRED OUTPUT
Five JSONL lines with {"id":"R0001","status":"READ","source":"restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf","page":3,"locator":"section label","quote":"exact five to ten words","gap":null}. Allowed status READ or NOT_ACCESSIBLE; if latter, locator and quote null and gap a specific reason. Return one summary JSON line with actual_tools, workers_used and inaccessible_ids, then HK261_PARENT_ACCESS_COMPLETE.

# ACCEPTANCE CRITERIA
- Exactly five expected IDs, five quotations independently verified in the exact physical pages for a successful check, zero duplicate or missing IDs, quotations and locators exact.
- No worker/task handoffs, no unsupported numbers or inferred file access. Explicitly list each unresolved access. No new bibliographic records or eligibility assessments.
- One consolidated response with marker HK261_PARENT_ACCESS_COMPLETE.

# BOUNDARIES
Read-only access test, no extraction or conclusion, no web, no downloads, no project edits. Only the named original local files. Do not invent access, data, quotes or locators and do not use memory of earlier files. If client:view_file is missing, return NOT_ACCESSIBLE. No subagents.
