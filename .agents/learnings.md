# Stream Coding Learnings

### L082: Avoid Exact Emoji String Matching Across Platforms
- **Date:** 2026-05-21
- **Source:** Air Liquide — create_analysis.gs
- **Evidence:** Empty filter results when comparing `String(r[col["IT_Flag"]]) === "⚠️ IT"` in Apps Script, while a substring check `val.indexOf("IT") !== -1` perfectly matched the 81 IT use cases.
- **Anti-pattern:** Performing exact string comparison (`===`) on cells containing emojis across different systems (e.g., Python `openpyxl` writing to Excel, converted to Google Sheets). Emojis like `⚠️` (`\u26a0\ufe0f`) may have their variation selectors (like `\ufe0f`) stripped or altered upon import/conversion.
- **Fix:** Use robust substring searches (e.g., `indexOf` or regex test on the non-emoji part of the string) or normalized keys to match flag cells, avoiding exact emoji string equality checks.

### L083: Exhaustive Scan Before Correction on Hardcoded-Text Scripts
- **Date:** 2026-05-21
- **Source:** Air Liquide — generate_docx.py / generate_pptx.py orthographic correction
- **Evidence:** 4 iterative correction passes across multiple sessions still left 41+ unaccented French words in generate_pptx.py. A single automated regex scan on all string literals caught everything in one shot.
- **Pattern to reproduce:** When fixing hardcoded text in a generation script (docx, pptx, pdf), the first action MUST be: (1) extract all string literals with regex, (2) run a domain-specific word list against them, (3) fix ALL hits in a single `multi_replace_file_content` call. Never correct by example.
- **Anti-pattern:** "Fix what's visible in the screenshots, re-run, repeat." This creates rework cycles because screenshots only show a fraction of the output. The scan is the gate.

### L084: `python3 -m py_compile` is Mandatory After String Corrections on Python Scripts
- **Date:** 2026-05-21
- **Source:** Air Liquide — generate_docx.py / generate_pptx.py
- **Evidence:** French f-strings with accented characters (e.g., `f"…à réaliser…"`) can introduce syntax errors if quotes or escape sequences are misaligned during a multi-replace. Compile check catches this in <1s before running the full generation (which takes 30s+).
- **Fix:** Always run `python3 -m py_compile <file>` immediately after any string correction pass, before executing the script.
