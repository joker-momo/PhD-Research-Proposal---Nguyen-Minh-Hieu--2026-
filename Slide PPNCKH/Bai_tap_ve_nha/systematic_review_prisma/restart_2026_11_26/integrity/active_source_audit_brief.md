# TASK
Check bibliographic identity and documented corrections, expressions of concern and retractions for the 47 exact HK261 references below.

# REQUIRED WORK
1. Read the current manuscript bibliography at manuscript/sn_computer_science/references.bib in the approved attachment. For the 46 recorded DOIs, consult the Crossref works record or first-party bibliographic metadata. Check exact title, lead-to-last author sequence, year and venue. Resolve mixed online/issue year only where supported. Verify R0113 by exact title, the publisher article URL below and the masthead on physical PDF p. 1. Do not assign a DOI to R0113 without an actual exact record.
2. For each ID, consult Crossref publisher-supplied update or reverse links, the official Crossref Retraction Watch data, publisher or Crossmark notice evidence as available. Report only the sources actually checked and their actual status. Report titles and available notice types exactly. Source-specific unknowns remain explicit. Crossref absence is limited to the checked record and index. It is not publisher-level clearance.
3. Return one consolidated result. If internal workers are available and you choose to use them, assign each ID exactly once and report their IDs and non-overlapping allocations. Otherwise do the work in the parent. Use only authorized attachment access and public first-party sources. State tools used.

# REQUIRED OUTPUT
Use a compact JSONL object per ID. Example:
{"id":"R0001","doi":"10.xx/xx","t":"exact title","a":["A Last","B Last"],"y":2026,"v":"venue","i":"VERIFIED","s":"https://api.crossref.org/works/10.xx/xx","n":"NO_NOTICE_FOUND_AT_CHECKED_SOURCES","c":["https://api.crossref.org/works/10.xx/xx"],"u":null,"g":null}
Use identity VERIFIED, MISMATCH or UNRESOLVED. Use notice NO_NOTICE_FOUND_AT_CHECKED_SOURCES, CORRECTION_FOUND, RETRACTED, CONCERN or UNRESOLVED. Field c lists actual checked notice URLs, u the formal notice if one was found, and g a specific unresolved or blocked reason if applicable. R0113 can use the supplied PDF path for identity, PDF page 1, and DOI_NOT_FOUND. Use short safe JSON strings with no extra literal quotation marks. Final separate object id SUMMARY, reference_count, tools_used, workers_used, allocations, unresolved_ids, and standalone HK261_ACTIVE_SOURCE_AUDIT_COMPLETE.

# ACCEPTANCE CRITERIA
47 unique expected IDs with the exact 46 DOI strings and the R0113 DOI_NOT_FOUND marker, or a declared shortfall. Every adopted identity has matching title, ordered authors, year, venue and supplied-file locator or first-party source. Zero unsupported scholarly status claims, zero duplicate keys or accidental normalized DOI duplicates. Each no-notice result is scoped to actual checked URLs. Each notice has an exact official URL. Every unresolved item appears in the summary with a reason in its row. Scope is the current 46 studies and PRISMA statement.

# BOUNDARIES
Read-only research, no project changes, manuscript drafts, PDF upload, credentials, submission or email. Do not revisit screening, add studies, include record IDs outside this exact list, or read other local paths. For R0113 use https://ajaccm.com/journal/index.php/ajaccm/article/view/771 and restart_2026_11_26/fulltext_retrieval/pdf/R0113.pdf, p. 1. Publisher article may be unavailable. Report actual source access and distinguish a local masthead with no displayed DOI from an exhaustive identity search.

Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.

Exact reference keys:
- R0001 10.1109/icws72778.2026.00154
- R0002 10.1109/icws72778.2026.00067
- R0003 10.1109/wcsp58612.2023.10405273
- R0006 10.1109/icpads67057.2025.11322921
- R0009 10.1109/tits.2025.3629117
- R0010 10.1109/wcnc57260.2024.10570535
- R0014 10.1109/tmc.2024.3427420
- R0015 10.1109/bigcom61073.2023.00034
- R0019 10.1109/jiot.2022.3231341
- R0022 10.1109/icct67417.2025.11374232
- R0029 10.1109/iwcmc55113.2022.9824945
- R0036 10.1109/tccn.2025.3641511
- R0038 10.1109/wincom65874.2025.11313424
- R0043 10.1109/ucom59132.2023.10257649
- R0044 10.1109/ispce-asia64773.2024.10756252
- R0045 10.1109/jiot.2026.3685675
- R0048 10.1109/tgcn.2025.3625726
- R0054 10.1109/lwc.2026.3743641
- R0058 10.1142/s0218126626440020
- R0059 10.1016/j.cja.2025.103564
- R0062 10.1109/mcom.002.2300129
- R0063 10.3389/fnbot.2026.1799054
- R0064 10.1016/j.comnet.2025.111540
- R0068 10.1109/access.2025.3572036
- R0071 10.1109/icc52391.2025.11162059
- R0073 10.3390/app142310832
- R0074 10.3390/drones10060410
- R0075 10.1109/jiot.2026.3746980
- R0077 10.1016/j.sysarc.2026.103804
- R0080 10.1109/vtc2025-fall65116.2025.11310097
- R0083 10.1016/j.iot.2024.101479
- R0089 10.1016/j.phycom.2023.102129
- R0090 10.1109/icoeit63558.2025.11457712
- R0092 10.1109/jiot.2026.3740035
- R0095 10.1016/j.adhoc.2026.104347
- R0106 10.1109/twc.2025.3573654
- R0107 10.1109/tvt.2026.3733130
- R0110 10.1109/tvt.2026.3755123
- R0113 DOI_NOT_FOUND
- R0118 10.1109/jiot.2026.3755315
- R0121 10.23939/ictee2026.02.144
- R0125 10.1109/sm69703.2026.11614110
- R0137 10.1109/tcsvt.2026.3745821
- R0145 10.1145/3774655
- R0223 10.1145/3760269.3760299
- R0292 10.1145/3711875.3737661
- prisma2020 10.1136/bmj.n71
