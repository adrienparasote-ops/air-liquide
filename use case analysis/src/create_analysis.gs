/**
 * create_analysis.gs
 * ──────────────────
 * Google Apps Script à coller dans le Google Sheet converti depuis use_cases_catalog.xlsx
 *
 * COMMENT L'UTILISER :
 *  1. Ouvrir le Google Sheet (converti depuis use_cases_catalog.xlsx)
 *  2. Extensions → Apps Script
 *  3. Coller ce code (remplacer tout le contenu existant)
 *  4. Sauvegarder (Ctrl+S) — le menu "🤖 AI Champions" apparaît automatiquement
 *  5. Lors de la première exécution : autoriser les permissions demandées
 *
 * MENU : le menu "🤖 AI Champions" apparaît dans la barre de menu Google Sheets
 *  → Analyse complète       : crée Synthèse + Graphiques en une fois
 *  → Créer tableaux seulement
 *  → Créer graphiques seulement
 *  → Réinitialiser          : supprime les onglets générés
 */

// ── Menu Google Sheets ────────────────────────────────────────────────────────

/**
 * Crée le menu personnalisé à l'ouverture du fichier.
 * Déclenché automatiquement par Google Sheets (trigger onOpen).
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("🤖 AI Champions")
    .addItem("▶ Analyse complète (Synthèse + Tous les graphiques)", "runFullAnalysis")
    .addSeparator()
    .addItem("📋 Créer les tableaux de synthèse", "runSynthèseOnly")
    .addItem("📊 Créer les graphiques généraux", "runGraphiquesGénérauxOnly")
    .addItem("📈 Créer le focus Medium & Large", "runFocusMediumLargeOnly")
    .addSeparator()
    .addItem("🗑️ Réinitialiser (supprimer les onglets)", "resetSheets")
    .addToUi();
}

/** Lance l'analyse complète (tableaux + graphiques). */
function runFullAnalysis() {
  createAnalysis();
}

/** Crée uniquement l'onglet Synthèse. */
function runSynthèseOnly() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const existing = ss.getSheetByName("Synthèse");
  if (existing) ss.deleteSheet(existing);

  const { rows, col } = _loadCatalogue(ss);
  if (!rows) return;

  const synthSheet = ss.insertSheet("Synthèse");
  buildSynthèse(synthSheet, rows, col);
  ss.setActiveSheet(synthSheet);
  SpreadsheetApp.getUi().alert("✅ Onglet 'Synthèse' créé avec les tableaux croisés.");
}

/** Crée uniquement l'onglet Graphiques généraux. */
function runGraphiquesGénérauxOnly() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const existing = ss.getSheetByName("Graphiques généraux");
  if (existing) ss.deleteSheet(existing);

  const { rows, col } = _loadCatalogue(ss);
  if (!rows) return;

  const genChartSheet = ss.insertSheet("Graphiques généraux");
  buildGraphiquesGénéraux(ss, genChartSheet, rows, col);
  ss.setActiveSheet(genChartSheet);
  SpreadsheetApp.getUi().alert("✅ Onglet 'Graphiques généraux' créé avec 6 graphiques natifs.");
}

/** Crée uniquement l'onglet Focus Medium & Large. */
function runFocusMediumLargeOnly() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const existing = ss.getSheetByName("Focus Medium & Large");
  if (existing) ss.deleteSheet(existing);

  const { rows, col } = _loadCatalogue(ss);
  if (!rows) return;

  const mlChartSheet = ss.insertSheet("Focus Medium & Large");
  buildFocusMediumLarge(ss, mlChartSheet, rows, col);
  ss.setActiveSheet(mlChartSheet);
  SpreadsheetApp.getUi().alert("✅ Onglet 'Focus Medium & Large' créé avec 5 graphiques dédiés.");
}

/** Supprime les onglets générés. */
function resetSheets() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();

  const response = ui.alert(
    "🗑️ Réinitialiser",
    "Supprimer les onglets 'Synthèse', 'Graphiques généraux' et 'Focus Medium & Large' ?",
    ui.ButtonSet.YES_NO
  );
  if (response !== ui.Button.YES) return;

  ["Synthèse", "Graphiques généraux", "Focus Medium & Large", "Graphiques"].forEach(name => {
    const sheet = ss.getSheetByName(name);
    if (sheet) ss.deleteSheet(sheet);
  });
  ui.alert("✅ Onglets supprimés. Vous pouvez relancer l'analyse via le menu.");
}


/**
 * Charge et indexe les données de l'onglet Catalogue.
 * @returns {{ rows: any[][], col: Object }} ou { rows: null } si erreur.
 */
function _loadCatalogue(ss) {
  const catalogSheet = ss.getSheetByName("Catalogue");
  if (!catalogSheet) {
    SpreadsheetApp.getUi().alert(
      "❌ Onglet 'Catalogue' introuvable.\n\nVérifiez que votre fichier contient bien un onglet nommé exactement 'Catalogue'."
    );
    return { rows: null, col: null };
  }
  const rawData = catalogSheet.getDataRange().getValues();
  const headers = rawData[0];
  const rows    = rawData.slice(1);
  const col     = {};
  headers.forEach((h, i) => { col[h] = i; });
  return { rows, col };
}


// ── Palette de couleurs ──────────────────────────────────────────────────────
const COLORS = {
  navy:       "#0D2137",
  blue_dark:  "#1B4F72",
  blue_mid:   "#2980B9",
  blue_light: "#5DADE2",
  teal:       "#1ABC9C",
  green:      "#27AE60",
  gold:       "#F39C12",
  red:        "#E74C3C",
  purple:     "#8E44AD",
  orange:     "#E67E22",
  white:      "#FFFFFF",
  gray_light: "#F2F2F2",
  gray_mid:   "#D9D9D9",
  small_bg:   "#E9F7EF",
  medium_bg:  "#FEF9E7",
  large_bg:   "#FDEDEC",
  header_bg:  "#1B4F72",
  total_bg:   "#D6EAF8",
};

const TIER_COLORS = {
  "Small":  COLORS.green,
  "Medium": COLORS.gold,
  "Large":  COLORS.red,
};

const FAMILY_COLORS = [
  COLORS.blue_dark, COLORS.blue_mid, COLORS.blue_light, COLORS.teal,
  COLORS.purple, COLORS.orange, COLORS.green,
];

// ── Point d'entrée principal ──────────────────────────────────────────────────
function createAnalysis() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // Supprimer les onglets existants si relance
  ["Synthèse", "Graphiques généraux", "Focus Medium & Large", "Graphiques"].forEach(name => {
    const existing = ss.getSheetByName(name);
    if (existing) ss.deleteSheet(existing);
  });

  const { rows, col } = _loadCatalogue(ss);
  if (!rows) return;

  const synthSheet      = ss.insertSheet("Synthèse");
  const genChartSheet   = ss.insertSheet("Graphiques généraux");
  const mlChartSheet    = ss.insertSheet("Focus Medium & Large");

  buildSynthèse(synthSheet, rows, col);
  buildGraphiquesGénéraux(ss, genChartSheet, rows, col);
  buildFocusMediumLarge(ss, mlChartSheet, rows, col);

  ss.setActiveSheet(synthSheet);
  SpreadsheetApp.getUi().alert("✅ Analyse créée !\n\nOnglets ajoutés :\n• Synthèse : tableaux croisés\n• Graphiques généraux : 6 graphiques généraux\n• Focus Medium & Large : 5 graphiques dédiés aux cas d'usage complexes (dont 2 sur les sources de données)");
}


// ════════════════════════════════════════════════════════════════════════════
// ONGLET SYNTHÈSE
// ════════════════════════════════════════════════════════════════════════════

function buildSynthèse(sheet, rows, col) {
  sheet.setTabColor(COLORS.blue_dark);
  sheet.setColumnWidth(1, 280);
  for (let c = 2; c <= 6; c++) sheet.setColumnWidth(c, 100);
  sheet.setColumnWidth(7, 20); // séparateur

  let cursor = 1;

  // ── En-tête de page ──────────────────────────────────────────────────────
  const hdrRange = sheet.getRange(cursor, 1, 1, 6);
  hdrRange.merge();
  hdrRange.setValue("AIR LIQUIDE · AI Champions — Tableaux de synthèse");
  hdrRange.setBackground(COLORS.navy);
  hdrRange.setFontColor(COLORS.white);
  hdrRange.setFontSize(13);
  hdrRange.setFontWeight("bold");
  hdrRange.setVerticalAlignment("middle");
  sheet.setRowHeight(cursor, 36);
  cursor++;

  // Bande accent teal
  sheet.getRange(cursor, 1, 1, 6).setBackground(COLORS.teal);
  sheet.setRowHeight(cursor, 4);
  cursor += 2;

  // ── Tableau 1 : Famille × Tier ───────────────────────────────────────────
  cursor = writePivotTable(
    sheet, rows, col, cursor, 1,
    "① Famille fonctionnelle × Complexité",
    "Family_Label", "Complexity_Tier",
    ["Small", "Medium", "Large"],
    TIER_COLORS
  );
  cursor += 2;

  // ── Tableau 2 : Cluster × Tier ───────────────────────────────────────────
  cursor = writePivotTable(
    sheet, rows, col, cursor, 1,
    "② Cluster × Complexité",
    "Cluster", "Complexity_Tier",
    ["Small", "Medium", "Large"],
    TIER_COLORS
  );
  cursor += 2;

  // ── Tableau 3 : Job Family × Tier ────────────────────────────────────────
  cursor = writePivotTable(
    sheet, rows, col, cursor, 1,
    "③ Job Family × Complexité",
    "Job Family", "Complexity_Tier",
    ["Small", "Medium", "Large"],
    TIER_COLORS
  );
  cursor += 2;

  // ── Tableau 4 : Stage × Tier ─────────────────────────────────────────────
  cursor = writePivotTable(
    sheet, rows, col, cursor, 1,
    "④ Stage déclaré × Complexité",
    "Stage", "Complexity_Tier",
    ["Small", "Medium", "Large"],
    TIER_COLORS
  );
  cursor += 2;

  // ── Tableau 5 : Niveau outil × Tier ─────────────────────────────────────
  cursor = writePivotTable(
    sheet, rows, col, cursor, 1,
    "⑤ Niveau technique max × Complexité",
    "Max_Tool_Level", "Complexity_Tier",
    ["Small", "Medium", "Large"],
    TIER_COLORS
  );
  cursor += 2;

  // ── Tableau 6 : Top 10 Quick Wins ────────────────────────────────────────
  cursor = writeQuickWins(sheet, rows, col, cursor, 1);
  cursor += 2;

  // ── Tableau 7 : Sources de données nécessaires par famille ──────────────────
  cursor = writeSourcesTable(sheet, rows, col, cursor, 1);
}


// ── Générateur de tableau croisé générique ───────────────────────────────────
function writePivotTable(sheet, rows, col, startRow, startCol, title, rowField, colField, colOrder, colColors) {
  // Titre section
  const titleRange = sheet.getRange(startRow, startCol, 1, colOrder.length + 2);
  titleRange.merge();
  titleRange.setValue(title);
  titleRange.setBackground(COLORS.header_bg);
  titleRange.setFontColor(COLORS.white);
  titleRange.setFontWeight("bold");
  titleRange.setFontSize(10);
  sheet.setRowHeight(startRow, 26);
  startRow++;

  // Calculer le pivot
  const pivot = {};
  const rowKeys = new Set();
  rows.forEach(r => {
    const rowVal = String(r[col[rowField]] || "N/A");
    const colVal = String(r[col[colField]] || "N/A");
    rowKeys.add(rowVal);
    if (!pivot[rowVal]) pivot[rowVal] = {};
    pivot[rowVal][colVal] = (pivot[rowVal][colVal] || 0) + 1;
  });

  // En-têtes colonnes
  const headerRow = [rowField, ...colOrder, "Total"];
  const headerRange = sheet.getRange(startRow, startCol, 1, headerRow.length);
  headerRange.setValues([headerRow]);
  headerRange.setBackground(COLORS.blue_mid);
  headerRange.setFontColor(COLORS.white);
  headerRange.setFontWeight("bold");
  headerRange.setHorizontalAlignment("center");
  if (colColors) {
    colOrder.forEach((c, i) => {
      if (colColors[c]) {
        const cell = sheet.getRange(startRow, startCol + 1 + i);
        cell.setBackground(colColors[c] + "CC"); // avec transparence simulée
      }
    });
  }
  startRow++;

  // Lignes de données (triées par total desc)
  const sortedKeys = Array.from(rowKeys).sort((a, b) => {
    const totA = colOrder.reduce((s, c) => s + (pivot[a][c] || 0), 0);
    const totB = colOrder.reduce((s, c) => s + (pivot[b][c] || 0), 0);
    return totB - totA;
  });

  let grandTotal = 0;
  const colTotals = {};
  colOrder.forEach(c => colTotals[c] = 0);

  sortedKeys.forEach((key, idx) => {
    const rowTotal = colOrder.reduce((s, c) => s + (pivot[key][c] || 0), 0);
    grandTotal += rowTotal;
    const dataRow = [key, ...colOrder.map(c => { colTotals[c] += (pivot[key][c] || 0); return pivot[key][c] || 0; }), rowTotal];
    const range = sheet.getRange(startRow, startCol, 1, dataRow.length);
    range.setValues([dataRow]);
    range.setHorizontalAlignment("center");
    range.getCell(1, 1).setHorizontalAlignment("left");
    if (idx % 2 === 0) range.setBackground(COLORS.gray_light);
    startRow++;
  });

  // Ligne Total
  const totalRow = ["TOTAL", ...colOrder.map(c => colTotals[c]), grandTotal];
  const totalRange = sheet.getRange(startRow, startCol, 1, totalRow.length);
  totalRange.setValues([totalRow]);
  totalRange.setBackground(COLORS.total_bg);
  totalRange.setFontWeight("bold");
  totalRange.setHorizontalAlignment("center");
  totalRange.getCell(1, 1).setHorizontalAlignment("left");
  startRow++;

  return startRow;
}


// ── Quick Wins ────────────────────────────────────────────────────────────────
function writeQuickWins(sheet, rows, col, startRow, startCol) {
  const titleRange = sheet.getRange(startRow, startCol, 1, 6);
  titleRange.merge();
  titleRange.setValue("⑥ Top 10 Quick Wins — Small, 1 outil");
  titleRange.setBackground(COLORS.green);
  titleRange.setFontColor(COLORS.white);
  titleRange.setFontWeight("bold");
  titleRange.setFontSize(10);
  sheet.setRowHeight(startRow, 26);
  startRow++;

  const headers = ["UC_ID", "Famille", "Cluster", "Outil", "Score", "Stage"];
  const hRange = sheet.getRange(startRow, startCol, 1, headers.length);
  hRange.setValues([headers]);
  hRange.setBackground(COLORS.blue_mid);
  hRange.setFontColor(COLORS.white);
  hRange.setFontWeight("bold");
  startRow++;

  const seenIds = new Set();
  let count = 0;
  rows.filter(r =>
    String(r[col["Complexity_Tier"]]) === "Small" &&
    Number(r[col["Nb_Tools"]]) <= 1
  ).forEach((r, idx) => {
    if (count >= 10) return;
    const ucId = String(r[col["UC_ID"]]);
    if (seenIds.has(ucId)) return;
    seenIds.add(ucId);
    const row = [
      ucId,
      String(r[col["Family_Label"]] || ""),
      String(r[col["Cluster"]] || ""),
      String(r[col["Tools"]] || "").substring(0, 40),
      Number(r[col["Score_Total"]] || 0),
      String(r[col["Stage"]] || ""),
    ];
    const range = sheet.getRange(startRow, startCol, 1, row.length);
    range.setValues([row]);
    if (idx % 2 === 0) range.setBackground(COLORS.small_bg);
    startRow++;
    count++;
  });

  return startRow;
}


// ════════════════════════════════════════════════════════════════════════════
// ONGLET GRAPHIQUES GÉNÉRAUX
// ════════════════════════════════════════════════════════════════════════════

function buildGraphiquesGénéraux(ss, sheet, rows, col) {
  const TOTAL_COLS = 55;

  const currentCols = sheet.getMaxColumns();
  if (currentCols < TOTAL_COLS) {
    sheet.insertColumnsAfter(currentCols, TOTAL_COLS - currentCols);
  }

  sheet.setTabColor(COLORS.blue_mid);
  sheet.setColumnWidths(1, TOTAL_COLS, 35);

  // En-tête banner
  const hdr = sheet.getRange(1, 1, 1, TOTAL_COLS);
  hdr.merge();
  hdr.setValue("AIR LIQUIDE  ·  AI Champions Use Cases  ·  Graphiques généraux");
  hdr.setBackground(COLORS.navy);
  hdr.setFontColor(COLORS.white);
  hdr.setFontSize(14);
  hdr.setFontWeight("bold");
  hdr.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 36);

  sheet.getRange(2, 1, 1, TOTAL_COLS).setBackground(COLORS.teal);
  sheet.setRowHeight(2, 4);

  const DATA_START_COL = 45; // AS - hors de la vue principale
  let dataRow = 5;

  // D1 : Tier distribution
  const tierCounts = countBy(rows, col["Complexity_Tier"]);
  const tierOrder  = ["Small", "Medium", "Large"];
  const D1_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Tier");
  sheet.getRange(dataRow, DATA_START_COL + 1).setValue("Count");
  dataRow++;
  tierOrder.forEach(t => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(t);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(tierCounts[t] || 0);
    dataRow++;
  });
  const D1_END = dataRow - 1;
  dataRow += 2;

  // D2 : Top outils
  const toolCounts = {};
  rows.forEach(r => {
    const tags = String(r[col["Tools_Tags"]] || "").split(",").map(t => t.trim()).filter(Boolean);
    tags.forEach(t => { toolCounts[t] = (toolCounts[t] || 0) + 1; });
  });
  const sortedTools = Object.entries(toolCounts).sort((a,b) => b[1] - a[1]);
  const D2_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Outil");
  sheet.getRange(dataRow, DATA_START_COL + 1).setValue("Count");
  dataRow++;
  sortedTools.forEach(([tool, count]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(tool);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(count);
    dataRow++;
  });
  const D2_END = dataRow - 1;
  dataRow += 2;

  // D3 : Famille × Tier
  const famTierPivot = crossTab(rows, col["Family_Label"], col["Complexity_Tier"], tierOrder);
  const D3_ROW = dataRow;
  const D3_HEADERS = ["Famille", "Small", "Medium", "Large"];
  D3_HEADERS.forEach((h, i) => sheet.getRange(dataRow, DATA_START_COL + i).setValue(h));
  dataRow++;
  famTierPivot.forEach(([key, vals]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(key);
    tierOrder.forEach((t, i) => sheet.getRange(dataRow, DATA_START_COL + 1 + i).setValue(vals[t] || 0));
    dataRow++;
  });
  const D3_END = dataRow - 1;
  dataRow += 2;

  // D4 : Cluster × Tier
  const clusterCounts = countBy(rows, col["Cluster"]);
  const top9Clusters  = Object.entries(clusterCounts).sort((a,b) => b[1]-a[1]).slice(0,9).map(e => e[0]);
  const clTierPivot   = crossTab(rows, col["Cluster"], col["Complexity_Tier"], tierOrder, top9Clusters);
  const D4_ROW = dataRow;
  ["Cluster","Small","Medium","Large"].forEach((h,i) => sheet.getRange(dataRow, DATA_START_COL+i).setValue(h));
  dataRow++;
  clTierPivot.forEach(([key, vals]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(key);
    tierOrder.forEach((t,i) => sheet.getRange(dataRow, DATA_START_COL+1+i).setValue(vals[t]||0));
    dataRow++;
  });
  const D4_END = dataRow - 1;
  dataRow += 2;

  // D5 : Volume par famille
  const famCounts = countBy(rows, col["Family_Label"]);
  const sortedFam = Object.entries(famCounts).sort((a,b) => b[1]-a[1]);
  const D5_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Famille");
  sheet.getRange(dataRow, DATA_START_COL+1).setValue("Total");
  dataRow++;
  sortedFam.forEach(([fam, cnt]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(fam);
    sheet.getRange(dataRow, DATA_START_COL+1).setValue(cnt);
    dataRow++;
  });
  const D5_END = dataRow - 1;
  dataRow += 2;

  // D6 : IT par famille
  let itFlagCol = "IT_Flag";
  if (col[itFlagCol] === undefined) {
    Object.keys(col).forEach(k => {
      if (k.trim().toLowerCase().replace(" ", "_") === "it_flag") itFlagCol = k;
    });
  }
  const itRows = rows.filter(r => {
    const val = col[itFlagCol] !== undefined ? String(r[col[itFlagCol]] || "") : "";
    return val.indexOf("IT") !== -1;
  });
  const itFamCounts = countBy(itRows, col["Family_Label"]);
  const sortedIT = Object.entries(itFamCounts).sort((a,b) => b[1]-a[1]);
  const D6_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Famille");
  sheet.getRange(dataRow, DATA_START_COL+1).setValue("Nb IT");
  dataRow++;
  
  if (sortedIT.length === 0) {
    sheet.getRange(dataRow, DATA_START_COL).setValue("Aucune donnée IT");
    sheet.getRange(dataRow, DATA_START_COL+1).setValue(0);
    dataRow++;
  } else {
    sortedIT.forEach(([fam, cnt]) => {
      sheet.getRange(dataRow, DATA_START_COL).setValue(fam);
      sheet.getRange(dataRow, DATA_START_COL+1).setValue(cnt);
      dataRow++;
    });
  }
  const D6_END = dataRow - 1;

  // G1 : Donut — Répartition par complexité
  insertChart(sheet, Charts.ChartType.PIE, {
    title:    "Répartition par complexité",
    dataRange: sheet.getRange(D1_ROW, DATA_START_COL, D1_END - D1_ROW + 1, 2),
    anchorRow: 4,  anchorCol: 2,
    width: 430, height: 360,
    options: {
      "pieHole":      0.55,
      "colors":       [COLORS.green, COLORS.gold, COLORS.red],
      "legend.position": "bottom",
      "chartArea.left":  "10%",
      "chartArea.width": "80%",
      "fontName":     "Calibri",
    }
  });

  // G2 : Bar horizontal — Top outils
  insertChart(sheet, Charts.ChartType.BAR, {
    title:    "Outils les plus utilisés",
    dataRange: sheet.getRange(D2_ROW, DATA_START_COL, D2_END - D2_ROW + 1, 2),
    anchorRow: 4,  anchorCol: 15,
    width: 480, height: 380,
    options: {
      "colors":           [COLORS.blue_mid],
      "legend.position":  "none",
      "hAxis.title":      "Nombre de use cases",
      "chartArea.left":   "35%",
      "chartArea.width":  "55%",
      "bar.groupWidth":   "70%",
      "fontName":         "Calibri",
    }
  });

  // G3 : Stacked bar — Famille × Tier
  insertChart(sheet, Charts.ChartType.BAR, {
    title:    "Mix de complexité par famille fonctionnelle",
    dataRange: sheet.getRange(D3_ROW, DATA_START_COL, D3_END - D3_ROW + 1, 4),
    anchorRow: 26, anchorCol: 2,
    width: 560, height: 400,
    options: {
      "isStacked":        true,
      "colors":           [COLORS.green, COLORS.gold, COLORS.red],
      "legend.position":  "top",
      "hAxis.title":      "Nombre de use cases",
      "chartArea.left":   "38%",
      "chartArea.width":  "52%",
      "bar.groupWidth":   "70%",
      "fontName":         "Calibri",
    }
  });

  // G4 : Stacked bar — Cluster × Tier
  insertChart(sheet, Charts.ChartType.BAR, {
    title:    "Mix de complexité par cluster",
    dataRange: sheet.getRange(D4_ROW, DATA_START_COL, D4_END - D4_ROW + 1, 4),
    anchorRow: 26, anchorCol: 19,
    width: 520, height: 400,
    options: {
      "isStacked":        true,
      "colors":           [COLORS.green, COLORS.gold, COLORS.red],
      "legend.position":  "top",
      "hAxis.title":      "Nombre de use cases",
      "chartArea.left":   "38%",
      "chartArea.width":  "52%",
      "bar.groupWidth":   "70%",
      "fontName":         "Calibri",
    }
  });

  // G5 : Column — Volume par famille
  insertChart(sheet, Charts.ChartType.COLUMN, {
    title:    "Volume total par famille fonctionnelle",
    dataRange: sheet.getRange(D5_ROW, DATA_START_COL, D5_END - D5_ROW + 1, 2),
    anchorRow: 48, anchorCol: 2,
    width: 560, height: 360,
    options: {
      "colors":          FAMILY_COLORS,
      "legend.position": "none",
      "vAxis.title":     "Nb use cases",
      "chartArea.left":  "10%",
      "chartArea.width": "85%",
      "bar.groupWidth":  "65%",
      "fontName":        "Calibri",
    }
  });

  // G6 : Column — IT par famille
  insertChart(sheet, Charts.ChartType.COLUMN, {
    title:    "⚠️ Points d'attention IT par famille",
    dataRange: sheet.getRange(D6_ROW, DATA_START_COL, D6_END - D6_ROW + 1, 2),
    anchorRow: 48, anchorCol: 19,
    width: 490, height: 360,
    options: {
      "colors":          [COLORS.red],
      "legend.position": "none",
      "vAxis.title":     "Use cases à escalader IT",
      "chartArea.left":  "12%",
      "chartArea.width": "82%",
      "bar.groupWidth":  "65%",
      "fontName":        "Calibri",
    }
  });
}

function buildFocusMediumLarge(ss, sheet, rows, col) {
  const TOTAL_COLS = 55;

  const currentCols = sheet.getMaxColumns();
  if (currentCols < TOTAL_COLS) {
    sheet.insertColumnsAfter(currentCols, TOTAL_COLS - currentCols);
  }

  sheet.setTabColor(COLORS.gold);
  sheet.setColumnWidths(1, TOTAL_COLS, 35);

  // En-tête banner
  const hdr = sheet.getRange(1, 1, 1, TOTAL_COLS);
  hdr.merge();
  hdr.setValue("AIR LIQUIDE  ·  AI Champions Use Cases  ·  Focus Medium & Large");
  hdr.setBackground(COLORS.navy);
  hdr.setFontColor(COLORS.gold);
  hdr.setFontSize(14);
  hdr.setFontWeight("bold");
  hdr.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 36);

  sheet.getRange(2, 1, 1, TOTAL_COLS).setBackground(COLORS.gold);
  sheet.setRowHeight(2, 4);

  const DATA_START_COL = 45; // AS - hors de la vue principale
  let dataRow = 5;

  const mlRows = rows.filter(r => {
    const tier = String(r[col["Complexity_Tier"]] || "");
    return tier === "Medium" || tier === "Large";
  });
  const mlTierOrder = ["Medium", "Large"];
  const stageOrder = ["Ideation", "POC", "MVP", "Testing / Eval", "In Development", "Scale-up", "Production", "A revoir avec le builder"];

  // D7 : Famille × Stage
  const famStagePivot = crossTab(mlRows, col["Family_Label"], col["Stage"], stageOrder);
  const D7_ROW = dataRow;
  const D7_HEADERS = ["Famille", ...stageOrder];
  D7_HEADERS.forEach((h, i) => sheet.getRange(dataRow, DATA_START_COL + i).setValue(h));
  dataRow++;
  famStagePivot.forEach(([key, vals]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(key);
    stageOrder.forEach((s, i) => sheet.getRange(dataRow, DATA_START_COL + 1 + i).setValue(vals[s] || 0));
    dataRow++;
  });
  const D7_END = dataRow - 1;
  dataRow += 2;

  // D9 : Medium vs Large donut
  const mlTierCounts = countBy(mlRows, col["Complexity_Tier"]);
  const D9_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Tier");
  sheet.getRange(dataRow, DATA_START_COL + 1).setValue("Count");
  dataRow++;
  mlTierOrder.forEach(t => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(t);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(mlTierCounts[t] || 0);
    dataRow++;
  });
  const D9_END = dataRow - 1;
  dataRow += 2;

  // D10 : Volume M+L par famille (Medium / Large séparés)
  const mlFamTierPivot = crossTab(mlRows, col["Family_Label"], col["Complexity_Tier"], mlTierOrder);
  const D10_ROW = dataRow;
  ["Famille", "Medium", "Large"].forEach((h, i) => sheet.getRange(dataRow, DATA_START_COL + i).setValue(h));
  dataRow++;
  mlFamTierPivot.forEach(([key, vals]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(key);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(vals["Medium"] || 0);
    sheet.getRange(dataRow, DATA_START_COL + 2).setValue(vals["Large"] || 0);
    dataRow++;
  });
  const D10_END = dataRow - 1;
  dataRow += 2;

  // D11 : Top Sources de données (Medium & Large uniquement)
  const mlSourceCounts = {};
  mlRows.forEach(r => {
    const rawSources = String(r[col["Data_Sources"]] || "A revoir avec le builder");
    const individualSources = rawSources.split(",").map(s => s.trim()).filter(Boolean);
    individualSources.forEach(src => {
      mlSourceCounts[src] = (mlSourceCounts[src] || 0) + 1;
    });
  });
  const sortedMlSources = Object.entries(mlSourceCounts).sort((a, b) => b[1] - a[1]);
  const D11_ROW = dataRow;
  sheet.getRange(dataRow, DATA_START_COL).setValue("Source de données");
  sheet.getRange(dataRow, DATA_START_COL + 1).setValue("Total");
  dataRow++;
  sortedMlSources.forEach(([src, count]) => {
    sheet.getRange(dataRow, DATA_START_COL).setValue(src);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(count);
    dataRow++;
  });
  const D11_END = dataRow - 1;
  dataRow += 2;

  // D12 : Top 8 Sources × Complexité (Medium & Large uniquement)
  const top8Sources = sortedMlSources.slice(0, 8).map(e => e[0]);
  const D12_ROW = dataRow;
  ["Source de données", "Medium", "Large"].forEach((h, i) => sheet.getRange(dataRow, DATA_START_COL + i).setValue(h));
  dataRow++;
  top8Sources.forEach(src => {
    let mediumCount = 0;
    let largeCount = 0;
    mlRows.forEach(r => {
      const rawSources = String(r[col["Data_Sources"]] || "A revoir avec le builder");
      const individualSources = rawSources.split(",").map(s => s.trim()).filter(Boolean);
      if (individualSources.includes(src)) {
        const tier = String(r[col["Complexity_Tier"]] || "");
        if (tier === "Medium") mediumCount++;
        else if (tier === "Large") largeCount++;
      }
    });
    sheet.getRange(dataRow, DATA_START_COL).setValue(src);
    sheet.getRange(dataRow, DATA_START_COL + 1).setValue(mediumCount);
    sheet.getRange(dataRow, DATA_START_COL + 2).setValue(largeCount);
    dataRow++;
  });
  const D12_END = dataRow - 1;

  // G7 : Donut — Medium vs Large
  insertChart(sheet, Charts.ChartType.PIE, {
    title:    "Répartition Medium vs Large",
    dataRange: sheet.getRange(D9_ROW, DATA_START_COL, D9_END - D9_ROW + 1, 2),
    anchorRow: 71, anchorCol: 2,
    width: 400, height: 340,
    options: {
      "pieHole":         0.55,
      "colors":          [COLORS.gold, COLORS.red],
      "legend.position": "bottom",
      "chartArea.left":  "10%",
      "chartArea.width": "80%",
      "fontName":        "Calibri",
    }
  });

  // G8 : Stacked Column — Volume Medium + Large par famille
  insertChart(sheet, Charts.ChartType.COLUMN, {
    title:    "Volume Medium + Large par famille",
    dataRange: sheet.getRange(D10_ROW, DATA_START_COL, D10_END - D10_ROW + 1, 3),
    anchorRow: 71, anchorCol: 16,
    width: 520, height: 360,
    options: {
      "isStacked":       true,
      "colors":          [COLORS.gold, COLORS.red],
      "legend.position": "top",
      "vAxis.title":     "Nb use cases",
      "chartArea.left":  "10%",
      "chartArea.width": "80%",
      "bar.groupWidth":  "65%",
      "fontName":        "Calibri",
    }
  });

  // G9 : Stacked column — Famille × Stage (M+L only)
  insertChart(sheet, Charts.ChartType.COLUMN, {
    title:    "Maturité par famille (Medium + Large)",
    dataRange: sheet.getRange(D7_ROW, DATA_START_COL, D7_END - D7_ROW + 1, stageOrder.length + 1),
    anchorRow: 92, anchorCol: 2,
    width: 720, height: 420,
    options: {
      "isStacked":        true,
      "colors":           ["#BDC3C7", COLORS.blue_light, COLORS.teal, COLORS.blue_mid, COLORS.blue_dark, COLORS.green, COLORS.purple, "#F0F0F0"],
      "legend.position":  "top",
      "vAxis.title":      "Nombre de use cases",
      "chartArea.left":   "8%",
      "chartArea.width":  "85%",
      "bar.groupWidth":   "70%",
      "fontName":         "Calibri",
      "series":           { 7: { color: "#F0F0F0" } },
    }
  });

  // G10 : Bar horizontal — Top sources de données (Medium & Large)
  insertChart(sheet, Charts.ChartType.BAR, {
    title:    "Top des sources de données (Medium + Large)",
    dataRange: sheet.getRange(D11_ROW, DATA_START_COL, D11_END - D11_ROW + 1, 2),
    anchorRow: 115, anchorCol: 2,
    width: 480, height: 380,
    options: {
      "colors":           [COLORS.blue_mid],
      "legend.position":  "none",
      "hAxis.title":      "Nombre de sollicitations",
      "chartArea.left":   "30%",
      "chartArea.width":  "60%",
      "bar.groupWidth":   "70%",
      "fontName":         "Calibri",
    }
  });

  // G11 : Stacked Column — Top 8 sources × Complexité (Medium vs Large)
  insertChart(sheet, Charts.ChartType.COLUMN, {
    title:    "Complexité par source de données (Top 8)",
    dataRange: sheet.getRange(D12_ROW, DATA_START_COL, D12_END - D12_ROW + 1, 3),
    anchorRow: 115, anchorCol: 18,
    width: 520, height: 380,
    options: {
      "isStacked":        true,
      "colors":           [COLORS.gold, COLORS.red],
      "legend.position":  "top",
      "vAxis.title":      "Nombre de use cases",
      "chartArea.left":   "10%",
      "chartArea.width":  "80%",
      "bar.groupWidth":   "65%",
      "fontName":         "Calibri",
    }
  });
}


// ── Utilitaires ───────────────────────────────────────────────────────────────

/** Compte les occurrences d'une colonne */
function countBy(rows, colIdx) {
  const counts = {};
  rows.forEach(r => {
    const val = String(r[colIdx] || "N/A");
    counts[val] = (counts[val] || 0) + 1;
  });
  return counts;
}

/** Tableau croisé dynamique : rowField × colField */
function crossTab(rows, rowColIdx, colColIdx, colOrder, filterKeys) {
  const pivot = {};
  rows.forEach(r => {
    const rowVal = String(r[rowColIdx] || "N/A");
    const colVal = String(r[colColIdx] || "N/A");
    if (filterKeys && !filterKeys.includes(rowVal)) return;
    if (!pivot[rowVal]) pivot[rowVal] = {};
    pivot[rowVal][colVal] = (pivot[rowVal][colVal] || 0) + 1;
  });
  const keys = filterKeys || Object.keys(pivot);
  return keys
    .filter(k => pivot[k])
    .sort((a,b) => {
      const tA = colOrder.reduce((s,c) => s + (pivot[a][c]||0), 0);
      const tB = colOrder.reduce((s,c) => s + (pivot[b][c]||0), 0);
      return tB - tA;
    })
    .map(k => [k, pivot[k]]);
}

/** Insère un graphique Google Sheets natif */
function insertChart(sheet, chartType, { title, dataRange, anchorRow, anchorCol, width, height, options }) {
  let builder = sheet.newChart()
    .setChartType(chartType)
    .addRange(dataRange)
    .setPosition(anchorRow, anchorCol, 0, 0)
    .setNumHeaders(1)
    .setOption("title", title)
    .setOption("titleTextStyle", { fontSize: 13, bold: true, color: COLORS.navy })
    .setOption("backgroundColor", COLORS.white)
    .setOption("width",  width)
    .setOption("height", height);

  Object.entries(options).forEach(([k, v]) => { builder = builder.setOption(k, v); });

  sheet.insertChart(builder.build());
}


// ── Tableau des Sources de données nécessaires par famille ──────────────────
function writeSourcesTable(sheet, rows, col, startRow, startCol) {
  const families = ["F1", "F2", "F3", "F4", "F5", "F6", "F7"];
  const famLabels = {
    "F1": "Automatisation documentaire",
    "F2": "Assistant BI & décisionnel",
    "F3": "Customer & Sales Intelligence",
    "F4": "Monitoring & Maintenance industrielle",
    "F5": "Knowledge Management & Formation",
    "F6": "Automatisation de workflows internes",
    "F7": "Data Engineering & Reporting"
  };

  // Titre section
  const colCount = families.length + 3; // Source + F1..F7 + Total + % Global
  const titleRange = sheet.getRange(startRow, startCol, 1, colCount);
  titleRange.merge();
  titleRange.setValue("⑦ Sources de données nécessaires par famille (Comptage unitaire)");
  titleRange.setBackground(COLORS.header_bg);
  titleRange.setFontColor(COLORS.white);
  titleRange.setFontWeight("bold");
  titleRange.setFontSize(10);
  sheet.setRowHeight(startRow, 26);
  startRow++;

  // En-têtes colonnes
  const headers = ["Source de données", ...families, "Total", "% Global"];
  const hRange = sheet.getRange(startRow, startCol, 1, headers.length);
  hRange.setValues([headers]);
  hRange.setBackground(COLORS.blue_mid);
  hRange.setFontColor(COLORS.white);
  hRange.setFontWeight("bold");
  hRange.setHorizontalAlignment("center");
  hRange.getCell(1, 1).setHorizontalAlignment("left");
  startRow++;

  // Calculer l'occurrence unitaire par famille et par source
  const sourceFamilyCounts = {}; // { sourceName: { F1: count, F2: count, ... } }
  const sourceTotals = {};
  const globalTotalUseCases = rows.length;

  rows.forEach(r => {
    const rawSources = String(r[col["Data_Sources"]] || "A revoir avec le builder");
    const familyCode = String(r[col["Family"]] || "F1"); // F1-F7
    
    // Separer les sources de donnees unitaires
    const individualSources = rawSources.split(",").map(s => s.trim()).filter(Boolean);
    
    individualSources.forEach(src => {
      if (!sourceFamilyCounts[src]) {
        sourceFamilyCounts[src] = {};
        families.forEach(f => sourceFamilyCounts[src][f] = 0);
        sourceTotals[src] = 0;
      }
      sourceFamilyCounts[src][familyCode] = (sourceFamilyCounts[src][familyCode] || 0) + 1;
      sourceTotals[src]++;
    });
  });

  // Trier les sources par total décroissant (avec "A revoir avec le builder" à la fin)
  const sortedSources = Object.keys(sourceFamilyCounts).sort((a, b) => {
    if (a === "A revoir avec le builder") return 1;
    if (b === "A revoir avec le builder") return -1;
    return sourceTotals[b] - sourceTotals[a];
  });

  // Écrire les lignes
  sortedSources.forEach((src, idx) => {
    const rowData = [src];
    families.forEach(f => {
      rowData.push(sourceFamilyCounts[src][f] || 0);
    });
    rowData.push(sourceTotals[src]);
    // Calculer le % global par rapport au total de tous les use cases
    const pct = sourceTotals[src] / globalTotalUseCases;
    rowData.push(pct);

    const range = sheet.getRange(startRow, startCol, 1, rowData.length);
    range.setValues([rowData]);
    range.setHorizontalAlignment("center");
    range.getCell(1, 1).setHorizontalAlignment("left");
    
    // Formater le pourcentage
    const pctCell = range.getCell(1, rowData.length);
    pctCell.setNumberFormat("0.0%");

    if (idx % 2 === 0) range.setBackground(COLORS.gray_light);
    startRow++;
  });

  // Légende explicative
  startRow++;
  const legTitle = sheet.getRange(startRow, startCol, 1, colCount);
  legTitle.setValue("Légende des familles fonctionnelles :");
  legTitle.setFontWeight("bold");
  legTitle.setFontSize(9);
  startRow++;

  families.forEach(f => {
    const legRange = sheet.getRange(startRow, startCol, 1, colCount);
    legRange.merge();
    legRange.setValue(`• ${f} : ${famLabels[f]}`);
    legRange.setFontSize(9);
    legRange.setFontColor("#555555");
    startRow++;
  });

  return startRow;
}

