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

### L085: PyltechDeck template methods block font-size control — rebuild manually
- **Date:** 2026-05-22
- **Source:** Air Liquide — generate_pptx.py layout corrections (slides 05, 12)
- **Evidence:** `add_content_3_blocs` and `add_content_4_blocs_horiz` use fixed font sizes baked into the PPTX master — 2 rework iterations on slide 12 (first attempt used template, second rebuilt manually). Manual rebuild with `add_content_card(body_font_size=13)` resolved in 1 pass.
- **Anti-pattern:** Using `deck.add_content_N_blocs(...)` when the spec requires a specific body font size. The template method locks all text to the master's default size.
- **Fix:** When `body_font_size` matters (>11pt or explicit spec requirement), use `deck.add_schema()` + `add_content_card(..., body_font_size=N)` instead of template shortcuts. Check font control requirement BEFORE choosing the layout method.

### L086: PPTX card line_h must account for word-wrap on narrow cards
- **Date:** 2026-05-22
- **Source:** Air Liquide — generate_pptx.py (slides 05, 08, 21)
- **Evidence:** With `body_font_size=13` and card width ≤ 3.0", bullet text wraps to 2 lines. `line_h=0.6"` caused the next bullet to overlap the wrapped line. Increasing to `line_h=0.78"` eliminated all overlap in 1 pass.
- **Pattern:** For `body_font_size > 11`, set `line_h = Inches(0.78)` (not 0.42"). For card widths < 3.0" at any font size, pre-verify: (card_width - 0.3") / (font_size_pt × 0.014) ≈ chars per line. If a bullet exceeds this → it wraps → increase line_h.
- **Fix:** Add font-size/card-width → line_h mapping to `add_content_card` as a lookup table instead of a binary `if body_font_size <= 11`.

### L087: Monolithic `main()` with External Rendering Dependency Blocks All Unit Testing
- **Date:** 2026-05-22
- **Source:** Air Liquide — generate_pptx.py refactor (34-test failure recovery)
- **Evidence:** 34/220 tests failed with `AttributeError: module 'generate_pptx' has no attribute 'SLIDE_W'`. Root cause: `main()` contained all slide logic and delegated rendering to PyltechDeck, leaving zero testable public surface. Full refactor (9 `build_*()` functions + module-level constants) required. Zero additional iterations after refactor — 220/220 passed.
- **Anti-pattern:** Writing a generation script where `main()` contains all business logic AND delegates rendering to an opaque third-party library (PyltechDeck, ReportLab, Jinja env, etc.). The tests can't reach anything. `AttributeError` on the first constant is the canary.
- **Fix:** For any generation script, the spec MUST require: (1) module-level constants (`SLIDE_W`, `SLIDE_H`, color palette), (2) low-level drawing helpers (`add_rect`, `add_textbox`, etc.) as public functions, (3) one `build_<slide_name>(prs, df, ...)` function per slide — all independently callable with a plain `Presentation()` object. `main()` is only the orchestrator. Write this structure BEFORE the first line of rendering code.

### L088: HARDEN Re-run Did Not Catch Test Regression — Human Had to Intervene
- **Date:** 2026-05-22
- **Source:** Air Liquide — generate_pptx.py HARDEN cycle
- **Evidence:** A previous HARDEN cycle completed and committed without running `pytest`. The 34-test regression (from `gp.SLIDE_W` missing) persisted undetected across at least one session. The user had to explicitly ask "on est toujours à 99 sur les tests u?" to surface it.
- **Anti-pattern:** Treating "HARDEN completed" as equivalent to "tests pass". The Commit Gate lists `verify.py` as item 1 — but without a local `verify.py` script, the agent substituted a softer check and silently moved on. Human enforcement was required.
- **Fix:** When `verify.py` is unavailable (class (d) waiver), the mandatory substitute is `python3 -m pytest --tb=short -q` and the output MUST appear in the HARDEN log before the commit step. Absence of pytest output in HARDEN = gate not passed. Add this as an explicit fallback in the Skip/Waiver Register template: "verify.py unavailable → run pytest, paste output, confirm N passed 0 failed."
