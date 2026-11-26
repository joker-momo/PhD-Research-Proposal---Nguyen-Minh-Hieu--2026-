# TASK
Correct only flagged evidence in HK261 full-text batch 01, parent Task 2418e1e9-4e07-4a47-be11-8c7a4112bca2, context 584bdcc4-936c-4210-972e-ee952e60bf5b.

# REQUIRED WORK
1. Read P03/P06 in restart_2026_11_26/protocol_restart.md and directly reopen only R0001, R0002, R0019 and R0022 under restart_2026_11_26/fulltext_retrieval/pdf/.
2. For R0001 recheck E4 and E7. The original response said both figures were missing. On physical PDF page 3, Fig. 2 and Fig. 3 appear under III. EXPERIMENT EVALUATION and have visible plots and captions. Check the evaluation conditions/results and judge substantive method/results despite the WIP track. IEEE lists R0001 as WIP at https://services.conferences.computer.org/2026/icws-program/; check published peer-review policy at https://services.conferences.computer.org/2026/info-for-authors/ . Reassess decision.
3. For R0001 and R0002 replace E5 conference date with the observed publisher's Date Added to IEEE Xplore, labelled as such (IEEE proof the proceedings record was public by that date, not conference date or local download). Check https://xplorestaging.ieee.org/document/11670054/ and https://ieeexplore.ieee.org/abstract/document/11670091/ against the exact DOI.
4. Replace only R0019 E4 and R0022 E2 with short continuous quotes that are actually on the cited 1-based physical page. For R0022 avoid table column fragments; check the prose in results around Figure 6. For R0019 use the actual simulation and results text; avoid phrases assembled across pages. Recheck the disposition for the four records.

# REQUIRED OUTPUT
Return exactly four JSON lines, no markdown. Each row: id, decision, primary, reason, e. e contains only patch keys defined here: R0001 E4/E5/E7, R0002 E5, R0019 E4, R0022 E2. Each entry [state,page,section,quote,note,source], state T/F/U; use PDF and physical page number, or actual HTTPS URL and page 0 with exact publisher field/quote. Use one verbatim quote per entry and support additional E7 facts with the checked PDF page/official policy URL in the note. Keep reasons concise with no unnecessary numbers. If unable to verify a requested assertion, explicitly mark U and identify what was checked.

# ACCEPTANCE CRITERIA
C1 four exact IDs and six exact correction fields with no additional scope. C2 100% adopted excerpts and physical pages or official fields verifiable. C3 all four decisions consistent with P03 and priority in P06. C4 zero unsupported claims about missing figures, publication dates or policy. Locked bibliography joins by ID.

# BOUNDARIES
Read-only, named files/sources only. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
