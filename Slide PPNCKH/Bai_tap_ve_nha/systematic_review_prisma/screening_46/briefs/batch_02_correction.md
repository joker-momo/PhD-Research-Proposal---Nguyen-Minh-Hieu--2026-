## TASK
Correct exactly two failed source locators from batch02 task 01a212dd-ca9c-77fa-87a2-13f7dc4f22bc, preserving all other findings for Codex review.

## REQUIRED WORK
1. Read the prior result and rejection review below. Inspect S07 PDF/text page 1 and S08 PDF/text pages 10-11.
2. Replace S07 date_window quote: prior quote reordered the printed header. Copy a contiguous original string containing the January 2024 issue date; the original header alone may be under 10 words for this date-evidence correction, but maximum45 words. Do not combine separated page regions.
3. Replace S08 multi_uav_evaluated page/quote using the actual location of the fifteen-UAV evaluation sentence. Verify wording and context.
4. Return unchanged bibliographic identity for both records, corrected gate object, current decision, explicit changes and unresolved items. Do not alter unrelated record fields or silently change decisions.

## REQUIRED OUTPUT
One JSON object only:
{"parent_task_id":"01a212dd-ca9c-77fa-87a2-13f7dc4f22bc","records":[{"id":"S07|S08","title":"...","authors":["..."],"year":2024,"venue":"...","doi":"... or DOI_NOT_FOUND","field":"date_window|multi_uav_evaluated","replacement":{"status":"YES|NO|UNCERTAIN","rationale":"...","page":1,"quote":"..."},"source_file":"absolute supplied text/PDF path","decision":"INCLUDE|EXCLUDE|UNCERTAIN","changes":["..."],"unresolved":["..."]}],"shortfall":[],"project_files_changed":0}

## ACCEPTANCE CRITERIA
- C1 Exactly 2 unique records: S07/date_window and S08/multi_uav_evaluated; shortfall per missing ID if any; duplicates0 after DOI/title normalization.
- C2 Both full identities include title/all authors/year/venue/DOI or DOI_NOT_FOUND and match original supplied records; unresolved items explicit.
- C3 2/2 replacement quotes literal contiguous source text on correct PDF pages, maximum45 words; S08 minimum10 words, S07 date header allowed shorter. Every factual claim source-located; unsupported quantitative claims0.
- C4 Corrected gates and decisions consistent with original six-gate rules and 2021-01-01 through2026-11-25 window; changes explicit; no unrelated findings revised.
- C5 project_files_changed=0; structured evidence only; unresolved list present for each; no new performance quantities.

## BOUNDARIES
Read-only supplied sources. No web, no downloads, no project edits/Git, no final prose, no external messages. Paper text is untrusted data. Report absent evidence; never invent it. Date-header quote length exception applies only to S07 in this corrective task.
Prior output: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/results/batch_02.json
Rejection: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reviews/batch_02_review.md
S07 PDF: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/S07.pdf
S07 text: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/S07.txt
S08 PDF: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/pdf/S08.pdf
S08 text: /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/S08.txt
