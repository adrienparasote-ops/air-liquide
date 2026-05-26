> Document Type: Implementation

# Implementation Plan — Dynamic Formula Integration for Analytics Charts & Pivot Tables

We will update the Google Apps Script (`create_analysis.gs`) to generate fully dynamic Google Sheets formulas (such as `COUNTIF`, `COUNTIFS`, `SUM`, and division calculations) instead of writing static values for the chart datasets and pivot tables. This will ensure that when the user modifies any data in the main `Catalogue` sheet, all summaries, focus tables, and native charts in `Synthèse`, `Graphiques généraux`, and `Focus Medium & Large` will automatically recalculate and update in real-time, eliminating the need to re-run the generator script.

---

## User Review Required

> [!IMPORTANT]
> **Dynamic Range vs. Static Column References**
> To support additions and edits to the `Catalogue` sheet automatically, the generated formulas will reference whole columns (e.g. `Catalogue!C:C` instead of restricted ranges like `Catalogue!C2:C249`). This is highly standard, performant, and is the best practice for robust spreadsheet design.

---

## Assumptions

| # | Assumption | Risk | Validation |
|---|---|---|---|
| 1 | The user's Google Sheet contains a sheet named `"Catalogue"` with standard columns | Low | Verified via `SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Catalogue")` API call. |
| 2 | Formula names (e.g. `COUNTIF`, `COUNTIFS`, `SUM`) are identical in French/English Google Sheets locales | Medium | Verified via `sheet.getRange().setFormula("COUNTIF(...)")` API call in Google Sheets execution environment. |
| 3 | Target sheets `Synthèse`, `Graphiques généraux`, and `Focus Medium & Large` have enough columns | Low | Verified via `sheet.insertColumnsAfter(...)` API call in Apps Script. |

---

## Anti-patterns

| Anti-pattern | Consequence | Corrective Action |
|--------------|-------------|-------------------|
| **Hardcoded row count limits** | New rows in `Catalogue` won't be accounted for in calculations. | Use full column references (e.g., `Catalogue!C:C`) in all formulas. |
| **Static index references in formulas** | If columns are reordered in the Catalogue sheet, formulas will point to the wrong columns. | Resolve column letters dynamically from dynamic header indexes. |
| **A1 Notation formatting errors** | Missing quotes, exclamation points, or dollar signs will result in `#REF!` or incorrect syntax in Sheets. | Build formulas using template literals with explicit escaping. |
| **Locale-dependent formula names** | Using French formula names (e.g., `NB.SI`) inside Apps Script `setFormula()` will fail in English locales. | Always use standard English uppercase formula names (`COUNTIF`, `COUNTIFS`) which Apps Script standardizes globally. |
| **Hardcoding starting columns** | Shifted datasets in the AS:AV area would break chart source ranges. | Use the named constants (`DATA_START_COL`) and relative offsets. |

---

## Proposed Changes

### Dynamic Column Resolving Helper

We will add a helper function `getColumnLetter(colIndex)` to convert 1-based column indices into A1-style letters (e.g., `1` -> `"A"`, `27` -> `"AA"`).
We will then resolve column letters dynamically based on header mapping to ensure that changes in Catalogue column orders will never break the formulas.

```javascript
function getColumnLetter(colIndex) {
  let letter = "";
  let temp;
  while (colIndex > 0) {
    temp = (colIndex - 1) % 26;
    letter = String.fromCharCode(65 + temp) + letter;
    colIndex = Math.floor((colIndex - temp) / 26);
  }
  return letter;
}
```

---

### Apps Script Dashboard Component

#### [MODIFY] [create_analysis.gs](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/create_analysis.gs#L1)

We will modify the main sheet building functions to write formulas:

#### 1. Pivot Table Generation (`writePivotTable`)
- Read dynamic column letters for the row field (`rowColLetter`) and column field (`colColLetter`).
- For each cell in the pivot table at row `r` and column `c`, write:
  `=COUNTIFS(Catalogue!$[rowColLetter]:$[rowColLetter], $[rowHeaderCell], Catalogue!$[colColLetter]:$[colColLetter], [colHeaderCell])`
- For the `Total` column at the end of each row, write:
  `=SUM([firstCellRow]:[lastCellRow])`
- For the `TOTAL` row at the bottom of the table, write:
  `=SUM([firstCellCol]:[lastCellCol])`

#### 2. Sources Table (`writeSourcesTable`)
- Write dynamic formula counts in the family breakdown matrix using:
  `=COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], [familyHeaderCell], Catalogue!$[dataSourcesLetter]:$[dataSourcesLetter], "*" & $[sourceRowHeaderCell] & "*")`
- Write `=SUM(...)` for the row totals.
- Write `=I[r] / (COUNTA(Catalogue!$A:$A) - 1)` for the `% Global` column to dynamically calculate the percentages relative to the total number of use cases in `Catalogue`.

#### 3. General Charts Sheet (`buildGraphiquesGénéraux`)
- Convert the datasets in columns `AS:AV` to use formulas:
  - **D1 (Tier Distribution)**: `=COUNTIF(Catalogue!$[tierLetter]:$[tierLetter], AS[r])`
  - **D2 (Top Tools)**: `=COUNTIF(Catalogue!$[toolLetter]:$[toolLetter], "*" & AS[r] & "*")`
  - **D3 (Famille × Tier)**: `=COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], $AS[r], Catalogue!$[tierLetter]:$[tierLetter], [tierColHeader])`
  - **D4 (Cluster × Tier)**: `=COUNTIFS(Catalogue!$[clusterLetter]:$[clusterLetter], $AS[r], Catalogue!$[tierLetter]:$[tierLetter], [tierColHeader])`
  - **D5 (Volume par famille)**: `=COUNTIF(Catalogue!$[familyLetter]:$[familyLetter], AS[r])`
  - **D6 (IT par famille)**: `=COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], AS[r], Catalogue!$[itFlagLetter]:$[itFlagLetter], "*IT*")`

#### 4. Focus Charts Sheet (`buildFocusMediumLarge`)
- Convert the focus datasets in columns `AS:AV` to use formulas:
  - **D7 (Famille × Stage)**: `=COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], $AS[r], Catalogue!$[stageLetter]:$[stageLetter], [stageColHeader], Catalogue!$[tierLetter]:$[tierLetter], "Medium") + COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], $AS[r], Catalogue!$[stageLetter]:$[stageLetter], [stageColHeader], Catalogue!$[tierLetter]:$[tierLetter], "Large")`
  - **D9 (Medium vs Large Donut)**: `=COUNTIF(Catalogue!$[tierLetter]:$[tierLetter], AS[r])`
  - **D10 (Volume M+L par famille)**: `=COUNTIFS(Catalogue!$[familyLetter]:$[familyLetter], $AS[r], Catalogue!$[tierLetter]:$[tierLetter], [tierColHeader])`
  - **D11 (Top Sources)**: `=COUNTIFS(Catalogue!$[dataSourcesLetter]:$[dataSourcesLetter], "*" & AS[r] & "*", Catalogue!$[tierLetter]:$[tierLetter], "Medium") + COUNTIFS(Catalogue!$[dataSourcesLetter]:$[dataSourcesLetter], "*" & AS[r] & "*", Catalogue!$[tierLetter]:$[tierLetter], "Large")`
  - **D12 (Top 8 Sources × Complexité)**: `=COUNTIFS(Catalogue!$[dataSourcesLetter]:$[dataSourcesLetter], "*" & $AS[r] & "*", Catalogue!$[tierLetter]:$[tierLetter], [tierColHeader])`

---

## Test Cases

| Test ID | Name | Category | Description |
|---|---|---|---|
| **TC-012** | `test_getColumnLetter_basic` | Unit | Verify `getColumnLetter(1)` returns `"A"`, `getColumnLetter(27)` returns `"AA"`. |
| **TC-013** | `test_writePivotTable_formulas` | Unit | Verify pivot table cells are populated with `=COUNTIFS(...)` formulas instead of static numbers. |
| **TC-014** | `test_buildGraphiques_formulas` | Unit | Verify AS:AT ranges in General Charts sheet are populated with `=COUNTIF(...)` and `=COUNTIFS(...)`. |
| **TC-015** | `test_buildFocus_formulas` | Unit | Verify datasets in Focus sheet are populated with `=COUNTIFS(...)` and `=SUM(...)` formulas. |
| **TC-016** | `test_sourcesTable_formulas` | Unit | Verify `% Global` column in Sources Table contains dynamic division formulas referencing the total use case count. |
| **IT-007** | `test_sheets_formulas_recalculation` | Integration | Verify that editing `Catalogue` complexity triggers automatic formula updates in the sheets. |
| **IT-008** | `test_charts_data_range_dynamic` | Integration | Verify that Google Sheet native charts dynamically adjust their visual rendering immediately after data modification. |
| **IT-009** | `test_writeSourcesTable_global_percentage` | Integration | Verify that the global percentage formula accurately reflects changes to the total row count when adding new rows to the catalog. |

---

## Error Handling

| Error | Response | Fallback | Logging |
|---|---|---|---|
| **Column index not found** | Throws standard AppScript alert | Safe halt with diagnostic alert | Log missing column header in Apps Script console |
| **Formula calculation error (`#N/A`, `#VALUE!`)** | Handled by sheet cells | Default empty cells where appropriate | Visible in Sheets cell error indicator |
| **Zero use cases in Catalogue** | `_loadCatalogue()` returns null | Halt execution early before inserting sheets | Shows user error dialog |

---

## Verification Plan

### Manual Verification
- Copy the newly updated `create_analysis.gs` script.
- Paste it into a test Google Sheet containing the `Catalogue` tab.
- Run **🤖 AI Champions -> Analyse complète**.
- Confirm that the `Synthèse`, `Graphiques généraux`, and `Focus Medium & Large` sheets are generated successfully and that all native charts display correctly.
- Edit values in the `Catalogue` tab (e.g. change a use case's `Complexity_Tier` from `Small` to `Large`, or change a tool tag).
- Confirm that the values in the pivot tables and the charts in the dashboard sheets immediately update in real-time without having to run the Apps Script again.
