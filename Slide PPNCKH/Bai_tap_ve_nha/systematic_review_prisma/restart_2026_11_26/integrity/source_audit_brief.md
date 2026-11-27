## TASK

Verify bibliographic identity and any formal correction, expression-of-concern or retraction notice for all 26 citations in the HK261 restart manuscript.

## REQUIRED WORK

1. Read the exact ID and DOI list below and, if accessible, `manuscript/sn_computer_science/references.bib` in the attached project. Treat the bibliography as input, independently checking against first-party sources.
2. Resolve each DOI against its publisher and/or Crossref. Record the exact titled work, authors in source order, year and venue. Give source-specific year distinctions if online-first and issue year differ. Flag discrepancies without editing the bibliography.
3. For each work inspect the publisher or Crossmark notice area and Crossref update/relations metadata as available. Report the actual URLs and whether a check succeeded or was blocked. If a notice exists, identify it, link it and state its type.
4. Return one Task result. If workers are available, assign each ID once with no overlap, reconcile centrally and state who handled which keys. If unavailable or unconfirmed, do the work in the parent and state that.
5. Allow no ambiguity about missing checks: mark any incomplete identity or notice determination explicitly with the blocking source/status.

## REQUIRED OUTPUT

Compact JSONL with exactly one object per ID. Enum for identity: VERIFIED, MISMATCH, UNRESOLVED. Enum for notice: NO_NOTICE_FOUND_AT_CHECKED_SOURCES, CORRECTION_FOUND, RETRACTED, CONCERN, UNRESOLVED. Example shape (example values are schematic):
`{"id":"R0001","doi":"10.1109/ICWS72778.2026.00154","title":null,"authors":[],"year":null,"venue":null,"identity":"UNRESOLVED","identity_url":null,"notice":"UNRESOLVED","checked_notice_urls":[],"notice_url":null,"issue":"Publisher and registry unavailable."}`
After the records give `returned_ids`, `unresolved_ids`, worker use and allocation, and `SOURCE_AUDIT_COMPLETE`. Preserve the bridge output markers.

## ACCEPTANCE CRITERIA

1. Exactly 26 unique expected IDs and DOI pairs, or an explicitly identified missing-ID shortfall (coverage criterion fails if any required row is missing).
2. Every VERIFIED or MISMATCH identity has a first-party URL and precise title, author sequence, year and venue. Every unavailable field is explicit.
3. Zero DOI/title duplicates after normalization.
4. Every notice disposition has actual first-party or authoritative registry evidence, or an explicit UNRESOLVED with attempted URLs and access/status. Do not assert absence beyond checked sources.
5. Every correction/retraction/concern has a traceable formal notice URL. Unsupported quantitative or status claims equal zero.
6. Unresolved list matches row statuses exactly. Worker-use statement and completion marker are present.

## BOUNDARIES

Native Gemini.app Task, research only, one consolidated result. No uploads of PDFs, no project edits, no credential use, no searching outside these 26 records except their notices, and no switching tools or authoring final prose. Do not invent bibliographic fields, access, relationships or dates.

Expected keys and DOI values:
- prisma2020 10.1136/bmj.n71
- R0001 10.1109/icws72778.2026.00154
- R0002 10.1109/icws72778.2026.00067
- R0003 10.1109/wcsp58612.2023.10405273
- R0006 10.1109/icpads67057.2025.11322921
- R0009 10.1109/tits.2025.3629117
- R0010 10.1109/wcnc57260.2024.10570535
- R0015 10.1109/bigcom61073.2023.00034
- R0019 10.1109/jiot.2022.3231341
- R0022 10.1109/icct67417.2025.11374232
- R0029 10.1109/iwcmc55113.2022.9824945
- R0044 10.1109/ispce-asia64773.2024.10756252
- R0045 10.1109/jiot.2026.3685675
- R0048 10.1109/tgcn.2025.3625726
- R0054 10.1109/lwc.2026.3743641
- R0059 10.1016/j.cja.2025.103564
- R0062 10.1109/mcom.002.2300129
- R0063 10.3389/fnbot.2026.1799054
- R0068 10.1109/access.2025.3572036
- R0071 10.1109/icc52391.2025.11162059
- R0073 10.3390/app142310832
- R0074 10.3390/drones10060410
- R0083 10.1016/j.iot.2024.101479
- R0089 10.1016/j.phycom.2023.102129
- R0095 10.1016/j.adhoc.2026.104347
- R0121 10.23939/ictee2026.02.144
