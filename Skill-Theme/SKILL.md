---
name: pyltech-theme
description: Applique la charte graphique officielle Pyl.Tech à toute création visuelle (slides PowerPoint, documents Word, PDF, artifacts HTML, dashboards, posters, présentations commerciales). Utiliser systématiquement cette skill dès que l'utilisateur demande un document Pyl.Tech, une proposition commerciale, une présentation client, un livrable de mission, ou mentionne "charte Pyl.Tech", "look Pyl", "thème Pyl.Tech", ou même quand l'utilisateur produit un livrable au nom de Pyl.Tech sans le préciser. Couvre les couleurs officielles (jaune #F4BF46, navy #0b132b, gris corps #4f4f4f, accents bleu turquoise et teal), la typographie Poppins, les layouts de slide, les patterns de cards, le surlignage jaune et les badges NEW/UPDATED.
---

# Pyl.Tech Theme Factory

Skill pour appliquer la charte graphique **officielle** Pyl.Tech sur tout artefact visuel : slides (.pptx), documents (.docx), PDF, artifacts HTML/React, dashboards, posters, mockups.

## Quand l'utiliser

- L'utilisateur demande un livrable au nom de Pyl.Tech (proposition, présentation, deck commercial, rapport client, slide unique)
- L'utilisateur mentionne "charte Pyl.Tech", "look Pyl", "thème Pyl.Tech", "habiller aux couleurs Pyl"
- L'utilisateur fait évoluer un livrable Pyl.Tech existant (refonte d'une slide, ajout d'une page)
- L'utilisateur crée un artifact (mockup HTML, dashboard, infographie) dans un contexte Pyl.Tech (mission client, offre, RFP)

Si le contexte est ambigu (ex: "fais-moi un slide sur X" sans indication d'entreprise), demander brièvement si la charte Pyl.Tech doit s'appliquer avant de procéder.

## Le thème

La charte est définie dans `themes/pyltech-brand.md`. **Lire ce fichier en premier** avant toute production graphique : il contient les codes hex exacts officiels, les polices, les tailles et les règles d'usage.

### Couleurs officielles (résumé)

| Rôle | Hex |
|------|-----|
| Titles / Dark background | `#0b132b` |
| Slides background | `#ffffff` |
| **Body text color** | **`#4f4f4f`** (gris foncé, PAS navy !) |
| Shape / grey slide background | `#eeeeee` |
| Primary (Accent 1) | `#F4BF46` |
| Accent 2 | `#0d2149` |
| Accent 3 | `#208AAE` |
| Accent 4 | `#5BC0BE` |
| Succès | `#138636` |
| Danger | `#C91432` |

**Polices** : Poppins (12 pt corps, 10 pt tableaux)

## Workflow recommandé

1. **Lire `themes/pyltech-brand.md`** : récupérer la palette officielle, les polices, les patterns.
2. **Identifier le type de livrable** (slide deck, doc Word, artifact HTML, poster…) et lire la référence correspondante dans `references/` :
   - `references/slides.md` — pour les présentations PowerPoint/Google Slides
   - `references/documents.md` — pour les documents Word/PDF/rapports
   - `references/web-artifacts.md` — pour HTML/React/dashboards/mockups
3. **Combiner avec la skill de format** (pptx, docx, frontend-design) : la charte Pyl.Tech définit les couleurs/typo/patterns ; la skill de format (par ex. `pptx`) gère la mécanique de génération du fichier. Toujours lire les deux.
4. **Produire** en appliquant rigoureusement la palette et les patterns récurrents.

## Règles d'or non-négociables

Quel que soit le livrable :

- **Le texte courant est en gris `#4f4f4f`**, jamais en navy. Le navy `#0b132b` est réservé aux titres et fonds sombres. C'est l'erreur la plus fréquente à éviter.
- **Le footer "© Copyright [année] Pyl.Tech"** apparaît en bas de toutes les pages/slides en **turquoise `#208AAE`** (pas en gris).
- **La pagination** est en bas à droite, aussi en turquoise `#208AAE`.
- **Le logo Pyl.Tech** apparaît en haut à droite de chaque slide intérieure.
- **Le titre de slide** est encadré par 2 traits horizontaux fins navy (haut et bas), précédé d'un cartouche jaune carré (`#F4BF46`) avec le numéro de section.
- **Le sous-titre** apparaît sous le titre, en gris `#4f4f4f`, sans gras.
- **Les bullets sont des carrés jaunes** `#F4BF46`, pas des disques.
- **Mise en valeur** : gras + **surlignage jaune `#F4BF46`** (style marqueur fluo) — pattern caractéristique de la charte.
- **Tailles officielles** : 12 pt pour le corps, 10 pt pour les tableaux.
- **Ne jamais introduire** de couleurs hors palette officielle.
- **Ne jamais utiliser** d'emoji décoratifs dans les livrables formels.

## Patterns spéciaux à connaître

### Badge "NEW" / "UPDATED" triangulaire

Triangle navy `#0b132b` en haut à gauche d'une slide ou d'un élément, avec texte blanc en rotation -45°. Sert à signaler une nouveauté ou une mise à jour.

### Surlignage jaune

Pattern signature de la charte : appliquer un fond `#F4BF46` derrière des mots-clés (style "marqueur fluo"). Très utilisé dans les CV consultants (rôle, dates, entreprise+poste) et pour mettre en avant des éléments forts.

## Variantes de scénario

- **Slide de couverture** : fond jaune intégral `#F4BF46`, titre en gros navy `#0b132b` centré, logo Pyl.Tech en haut à gauche, partenaire (Google Cloud Partner…) en haut à droite, version+date en bas à gauche.
- **Slide de section (intercalaire)** : split visuel 1/3 (image client teintée jaune en overlay avec gros numéro blanc) + 2/3 (sommaire avec section active en navy gras, autres en gris).
- **Slide de contenu** : header avec 2 traits navy + cartouche jaune + titre navy + sous-titre gris, puis layout en cards (2 à 4 cards par slide, headers colorés alternés navy/turquoise/teal/jaune).
- **Slide de tarif/offre** : cards "offre" avec header coloré pleine largeur (navy ou teal), prix mis en avant en grand, détails à droite en liste à puces carrées jaunes.
- **Slide CV** : bandeau navy `#0b132b` en haut avec photo, nom, et **surlignages jaunes** sur le rôle et l'expérience.

## Création d'un livrable composite

Si l'utilisateur demande un document complet (ex: proposition commerciale), prévoir l'ossature standard Pyl.Tech :

1. Couverture (fond jaune)
2. Tour de table de l'équipe (4 cards portrait)
3. Sommaire (liste à puces carrées jaunes)
4. Page intercalaire de section 01
5. Slides de contenu de la section 01
6. Page intercalaire 02 (sommaire avec 01 grisé et 02 actif)
7. … (idem pour chaque section)
8. Slide de références (table client/volume/projet/expert)
9. Slides CV experts (1 par expert clé, avec surlignages jaunes)
10. Slide de conclusion ".Transformez avec Pyl.Tech."

## Pour aller plus loin

- `references/slides.md` — détails par type de slide, dimensions, marges, code python-pptx prêt à l'emploi
- `references/documents.md` — adaptation Word/PDF, en-têtes, styles paragraphe, code python-docx
- `references/web-artifacts.md` — variables CSS, composants React, tokens Tailwind
- `assets/colors.json` — palette officielle exportable en JSON pour scripts pptx/docx
