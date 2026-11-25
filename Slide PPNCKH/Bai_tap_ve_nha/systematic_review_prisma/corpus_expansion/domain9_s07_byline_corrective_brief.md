## TASK

Correct only the duplicated S07 author in rejected task01a21251-5851-757e-b48e-ae21213a0cc9.

## REQUIRED WORK

1. Read /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/sources/extracted_text_for_review/original20/10.1109_MCOM.002.2300129.txt lines5-9 and interim_26report/eligibility_reaudit.csv rowS07, after completing the project's onboarding.
2. The prior response listed Jiawen Kang twice,producing8 names. Return the original ordered7-author byline with no duplicate author. Preserve verified title,year,venue,DOI and source locator.
3. Return no other study or changed appraisal;report unresolved items.

## REQUIRED OUTPUT

Exactly1 JSON object:
{"records":[{"study_id":"S07","title":"...","authors":["7 source-listed names in order"],"year":2024,"venue":"...","doi":"10.1109/MCOM.002.2300129","source_locator":"absolute supplied txt path:lines5-9","unresolved_items":[]}],"summary":{"records":1,"authors":7,"duplicate_authors":0,"duplicate_records":0,"files_written":0}}

## ACCEPTANCE CRITERIA

J1: Exactly1 S07 record and exactly7 authors,ordered exactly as original byline;duplicate author names0.
J2: Title,authors,year,venue and DOI match supplied original and identity table;source locator exists;every factual claim source-located;unsupported quantitative claims0.
J3: One JSON object only;summary records1,authors7,duplicate_authors0,duplicate_records0,files_written0;unresolved array explicit;no other ratings/eligibility/prose changed.

## BOUNDARIES

Read-only byline extraction only. No project/scratch writes,downloads,private data,credentials,manuscript prose or invented evidence. Gemini primary;recognized quota only may route identical brief to gpt-5.6-luna/low;no escalation.
