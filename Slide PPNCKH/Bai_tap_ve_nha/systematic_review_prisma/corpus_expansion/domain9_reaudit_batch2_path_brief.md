## TASK

Repair exactly3 absolute file locators for S15,S16,S17 from rejected task01a2125e-a67f-7718-92ae-45c2f806e22f.

## REQUIRED WORK

1. Read /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/corpus_expansion/domain9_reaudit_batch2_notes.json. This is a file-locator correction,not new scholarly records;do not regenerate bibliographic metadata or ratings.
2. Verify the3 actual files under /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/sources/extracted_text_for_review/original20/:15_10.1016_j.cja.2025.103564.txt,2503.16146.txt,17_10.1016_j.iot.2024.101479.txt. The previous directory Bai_tap_ve_hoc_nha is wrong;the real directory is Bai_tap_ve_nha.
3. Return existing absolute paths and one existing body line range for each. Report missing evidence rather than guess. Do not change file contents.

## REQUIRED OUTPUT

One JSON object:{"mappings":[{"study_id":"S15|S16|S17","source_file":"existing absolute path","verified_body_locator":"existing line range"}],"summary":{"requested":3,"returned":3,"duplicates":0,"files_written":0},"unresolved_items":[]}

## ACCEPTANCE CRITERIA

P1: Exactly3 unique mappings,S15,S16,S17;all3 absolute source_file paths exist and refer to the supplied source filename;duplicates0.
P2: Every mapping has a body line locator within its actual source;unsupported claims0;no changed scholarly metadata,ratings or eligibility.
P3: One JSON object;summary requested3,returned3,duplicates0,files_written0;unresolved items explicit. Bibliographic-record fields are inapplicable because this task returns only path mappings to existing records.

## BOUNDARIES

Read-only locator verification;no final prose,project/scratch writes,downloads,credentials,private files or invented paths. Gemini primary;quota-only identical brief on gpt-5.6-luna/low;no escalation.
