## TASK

Supply the single missing C01 source_locators field from rejected task01a21225-4f5a-73b5-a21e-dfedbfa9e9db.

## REQUIRED WORK

1. Read corpus_expansion/priority_access_batchA_repair_notes.json in /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma. The prior repair contains7 extraction changes instead of8;only the source_locators rollup is missing.
2. Return one C01 scholarly record with its verified title,all4 authors,year2026,venue Drones,DOI10.3390/drones10060410 and publisher URL.
3. Aggregate the existing supported locators:method Sections3.1-3.3;evaluation4.1-4.8,explicitly4.7 and4.8;physical-validation limitation5.5;Funding,Data Availability and Conflicts sections. Use the original subsection locators;no new research claim or comparative effect.
4. Report unresolved evidence explicitly. Do not write files or modify the manuscript.

## REQUIRED OUTPUT

Exactly one JSON object:
{"records":[{"candidate_id":"C01","title":"...","authors":["..."],"year":2026,"venue":"Drones","doi":"10.3390/drones10060410","source_url":"https://www.mdpi.com/2504-446X/10/6/410","source_locators":"supported URL plus explicit subsection list","unresolved_items":[]}],"summary":{"records":1,"duplicates":0,"files_written":0}}

## ACCEPTANCE CRITERIA

D1: Exactly1 record,C01;all6 scholarly identity fields present and matching the cited publisher/supplied notes.
D2: source_locators is nonempty and explicitly includes3.1-3.3,4.7,4.8,5.5 and funding/data/conflict locators with publisher URL.
D3: Every factual claim has publisher URL or supplied-file locator;unsupported quantitative claims=0;comparative effects=0;duplicates=0;unresolved_items is an array.
D4: Exactly1 JSON object,summary.records=1,files_written=0;no manuscript prose or project edits.

## BOUNDARIES

Read-only structured locator synthesis only;do not invent evidence,run new experiments,download files,edit projects,handle credentials or bypass access controls. Gemini3.8 Flash primary;only router-recognized provider quota authorizes the identical brief on gpt-5.6-luna/low. No model/effort escalation.
