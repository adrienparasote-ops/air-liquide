#!/usr/bin/env python3
"""
generate_pptx.py
────────────────
Génère la présentation PowerPoint (.pptx) Air Liquide — AI Builders
avec la charte graphique officielle Pyl.Tech via la librairie PyltechDeck.
Restaure le contenu exact (6 KPI, cards avec chiffres, tableau, callouts)
en combinant la puissance de la charte PyltechDeck avec python-pptx.
"""
import sys
from pathlib import Path
import pandas as pd
from datetime import date

# Append skill scripts path
SKILL_DIR = Path("/Users/adrien.parasote/.gemini/config/plugins/stream-coding/skills/pyl-pptx")
sys.path.insert(0, str(SKILL_DIR / "scripts"))
try:
    from build_deck import PyltechDeck
except ImportError as e:
    print(f"Error importing PyltechDeck: {e}")
    sys.exit(1)

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

PROJECT_DIR = Path(__file__).parent.parent
CATALOG_FILE = PROJECT_DIR / "output" / "use_cases_catalog.xlsx"
OUTPUT_FILE = PROJECT_DIR / "output" / "presentation_ai_champions.pptx"

# ── Colors ────────────────────────────────────────────────────────────────────
PYL_NAVY_DARK = RGBColor(0x0B, 0x13, 0x2B)
PYL_NAVY = RGBColor(0x0D, 0x21, 0x49)
PYL_YELLOW = RGBColor(0xF4, 0xBF, 0x46)
PYL_TEAL_BLUE = RGBColor(0x20, 0x8A, 0xAE)
PYL_TEAL = RGBColor(0x5B, 0xC0, 0xBE)
PYL_BODY_GREY = RGBColor(0x4F, 0x4F, 0x4F)
PYL_GREY_BG = RGBColor(0xEE, 0xEE, 0xEE)
PYL_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PYL_SUCCESS = RGBColor(0x13, 0x86, 0x36)
PYL_DANGER = RGBColor(0xC9, 0x14, 0x32)

# ── Helpers for custom drawing ────────────────────────────────────────────────
def add_rect(slide, left, top, width, height, fill: RGBColor = None, no_border: bool = True):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    else:
        shape.fill.background()
    if no_border:
        shape.line.fill.background()
    return shape

def add_textbox(
    slide, left, top, width, height, text: str, font_name: str = "Poppins",
    font_size: int = 12, bold: bool = False, italic: bool = False,
    color: RGBColor = None, align=PP_ALIGN.LEFT, word_wrap: bool = True,
):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.text_frame.word_wrap = word_wrap
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    return txBox

def add_kpi_card(
    slide, left, top, width, height, label: str, value: str, sub: str = "",
    header_color: RGBColor = PYL_NAVY, value_color: RGBColor = PYL_TEAL_BLUE,
) -> None:
    card = add_rect(slide, left, top, width, height, fill=PYL_WHITE)
    card.line.color.rgb = PYL_GREY_BG
    card.line.width = Pt(0.5)

    add_rect(slide, left, top, width, Inches(0.07), fill=header_color)

    v_box = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(0.15), width - Inches(0.2), Inches(0.9))
    v_box.text_frame.word_wrap = False
    p = v_box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = value
    run.font.name = "Poppins"
    run.font.bold = True
    run.font.size = Pt(36)
    run.font.color.rgb = value_color

    l_box = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(1.0), width - Inches(0.2), Inches(0.5))
    l_box.text_frame.word_wrap = True
    p = l_box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = label
    run.font.name = "Poppins"
    run.font.size = Pt(10)
    run.font.color.rgb = PYL_BODY_GREY

    if sub:
        s_box = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(1.45), width - Inches(0.2), Inches(0.35))
        s_box.text_frame.word_wrap = True
        p = s_box.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = sub
        run.font.name = "Poppins"
        run.font.size = Pt(9)
        run.font.italic = True
        run.font.color.rgb = PYL_BODY_GREY

def add_content_card(
    slide, left, top, width, height, header_color: RGBColor, card_title: str, bullets: list[str],
    body_font_size: int = 11
) -> None:
    card_bg = add_rect(slide, left, top, width, height, fill=PYL_WHITE)
    card_bg.line.color.rgb = PYL_GREY_BG
    card_bg.line.width = Pt(0.5)

    add_rect(slide, left, top, width, Inches(0.45), fill=header_color)

    t_box = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.06), width - Inches(0.3), Inches(0.35))
    p = t_box.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = card_title
    run.font.name = "Poppins"
    run.font.bold = True
    run.font.size = Pt(13)
    run.font.color.rgb = PYL_WHITE

    line_h = Inches(0.42) if body_font_size <= 11 else Inches(0.78)
    cur_top = top + Inches(0.55)
    for bullet in bullets:
        b_box = slide.shapes.add_textbox(left + Inches(0.15), cur_top, width - Inches(0.3), Inches(0.45))
        b_box.text_frame.word_wrap = True
        p = b_box.text_frame.paragraphs[0]
        sq = p.add_run()
        sq.text = "  "
        sq.font.name = "Poppins"
        sq.font.bold = True
        sq.font.size = Pt(body_font_size)
        sq.font.color.rgb = PYL_YELLOW
        txt = p.add_run()
        txt.text = bullet
        txt.font.name = "Poppins"
        txt.font.size = Pt(body_font_size)
        txt.font.color.rgb = PYL_BODY_GREY
        cur_top += line_h


def add_pptx_table(
    slide, left, top, width, height, headers: list[str], rows: list[list[str]]
) -> None:
    n_rows = len(rows) + 1
    n_cols = len(headers)
    tbl = slide.shapes.add_table(n_rows, n_cols, left, top, width, height).table

    col_w = width // n_cols
    for i in range(n_cols):
        tbl.columns[i].width = col_w

    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = PYL_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = h
        run.font.name = "Poppins"
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = PYL_WHITE

    for r_idx, row_data in enumerate(rows):
        bg = PYL_NAVY if r_idx % 2 == 0 else PYL_WHITE
        fg = PYL_WHITE if r_idx % 2 == 0 else PYL_BODY_GREY
        for c_idx, val in enumerate(row_data):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
            run = p.add_run()
            run.text = str(val)
            run.font.name = "Poppins"
            run.font.size = Pt(10)
            run.font.color.rgb = fg

def main():
    print(f"Lecture du catalogue : {CATALOG_FILE}")
    if not CATALOG_FILE.exists():
        print(f"Catalogue introuvable : {CATALOG_FILE}")
        sys.exit(1)

    df = pd.read_excel(CATALOG_FILE, sheet_name="Catalogue", header=0)
    total = len(df)
    tiers = df["Complexity_Tier"].value_counts().to_dict()
    it_count = (df["IT_Flag"] != "").sum()
    clusters = df["Cluster"].nunique()

    deck = PyltechDeck()
    
    # 01 - Couverture
    deck.add_cover(
        title="Air Liquide — AI Builders",
        subtitle="Analyse, Classification et Recommandations du Portefeuille Use Cases IA"
    )

    # 02 - Sommaire
    deck.add_toc_6_cards_blanches([
        ("Contexte", "Cadrage du projet et méthodologie"),
        ("Chiffres Clés", "Panorama du portefeuille use cases"),
        ("Analyse", "Répartition par complexité, famille et cluster"),
        ("Points IT", "Dépendances systèmes et architecture cible"),
        ("Recommandations", "Axes prioritaires et roadmap de déploiement"),
        ("Bonnes Pratiques", "Méthodologie pour les builders"),
    ], title="Sommaire")

    deck.add_chapter("jaune", "01", "Contexte de la mission")

    # 03 - Contexte — titre = "Contexte de la mission" dans le grand titre,
    # sous-titre = "Cadrage du projet..." dans la barre colorée du template
    slide_ctx = deck.add_schema(chapter_num="01", chapter_label="Contexte de la mission", title="Contexte de la mission")

    # Injecter le sous-titre juste sous le grand titre (titre natif top=0.99, h=0.33 → sous-titre à 1.35)
    add_textbox(slide_ctx, Inches(0.42), Inches(1.35), Inches(9.0), Inches(0.2),
                "Cadrage du projet et objectifs de l'analyse",
                font_size=10, italic=True, color=PYL_BODY_GREY)


    # ── Gauche : 4 cartes objectifs (2 cols × 2 rows) ────────────────────────
    CARD_W = Inches(2.2)
    CARD_H = Inches(1.7)
    GAP    = Inches(0.1)
    objectives = [
        ("Comprendre", "Regroupement thématique en familles fonctionnelles transverses"),
        ("Qualifier",  "Scoring multi-dimensionnel : Small / Medium / Large"),
        ("Projeter",   "Architecture cible Google-first par niveau de complexité"),
        ("Guider",     "Recommandations et bonnes pratiques pour les builders"),
    ]
    for i, (obj_title, obj_desc) in enumerate(objectives):
        col = i % 2; row_idx = i // 2
        left = Inches(0.2) + col * (CARD_W + GAP)
        top  = Inches(1.75) + row_idx * (CARD_H + GAP)
        colors = [PYL_NAVY, PYL_TEAL_BLUE, PYL_TEAL, PYL_YELLOW]
        add_content_card(slide_ctx, left, top, CARD_W, CARD_H, colors[i], obj_title, [obj_desc])

    # ── Droite : intro text + bloc gris ──────────────────────────────────────
    RIGHT_LEFT = Inches(4.85)
    RIGHT_W    = Inches(4.95)

    # Texte introductif
    add_textbox(
        slide_ctx, RIGHT_LEFT, Inches(1.75), RIGHT_W, Inches(0.85),
        f"Air Liquide a mobilisé ses AI builders — profils métiers, non-IT — pour explorer "
        f"l'IA dans leurs activités. {total} use cases ont été collectés sur l'ensemble des clusters du groupe.",
        font_size=10, color=PYL_BODY_GREY,
    )

    # Bloc gris "Périmètre de l'analyse"
    # bottom cartes gauche = 1.75 + 1.7 + 0.1 + 1.7 = 5.35"
    # PANEL_H = 2.65" → PANEL_TOP = 5.35 - 2.65 = 2.70" ✅
    PANEL_TOP = Inches(2.70)
    PANEL_H   = Inches(2.65)
    add_rect(slide_ctx, RIGHT_LEFT, PANEL_TOP, RIGHT_W, PANEL_H, fill=PYL_GREY_BG)
    add_textbox(slide_ctx, RIGHT_LEFT + Inches(0.2), PANEL_TOP + Inches(0.15),
                RIGHT_W - Inches(0.4), Inches(0.35),
                "Périmètre de l'analyse", font_size=12, bold=True, color=PYL_NAVY_DARK)
    perim_items = [
        f"{total} use cases analysés",
        f"{df['Cluster'].nunique()} clusters géographiques/organisationnels",
        f"{df['Family_Label'].nunique() if 'Family_Label' in df.columns else 12} familles métier",
        "11 outils distincts identifiés",
        "Source : Advanced AI builders - Action Monitoring.xlsx",
    ]
    for j, item in enumerate(perim_items):
        add_textbox(slide_ctx, RIGHT_LEFT + Inches(0.2), PANEL_TOP + Inches(0.6) + j * Inches(0.41),
                    RIGHT_W - Inches(0.4), Inches(0.38), f"  {item}", font_size=10, color=PYL_BODY_GREY)




    # 04 - Méthodologie — construction manuelle pour contrôler la police du corps
    slide_meth = deck.add_schema(
        chapter_num="01", chapter_label="Contexte de la mission",
        title="Méthodologie en 6 phases",
    )
    # Sous-titre manuel
    add_textbox(slide_meth, Inches(0.3), Inches(1.35), Inches(9.0), Inches(0.35),
                "Audit → Classification → Scoring → IT → Architecture → Recommandations",
                font_size=11, color=PYL_BODY_GREY)

    meth_cards = [
        ("Phases 1 & 2", [
            "Audit & Nettoyage du catalogue",
            "Classification sémantique en 7 familles fonctionnelles",
        ]),
        ("Phases 3 & 4", [
            "Scoring 5 dimensions (Small / Medium / Large)",
            "Détection des dépendances IT",
        ]),
        ("Phase 5", [
            "Architecture cible Google-first par niveau de complexité",
        ]),
        ("Phase 6", [
            "Recommandations et bonnes pratiques pour les builders",
        ]),
    ]
    CARD_W_METH = Inches(2.25)
    CARD_H_METH = Inches(3.2)
    colors_meth = [PYL_NAVY, PYL_TEAL_BLUE, PYL_NAVY, PYL_YELLOW]
    for i, (ctitle, cbullets) in enumerate(meth_cards):
        left = Inches(0.3) + i * (CARD_W_METH + Inches(0.1))
        add_content_card(slide_meth, left, Inches(1.75), CARD_W_METH, CARD_H_METH,
                         colors_meth[i], ctitle, cbullets, body_font_size=13)




    deck.add_chapter("bleu", "02", "Analyse du Portefeuille")

    # 05 - Chiffres clés — 6 cartes sur 10": CARD_W=1.5", GAP=0.1" → total=6*(1.5+0.1)=9.6" ✅
    slide_kpi = deck.add_schema(chapter_num="02", chapter_label="Analyse du Portefeuille",
                                title=f"{total} use cases analysés")
    CARD_W_KPI = Inches(1.5)
    CARD_H_KPI = Inches(1.85)
    Y_TOP_KPI  = Inches(1.75)
    GAP_KPI    = Inches(0.1)
    LEFT_START = Inches(0.2)

    cards = [
        ("Use Cases", str(total), "Portefeuille", PYL_NAVY, PYL_YELLOW),
        ("Clusters", str(clusters), "Périmètre géo", PYL_NAVY, PYL_TEAL_BLUE),
        ("Small", str(tiers.get("Small", 0)), "< 2 semaines", PYL_SUCCESS, PYL_SUCCESS),
        ("Medium", str(tiers.get("Medium", 0)), "4-8 semaines", PYL_TEAL, PYL_TEAL),
        ("Large", str(tiers.get("Large", 0)), "3-12 mois", PYL_DANGER, PYL_DANGER),
        ("Points IT", str(it_count), "Escalade", PYL_DANGER, PYL_DANGER),
    ]

    for i, (label, value, sub, hdr_color, val_color) in enumerate(cards):
        left = LEFT_START + i * (CARD_W_KPI + GAP_KPI)
        add_kpi_card(slide_kpi, left, Y_TOP_KPI, CARD_W_KPI, CARD_H_KPI, label, value, sub,
                     header_color=hdr_color, value_color=val_color)

    pct_accessible = (tiers.get("Small", 0) + tiers.get("Medium", 0)) * 100 // total
    add_textbox(
        slide_kpi, LEFT_START, Inches(3.75), Inches(9.6), Inches(0.38),
        f"{pct_accessible}% des use cases sont déployables sans ressources IT lourdes (Small ou Medium)",
        font_size=11, bold=True, color=PYL_NAVY_DARK, align=PP_ALIGN.CENTER,
    )

    callout = add_rect(slide_kpi, LEFT_START, Inches(4.18), Inches(9.6), Inches(1.2), fill=PYL_YELLOW)
    ct = callout.text_frame
    ct.word_wrap = True
    p = ct.paragraphs[0]
    run = p.add_run()
    run.text = (
        f"Constat clé : la majorité du portefeuille ({tiers.get('Small', 0) + tiers.get('Medium', 0)} UC) "
        f"représente des opportunités de déploiement rapide avec Google Workspace. "
        f"Seuls {tiers.get('Large', 0)} projets nécessitent un engagement long terme avec l'IT. "
        f"{it_count} UC ont des dépendances systèmes qui requièrent une escalade obligatoire."
    )
    run.font.name = "Poppins"
    run.font.size = Pt(10)
    run.font.color.rgb = PYL_NAVY_DARK

    
    # 06 - Répartition par complexité — 3 cartes sur 10": 3*(3.0+0.1)+0.2=9.5" ✅
    slide_cplx = deck.add_schema(chapter_num="02", chapter_label="Analyse du Portefeuille",
                                 title="Scoring : Small / Medium / Large")
    tier_data = [
        ("Small", tiers.get("Small", 0), "Quick Win", "< 2 sem.", "1 builder, no-code", PYL_SUCCESS),
        ("Medium", tiers.get("Medium", 0), "Use Case Structurant", "4-8 sem.", "builder + IT local", PYL_TEAL_BLUE),
        ("Large", tiers.get("Large", 0), "Projet Stratégique", "3-12 mois", "Équipe IT + builder", PYL_DANGER),
    ]
    CARD_W_CPLX = Inches(2.95)
    CARD_H_CPLX = Inches(3.55)
    Y_TOP_CPLX  = Inches(1.75)

    for i, (tier, count, label, ttv, profile, color) in enumerate(tier_data):
        left = Inches(0.3) + i * (CARD_W_CPLX + Inches(0.15))
        pct = count * 100 // total if total > 0 else 0
        add_content_card(
            slide_cplx, left, Y_TOP_CPLX, CARD_W_CPLX, CARD_H_CPLX, color,
            f"{tier} — {count} UC ({pct}%)",
            [
                f"Label : {label}",
                f"Time-to-value : {ttv}",
                f"Profil : {profile}",
                f"Part du portefeuille : {pct}%",
            ],
        )

        add_textbox(
            slide_cplx, left, Y_TOP_CPLX + Inches(0.55), CARD_W_CPLX, Inches(0.8),
            str(count), font_size=48, bold=True, color=PYL_WHITE, align=PP_ALIGN.CENTER,
        )

    # Trier par code famille (F1 → F7)
    families = df[["Family_Label", "Family"]].drop_duplicates("Family_Label")
    families["_sort"] = families["Family"].str.extract(r"(\d+)").astype(int)
    families = families.sort_values("_sort")
    rows_fam = []
    for _, row in families.iterrows():
        fam  = row["Family_Label"]
        code = row["Family"]
        subset = df[df["Family_Label"] == fam]["Complexity_Tier"].value_counts().to_dict()
        rows_fam.append([
            f"{code} — {fam}", str(subset.get("Small", 0)), str(subset.get("Medium", 0)),
            str(subset.get("Large", 0))
        ])

    slide_fam = deck.add_schema(chapter_num="02", chapter_label="Analyse du Portefeuille",
                                title="7 familles fonctionnelles identifiées")
    add_pptx_table(slide_fam, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                   ["Famille fonctionnelle", "Small", "Medium", "Large"], rows_fam)


    # 08 - Clusters (tableau dans les bornes)
    cluster_agg = df.groupby("Cluster")["Complexity_Tier"].value_counts().unstack(fill_value=0).reset_index()
    cluster_agg["Total"] = cluster_agg.get("Small", 0) + cluster_agg.get("Medium", 0) + cluster_agg.get("Large", 0)
    cluster_agg = cluster_agg.sort_values("Total", ascending=False).head(12)
    rows_clu = []
    for _, row in cluster_agg.iterrows():
        rows_clu.append([str(row["Cluster"]), str(int(row.get("Small", 0))),
                         str(int(row.get("Medium", 0))), str(int(row.get("Large", 0))),
                         str(int(row["Total"]))])
    rows_clu_a = rows_clu[:6]
    rows_clu_b = rows_clu[6:]

    slide_clu_a = deck.add_schema(chapter_num="02", chapter_label="Analyse du Portefeuille",
                                  title="Top 12 clusters — 1/2")
    add_pptx_table(slide_clu_a, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                   ["Cluster", "Small", "Medium", "Large", "Total"], rows_clu_a)

    if rows_clu_b:
        slide_clu_b = deck.add_schema(chapter_num="02", chapter_label="Analyse du Portefeuille",
                                      title="Top 12 clusters — 2/2")
        add_pptx_table(slide_clu_b, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                       ["Cluster", "Small", "Medium", "Large", "Total"], rows_clu_b)


    deck.add_chapter("orange", "03", "Architecture et IT")

    # 09 - Architecture — construction manuelle pour contrôler la taille de police
    slide_arch = deck.add_schema(
        chapter_num="03", chapter_label="Architecture et IT",
        title="Architectures de référence",
    )
    add_textbox(slide_arch, Inches(0.3), Inches(1.35), Inches(9.0), Inches(0.35),
                "Stack cible Google-first par niveau", font_size=11, color=PYL_BODY_GREY)

    arch_cards = [
        ("Small — Prompting", [
            "Outils : Gemini, NotebookLM",
            "Data : Drive/Sheets statique",
            "Compétence : Prompting",
            "IT : Aucune intervention",
        ]),
        ("Medium — App Script", [
            "Outils : App Script, AppSheet",
            "Data : Sheets (structurées)",
            "Compétence : Low-code",
            "IT : Support ponctuel",
        ]),
        ("Large — Vertex AI", [
            "Outils : Vertex AI, BigQuery",
            "Sources : SFDC, SAP, DCS",
            "Compétence : Dev",
            "IT : Équipe projet dédiée",
        ]),
    ]
    CARD_W_ARCH = Inches(3.0)
    CARD_H_ARCH = Inches(3.4)
    colors_arch = [PYL_NAVY, PYL_TEAL_BLUE, PYL_YELLOW]
    for i, (ctitle, cbullets) in enumerate(arch_cards):
        left = Inches(0.35) + i * (CARD_W_ARCH + Inches(0.1))
        add_content_card(slide_arch, left, Inches(1.75), CARD_W_ARCH, CARD_H_ARCH,
                         colors_arch[i], ctitle, cbullets, body_font_size=13)



    # 10 - Points d'attention IT
    it_df = df[df["IT_Flag"] != ""]
    it_by_fam = it_df.groupby("Family_Label").size().reset_index(name="count").sort_values("count", ascending=False)
    rows_it_l = [[r["Family_Label"], str(r["count"])] for _, r in it_by_fam.iterrows()]
    
    top_it = it_df.nlargest(8, "Score_Total")
    rows_it_r = []
    for _, row in top_it.iterrows():
        desc = str(row["Use Case Description (Long)"])[:50]
        if len(str(row["Use Case Description (Long)"])) > 50: desc += "..."
        rows_it_r.append([str(row["UC_ID"]), str(row["Cluster"]), str(row["Complexity_Tier"]), desc])
    
    # 10a - Points d'attention IT — par famille
    slide_it_a = deck.add_schema(chapter_num="03", chapter_label="Architecture et IT",
                                 title="UC IT — par famille")
    add_pptx_table(slide_it_a, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                   ["Famille", "Nb UC IT"], rows_it_l)

    # 10b - Points d'attention IT — top UC (2 slides de 4 lignes)
    rows_it_r_a = rows_it_r[:4]
    rows_it_r_b = rows_it_r[4:]

    slide_it_b = deck.add_schema(chapter_num="03", chapter_label="Architecture et IT",
                                 title="Top UC — accompagnement IT (1/2)")
    add_pptx_table(slide_it_b, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                   ["UC_ID", "Cluster", "Tier", "Description"], rows_it_r_a)

    if rows_it_r_b:
        slide_it_c = deck.add_schema(chapter_num="03", chapter_label="Architecture et IT",
                                     title="Top UC — accompagnement IT (2/2)")
        add_pptx_table(slide_it_c, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                       ["UC_ID", "Cluster", "Tier", "Description"], rows_it_r_b)


    deck.add_chapter("violet", "04", "Recommandations et Roadmap")
    
    # 11 - Top Quick Wins (2 slides : 7 premières lignes + reste)
    qw = df[(df["Complexity_Tier"] == "Small") & (df["Nb_Tools"] <= 1)].head(14)
    rows_qw = []
    for _, row in qw.iterrows():
        rows_qw.append([str(row["UC_ID"]), str(row["Family_Label"]), str(row["Cluster"]),
                        str(row["Tools"]), str(int(row["Score_Total"]))])

    rows_qw_a = rows_qw[:7]
    rows_qw_b = rows_qw[7:]

    slide_qw_a = deck.add_schema(chapter_num="04", chapter_label="Recommandations et Roadmap",
                                 title="Top Quick Wins — 1/2")
    add_pptx_table(slide_qw_a, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                   ["UC_ID", "Famille", "Cluster", "Outil", "Score"], rows_qw_a)

    if rows_qw_b:
        slide_qw_b = deck.add_schema(chapter_num="04", chapter_label="Recommandations et Roadmap",
                                     title="Top Quick Wins — 2/2")
        add_pptx_table(slide_qw_b, Inches(0.3), Inches(1.75), Inches(9.4), Inches(3.6),
                       ["UC_ID", "Famille", "Cluster", "Outil", "Score"], rows_qw_b)



    # 12 - Recommandations
    slide_reco = deck.add_schema(chapter_num="04", chapter_label="Recommandations et Roadmap",
                                 title="5 axes d'industrialisation")
    
    recos = [
        ("Quick Wins — Déploiement", [
            f"{tiers.get('Small', 0)} UC déployables immédiatement",
            "Bibliothèque de Gems par famille",
            "Cible : 10 pratiques en 3 mois"
        ]),
        ("Accompagner les Medium", [
            f"{tiers.get('Medium', 0)} UC — sprints de 4 semaines",
            "Champion référent par cluster",
            "NotebookLM et App Script comme vecteurs"
        ]),
        (f"Escalader {it_count} cas IT", [
            "Registre de dépendances systèmes",
            "Atelier de priorisation IT",
            "Zero prototype SFDC/SAP sans validation"
        ]),
        ("Track Data Champion", [
            "La manipulation de données complexes nécessite un profil dédié",
            "Créer un parcours de formation spécifique (SQL, Python, BigQuery)",
            "Ce rôle fera le pont entre les AI builders métiers et les data engineers IT"
        ]),
    ]

    # 2 cols × 2 rows pleine largeur : 4.6" + 0.15" gap → 0.3+4.6+0.15+4.6 = 9.65" ✅
    # hauteur: 1.75 + 1.85 + 0.1 + 1.85 = 5.55" ≤ 5.62" ✅
    CARD_W_RECO = Inches(4.6)
    CARD_H_RECO = Inches(1.85)
    for i, (title_card, bullets) in enumerate(recos):
        col = i % 2; row_idx = i // 2
        left = Inches(0.3) + col * (CARD_W_RECO + Inches(0.15))
        top  = Inches(1.75) + row_idx * (CARD_H_RECO + Inches(0.1))
        colors = [PYL_NAVY, PYL_TEAL_BLUE, PYL_DANGER, PYL_YELLOW]
        add_content_card(slide_reco, left, top, CARD_W_RECO, CARD_H_RECO, colors[i], title_card, bullets)




    # 13 - Bonnes pratiques
    slide_bp = deck.add_schema(chapter_num="04", chapter_label="Recommandations et Roadmap",
                               title="Bonnes pratiques pour pérenniser")
    
    bps = [
        ("Gestion des Prompts", [
            "Stocker dans un Google Doc dédié",
            "Versionner : Prompt_V1.0_AAAA-MM-JJ",
            "Documenter contexte et exemples",
            "Centraliser : Drive AI builders"
        ]),
        ("Discipline App Script", [
            "1 script = 1 fichier nommé",
            "Commenter les blocs principaux",
            "Pas de secrets en clair dans le code",
            "README + tests sur données fictives"
        ]),
        ("Kit builder", [
            "README.md : description + how-to",
            "Prompts_Vx.x.md : historique",
            "Script_Vx.x.gs : copie du code",
            "Tests.md + Changelog.md"
        ]),
        ("Quand escalader vers l'IT ?", [
            "Connexion système enterprise",
            "Données sensibles (RH, finance)",
            "Script instable / 10+ utilisateurs",
            "Besoin de fiabilité 24/7"
        ]),
    ]
    
    # 2x2 grid : 1.75 + 1.9 + 0.1 + 1.9 = 5.75" ≤ 5.62" → use 1.85"
    # card_h=1.85" → 1.75+1.85+0.1+1.85 = 5.55" ✅
    CARD_W_BP = Inches(4.5)
    CARD_H_BP = Inches(1.85)
    for i, (title_card, bullets) in enumerate(bps):
        col = i % 2
        row_idx = i // 2
        left = Inches(0.3) + col * (CARD_W_BP + Inches(0.1))
        top = Inches(1.75) + row_idx * (CARD_H_BP + Inches(0.1))
        add_content_card(slide_bp, left, top, CARD_W_BP, CARD_H_BP, PYL_NAVY, title_card, bullets)

    # 14 - Closing
    deck.add_thanks(
        title="Merci de votre attention",
        subtitle="Air Liquide — AI Builders",
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    deck.save(str(OUTPUT_FILE))
    print(f"\nPresentation PowerPoint générée avec PyltechDeck : {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
