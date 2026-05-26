> Document Type: Implementation

# Implementation Plan — Data Source Distribution by Functional Family Chart (Medium & Large Focus)

We will update the Google Apps Script (`create_analysis.gs`) to generate the new premium dynamic chart: **Répartition des sources de données par famille** (Data Source Distribution by Family) specifically inside the **"Focus Medium & Large"** sheet. This chart will show the detailed breakdown of the top 8 required data sources for functional families F1 to F7, focusing exclusively on **Medium and Large** use cases.

To maintain dynamic sheet reactivity, the chart will reference a dynamically generated pivot-style dataset in the `AS:BA` columns of the `Focus Medium & Large` sheet. This dataset will use `COUNTIFS` formulas to automatically recalculate values in real-time when the user modifies any data in the master `Catalogue` sheet.

We will also remove the temporary implementation of this chart from `"Graphiques généraux"` to ensure clean visual separation.

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
> - The data preparation grid in columns `AS:BA` uses dynamic whole-column references (`Catalogue!$D:$D`, `Catalogue!$Z:$Z`, `Catalogue!$B:$B`), ensuring that any new use cases added to the `Catalogue` are instantly accounted for.

---

## Assumptions

| # | Assumption | Risk | Validation |
|---|---|---|---|
| 1 | The master `Catalogue` sheet contains the columns `"Family"` (e.g. F1, F2...), `"Complexity_Tier"` (e.g. Medium, Large), and `"Data_Sources"` (comma-separated list of sources). | Low | Verified via `_loadCatalogue()` which maps headers dynamically. |
| 2 | The family codes in the `"Family"` column are standardized (F1, F2, F3, F4, F5, F6, F7). | Low | Match labels defined in `writeSourcesTable`. |
| 3 | The sheet has enough columns to hold the new `AS:BA` data matrix. | Low | Already verified. The sheet is configured to expand to 55 columns dynamically. |

---

## Anti-patterns

| Anti-pattern | Consequence | Corrective Action |
|--------------|-------------|-------------------|
| **Hardcoding top data sources** | If the catalog data changes and new sources become prominent, the chart won't reflect them. | Compute the top 8 sources dynamically from `mlRows` (Medium & Large rows) *before* writing the formulas. |
| **Hardcoding formula column letters** | If columns are reordered in the Catalogue sheet, formulas will point to wrong data. | Resolve column letters dynamically using `getColumnLetter()` with mapped header indexes. |
| **Using static values in the dataset** | The chart will not update when use cases are modified or added. | Write `=COUNTIFS(Catalogue!$D:$D, $AS72, Catalogue!$Z:$Z, "*" & AT$71 & "*", Catalogue!$B:$B, "Medium") + COUNTIFS(Catalogue!$D:$D, $AS72, Catalogue!$Z:$Z, "*" & AT$71 & "*", Catalogue!$B:$B, "Large")` formulas. |
| **Overlapping chart coordinates** | The new chart will render on top of G10/G11, creating a messy UI. | Anchor the chart exactly at Row 62, Col 2, with explicit size coordinates (960x400). |
| **Inconsistent color palette** | The chart will look like generic "AI slop" or default Excel styling. | Use the premium corporate HSL-tailored colors defined in `COLORS`. |

---

## Proposed Changes

### Apps Script Dashboard Component

#### [MODIFY] [create_analysis.gs](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/use%20case%20analysis/src/create_analysis.gs)

We will make the following changes:

##### 1. Clean up `buildGraphiquesGénéraux`
- Revert the temporary chart G7 and data table D7.
- Restore the column count alerts to `"6 graphiques natifs"`.

##### 2. Update `buildFocusMediumLarge` to prepare the data matrix and insert the new chart
- Retrieve `top8MlSources` dynamically from the pre-filtered `mlRows` (ignoring `"A revoir avec le builder"`).
- Write the dynamic headers `["Famille", ...top8MlSources]` at the next available `dataRow` (after `D12_END`) in columns `AS:BA` of `"Focus Medium & Large"`.
- Loop through families `["F1", "F2", "F3", "F4", "F5", "F6", "F7"]` and write:
  - Column 1: Family Code (F1..F7)
  - Columns 2 to 9: Formula `=COUNTIFS(Catalogue!$[familyCodeCol]:$[familyCodeCol], $[rowLabelCell], Catalogue!$[dataSourcesCol]:$[dataSourcesCol], "*" & $[headerCell] & "*", Catalogue!$[tierCol]:$[tierCol], "Medium") + COUNTIFS(...)`
- Insert a stacked column chart (`Charts.ChartType.COLUMN`) at row 62, col 2:
  - Title: `"Répartition des sources de données par famille (Medium + Large)"`
  - Data Range: `D13_ROW:D13_END` spanning columns `AS` to `AS + top8MlSources.length`.
  - Stacking: `true` (stacked columns).
  - Premium colors from `COLORS` and custom options matching other native charts.

##### 3. Update descriptive alerts and header comments
- Update Line 71 to say `"6 graphiques natifs"`.
- Update Line 86 to say `"6 graphiques dédiés (dont la répartition des sources de données par famille)"`.
- Update Line 185 to say `"Focus Medium & Large : 6 graphiques dédiés aux cas d'usage complexes (dont la répartition des sources par famille)"`.

---

## Test Cases

| Test ID | Name | Category | Description |
|---|---|---|---|
| **TC-017** | `test_dynamic_top_sources_ml` | Unit | Verify that top 8 data sources are correctly extracted and sorted in descending order from Medium & Large rows only. |
| **TC-018** | `test_data_matrix_formulas_ml` | Unit | Verify that the written formulas are correctly formatted with double COUNTIFS matching Medium & Large tiers. |
| **TC-019** | `test_chart_dimensions_ml` | Unit | Verify that the chart is inserted at Row 62, Col 2, with width 960 and height 400. |
| **TC-020** | `test_chart_stacked_property` | Unit | Verify that the chart has the `"isStacked": true` option set. |
| **IT-010** | `test_dashboard_refresh_ml` | Integration | Verify that editing a use case's `Data_Sources` in the `Catalogue` tab immediately updates the stacked columns in the new chart in real-time. |

---

## Error Handling Matrix

| Error | Response | Fallback | Logging |
|---|---|---|---|
| **`Family` or `Data_Sources` column missing** | Alerts user, stops building sheet safely. | Diagnostic alert popup | Log header mismatch details to Apps Script Logger. |
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
5. In the menu, click **🤖 AI Champions -> Focus Medium & Large**.
6. Check that the `"Focus Medium & Large"` sheet contains exactly 6 native charts, with the new stacked column chart positioned perfectly at the bottom.
7. Change the data source of a Medium use case in the `"Catalogue"` sheet.
8. Verify that the stacked column for the corresponding family instantly updates in the chart.
