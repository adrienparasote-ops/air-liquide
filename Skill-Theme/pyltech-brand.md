# Pyl.Tech Brand

Charte graphique **officielle** Pyl.Tech : jaune doré + bleu marine très foncé + bleus/turquoise d'accentuation, sur fond blanc épuré. Identité d'un pure player Google Cloud français, à la fois technique et premium.

## Palette de couleurs officielle

### Couleurs de base (text et arrière-plans)

| Rôle | Hex | Usage |
|------|-----|-------|
| **Titles color / Dark background** | `#0b132b` | Couleur des titres ; fond des slides "dark" |
| **Slides background** | `#ffffff` | Fond standard des slides |
| **Body text color** | `#4f4f4f` | **Couleur du texte courant** (gris foncé, PAS navy) |
| **Shape / Grey slide background** | `#eeeeee` | Fond des shapes ou slides en variante grise |

### Couleurs d'accentuation

| Rôle | Hex | Usage |
|------|-----|-------|
| **Primary color (Accentuation 1)** | `#F4BF46` | Jaune doré signature — cartouche de titre, surlignage, bullets, accents |
| **Accentuation 2** | `#0d2149` | Bleu marine — fond des cards primaires, header de tableau |
| **Accentuation 3** | `#208AAE` | Bleu turquoise — chiffres, pagination, accents secondaires |
| **Accentuation 4** | `#5BC0BE` | Vert d'eau / teal — différenciation des cards, KPI |

### Couleurs sémantiques

| Rôle | Hex | Usage |
|------|-----|-------|
| **Succès (Accentuation 5)** | `#138636` | OK, validation, métrique positive |
| **Danger (Accentuation 6)** | `#C91432` | Alerte, P1 critique, erreur |

### Couleur partenaire

- **Intelcia Pink** : `#E91E63` — uniquement pour distinguer visuellement les blocs Intelcia dans un schéma de co-delivery. Jamais utilisé en décoration.

## Typographie

### Police principale

**Poppins** (à défaut : Inter, Montserrat, ou DejaVu Sans pour les environnements sans accès aux web fonts).

### Tailles officielles

- **Corps de texte (plain text)** : **12 pt** — utiliser l'espacement (line-height, paragraph spacing) pour améliorer la lisibilité, pas la taille
- **Texte dans les tableaux** : **10 pt**
- **Titres de slide / H1** : 28–32 pt, Poppins Bold, couleur `#0b132b`
- **Sous-titres / H2** : 14–16 pt, Poppins Regular, couleur `#4f4f4f`
- **Headers de cards** : 16–18 pt, Poppins Bold (couleur selon la card)
- **Chiffres clés (KPI géants)** : 48–72 pt, Poppins Bold, en `#208AAE` ou `#F4BF46`
- **Footer / pagination** : 9 pt, Poppins Regular, en `#208AAE` (oui, la pagination est en bleu turquoise dans la charte officielle)

### Règle de couleur de texte

- **Titres** : toujours en `#0b132b` (navy très foncé)
- **Texte courant** : toujours en `#4f4f4f` (gris foncé)
- **Texte sur fond sombre** : `#ffffff` (blanc)
- **Texte sur fond jaune (`#F4BF46`)** : `#0b132b` (navy)
- **Le jaune n'est JAMAIS utilisé pour du texte de grande taille** (illisible)

## Règles de mise en valeur

Deux méthodes officielles pour mettre en avant un mot ou une phrase :

1. **Gras** : utiliser le poids 700 (Bold) sur le mot-clé
2. **Surlignage jaune charte** : appliquer un fond `#F4BF46` derrière le texte (style "marqueur fluo") — particulièrement utilisé dans les CV et pour marquer des éléments critiques

Ne pas combiner italique + gras + couleur sur le même texte (surcharge).

## Patterns visuels récurrents

### Cartouche de titre intégré

Le titre de slide est précédé d'un **cartouche jaune `#F4BF46`** carré contenant un mini "Click to add title" en blanc (ou le numéro de section "01", "02"…). Le titre lui-même est dans un rectangle blanc à droite, encadré en haut et en bas par un fin trait `#0b132b` ou `#eeeeee` qui s'étend sur toute la largeur de la slide.

Structure visuelle :
```
[ trait horizontal navy d'épaisseur 1 px sur toute la largeur ]
[carré jaune] [ Titre en gros navy ]
              [ Sous-titre en gris ]
[ trait horizontal navy d'épaisseur 1 px sur toute la largeur ]
```

### Badges triangulaires "NEW" / "UPDATED"

Pour signaler une nouveauté ou une mise à jour sur une slide, un **triangle navy `#0b132b`** est placé en haut à gauche de l'élément concerné, avec le texte "NEW" ou "UPDATED" en blanc Poppins Bold (rotation à -45°). Triangle plein, sans bordure.

### Logo Pyl.Tech en haut à droite

Le logo "Pyl.Tech" (texte noir + petit pictogramme "P" jaune en exposant à droite) est placé en haut à droite de toutes les slides intérieures. Hauteur ~25 px.

### Footer de page

En bas, sur une ligne :
- À gauche : `© Copyright [année] Pyl.Tech` en `#208AAE` (turquoise) Poppins Regular 9 pt
- À droite : numéro de page en `#208AAE` Poppins Regular 9 pt

Pas de séparateur horizontal au-dessus du footer.

### Cards

- **Rayon de coin** : 0 à 4 px (la charte officielle utilise des coins très peu arrondis, presque droits)
- **Bordure** : aucune, ou très fine `#eeeeee` 1 px
- **Fond** : blanc `#ffffff` ou gris pâle `#eeeeee`
- **Header** : si présent, fond plein navy `#0d2149` (Accentuation 2) ou jaune `#F4BF46` avec texte contrasté
- **Padding interne** : 20–24 px
- **Pas d'ombre marquée** (la charte est très flat)

### Listes à puces

Les puces sont des **carrés jaunes `#F4BF46`**, taille ~8 px, alignés verticalement avec le baseline de la première ligne du texte. Pour les listes imbriquées :
- Niveau 1 : carré jaune `#F4BF46`
- Niveau 2 : carré navy `#0d2149`
- Niveau 3 : tiret simple gris `#4f4f4f`

### Tableaux

- **Header row** : fond navy `#0b132b` ou `#0d2149`, texte blanc Poppins Bold
- **Lignes** : alternance navy / blanc, ou simplement blanc avec séparateurs `#eeeeee`
- **Police dans les tableaux** : 10 pt (taille officielle)
- **Pas de bordures verticales**, bordures horizontales fines `#eeeeee`

### Icônes

- Style ligne (outline), pas plein
- Couleur : navy `#0b132b` ou jaune `#F4BF46`
- Souvent encadrées dans un petit carré jaune (~36×36 px) avec coins droits

## Layouts standards

### Slide de couverture

- Fond entier `#F4BF46` (jaune)
- Logo Pyl.Tech en haut à gauche
- Logo partenaire (Google Cloud Partner…) en haut à droite dans un cadre blanc arrondi
- Titre principal centré en navy `#0b132b`, Poppins Bold ~48 pt
- Sous-titre en italique navy à 80 % d'opacité
- Logo client (ex: GALEC en bleu) sous le sous-titre
- Trait de pinceau orange décoratif sous le logo client (optionnel)
- En bas à gauche : "Version :" + valeur, "Date :" + valeur, séparés par une ligne verticale blanche
- Footer copyright centré

### Slide intercalaire (entre sections)

- Bandeau gauche ~30 % largeur : photo client teintée jaune en overlay et grand numéro de section "01"…"07" en blanc Poppins Bold ~180 pt
- Crédit "Image générée par Gemini" en blanc petit en bas du bandeau
- Partie droite ~70 % :
  - Logo Pyl.Tech en haut à droite
  - Pictogramme "P" jaune carré centré en haut
  - Frise verticale grise avec puces carrées jaunes
  - Liste des sections : active en navy `#0b132b` gras, inactives en gris très clair `#9CA3AF`

### Slide de contenu standard

- Header : cartouche jaune + titre navy + sous-titre gris + trait horizontal
- Body : layout en cards (2 à 4) ou en split texte/visuel
- Footer : copyright + pagination en turquoise

### Slide de tarif/offre

- 1 ou 2 cards "offre" très visibles
- Header de card pleine largeur en navy `#0d2149` (offre dédiée) ou turquoise `#5BC0BE` (offre mutualisée)
- 2 lignes "Delivery FRANCE … XX XXX € HT/MOIS" en grand
- Badge jaune en haut à droite "2,5 ETP backupés / mois"
- Colonne droite : "Détails" en liste à puces carrées jaunes

### Slide CV consultant

- Bandeau noir/navy `#0b132b` en haut sur toute la largeur, hauteur ~1.5"
  - Photo ronde du consultant à gauche
  - Nom en blanc Poppins Bold 22 pt
  - Rôle et années d'expérience **avec surlignage jaune `#F4BF46`**
  - Citation en italique blanche à droite
- Colonne gauche 30 % :
  - Encart noir "Compétences" : barres de progression 5 cercles dont X remplis en blanc/jaune
  - Encart blanc "Diplômes & Certifications"
- Colonne droite 70 % :
  - "Expériences professionnelles" comme titre
  - Frise verticale grise avec puces carrées navy
  - Pour chaque expérience : entreprise + poste **surlignés en jaune `#F4BF46`**, dates à droite

## Best Used For

Toute communication officielle Pyl.Tech : propositions commerciales (RFP), offres de service, présentations client, decks de pitch, rapports de mission, CV consultants, mockups d'architecture, dashboards de pilotage, supports de formation.

## À éviter

- Texte courant en navy (la charte impose `#4f4f4f` gris)
- Coins très arrondis (radius > 6 px) — la charte est plutôt droite
- Ombres portées marquées
- Mélanger 4+ couleurs principales sur une seule slide
- Texte jaune sur fond blanc (illisible)
- Emojis dans les livrables commerciaux
- Photos stock génériques (préférer photos d'équipe, captures Google Cloud, ou images IA Gemini créditées)
