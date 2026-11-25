# Preserved candidate full text

This directory replaces the removed `sources/candidate_fulltext` cache symlink
for the six exact source versions cited by `interim_27report/eligibility_reaudit.csv`.
The binary/HTML artifacts remain local and ignored; `checksums.sha256` is the
tracked integrity and version ledger.

- `C02.pdf` and `C07.pdf` intentionally preserve the versions used by the
  27-report audit. They are not assumed equivalent to the corresponding
  `screening_46/pdf/` files.
- `C03.pdf`, `C04.pdf`, and `C08.pdf` preserve the cited PDF versions.
- `C06_pmc.html` preserves the cited PubMed Central HTML rendition; it has no
  substitute in the 46-PDF evidence pack.

The rollback copies remain under
`/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/cache_candidate_fulltext/`.
