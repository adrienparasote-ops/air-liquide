#!/usr/bin/env python3
"""
generate_docx.py
────────────────
Génère le rapport de synthèse Word (.docx) Air Liquide — AI Champions
avec la charte graphique Pyl.Tech (navy #0b132b, jaune #F4BF46, turquoise #208AAE).

Usage : python3 src/generate_docx.py
Output: docs/rapport_ai_champions.docx
"""
import sys
from pathlib import Path
from datetime import date

try:
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    import pandas as pd
except ImportError as e:  # pragma: no cover
    print(f"❌ Dépendance manquante : {e}\n   pip install python-docx pandas openpyxl")  # noqa
    sys.exit(1)

# ── Chemins ───────────────────────────────────────────────────────────────────
PROJECT_DIR  = Path(__file__).parent.parent
CATALOG_FILE = PROJECT_DIR / "docs" / "use_cases_catalog.xlsx"
OUTPUT_FILE  = PROJECT_DIR / "docs" / "rapport_ai_champions.docx"

# ── Palette Pyl.Tech officielle ───────────────────────────────────────────────
PYL_NAVY_DARK  = RGBColor(0x0B, 0x13, 0x2B)   # Titres / fonds sombres
PYL_NAVY       = RGBColor(0x0D, 0x21, 0x49)   # Accent 2
PYL_YELLOW     = RGBColor(0xF4, 0xBF, 0x46)   # Jaune primaire
PYL_TEAL_BLUE  = RGBColor(0x20, 0x8A, 0xAE)   # Turquoise — footer, pagination
PYL_TEAL       = RGBColor(0x5B, 0xC0, 0xBE)   # Vert d'eau
PYL_BODY_GREY  = RGBColor(0x4F, 0x4F, 0x4F)   # Corps de texte
PYL_GREY_BG    = RGBColor(0xEE, 0xEE, 0xEE)   # Fond shapes
PYL_WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
PYL_SUCCESS    = RGBColor(0x13, 0x86, 0x36)
PYL_DANGER     = RGBColor(0xC9, 0x14, 0x32)

YEAR = date.today().year

# ── Helpers XML ───────────────────────────────────────────────────────────────

def set_cell_bg(cell, rgb: RGBColor) -> None:
    """Applique un fond coloré à une cellule de tableau."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    hex_val = f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    shd.set(qn("w:fill"), hex_val)
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def add_border_left(paragraph, hex_color: str, size_pt: int = 18) -> None:
    """Ajoute une bordure gauche colorée sur un paragraphe (callout)."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), str(size_pt))
    left.set(qn("w:space"), "4")
    left.set(qn("w:color"), hex_color)
    pBdr.append(left)
    pPr.append(pBdr)


def highlight_run(run, hex_color: str = "F4BF46") -> None:
    """Surlignage jaune charte (style marqueur fluo)."""
    rPr = run._r.get_or_add_rPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:val"), "clear")
    rPr.append(shd)


def set_paragraph_spacing(paragraph, space_before: int = 0, space_after: int = 6) -> None:
    pPr = paragraph._p.get_or_add_pPr()
    pSp = OxmlElement("w:spacing")
    pSp.set(qn("w:before"), str(space_before * 20))
    pSp.set(qn("w:after"), str(space_after * 20))
    pPr.append(pSp)


# ── Composants de document ────────────────────────────────────────────────────

def apply_base_styles(doc: Document) -> None:
    """Configure les styles globaux du document."""
    section = doc.sections[0]
    section.top_margin    = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

    # Style Normal (body)
    normal = doc.styles["Normal"]
    normal.font.name  = "Poppins"
    normal.font.size  = Pt(12)
    normal.font.color.rgb = PYL_BODY_GREY

    # Heading 1
    h1 = doc.styles["Heading 1"]
    h1.font.name  = "Poppins"
    h1.font.bold  = True
    h1.font.size  = Pt(24)
    h1.font.color.rgb = PYL_NAVY_DARK

    # Heading 2
    h2 = doc.styles["Heading 2"]
    h2.font.name  = "Poppins"
    h2.font.bold  = True
    h2.font.size  = Pt(18)
    h2.font.color.rgb = PYL_NAVY_DARK

    # Heading 3
    h3 = doc.styles["Heading 3"]
    h3.font.name  = "Poppins"
    h3.font.bold  = True
    h3.font.size  = Pt(14)
    h3.font.color.rgb = PYL_NAVY_DARK


def add_cover_page(doc: Document) -> None:
    """Page de couverture style Pyl.Tech (fond jaune simulé via tableaux)."""
    # Bandeau de titre en jaune
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = "Table Grid"
    cell = tbl.cell(0, 0)
    set_cell_bg(cell, PYL_YELLOW)
    cell.width = Cm(16)

    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Air Liquide — AI Champions")
    run.font.name  = "Poppins"
    run.font.bold  = True
    run.font.size  = Pt(28)
    run.font.color.rgb = PYL_NAVY_DARK
    set_paragraph_spacing(p, 24, 4)

    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("Analyse et Catalogue des Use Cases IA")
    r2.font.name  = "Poppins"
    r2.font.italic = True
    r2.font.size  = Pt(16)
    r2.font.color.rgb = PYL_NAVY_DARK
    set_paragraph_spacing(p2, 4, 24)

    # Sous-bloc info
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run(f"Produit par Pyl.Tech  •  {date.today().strftime('%B %Y')}")
    r3.font.name  = "Poppins"
    r3.font.size  = Pt(11)
    r3.font.color.rgb = PYL_TEAL_BLUE
    set_paragraph_spacing(p3, 12, 12)

    doc.add_page_break()


def add_section_header(doc: Document, number: str, title: str, subtitle: str = "") -> None:
    """Ajoute un titre de section avec cartouche jaune (simulé via couleur de run)."""
    p = doc.add_paragraph()
    p.style = "Heading 1"
    set_paragraph_spacing(p, 24, 6)

    badge = p.add_run(f" {number} ")
    badge.font.name  = "Poppins"
    badge.font.bold  = True
    badge.font.size  = Pt(14)
    badge.font.color.rgb = PYL_NAVY_DARK
    highlight_run(badge)

    p.add_run("  ")

    title_run = p.add_run(title)
    title_run.font.name  = "Poppins"
    title_run.font.bold  = True
    title_run.font.size  = Pt(20)
    title_run.font.color.rgb = PYL_NAVY_DARK

    if subtitle:
        p2 = doc.add_paragraph(subtitle)
        p2.style = "Normal"
        p2.runs[0].font.size  = Pt(12)
        p2.runs[0].font.color.rgb = PYL_BODY_GREY
        set_paragraph_spacing(p2, 0, 8)


def add_kpi_block(doc: Document, kpis: list[tuple[str, str, str]]) -> None:
    """Bloc KPIs en tableau (label / valeur / contexte) style Pyl.Tech."""
    tbl = doc.add_table(rows=1 + len(kpis), cols=3)
    tbl.style = "Table Grid"

    # Header
    headers = ["Indicateur", "Valeur", "Contexte"]
    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        set_cell_bg(cell, PYL_NAVY_DARK)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name  = "Poppins"
        run.font.bold  = True
        run.font.size  = Pt(10)
        run.font.color.rgb = PYL_WHITE

    # Body
    for r_idx, (label, value, context) in enumerate(kpis):
        bg = PYL_NAVY if r_idx % 2 == 0 else PYL_WHITE
        fg = PYL_WHITE if r_idx % 2 == 0 else PYL_BODY_GREY

        for c_idx, text in enumerate([label, value, context]):
            cell = tbl.cell(r_idx + 1, c_idx)
            set_cell_bg(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            run.font.name  = "Poppins"
            run.font.size  = Pt(10)
            run.font.color.rgb = fg
            if c_idx == 1:
                run.font.bold = True

    doc.add_paragraph()  # espacement


def add_pivot_table(doc: Document, title: str, headers: list[str], rows: list[list[str]]) -> None:
    """Tableau croisé Pyl.Tech."""
    p_title = doc.add_paragraph(title)
    p_title.style = "Heading 3"
    set_paragraph_spacing(p_title, 12, 4)

    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tbl.style = "Table Grid"

    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        set_cell_bg(cell, PYL_NAVY)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name  = "Poppins"
        run.font.bold  = True
        run.font.size  = Pt(10)
        run.font.color.rgb = PYL_WHITE

    for r_idx, row_data in enumerate(rows):
        bg = PYL_GREY_BG if r_idx % 2 == 0 else PYL_WHITE
        fg = PYL_BODY_GREY
        for c_idx, val in enumerate(row_data):
            cell = tbl.cell(r_idx + 1, c_idx)
            set_cell_bg(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(str(val))
            run.font.name  = "Poppins"
            run.font.size  = Pt(10)
            run.font.color.rgb = fg
            if c_idx == len(row_data) - 1:
                run.font.bold = True  # Total en gras

    doc.add_paragraph()


def add_callout(doc: Document, text: str, style: str = "info") -> None:
    """Encadré callout avec bordure gauche colorée."""
    color_map = {
        "info":    "F4BF46",
        "warning": "C91432",
        "success": "138636",
        "note":    "0b132b",
    }
    border_hex = color_map.get(style, "F4BF46")

    p = doc.add_paragraph()
    add_border_left(p, border_hex, size_pt=24)
    run = p.add_run(text)
    run.font.name  = "Poppins"
    run.font.size  = Pt(11)
    run.font.color.rgb = PYL_BODY_GREY
    run.font.italic = True
    set_paragraph_spacing(p, 6, 6)


def add_bullet(doc: Document, text: str, bold_prefix: str = "") -> None:
    """Bullet Pyl.Tech avec puce carrée jaune simulée par caractère."""
    p = doc.add_paragraph()
    p.style = "Normal"

    bullet_run = p.add_run("▪  ")
    bullet_run.font.name  = "Poppins"
    bullet_run.font.size  = Pt(12)
    bullet_run.font.color.rgb = PYL_YELLOW
    bullet_run.font.bold  = True

    if bold_prefix:
        bold_run = p.add_run(bold_prefix)
        bold_run.font.name  = "Poppins"
        bold_run.font.bold  = True
        bold_run.font.size  = Pt(12)
        bold_run.font.color.rgb = PYL_NAVY_DARK

        sep = p.add_run(" — ")
        sep.font.name  = "Poppins"
        sep.font.size  = Pt(12)
        sep.font.color.rgb = PYL_BODY_GREY

    body_run = p.add_run(text)
    body_run.font.name  = "Poppins"
    body_run.font.size  = Pt(12)
    body_run.font.color.rgb = PYL_BODY_GREY
    set_paragraph_spacing(p, 0, 4)


# ── Corps du document ─────────────────────────────────────────────────────────

def build_document(doc: Document, df: pd.DataFrame) -> None:
    """Construit le contenu complet du rapport."""

    # ── Métriques globales ────────────────────────────────────────────────────
    total = len(df)
    tiers = df["Complexity_Tier"].value_counts().to_dict()
    it_count = (df["IT_Flag"] != "").sum()
    clusters = df["Cluster"].nunique()
    job_families = df["Job Family"].nunique()

    # ══ PAGE 1 : EXECUTIVE SUMMARY ══════════════════════════════════════════
    add_section_header(doc, "01", "Executive Summary",
        "Vue d'ensemble de l'analyse du portefeuille AI Champions d'Air Liquide")

    summary_text = (
        f"L'analyse du portefeuille AI Champions d'Air Liquide porte sur {total} use cases validés, "
        f"répartis sur {clusters} clusters et {job_families} familles métier. "
        f"La majorité des initiatives ({tiers.get('Small', 0) + tiers.get('Medium', 0)} use cases) "
        f"présente un profil accessible (Small/Medium), confirmant une maturité collective "
        f"significative dans l'adoption des outils IA Google Workspace. "
        f"{it_count} use cases ({it_count * 100 // total}%) nécessitent un accompagnement IT dédié "
        f"en raison de leurs dépendances systèmes."
    )
    p = doc.add_paragraph(summary_text)
    p.style = "Normal"
    set_paragraph_spacing(p, 6, 12)

    # KPIs globaux
    kpis = [
        ("Use cases analysés", str(total), "248 identifiés, dupliqués exclus"),
        ("Clusters couverts", str(clusters), "Périmètre géographique/organisationnel"),
        ("Familles métier", str(job_families), "Profils de champions"),
        ("Quick Wins (Small)", str(tiers.get("Small", 0)), "Déployables en < 2 semaines"),
        ("Use cases structurants (Medium)", str(tiers.get("Medium", 0)), "4 à 8 semaines de delivery"),
        ("Projets stratégiques (Large)", str(tiers.get("Large", 0)), "3 à 12 mois — IT impliqué"),
        ("Points d'attention IT", str(it_count), "Escalade obligatoire"),
    ]
    add_kpi_block(doc, kpis)

    add_callout(doc,
        "La population de champions AI n'est pas une population IT. Les use cases Large ou "
        "impliquant des systèmes d'entreprise (SFDC, SAP, DCS, SCADA) ne peuvent être conduits "
        "sans accompagnement technique dédié.",
        style="warning")

    doc.add_page_break()

    # ══ PAGE 2 : RÉPARTITION PAR COMPLEXITÉ ════════════════════════════════
    add_section_header(doc, "02", "Répartition par complexité",
        "Classification Small / Medium / Large selon 5 dimensions de scoring")

    p = doc.add_paragraph(
        "Chaque use case est scoré sur 5 dimensions (intégration technique, périmètre organisationnel, "
        "complexité data, maturité IA, impact économique), chacune notée de 1 à 3 points. "
        "Le score total (5–15 pts) détermine le tier de complexité."
    )
    p.style = "Normal"
    set_paragraph_spacing(p, 6, 12)

    # Tableau de classification
    add_pivot_table(doc,
        "Grille de classification par tier",
        ["Tier", "Score", "Label", "Time-to-value", "Nb Use Cases"],
        [
            ["Small",  "5–7",   "Quick Win",             "< 2 semaines",  str(tiers.get("Small", 0))],
            ["Medium", "8–11",  "Use Case Structurant",  "4–8 semaines",  str(tiers.get("Medium", 0))],
            ["Large",  "12–15", "Projet Stratégique",    "3–12 mois",     str(tiers.get("Large", 0))],
            ["TOTAL",  "",      "",                       "",              str(total)],
        ]
    )

    # Répartition par famille fonctionnelle x tier
    add_section_header(doc, "", "Famille fonctionnelle x Tier", "")
    pivot_rows = []
    for fam_label in df["Family_Label"].unique():
        subset = df[df["Family_Label"] == fam_label]
        s = subset["Complexity_Tier"].value_counts().to_dict()
        tot = len(subset)
        pivot_rows.append([
            fam_label,
            str(s.get("Small", 0)),
            str(s.get("Medium", 0)),
            str(s.get("Large", 0)),
            str(tot),
        ])
    pivot_rows.sort(key=lambda x: -int(x[4]))
    pivot_rows.append(["TOTAL",
        str(tiers.get("Small", 0)),
        str(tiers.get("Medium", 0)),
        str(tiers.get("Large", 0)),
        str(total)])

    add_pivot_table(doc, "Famille x Complexité",
        ["Famille fonctionnelle", "Small", "Medium", "Large", "Total"],
        pivot_rows)

    doc.add_page_break()

    # ══ PAGE 3 : ANALYSE PAR CLUSTER ═══════════════════════════════════════
    add_section_header(doc, "03", "Analyse par Cluster",
        "Répartition géographique et organisationnelle des use cases")

    cluster_data = df.groupby("Cluster")["Complexity_Tier"].value_counts().unstack(fill_value=0)
    cluster_rows = []
    for cluster in cluster_data.index:
        row = [cluster]
        for tier in ["Small", "Medium", "Large"]:
            val = int(cluster_data.loc[cluster, tier]) if tier in cluster_data.columns else 0
            row.append(str(val))
        row.append(str(int(cluster_data.loc[cluster].sum())))
        cluster_rows.append(row)
    cluster_rows.sort(key=lambda x: -int(x[4]))

    add_pivot_table(doc, "Cluster x Complexité",
        ["Cluster", "Small", "Medium", "Large", "Total"],
        cluster_rows[:15])  # Top 15 clusters

    doc.add_page_break()

    # ══ PAGE 4 : CATALOGUE PAR FAMILLE ═════════════════════════════════════
    add_section_header(doc, "04", "Catalogue par famille fonctionnelle",
        "Présentation des 7 familles identifiées — définition et caractéristiques")

    family_descriptions = {
        "Automatisation documentaire":          ("F1", "Traduction, rédaction, résumé, génération de rapports et de contrats. Outils dominants : Gemini Prompts/Gems, NotebookLM."),
        "Assistant BI & décisionnel":           ("F2", "Tableaux de bord, analyses prédictives, alertes KPI, support à la décision. Outils dominants : Power BI, App Script, Gemini."),
        "Customer & Sales Intelligence":        ("F3", "Analyse clients SFDC, optimisation des visites, scoring commercial, CRM augmenté."),
        "Monitoring & Maintenance industrielle": ("F4", "Prédiction de pannes, analyse capteurs, surveillance process DCS/SCADA/AVEVA."),
        "Knowledge Management & Formation":     ("F5", "Bases de connaissance, FAQ intelligentes, chatbots formation, onboarding IA."),
        "Automatisation de workflows internes": ("F6", "Automatisation de processus administratifs, déclencheurs, flows App Script."),
        "Data Engineering & Reporting":         ("F7", "Pipelines de données, extraction/transformation, reporting Power BI, Python Fabric."),
    }

    for fam_label, (fam_code, fam_desc) in family_descriptions.items():
        subset = df[df["Family_Label"] == fam_label]
        if subset.empty:
            continue

        p_fam = doc.add_paragraph()
        p_fam.style = "Heading 2"
        badge = p_fam.add_run(f" {fam_code} ")
        badge.font.name  = "Poppins"
        badge.font.bold  = True
        badge.font.size  = Pt(12)
        badge.font.color.rgb = PYL_NAVY_DARK
        highlight_run(badge)
        p_fam.add_run("  ")
        tr = p_fam.add_run(fam_label)
        tr.font.name  = "Poppins"
        tr.font.bold  = True
        tr.font.size  = Pt(16)
        tr.font.color.rgb = PYL_NAVY_DARK
        set_paragraph_spacing(p_fam, 16, 4)

        desc_p = doc.add_paragraph(fam_desc)
        desc_p.style = "Normal"
        set_paragraph_spacing(desc_p, 0, 8)

        tier_s = subset["Complexity_Tier"].value_counts().to_dict()
        add_bullet(doc, f"{len(subset)} use cases identifiés", "Volume")
        add_bullet(doc,
            f"{tier_s.get('Small', 0)} Small / {tier_s.get('Medium', 0)} Medium / {tier_s.get('Large', 0)} Large",
            "Répartition")
        it_sub = (subset["IT_Flag"] != "").sum()
        if it_sub > 0:
            add_bullet(doc, f"{it_sub} use cases avec point d'attention IT", "Alerte IT")
        quick_wins_uc = subset[subset["Complexity_Tier"] == "Small"].head(3)
        if not quick_wins_uc.empty:
            p_h = doc.add_paragraph("Top Quick Wins de la famille")
            p_h.style = "Heading 3"
            set_paragraph_spacing(p_h, 8, 4)
            for _, row in quick_wins_uc.iterrows():
                desc_short = str(row["Use Case Description (Long)"])[:120].strip()
                if len(str(row["Use Case Description (Long)"])) > 120:
                    desc_short += "…"
                add_bullet(doc, f"[{row['UC_ID']}] {desc_short} (Score: {row['Score_Total']})")

        doc.add_paragraph()  # espace

    doc.add_page_break()

    # ══ PAGE 5 : POINTS D'ATTENTION IT ════════════════════════════════════
    add_section_header(doc, "05", "Points d'attention IT",
        f"{it_count} use cases nécessitant un accompagnement technique dédié")

    add_callout(doc,
        "Ces use cases impliquent des dépendances systèmes (SFDC, SAP, DCS, SCADA, BigQuery, API) "
        "ou ont un profil Large qui dépasse les capacités d'un champion seul. "
        "Une coordination avec les équipes IT locales est obligatoire avant tout déploiement.",
        style="warning")

    it_df = df[df["IT_Flag"] != ""].copy()
    it_by_family = it_df.groupby("Family_Label").size().reset_index(name="count").sort_values("count", ascending=False)

    add_pivot_table(doc,
        "Points d'attention IT par famille",
        ["Famille fonctionnelle", "Nb use cases IT"],
        [[row["Family_Label"], str(row["count"])] for _, row in it_by_family.iterrows()])

    # Top 15 use cases IT
    p_h = doc.add_paragraph("Sélection de use cases à escalader en priorité (Large ou multi-systèmes)")
    p_h.style = "Heading 3"
    set_paragraph_spacing(p_h, 12, 4)

    top_it = it_df.nlargest(15, "Score_Total")
    it_rows = []
    for _, row in top_it.iterrows():
        desc = str(row["Use Case Description (Long)"])[:80].strip()
        if len(str(row["Use Case Description (Long)"])) > 80:
            desc += "…"
        it_rows.append([
            str(row["UC_ID"]),
            str(row["Cluster"]),
            str(row["Family_Label"]),
            str(row["Complexity_Tier"]),
            desc,
        ])

    add_pivot_table(doc, "",
        ["UC_ID", "Cluster", "Famille", "Tier", "Description"],
        it_rows)

    doc.add_page_break()

    # ══ PAGE 6 : RECOMMANDATIONS ═══════════════════════════════════════════
    add_section_header(doc, "06", "Recommandations et Roadmap",
        "5 axes prioritaires pour industrialiser les use cases AI Champions")

    recommendations = [
        ("Industrialiser les Quick Wins (Small)",
         f"{tiers.get('Small', 0)} use cases Small sont déployables immédiatement avec peu ou pas de support IT. "
         "Constituer une bibliothèque de Gems et de Prompts partagés par famille fonctionnelle. "
         "Viser 3 mois pour dupliquer les 10 meilleures pratiques à l'ensemble des clusters."),
        ("Structurer l'accompagnement des Medium",
         f"{tiers.get('Medium', 0)} use cases Medium nécessitent un encadrement léger (champion + support IT local). "
         "Mettre en place des sprints de 4 semaines avec un champion référent par cluster. "
         "NotebookLM et App Script sont les vecteurs principaux pour ces cas."),
        ("Créer une filière IT pour les Large",
         f"{tiers.get('Large', 0)} projets stratégiques (Large) nécessitent une équipe projet dédiée. "
         "Identifier les sponsors métier et les correspondants IT pour chaque projet. "
         "Ces cas représentent des investissements 3–12 mois."),
        ("Adresser les 80 points d'attention IT",
         f"{it_count} use cases présentent des dépendances systèmes critiques (SFDC, SAP, DCS, API). "
         "Un atelier de priorisation avec les équipes IT est recommandé avant tout engagement. "
         "Créer un registre de dépendances partagé entre les champions et l'IT."),
        ("Consolider la famille F7 — Data Engineering",
         "La famille Data Engineering & Reporting (59 use cases) est la plus dense et la plus complexe. "
         "Elle nécessite des compétences Python/BigQuery qui dépassent le profil champion standard. "
         "Envisager un track spécifique 'Data Champion' avec certification."),
    ]

    for i, (title, body) in enumerate(recommendations, start=1):
        p_rec = doc.add_paragraph()
        badge_r = p_rec.add_run(f" 0{i} ")
        badge_r.font.name  = "Poppins"
        badge_r.font.bold  = True
        badge_r.font.size  = Pt(12)
        badge_r.font.color.rgb = PYL_NAVY_DARK
        highlight_run(badge_r)
        p_rec.add_run("  ")
        t_run = p_rec.add_run(title)
        t_run.font.name  = "Poppins"
        t_run.font.bold  = True
        t_run.font.size  = Pt(14)
        t_run.font.color.rgb = PYL_NAVY_DARK
        set_paragraph_spacing(p_rec, 14, 4)

        p_body = doc.add_paragraph(body)
        p_body.style = "Normal"
        set_paragraph_spacing(p_body, 0, 10)

    doc.add_page_break()

    # ══ PAGE 7 : BONNES PRATIQUES ══════════════════════════════════════════
    add_section_header(doc, "07", "Guide des bonnes pratiques",
        "Recommandations méthodologiques pour piloter les use cases AI Champions")

    best_practices = [
        ("Partir du besoin, pas de l'outil",
         "Identifier d'abord le problème à résoudre, puis sélectionner l'outil le plus adapté. "
         "Ne pas chercher à appliquer un outil pour lequel on vient de se former."),
        ("Documenter le use case avant de coder",
         "Un use case bien documenté (contexte, bénéficiaires, données utilisées, outil, résultat attendu) "
         "est un use case qui se déploie. Sans documentation, la duplication est impossible."),
        ("Mesurer le time-to-value réel",
         "Enregistrer la date de démarrage et la date de premier résultat mesurable. "
         "Les Small doivent produire un résultat en < 2 semaines ou revoir le scoring."),
        ("Ne pas sous-estimer la qualité des données",
         "La majorité des blocages IT vient de la qualité des données sources, pas de l'outil IA. "
         "Valider en amont l'accès et la qualité des données avec l'IT local."),
        ("Créer des Gems partagés par fonction",
         "Les Gems Gemini sont des actifs réutilisables. Un Gem bien configuré par une équipe "
         "peut être utilisé par 50 autres champions sans effort. Organiser des bibliothèques Gems par famille."),
        ("Alerter l'IT avant tout prototype sur systèmes d'entreprise",
         "Tout use case impliquant SFDC, SAP, DCS, Active Directory ou une API d'entreprise "
         "doit faire l'objet d'un point d'attention IT documenté AVANT le prototype, pas après."),
    ]

    for title, body in best_practices:
        add_bullet(doc, body, title)

    # Footer final
    doc.add_paragraph()
    p_footer = doc.add_paragraph()
    p_footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_footer = p_footer.add_run(f"© Copyright {YEAR} Pyl.Tech  •  Confidentiel  •  Air Liquide AI Champions")
    r_footer.font.name  = "Poppins"
    r_footer.font.size  = Pt(9)
    r_footer.font.color.rgb = PYL_TEAL_BLUE
    set_paragraph_spacing(p_footer, 24, 0)


# ── Point d'entrée ────────────────────────────────────────────────────────────

def main() -> None:
    print(f"📂 Lecture du catalogue : {CATALOG_FILE}")  # noqa
    if not CATALOG_FILE.exists():
        print(f"❌ Catalogue introuvable : {CATALOG_FILE}")  # noqa
        print("   Lancez d'abord : python3 src/generate_catalog.py")  # noqa
        sys.exit(1)

    df = pd.read_excel(CATALOG_FILE, sheet_name="Catalogue", header=0)
    print(f"   {len(df)} use cases chargés")  # noqa

    doc = Document()
    apply_base_styles(doc)
    add_cover_page(doc)
    build_document(doc, df)

    doc.save(OUTPUT_FILE)
    print(f"\n✅ Rapport Word généré : {OUTPUT_FILE}")  # noqa
    print(f"   Taille : {OUTPUT_FILE.stat().st_size // 1024} KB")  # noqa


if __name__ == "__main__":
    main()
