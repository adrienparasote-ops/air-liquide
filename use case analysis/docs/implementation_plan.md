> Document Type: Implementation

# Implementation Plan — Data Source Distribution by Functional Family Chart (Medium & Large Focus with Full Labels)

We will update the Google Apps Script (`create_analysis.gs`) to generate the new premium dynamic chart: **Répartition des sources de données par famille** (Data Source Distribution by Family) specifically inside the **"Focus Medium & Large"** sheet. This chart will show the detailed breakdown of the top 8 required data sources for functional families F1 to F7, focusing exclusively on **Medium and Large** use cases.

To improve readability and follow the user's preference, the categories (X-axis) will display the **full descriptive Family_Label** (e.g. `"Automatisation documentaire"`) instead of the short codes (`"F1"`, `"F2"`).

To maintain dynamic sheet reactivity, the chart will reference a dynamically generated pivot-style dataset in the `AS:BA` columns of the `Focus Medium & Large` sheet. This dataset will use `COUNTIFS` formulas to automatically recalculate values in real-time when the user modifies any data in the master `Catalogue` sheet.

---

## Constraints

| Tier | Examples |
|------|----------|
| **Always do** | Use English uppercase formula names (`COUNTIFS`, `COUNTIF`), use A1-style relative/absolute references correctly, preserve and extend the visual palette (`COLORS`), and test the spreadsheet locally before submitting. |
| **Ask first** | Any change to the columns or schemas of the master `Catalogue` sheet, or changes to the existing G1 to G11 chart configurations. |
| **Never do** | Write static values instead of dynamic formulas, hardcode sheet coordinates or row limits, or introduce external libraries/dependencies. |

---

## User Review Required

> [!IMPORTANT]
> **Dynamic Grid and Visual Dimensions**
> - The new chart (G12) will be added to the `"Focus Medium & Large"` sheet.
> - To maintain the premium look-and-feel and structure of the dashboard, the chart will be placed below G10 and G11 at Row 62, spanning a width of 960px (identical to the full-width maturity chart above it).
> - The data preparation grid in columns `AS:BA` uses dynamic whole-column references (`Catalogue!$E:$E` for `Family_Label`, `Catalogue!$Z:$Z`, `Catalogue!$B:$B`), ensuring that any new use cases added to the `Catalogue` are instantly accounted for.

---

## Assumptions

| # | Assumption | Risk | Validation |
|---|---|---|---|
| 1 | The master `Catalogue` sheet contains the columns `"Family_Label"` (e.g. `"Automatisation documentaire"`), `"Complexity_Tier"` (e.g. Medium, Large), and `"Data_Sources"` (comma-separated list of sources). | Low | Verified via `_loadCatalogue()` which maps headers dynamically. |
| 2 | The family labels are standardized and match `famLabels` lookup keys. | Low | Match labels defined in `writeSourcesTable`. |
| 3 | The sheet has enough columns to hold the new `AS:BA` data matrix. | Low | Already verified. The sheet is configured to expand to 55 columns dynamically. |

---

## Anti-patterns

| Anti-pattern | Consequence | Corrective Action |
|--------------|-------------|-------------------|
| **Hardcoding top data sources** | If the catalog data changes and new sources become prominent, the chart won't reflect them. | Compute the top 8 sources dynamically from `mlRows` (Medium & Large rows) *before* writing the formulas. |
| **Hardcoding formula column letters** | If columns are reordered in the Catalogue sheet, formulas will point to wrong data. | Resolve column letters dynamically using `getColumnLetter()` with mapped header indexes. |
| **Using static values in the dataset** | The chart will not update when use cases are modified or added. | Write `=COUNTIFS(Catalogue!$E:$E, $AS72, Catalogue!$Z:$Z, "*" & AT$71 & "*", Catalogue!$B:$B, "Medium") + COUNTIFS(...)` formulas. |
| **Overlapping chart coordinates** | The new chart will render on top of G10/G11, creating a messy UI. | Anchor the chart exactly at Row 62, Col 2, with explicit size coordinates (960x400). |
| **Inconsistent color palette** | The chart will look like generic "AI slop" or default Excel styling. | Use the premium corporate HSL-tailored colors defined in `COLORS`. |

---

## Proposed Changes

### Apps Script Dashboard Component

#### [MODIFY] [create_analysis.gs](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/create_analysis.gs)

We will make the following changes:

##### 1. Clean up `buildFocusMediumLarge`
- Define `famLabels` mapping functional family codes to descriptive labels inside the function.
- Write the descriptive labels `famLabels[fam]` into the first column (`DATA_START_COL`) of the `D13` preparation grid.
- Use `familyLetter` (referencing `col["Family_Label"]`) in the `COUNTIFS` formulas to search for full descriptive labels instead of short codes.
- Remove `familyCodeLetter` since it is no longer required.

---

## Test Cases

| Test ID | Name | Category | Description |
|---|---|---|---|
| **TC-017** | `test_dynamic_top_sources_ml` | Unit | Verify that top 8 data sources are correctly extracted and sorted in descending order from Medium & Large rows only. |
| **TC-018** | `test_data_matrix_formulas_ml_labels` | Unit | Verify that the written formulas are correctly formatted using full descriptive labels and familyLetter references. |
| **TC-019** | `test_chart_dimensions_ml` | Unit | Verify that the chart is inserted at Row 62, Col 2, with width 960 and height 400. |
| **TC-020** | `test_chart_stacked_property` | Unit | Verify that the chart has the `"isStacked": true` option set. |
| **IT-010** | `test_dashboard_refresh_ml_labels` | Integration | Verify that editing a use case's `Data_Sources` or `Family_Label` in the `Catalogue` tab immediately updates the stacked columns in the new chart in real-time. |

---

## Error Handling Matrix

| Error | Response | Fallback | Logging |
|---|---|---|---|
| **`Family_Label` or `Data_Sources` column missing** | Alerts user, stops building sheet safely. | Diagnostic alert popup | Log header mismatch details to Apps Script Logger. |
| **Fewer than 8 sources in mlRows** | Grid and chart adjust dynamically to actual count. | Slice up to actual length | Standard execution |
| **Formula parsing error (`#VALUE!`)** | Cell displays error in Sheet. | Cell visual indicator | None (handled natively by Google Sheets engine) |

---

## Verification Plan

### Automated Tests
We do not have a browser test suite, but we can verify the syntax and format of the Apps Script code using static analysis.

### Manual Verification
1. Open the target Google Sheet.
2. Extensions → Apps Script.
3. Paste the new code from [create_analysis.gs](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/create_analysis.gs).
4. Save the script (Ctrl+S) and refresh the Google Sheet.
5. In the menu, click **🤖 AI Champions -> Focus Medium & Large** (or **Analyse complète**).
6. Check that the `"Focus Medium & Large"` sheet contains exactly 6 native charts, with the new stacked column chart G12 displaying the **full family labels** on its X-axis.
7. Change the data source of a Medium use case in the `"Catalogue"` sheet.
8. Verify that the stacked column for the corresponding family instantly updates in the chart.
