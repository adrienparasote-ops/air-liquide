> Document Type: Implementation

# Implementation Plan — Semantic Scoring v2, Maturity Overrides & L4 Data Tools

Update `src/generate_catalog.py` using Test-Driven Development (TDD) to implement the Semantic Scoring v2 rules, DONE-marker parsing logic, and L4 data tools override. This ensures that the generated spreadsheet matches the validated counts in `docs/use_cases_catalog.md`.

## Assumptions

| # | Assumption | Risk | Validation |
|---|---|---|---|
| 1 | Description markers match exactly the 3 target use cases | Low | Test against actual Excel rows and verify only 3 are marked `Partiel`. |
| 2 | Complexity tiers are automatically derived from revised total scores | Low | Assert that recalculating `Score_Total` correctly yields Small/Medium/Large. |
| 3 | Indexing format syncs with Apps Script charts | Low | Verify column order: `Maturity_Status` must be directly before long description. |

## User Review Required

> [!IMPORTANT]
> The maturity overrides and L4 data tools minimum overrides are designed to be driven by semantic description markers and tool tag values rather than hardcoded row numbers. This preserves the script's robustness for future runs while ensuring perfect alignment with current counts:
> - **Small**: 110 (44.4%)
> - **Medium**: 130 (52.4%)
> - **Large**: 8 (3.2%)
> - **IT Flags**: 81
> - **Maturity Status (Partiel)**: Exactly 3 use cases (`UC_0004`, `UC_0093`, `UC_0104`).

## Anti-patterns

| Anti-pattern | Consequence | Corrective Action |
|--------------|-------------|-------------------|
| **Hardcoding Row Numbers / UC_IDs** | Breaks robustness if the source Excel file rows are reordered or filtered. | Drive overrides purely via semantic markers and tool values. |
| **Mutating Original DataFrame** | Violates immutability standards; makes debugging difficult and risks side effects. | Always operate on a copy via `.copy()` or return a new DataFrame. |
| **Global Overrides for All Mature Markers** | Unintended side effects on other rows that might have similar words. | Restrict overrides to specific recognized markers. |
| **Ignoring L4 Minimum Override for Mature Rows** | Setting mature scores blindly without checking if they have D3 L4 overrides. | Apply overrides in a clear, sequential priority list. |
| **Appending Column at the End** | Breaks index alignment in downstream Apps Script dashboards. | Insert `"Maturity_Status"` precisely before the long description. |

## Proposed Changes

We will implement the following changes in the source code:

---

### Core Data Processing & Export

#### [MODIFY] [generate_catalog.py](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/src/generate_catalog.py#L1)
- **Maturity Marker Detection**:
  - Add logic to scan `Use Case Description (Long)` case-insensitively for explicit mature markers:
    - Row 3 (`UC_0004`): `--DONE, SO FAR -`
    - Row 92 (`UC_0093`): `I have already done this with PowerBI` or `I have already initiated the movement`
    - Row 103 (`UC_0104`): `Project expanding on the existing tools already deployed`
  - If a marker is detected, set `Maturity_Status` column to `"🔄 Partiel"`, otherwise set to `""`.
- **Scoring Overrides**:
  - For rows identified as mature, reduce their complexity scores to reflect only the prospective remaining effort:
    - **Salesforce / Row 3**: Set `Score_Data = 1` and `Score_AI = 1`
    - **CMMS/OneMaximo / Row 92**: Set `Score_Data = 2` and `Score_AI = 1`
    - **AUQA Quoting / Row 103**: Set `Score_Data = 1`
  - Ensure `Score_Total` is re-calculated as the sum of all 5 dimensions after overrides are applied.
- **L4 Data Tools Override**:
  - Update `score_data` logic to check if `Python on Fabric` or `Python on DataStudio` is in the tools tags, or if `BigQuery` is in tags or the description (case-insensitive).
  - If present, ensure D3 (`Score_Data`) is at least 2.
- **Export Columns**:
  - Insert `"Maturity_Status"` in `EXPORT_COLS` list, immediately preceding `"Use Case Description (Long)"`.

---

### Unit Test Suite

#### [MODIFY] [test_generate_catalog.py](file:///Users/adrien.parasote/Documents/Projects/Air%20Liquide/src/tests/test_generate_catalog.py#L1)
- **TDD Requirement**: Add failing test cases in `src/tests/test_generate_catalog.py` *before* modifying `src/generate_catalog.py`:
  - Test description-based split and marker detection (`Maturity_Status` calculation).
  - Test the D3 override logic for `Python on Fabric`, `Python on DataStudio`, and `BigQuery` (L4 data tools minimum).
  - Test the specific score overrides for all 3 mature use cases.
  - Test the new `Maturity_Status` column population in `process_dataframe`.

## Test Cases

| Test ID | Name | Category | Description |
|---|---|---|---|
| **TC-001** | `test_maturity_status_none` | Unit | Verify descriptions without mature markers get empty string maturity status. |
| **TC-002** | `test_maturity_status_sfdc` | Unit | Verify `--DONE, SO FAR -` sets status to `"🔄 Partiel"`. |
| **TC-003** | `test_maturity_status_cmms` | Unit | Verify `I have already done this with PowerBI` or `I have already initiated the movement` sets status to `"🔄 Partiel"`. |
| **TC-004** | `test_maturity_status_auqa` | Unit | Verify `Project expanding on the existing tools already deployed` sets status to `"🔄 Partiel"`. |
| **TC-005** | `test_score_data_l4_override` | Unit | Verify `Python on DataStudio` and `BigQuery` force D3 >= 2. |
| **IT-001** | `test_process_dataframe_maturity_overrides` | Integration | Verify specific score reductions for Salesforce, CMMS, and AUQA are applied and `Score_Total` is correctly recalculated. |
| **IT-002** | `test_process_dataframe_l4_override` | Integration | Verify D3 >= 2 override works in the full pipeline for Fabric, DataStudio, and BigQuery. |
| **IT-003** | `test_main_workflow_end_to_end` | Integration | Run process on a dummy DataFrame and verify that the `Maturity_Status` column is in the final export in the correct position. |

## Error Handling

| Error | Response | Fallback | Logging |
|---|---|---|---|
| **Source file not found** | Exits with status 1 | None | Friendly terminal error message printed |
| **Missing expected columns** | Exits with status 1 | None | KeyError trace / terminal error message printed |
| **Excel write permission error** | Exits with status 1 | None | PermissionError / terminal error message printed |
| **Invalid/Empty description rows** | Row is skipped | Skip row | Silence skip in dataframe filter |

## Verification Plan

### Automated Tests
- Run `pytest src/tests/test_generate_catalog.py` to confirm that:
  - Phase 1 (RED): Newly added tests fail due to missing logic.
  - Phase 2 (GREEN): All unit tests pass once implementation is complete.

### Manual Verification
- Execute `python3 src/generate_catalog.py` to regenerate `docs/use_cases_catalog.xlsx`.
- Confirm that the terminal summary matches the target stats exactly:
  - Tiers: `{'Medium': 130, 'Small': 110, 'Large': 8}`
  - IT Flags: `81`
  - Exactly 3 rows with `"🔄 Partiel"` in the `"Maturity_Status"` column.
