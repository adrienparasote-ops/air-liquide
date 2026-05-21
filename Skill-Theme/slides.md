# Slides Pyl.Tech — Référence

Détails techniques pour produire des slides .pptx conformes à la charte **officielle** Pyl.Tech via python-pptx ou Google Slides.

## Dimensions

- Format : **16:9** (13.333 × 7.5 inches = 33.87 × 19.05 cm)
- Slide size dans python-pptx : `prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)`

## Marges

- Marge supérieure : 0.5" (titre commence à ~0.6")
- Marge inférieure : 0.4" (footer à ~0.2" du bas)
- Marge gauche/droite : 0.5"
- Espace entre cards : 0.2"

## Couleurs officielles (codes pour python-pptx `RGBColor`)

```python
from pptx.dml.color import RGBColor

# Base
PYL_NAVY_DARK     = RGBColor(0x0B, 0x13, 0x2B)  # Titles / dark background
PYL_WHITE         = RGBColor(0xFF, 0xFF, 0xFF)  # Slides background
PYL_BODY_GREY     = RGBColor(0x4F, 0x4F, 0x4F)  # Body text color
PYL_GREY_BG       = RGBColor(0xEE, 0xEE, 0xEE)  # Shape / grey slide background

# Accentuation
PYL_YELLOW        = RGBColor(0xF4, 0xBF, 0x46)  # Primary
PYL_NAVY          = RGBColor(0x0D, 0x21, 0x49)  # Accentuation 2
PYL_BLUE_TEAL     = RGBColor(0x20, 0x8A, 0xAE)  # Accentuation 3
PYL_TEAL          = RGBColor(0x5B, 0xC0, 0xBE)  # Accentuation 4

# Sémantique
PYL_SUCCESS       = RGBColor(0x13, 0x86, 0x36)  # Accentuation 5
PYL_DANGER        = RGBColor(0xC9, 0x14, 0x32)  # Accentuation 6

# Partenaire
INTELCIA_PINK     = RGBColor(0xE9, 0x1E, 0x63)
```

## Composants récurrents (code pseudo-python-pptx)

### Cartouche de section numérotée

```python
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Carré jaune en haut à gauche du titre
left = Inches(0.5)
top = Inches(0.5)
size = Inches(0.55)
shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, size, size)
shape.fill.solid()
shape.fill.fore_color.rgb = PYL_YELLOW
shape.line.fill.background()
# Numéro à l'intérieur
tf = shape.text_frame
tf.text = "01"
p = tf.paragraphs[0]
p.font.name = "Poppins"
p.font.bold = True
p.font.size = Pt(18)
p.font.color.rgb = PYL_WHITE
p.alignment = PP_ALIGN.CENTER
```

### Titre de slide (à droite du cartouche)

```python
title_box = slide.shapes.add_textbox(Inches(1.25), Inches(0.5), Inches(11.5), Inches(0.6))
tf = title_box.text_frame
tf.text = "Analyse de vos usages"
p = tf.paragraphs[0]
p.font.name = "Poppins"
p.font.bold = True
p.font.size = Pt(28)
p.font.color.rgb = PYL_NAVY_DARK  # #0b132b
```

### Sous-titre

```python
sub_box = slide.shapes.add_textbox(Inches(1.25), Inches(1.1), Inches(11.5), Inches(0.4))
tf = sub_box.text_frame
tf.text = "Une macro-analyse révélant un fort potentiel."
p = tf.paragraphs[0]
p.font.name = "Poppins"
p.font.size = Pt(14)
p.font.color.rgb = PYL_BODY_GREY  # #4f4f4f
```

### Traits horizontaux haut + bas du bloc titre

```python
from pptx.enum.shapes import MSO_CONNECTOR

# Trait du haut (au-dessus du titre)
top_line = slide.shapes.add_connector(
    MSO_CONNECTOR.STRAIGHT,
    Inches(0.5), Inches(0.45),
    Inches(12.83), Inches(0.45)
)
top_line.line.color.rgb = PYL_NAVY_DARK
top_line.line.width = Pt(0.75)

# Trait du bas (sous le sous-titre)
bottom_line = slide.shapes.add_connector(
    MSO_CONNECTOR.STRAIGHT,
    Inches(0.5), Inches(1.65),
    Inches(12.83), Inches(1.65)
)
bottom_line.line.color.rgb = PYL_NAVY_DARK
bottom_line.line.width = Pt(0.75)
```

### Badge triangulaire "NEW" / "UPDATED"

```python
# Triangle navy en haut à gauche, rotation -45°
from pptx.util import Inches, Emu

triangle = slide.shapes.add_shape(
    MSO_SHAPE.RIGHT_TRIANGLE,
    Inches(0.1), Inches(0.1),
    Inches(0.8), Inches(0.8)
)
triangle.fill.solid()
triangle.fill.fore_color.rgb = PYL_NAVY_DARK
triangle.line.fill.background()
triangle.rotation = -90  # selon orientation souhaitée

# Texte "NEW" par-dessus (textbox rotation -45°)
text = slide.shapes.add_textbox(Inches(0.05), Inches(0.25), Inches(0.5), Inches(0.2))
tf = text.text_frame
tf.text = "NEW"
p = tf.paragraphs[0]
p.font.name = "Poppins"
p.font.bold = True
p.font.size = Pt(8)
p.font.color.rgb = PYL_WHITE
text.rotation = -45
```

### Footer copyright + pagination (en turquoise)

```python
# Copyright à gauche, en turquoise officiel
copyr = slide.shapes.add_textbox(Inches(0.3), Inches(7.15), Inches(4), Inches(0.25))
copyr.text_frame.text = f"© Copyright {YEAR} Pyl.Tech"
p = copyr.text_frame.paragraphs[0]
p.font.name = "Poppins"
p.font.size = Pt(9)
p.font.color.rgb = PYL_BLUE_TEAL  # #208AAE — turquoise officiel

# Numéro de page à droite, aussi en turquoise
pagenum = slide.shapes.add_textbox(Inches(12.5), Inches(7.15), Inches(0.5), Inches(0.25))
pagenum.text_frame.text = str(page_number)
p = pagenum.text_frame.paragraphs[0]
p.font.name = "Poppins"
p.font.size = Pt(9)
p.font.color.rgb = PYL_BLUE_TEAL
p.alignment = PP_ALIGN.RIGHT
```

### Card avec header coloré

```python
def add_card(slide, left, top, width, height, header_color, title, body_text):
    # Fond de la card (blanc avec bordure très fine)
    card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = PYL_WHITE
    card.line.color.rgb = PYL_GREY_BG
    card.line.width = Pt(0.5)
    
    # Bande colorée en haut (header) — fine bande de ~6 px
    header_band = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.08)
    )
    header_band.fill.solid()
    header_band.fill.fore_color.rgb = header_color
    header_band.line.fill.background()
    
    # Titre de la card
    title_box = slide.shapes.add_textbox(
        left + Inches(0.2), top + Inches(0.2),
        width - Inches(0.4), Inches(0.4)
    )
    title_box.text_frame.text = title
    p = title_box.text_frame.paragraphs[0]
    p.font.name = "Poppins"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = header_color if header_color != PYL_YELLOW else PYL_NAVY_DARK
    
    # Body en gris officiel #4f4f4f
    body_box = slide.shapes.add_textbox(
        left + Inches(0.2), top + Inches(0.7),
        width - Inches(0.4), height - Inches(0.9)
    )
    body_box.text_frame.text = body_text
    p = body_box.text_frame.paragraphs[0]
    p.font.name = "Poppins"
    p.font.size = Pt(12)  # taille officielle body
    p.font.color.rgb = PYL_BODY_GREY  # #4f4f4f
```

### Surlignage jaune charte (style "marqueur fluo")

```python
# Pour mettre en avant un mot/segment dans un paragraphe
def add_highlighted_run(paragraph, text):
    run = paragraph.add_run()
    run.text = text
    run.font.name = "Poppins"
    run.font.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = PYL_NAVY_DARK
    # Le surlignage se gère via XML direct
    from pptx.oxml.ns import qn
    from lxml import etree
    rPr = run._r.get_or_add_rPr()
    highlight = etree.SubElement(rPr, qn('a:highlight'))
    srgb = etree.SubElement(highlight, qn('a:srgbClr'))
    srgb.set('val', 'F4BF46')  # jaune charte sans le #
```

### Bullet point carré jaune

```python
# Dans python-pptx, les bullets se définissent via XML
from pptx.oxml.ns import qn
from lxml import etree

def add_square_bullet(text_frame, text):
    p = text_frame.add_paragraph()
    p.text = text
    p.font.name = "Poppins"
    p.font.size = Pt(12)
    p.font.color.rgb = PYL_BODY_GREY
    
    pPr = p._pPr if p._pPr is not None else p._p.get_or_add_pPr()
    # Bullet caractère + couleur jaune
    buChar = etree.SubElement(pPr, qn('a:buChar'))
    buChar.set('char', '▪')  # carré
    buClr = etree.SubElement(pPr, qn('a:buClr'))
    srgb = etree.SubElement(buClr, qn('a:srgbClr'))
    srgb.set('val', 'F4BF46')
```

## Layouts par type de slide

### Couverture (slide 1)

- Fond entier `PYL_YELLOW` (`#F4BF46`)
- Logo Pyl.Tech version inversée (blanc) en haut à gauche, ~1.5" de large
- Cadre blanc arrondi en haut à droite contenant le logo partenaire (Google Cloud Partner, ~1.7" × 0.6")
- Titre centré (Poppins Bold 44pt, navy `#0b132b`), 2 lignes max
- Sous-titre en italique (Poppins Italic 18pt, navy 80%)
- Logo client (image) sous le sous-titre, centré
- En bas à gauche : "Version :" + valeur, "Date :" + valeur, séparés par une ligne verticale blanche fine
- Footer copyright centré

### Intercalaire de section

- Bandeau gauche 30 % : photo client (ou image générée) avec **overlay jaune `#F4BF46` à 70 % d'opacité**, et un énorme numéro "01"…"07" en blanc Poppins Bold ~180pt
- En bas du bandeau : crédit "Image générée par Gemini" en blanc petit
- Partie droite 70 % :
  - Logo Pyl.Tech en haut à droite
  - Pictogramme "P" jaune carré centré en haut
  - Frise verticale (ligne grise `#eeeeee`) avec puces carrées jaunes
  - Liste des sections : section active en navy `#0b132b` gras, autres en gris très clair `#9CA3AF`

### Slide de contenu — 3 cards horizontales

Layout type "Constats & opportunités" :
- Header standard (cartouche + titre + sous-titre + 2 traits horizontaux)
- 3 cards alignées horizontalement, chacune ~4" de large × 4.5" de haut, espacement 0.25"
- Headers colorés : 1ère navy `#0d2149`, 2ème turquoise `#208AAE`, 3ème teal `#5BC0BE`
- Dans chaque card :
  - Icône en haut (cercle ou carré coloré, ~0.5")
  - Titre de la card (Poppins Bold 18pt, couleur du header)
  - 2-3 bullets gris `#4f4f4f` avec puces carrées jaunes
  - Encadré "question" en bas (fond gris `#eeeeee`, italique, icône bulle de dialogue)

### Slide de KPI / chiffres clés

- Bandeau supérieur avec 4 KPI cards (Total, Demandes, Incidents, Priorité haute)
- Chaque KPI : icône + label + chiffre Poppins Bold 28pt
- Graphique principal à gauche (~50 % largeur)
- Bloc texte à droite avec 3 chiffres clés :
  - Chiffre géant turquoise `#208AAE` ~64pt
  - Texte explicatif en dessous en gris `#4f4f4f`

### Slide d'offre / tarif

- 1 ou 2 "offres" sous forme de cards horizontales très visibles
- Header de card pleine largeur en navy `#0d2149` (offre dédiée) ou teal `#5BC0BE` (offre mutualisée)
- À l'intérieur : 2 lignes "Delivery FRANCE ... XX XXX € HT/MOIS" et "Delivery MAROC ... XX XXX € HT/MOIS"
- Badge "2,5 ETP backupés / mois" en jaune `#F4BF46` dans le header
- Colonne droite : "Détails" en liste à puces carrées jaunes

### Slide d'équipe (4 portraits)

- 2×2 grille de cards
- Chaque card : photo ronde à gauche (cercle de 1.2" entouré d'un trait jaune `#F4BF46`), texte à droite (nom Poppins Bold navy `#0b132b`, rôle Poppins Regular jaune `#F4BF46`, courte bio en gris `#4f4f4f` 12pt)

### Slide de CV consultant

Layout très spécifique avec surlignage jaune omniprésent :
- Bandeau noir/navy `#0b132b` en haut sur toute la largeur, hauteur ~1.5"
  - Photo ronde du consultant à gauche
  - Nom en blanc Poppins Bold 22pt
  - Rôle **avec fond jaune `#F4BF46`** (surlignage) et texte navy
  - Années d'expérience **avec fond jaune** également
  - Citation en italique blanche à droite
- Colonne gauche 30 % :
  - Encart noir "Compétences" : pour chaque compétence, label blanc + 5 cercles dont X remplis en blanc
  - Encart blanc "Diplômes & Certifications"
- Colonne droite 70 % :
  - "Expériences professionnelles" comme titre
  - Frise verticale grise `#eeeeee` avec puces carrées navy
  - Pour chaque expérience : "**Entreprise** – Poste" avec poste **surligné en jaune**, dates en haut à droite **également surlignées jaune**, puis bullets gris `#4f4f4f`

## Tableaux

```python
def add_pyl_table(slide, left, top, width, height, headers, rows):
    table_shape = slide.shapes.add_table(
        len(rows) + 1, len(headers),
        left, top, width, height
    )
    table = table_shape.table
    
    # Header row
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = PYL_NAVY_DARK  # ou PYL_YELLOW
        cell.text = h
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Poppins"
        p.font.bold = True
        p.font.size = Pt(10)  # 10pt pour tableaux (officiel)
        p.font.color.rgb = PYL_WHITE
    
    # Body rows (alternance navy / blanc)
    for r, row_data in enumerate(rows, start=1):
        bg = PYL_NAVY if r % 2 == 1 else PYL_WHITE
        fg = PYL_WHITE if r % 2 == 1 else PYL_NAVY_DARK
        for c, val in enumerate(row_data):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            cell.text = str(val)
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Poppins"
            p.font.size = Pt(10)
            p.font.color.rgb = fg
```

## Génération via python-pptx

Toujours s'appuyer sur la skill `pptx` pour la mécanique de génération. Ce fichier complète la skill `pptx` en spécifiant **les valeurs précises officielles** (couleurs, polices, tailles) à utiliser dans les `slide.shapes.add_*()`.

Workflow recommandé :
1. Lire `/mnt/skills/public/pptx/SKILL.md`
2. Lire ce fichier (`references/slides.md`)
3. Lire le thème (`themes/pyltech-brand.md`)
4. Coder en combinant les trois sources

## Police Poppins indisponible ?

Si l'environnement ne dispose pas de Poppins :
- 1er fallback : **Inter** (très proche)
- 2ème fallback : **Montserrat**
- 3ème fallback : **DejaVu Sans** (toujours disponible en Linux)
- Last resort : **Arial** ou **Calibri**

Définir la police via `font.name = "Poppins"` et ajouter un commentaire dans le code Python pour signaler que Poppins doit être installé sur le système qui ouvrira le pptx pour un rendu optimal.
