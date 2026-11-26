# TASK
Replace just R0121 E7 in Batch 04. Original Task 7df7c644-f0ae-4dd9-95b4-7c5e68d023ff; previous correction 0a85c729-29cd-48c0-bd52-6a5b9f239284, context e21403f3-5c19-4c8e-869f-49bc073dbc42.

# REQUIRED WORK
1. Verify publisher policy at https://science.lpnu.ua/ictee/paper-review-process, heading Paper Review Process, item 4. The exact contiguous evidence is "is then sent to two independent reviewers" followed by parenthetical double-blind peer review. This is the journal's policy as verified on its own official site. The previous URL /node/23327 resolves to the unrelated SJS journal and is not usable.
2. Check R0121 PDF §§3,5,6 in the attached project for substantive method and analytical evaluation (current Step 09 source). Keep the previous E5 decision and other fields. Return the E7 patch only; point to the supplied verified ICTEE evidence if your browser cannot load it.

# REQUIRED OUTPUT
Exactly one JSONL line with id R0121, decision, primary, reason, e containing E7 only. E7 is [T/F/U,0,"Paper Review Process, item 4", exact quote, note with the PDF section check, exact official URL]. Primary must be empty for INCLUDE or AWAITING_CLASSIFICATION.

# ACCEPTANCE CRITERIA
One unique requested ID and one requested field, quote matches the actual ICTEE page, other 6 criteria unchanged, zero unsupported numbers, genuine uncertainties explicit.

# BOUNDARIES
Read directly from the attached project and the exact ICTEE policy page. No other records, no file edits, no manuscript. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Any unverified fact must be clearly marked. The locked index supplies scholarly metadata.
