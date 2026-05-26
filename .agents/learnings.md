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

### L089: Top-Align Visual Charts in Dashboard-Style Apps Script Sheets
- **Date:** 2026-05-26
- **Source:** Air Liquide — create_analysis.gs
- **Evidence:** The split "Focus Medium & Large" tab generated successfully, but the charts were placed starting at Row 71 (historical location) leaving Rows 4-70 completely empty, causing the user to think the charts were not created. Repositioning them to start at Row 4 resolved the issue immediately.
- **Anti-pattern:** Anchoring visual charts at historical/legacy rows (e.g., Row 71) when the data tables they depend on are moved to hidden/out-of-view columns (e.g., Column AS/45). This leaves the top of the worksheet blank and breaks the user experience.
- **Fix:** When moving data source tables to hidden columns to create a clean visual dashboard, always ensure that charts are top-aligned starting from Row 4 (or immediately below the header banner), and lay them out in a clean, side-by-side grid structure.

### L090: Use Blank Style Templates to Preserve User-Customized Styles and Embedded Fonts in Generation Scripts
- **Date:** 2026-05-26
- **Source:** Air Liquide — generate_docx.py
- **Evidence:** The user customized the Word report by embedding two Google Fonts (Poppins, Roboto, totaling 600 KB of TTF files) and adjusting layout margins. A naive script rerun would overwrite the file, wiping out all these changes. Generating a blank style template `assets/template.docx` (all paragraphs and tables cleared) and loading it in Python via `Document(template_path)` completely preserved all custom designs and embedded fonts.
- **Pattern to reproduce:** For any automated document generation script (Word, PowerPoint, PDF) where the output is subject to manual user customization (such as font embedding, custom margins, or headers/footers):
  1. Create a blank template (`assets/template.docx` or `.pptx`) by programmatically loading the user's styled output and stripping all text content (paragraphs and tables) while keeping styles, settings, and media.
  2. Modify the script to check for this template, load it, and clear any single placeholder paragraph if present, instead of starting from `Document()`.
  3. Keep the styling code inside a fallback block `if not TEMPLATE_FILE.exists(): apply_base_styles(doc)` to ensure backward compatibility and clean testing.
- **Anti-pattern:** Overwriting a customized output file from scratch, which silently destroys all manual styles, custom theme adjustments, and embedded fonts.

### L091: Dynamic Column Letter Resolution for Formula-Based Apps Script Dashboards
- **Date:** 2026-05-26
- **Source:** Air Liquide — create_analysis.gs
- **Evidence:** Refactored 100% of the Synthèse and Focus Sheets to use COUNTIF, COUNTIFS, SUM, and VLOOKUP formulas. 4 test scenarios passing with 100% dynamic updates.
- **Pattern:** When generating Google Sheets formulas programmatically in Apps Script (such as `=COUNTIF(Catalogue!$C:$C, AS6)`):
  1. Never hardcode column letters inside formula templates.
  2. Implement a `getColumnLetter(colIndex)` helper to dynamically resolve 1-based column indices into A1 notation column letters.
  3. Resolve all target column letters dynamically using dynamic header indices (e.g. `col["Complexity_Tier"] + 1`).
  4. Construct the formula string using template literals (e.g. `Catalogue!$${tierLetter}:$${tierLetter}`) to ensure the formulas will never break if Catalogue columns are added, removed, or reordered.
- **Anti-pattern:** Writing formulas with hardcoded column letters (e.g., `=COUNTIFS(Catalogue!$C:$C, ...)`) or hardcoded row counts. This immediately breaks if columns are reordered or if new rows are added to the source catalog.

### L092: Dynamic Multi-Category Comma-Separated Data Representation in Google Sheets Charts
- **Date:** 2026-05-26
- **Source:** Air Liquide — create_analysis.gs (G7 Stacked Column Chart)
- **Evidence:** Added a 100% dynamic stacked column chart (G7) showing the distribution of the top 8 data sources across the 7 functional families (F1..F7), automatically updating on Catalogue changes.
- **Pattern to reproduce:** When creating a native stacked chart to represent the distribution of a comma-separated column (e.g. `Data_Sources`) across another categorical field (e.g. `Family`):
  1. Dynamically extract the top $N$ unique items from the dataset at runtime (excluding stubs/placeholders like "A revoir avec le builder") to serve as the chart series.
  2. Structure the hidden data preparation table with categories (e.g. Families F1..F7) in **rows** and the top $N$ items as **columns**. This matches Sheets' native categorical chart orientation (row headers = X-axis, column headers = series) without requiring manual transpositions.
  3. Use wildcard `COUNTIFS` formulas (e.g. `=COUNTIFS(Catalogue!$Family, $RowLabel, Catalogue!$DataSources, "*" & ColumnHeader & "*")`) to dynamically search for each item inside the comma-separated strings.
- **Anti-pattern:** Including "Total" or "% Global" columns inside the stacked chart's data range, which heavily distorts the visual proportions by competing with the individual stacked parts.

### L093: XML-Level Sequential Splitting for Segmented Document Generation
- **Date:** 2026-05-26
- **Source:** Air Liquide — generate_report_table.py
- **Evidence:** 11 segmented documents successfully split from a master `[REPORT] AI builders.docx` file, preserving all inline formatting, margins, list numbering, and headers/footers with zero schema errors.
- **Pattern to reproduce:** When a master document needs to be split sequentially based on Heading sections:
  1. Load a copy of the master document, and clear all body paragraphs and tables (e.g. using `remove()` on their XML parents). This preserves the Document styles, settings, headers, and footers as a blank template.
  2. Iterate sequentially over `doc.element.body` to preserve the exact relative order of paragraphs and tables.
  3. Deep copy each XML element using `copy.deepcopy(element)`.
  4. Append the duplicated elements using `sectPr[0].addprevious(new_element)` inside the cleared template body to ensure the final section properties (`w:sectPr`) remain at the very end of the body, guaranteeing standard-compliant XML.

### L094: Split Complex Deliverables to Accommodate Shared Online Documents
- **Date:** 2026-05-26
- **Source:** Air Liquide — generate_report_table.py
- **Evidence:** Overwriting a client-shared Google Doc by re-importing a full `.docx` would wipe out active comments, revision history, and link IDs. Splitting the document into 11 section-based `.docx` files allowed the user to copy-paste updated parts safely.
- **Anti-pattern:** Assuming that automated report generation scripts should only output a single monolithic file. In real-world enterprise environments, deliverables are uploaded to platforms like Google Drive or SharePoint, converted to online formats, and shared with clients. Re-generating the full monolith blocks local-to-cloud updates.
- **Fix:** For any automation script generating report-style outputs, verify if the deliverable will be shared online. If yes, the script must support a "split mode" or automatically output section-segmented files, enabling users to copy-paste updated components cleanly into their shared cloud documents.


