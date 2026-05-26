> Document Type: Implementation

# Implementation Plan — Data Sources Extraction & Functional Family Synthesis Table

Add a `Data_Sources` column at the end of the `use_cases_catalog.xlsx` file. This column is dynamically extracted from use case descriptions and tools using a robust rule-based parsing engine. We will then update the Google Apps Script (`create_analysis.gs`) to add a detailed summary table under the "Synthèse" sheet showing data source needs by functional family and their global percentage of occurrence.

## Assumptions

| # | Assumption | Risk | Validation |
|---|---|---|---|
| 1 | `Data_Sources` column can be appended safely at the end of `EXPORT_COLS` without breaking Apps Script | Low | The Apps Script retrieves columns dynamically via header mapping (`col[h] = i`). An appended column has zero impact on existing columns. |
| 2 | Offline semantic rules are preferred over online LLM API calls | Low | The pipeline runs completely offline, deterministically, and in <1 second with 100% test coverage. Standardizing extraction using robust regex is highly reliable, cost-free, and avoids credential leakage or latency overhead. |
| 3 | Use cases with no identified source default to "A revoir avec le builder" | Low | Ensures no empty or null cells exist in the spreadsheet export. |
| 4 | Multiple sources are split and counted unitarily in Apps Script | Low | By format spec, sources are comma-separated (e.g. `"SAP, Sheets"`). The Apps Script will split them and aggregate counts unitarily (no combined rows). |

## Constraints

| Tier | Examples |
|------|----------|
| **Always do** | Run the complete pytest suite before proposing any change; ensure 100% test coverage for new parsing functions. |
| **Ask first** | Any change to core scoring weight dimensions (D1-D5). |
| **Never do** | Hardcode specific UC_IDs for data source overrides; rules must be purely semantic and generic. |

## Anti-patterns

| Anti-pattern | Consequence | Corrective Action |
|--------------|-------------|-------------------|
| **Hardcoding specific rows** | Breaks if the source Excel is updated or reordered. | Implement a robust, case-insensitive keyword regex extraction function. |
| **Adding duplicate names** | E.g. "Google Drive, Drive" in the same list. | Deduplicate extracted tags in the parser before joining them. |
| **Index-based Apps Script lookup** | If the Apps Script used hardcoded column indices, adding a column would shift everything and break the script. | Rely entirely on dynamic header indexing: `headers.forEach((h, i) => { col[h] = i; });`. |
| **Failing to clean N/A values** | Null or empty values can cause cell parsing errors in Sheets. | Default empty sources to `"A revoir avec le builder"`. |
| **Missing unit tests for new regex** | Risks regressions or silent extraction failures. | Write a comprehensive suite of unit tests for all regex variations in `test_generate_catalog.py`. |

## Proposed Changes

---

### Catalog Generation (Python)

#### [MODIFY] [generate_catalog.py](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/generate_catalog.py#L89)
- Define a list of semantic rules for data source detection:
  - **SAP**: `\bsap\b`, `s/4hana`, `erp`
  - **Salesforce**: `\bsfdc\b`, `\bsalesforce\b`, `crm`
  - **Power BI**: `\bpower\s?bi\b`
  - **Sheets**: `\bsheet\b`, `\bexcel\b`, `\bspreadsheet\b`, `\bvba\b`
  - **Google Drive**: `\bdrive\b`, `google drive`
  - **BigQuery**: `\bbigquery\b`, `\bbq\b`
  - **AVEVA**: `\baveva\b`
  - **DCS**: `\bdcs\b`
  - **SCADA**: `\bscada\b`
  - **Maximo**: `\bmaximo\b`
  - **CMMS**: `\bcmms\b`
  - **Oracle**: `\boracle\b`
  - **Lakehouse**: `\blakehouse\b`
  - **Database**: `\bdatabase\b`, `\bsql\b`
  - **PDF / Documents**: `\bpdf\b`, `\bdocument\b`, `\bcontract\b`, `\breport\b`, `\binvoice\b`, `\bletter\b`, `\bemail\b`, `\bmail\b`
- Create a function `extract_data_sources(desc: str, tools: str) -> str` that:
  - Scans both `Use Case Description (Long)` and `Tools` case-insensitively using regex.
  - Returns a comma-separated list of identified data sources (e.g. `"SAP, Google Drive"`).
  - Defaults to `"A revoir avec le builder"` if no sources are found.
- Append `"Data_Sources"` to the end of `EXPORT_COLS`.
- Update `process_dataframe` to populate the `Data_Sources` column.

---

### Unit Test Suite (Python)

#### [MODIFY] [test_generate_catalog.py](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/tests/test_generate_catalog.py#L627)
- Add comprehensive unit tests in `src/tests/test_generate_catalog.py` to cover:
  - `extract_data_sources` function for individual sources (SAP, Sheets, Power BI, Salesforce, Google Drive, SCADA, etc.).
  - Deduplication and multi-source combination (e.g. `"SAP, Google Drive"`).
  - Integration of `Data_Sources` column inside `process_dataframe`.

---

### Apps Script Dashboard (JavaScript)

#### [MODIFY] [create_analysis.gs](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/create_analysis.gs#L250)
- In `buildSynthèse(sheet, rows, col)`:
  - Add a call to `writeSourcesTable(sheet, rows, col, cursor, 1)`.
- Create the `writeSourcesTable` function which:
  - Dynamically extracts all unique individual data sources found in the `Data_Sources` column (excluding `"A revoir avec le builder"` which is placed at the end).
  - Groups use case counts by `Family_Label` (columns) and `Data Source` (rows).
  - Computes the `Total` count and `% Global` (relative to the total of 248 use cases).
  - Formats the table with the corporate blue header and alternating gray rows.

## Test Cases

| Test ID | Name | Category | Description |
|---|---|---|---|
| **TC-006** | `test_extract_data_sources_sap` | Unit | Verify description containing SAP is extracted as `"SAP"`. |
| **TC-007** | `test_extract_data_sources_sheets` | Unit | Verify Sheets/Excel triggers `"Sheets"`. |
| **TC-008** | `test_extract_data_sources_multiple` | Unit | Verify combining multiple sources (e.g. SAP and Google Drive). |
| **TC-009** | `test_extract_data_sources_none` | Unit | Verify fallback to `"A revoir avec le builder"` when no keywords match. |
| **TC-010** | `test_extract_data_sources_case_insensitivity` | Unit | Verify case-insensitive detection of SAP and Sheets. |
| **TC-011** | `test_extract_data_sources_deduplication` | Unit | Verify duplicate data sources are consolidated into one unique entry. |
| **IT-004** | `test_process_dataframe_data_sources` | Integration | Verify that `Data_Sources` is correctly populated and exported at the end of the dataframe in `process_dataframe`. |
| **IT-005** | `test_main_runs_completely_with_new_column` | Integration | Verify main pipeline completes without permission or formatting errors. |
| **IT-006** | `test_generate_catalog_data_sources_coverage` | Integration | Verify all rows have a non-empty `Data_Sources` column in the output file. |

## Error Handling

| Error | Response | Fallback | Logging |
|---|---|---|---|
| **Empty or NaN values in source** | Handle gracefully in `extract_data_sources` | Return `"A revoir avec le builder"` | Friendly return without throwing exceptions |
| **Invalid tool tags format** | Skip and proceed | Return `"A revoir avec le builder"` | Silence skip in dataframe mapping |

## Verification Plan

### Automated Tests
- Run `python3 -m pytest src/tests/ -v --cov=src` to verify that all 220+ tests pass with 100% coverage.

### Manual Verification
- Run `python3 src/generate_catalog.py` to regenerate the catalog Excel sheet.
- Inspect the generated spreadsheet's last column `Data_Sources` to confirm correct extraction.
- Deploy the updated `create_analysis.gs` script to Google Sheets.
- Trigger "Analyse complète" or "Créer les tableaux de synthèse" and verify the beautiful new data sources functional breakdown table.
