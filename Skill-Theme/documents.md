# Documents Pyl.Tech (Word & PDF) — Référence

Adaptation de la charte **officielle** Pyl.Tech aux documents longs : rapports, propositions au format Word, livrables PDF.

## Format général

- **Taille de page** : A4 portrait (21 × 29.7 cm) pour les rapports, A4 paysage pour les livrables type "deck PDF"
- **Marges** : 2 cm haut/bas, 2.5 cm gauche/droite
- **Police par défaut** : Poppins (fallback Inter / Calibri)
- **Interligne** : 1.15
- **Espacement entre paragraphes** : 6 pt après

## En-tête de document

L'en-tête (`header`) répété sur chaque page contient :
- À gauche : logo Pyl.Tech (image, hauteur ~1 cm)
- À droite : titre court du document en navy `#0b132b` Poppins Regular 9 pt
- Filet horizontal jaune `#F4BF46` de 1 pt sous l'en-tête

## Pied de page

Le pied de page (`footer`) répété sur chaque page :
- À gauche : `© Copyright [année] Pyl.Tech` en turquoise `#208AAE` Poppins 9 pt
- À droite : `Page X / Y` en turquoise `#208AAE` Poppins 9 pt
- Filet horizontal gris `#eeeeee` de 0.5 pt au-dessus

## Page de couverture

- Fond entier jaune `#F4BF46`
- Logo Pyl.Tech en haut à gauche (version blanche/inversée)
- Logo partenaire en haut à droite dans un encadré blanc arrondi
- Titre principal centré verticalement, navy `#0b132b`, Poppins Bold 36 pt
- Sous-titre en italique, navy 80 %, Poppins Italic 16 pt
- Bloc client en bas-milieu : nom du client en gros navy
- Version & date en bas à gauche

## Hiérarchie des titres

Configurer les styles Word en respectant :

| Style | Police | Taille | Couleur | Espacement avant |
|-------|--------|--------|---------|------------------|
| Heading 1 | Poppins Bold | 24 pt | Navy `#0b132b` | 24 pt |
| Heading 2 | Poppins Bold | 18 pt | Navy `#0b132b` | 18 pt |
| Heading 3 | Poppins Bold | 14 pt | Navy `#0b132b` | 12 pt |
| Heading 4 | Poppins SemiBold | 12 pt | Turquoise `#208AAE` | 8 pt |
| Body | Poppins Regular | **12 pt** | **Gris `#4f4f4f`** | 6 pt |
| Caption | Poppins Italic | 9 pt | Gris `#4f4f4f` | 4 pt |
| Quote | Poppins Italic | 12 pt | Navy `#0b132b` | 12 pt |

**Note importante** : le corps de texte est en `#4f4f4f` (gris foncé), pas en navy. Le navy `#0b132b` est réservé aux titres et fonds sombres.

**Pattern visuel des Heading 1** : précédés d'un cartouche jaune carré contenant le numéro de chapitre (image insérée à gauche du titre, ou bordure gauche jaune épaisse de 6 pt).

## Listes à puces

Utiliser des **puces carrées colorées** (Wingdings caractère `n` ou Unicode `▪` `■`) :
- Niveau 1 : puce carrée jaune `#F4BF46`, retrait 0.5 cm
- Niveau 2 : puce carrée navy `#0d2149`, retrait 1 cm
- Niveau 3 : tiret simple en gris `#4f4f4f`, retrait 1.5 cm

## Tableaux

- **Header row** : fond navy `#0b132b`, texte blanc Poppins Bold **10 pt**, centré
- **Body rows** : alternance navy `#0d2149` (texte blanc Poppins Regular 10 pt) / blanc (texte gris `#4f4f4f` Poppins Regular 10 pt)
- **Pas de bordures verticales**, bordures horizontales fines `#eeeeee`
- Padding interne des cellules : 6 pt en haut/bas, 10 pt gauche/droite

## Encadrés "callout"

Quatre types d'encadrés possibles :

1. **Info** : fond `#eeeeee`, bordure gauche jaune `#F4BF46` 4 pt
2. **Constat / Important** : fond gris `#eeeeee`, bordure gauche navy `#0b132b` 4 pt
3. **Attention / Danger** : fond rouge pâle, bordure gauche `#C91432` 4 pt
4. **Succès / Bonne pratique** : fond vert pâle, bordure gauche `#138636` 4 pt

À l'intérieur : titre court en gras (couleur de la bordure), corps en gris `#4f4f4f` regular 11 pt.

## Mise en valeur dans le texte

Comme dans la charte officielle, deux méthodes pour mettre en avant :

1. **Gras** sur le mot-clé (`<strong>`)
2. **Surlignage jaune charte** : appliquer un fond `#F4BF46` derrière le texte
   - Dans Word : Mise en surbrillance > Personnaliser > `#F4BF46`
   - Dans python-docx :
   ```python
   from docx.oxml.ns import qn
   from docx.oxml import OxmlElement
   
   def highlight_run(run, hex_color="F4BF46"):
       rPr = run._element.get_or_add_rPr()
       shd = OxmlElement('w:shd')
       shd.set(qn('w:fill'), hex_color)
       rPr.append(shd)
   ```

## Citations

Mises en avant en italique 12 pt navy `#0b132b`, entourées de guillemets décoratifs « ... » jaunes `#F4BF46` (taille 20 pt). Retrait gauche 1 cm.

## Images

- Toujours redimensionnées proportionnellement
- Légende sous l'image en Poppins Italic 9 pt gris `#4f4f4f` : `Figure X : description courte`
- Pour les visuels générés par IA : mentionner explicitement *"Image générée par Gemini"* en bas à gauche, Poppins Regular 8 pt blanc sur fond image

## Sommaire

- Style "Table of Contents" personnalisé
- Heading 1 → niveau 1, Heading 2 → niveau 2, Heading 3 → niveau 3
- Police Poppins Regular 11 pt
- Numéros de page alignés à droite, séparés du texte par des points en gris `#eeeeee`

## Génération via python-docx

Toujours s'appuyer sur la skill `docx` pour la mécanique de génération. Utiliser ce fichier en complément pour les **valeurs précises officielles**.

Snippet utile pour configurer les styles globaux :

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Marges
section = doc.sections[0]
section.top_margin = Cm(2)
section.bottom_margin = Cm(2)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)

# Style par défaut — body en GRIS officiel
style = doc.styles['Normal']
style.font.name = 'Poppins'
style.font.size = Pt(12)  # taille officielle
style.font.color.rgb = RGBColor(0x4F, 0x4F, 0x4F)  # #4f4f4f gris officiel

# Heading 1 en navy
h1 = doc.styles['Heading 1']
h1.font.name = 'Poppins'
h1.font.bold = True
h1.font.size = Pt(24)
h1.font.color.rgb = RGBColor(0x0B, 0x13, 0x2B)  # #0b132b navy officiel
```

## Export PDF

- Imprimer/Exporter depuis Word avec l'option "haute qualité"
- Vérifier que les polices sont **embarquées** dans le PDF (paramètres d'export Word → "incorporer les polices")
- Format de page conservé en A4
- Couleurs en RGB (pas CMYK sauf demande explicite imprimeur)

## Pour les PDF générés directement (sans Word)

Si génération via la skill `pdf` (reportlab, pypdf) :
- Définir les couleurs en hex via `colors.HexColor("#F4BF46")`
- Embarquer Poppins TTF en début de script (`pdfmetrics.registerFont(...)`)
- Reproduire les mêmes patterns visuels : en-tête, pied de page, cartouches numérotés
