# TASK
Correct the remaining three exact evidence fields in HK261 full-text Batch 01, parent correction task ae2aeba0-8e4e-40e6-bc97-a7120eac4a0e, context f650b18a-c5fd-4dba-a5bc-af2ec2f97548.

# REQUIRED WORK
1. Read P03/P06 and directly open R0019.pdf in restart_2026_11_26/fulltext_retrieval/pdf/. On physical p.12 use the short verbatim figure 9 caption "Comparing optimal and RL solutions in terms of latency." as the E4 locator if it is confirmed; describe the evaluation plainly and omit other numbers. Do not join prose from different pages. Return E4 for only R0019.
2. Apply E5 for R0001 and R0002 using evidence transcribed and independently checked by Codex from the publisher page. For R0001 the matching IEEE record https://xplorestaging.ieee.org/document/11670054/ has DOI 10.1109/ICWS72778.2026.00154 and the exact field "Date Added to IEEE Xplore: 07 September 2026". For R0002 the matching IEEE record https://ieeexplore.ieee.org/abstract/document/11670091/ has DOI 10.1109/ICWS72778.2026.00067 and the same exact field. Use this supplied field as proof of availability by the cutoff; label it Date Added, not the conference date or presumed exact first publication. If your browser blocks the link, acknowledge this is supplied authoritative evidence; do not state that you opened it. Both prior merged E1–E4 and E6–E7 were T for these two IDs.
3. Recompute the three dispositions. primary is empty for INCLUDE or AWAITING_CLASSIFICATION; an E-code appears only for EXCLUDE. No unrelated evidence changes.

# REQUIRED OUTPUT
Exactly 3 plain JSON lines, keys id, decision, primary, reason, e. e has only E5 for R0001 and R0002, and only E4 for R0019. Evidence is [state,page,section,quote,note,source]; use "PDF" for the short R0019 cite. For E5 page=0, exact field and exact supplied URL. Keep reason short.

# ACCEPTANCE CRITERIA
C1: 3 exact IDs and 3 exact patch keys, zero duplicates. C2: 3/3 exact source locators/fields. C3: 3/3 dispositions and primary fields consistent with P06. C4: zero claims of visits not performed or guessed numerical details. Locked bibliographic metadata joins by ID.

# BOUNDARIES
Read-only, no project edits. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
