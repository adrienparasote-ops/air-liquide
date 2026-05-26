<!-- Generated: 2026-05-26 | Files scanned: 6 | Token estimate: ~420 -->

# Backend Pipeline Map

## Data Pipeline
Raw Excel (`assets/`) → `generate_catalog.py` → Cleaned Excel (`output/`) → `generate_docx.py` & `generate_pptx.py` → DOCX Report & PPTX Presentation (`output/`)

## Module Index

### Core Processing Script
* **File**: `src/generate_catalog.py` (~451 lines)
* **Responsibility**: Loads the raw Excel file, performs tool mapping, executes semantic DONE-marker split logic, computes complexity scores (Integration, Scope, Data, AI, Economic), flags IT security requirements, and extracts data sources.
* **Key Functions**:
  - `process_dataframe(df)`: Main pipeline function that clones the raw data and applies all formatting and classification rules.
  - `extract_data_sources(desc, tools)`: Extracts unit data sources from the description and tools using rule-based regex patterns.
  - `score_data(tags, desc)`: Scores data complexity with overrides for L4 tools and DONE markers.
  - `score_ai(tags, desc)`: Scores AI maturity with overrides for completed phases.
  - `detect_maturity_status(desc)`: Parses description for maturity markers like `--DONE, SO FAR -`.
  - `it_attention(desc, tags, tier)`: Scans for enterprise security triggers (ssbi, db, cloud, sap).

### Document Generator
* **File**: `src/generate_docx.py` (~1380 lines)
* **Responsibility**: Reads the cleaned Excel catalog and generates the corporate DOCX report with styled tables, statistics, IT governance classifications, and domain recommendations.
* **Key Libraries**: `python-docx`

### Presentation Generator
* **File**: `src/generate_pptx.py` (~560 lines)
* **Responsibility**: Reads the cleaned Excel catalog and creates a styled slideshow based on custom layout coordinates and the corporate theme.
* **Key Libraries**: `python-pptx`

## Test Suite
* **`src/tests/test_generate_catalog.py`** (~840 lines): Tests scoring formulas, overrides, IT flagging, data sources extraction, and full pipeline outputs.
* **`src/tests/test_generate_docx.py`** (~345 lines): Tests document table layout, paragraph formatting, IT governance sections, and export generation.
* **`src/tests/test_generate_pptx.py`** (~390 lines): Tests presentation slide count, placeholder mappings, and template creation.
