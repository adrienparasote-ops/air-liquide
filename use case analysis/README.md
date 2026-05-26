# Air Liquide — AI Champions

Outillage d'analyse et de reporting du portefeuille de use cases IA pour le programme AI Champions d'Air Liquide.

## Pipeline

```
[Source Excel brut]
        ↓
src/generate_catalog.py   →  docs/use_cases_catalog.xlsx  (248 UC enrichis)
        ↓
[Upload Google Drive → convertir en Google Sheet]
        ↓
src/create_analysis.gs    →  Onglets "Synthèse" + "Graphiques généraux" + "Focus Medium & Large" (menu 🤖 AI Champions)
        ↓
src/generate_docx.py      →  docs/[REPORT] AI builders.docx   (rapport Word 7 sections)
src/generate_pptx.py      →  docs/presentation_ai_champions.pptx  (9 slides Pyl.Tech)
```

## Structure

```
.
├── docs/
│   ├── use_cases_catalog.xlsx          # Catalogue enrichi (248 use cases)
│   ├── [REPORT] AI builders.docx       # Rapport Word de synthèse
│   ├── presentation_ai_champions.pptx  # Présentation PowerPoint (charte Pyl.Tech)
│   ├── methodology_use_case_analysis.md # Méthodologie de scoring (5 dimensions)
│   └── catalog_column_dictionary.md    # Dictionnaire des colonnes du catalogue
├── src/
│   ├── generate_catalog.py   # Génération du catalogue enrichi depuis la source Excel
│   ├── generate_docx.py      # Rapport Word (python-docx, charte Pyl.Tech)
│   ├── generate_pptx.py      # Présentation PowerPoint (python-pptx, charte Pyl.Tech)
│   ├── create_analysis.gs    # Apps Script Google Sheets (tableau de bord + graphiques)
│   └── tests/
│       ├── test_generate_catalog.py  # 144 tests, 100% coverage
│       ├── test_generate_docx.py     # 33 tests, 99% coverage
│       └── test_generate_pptx.py     # 36 tests, 100% coverage
├── Skill-Theme/                        # Charte graphique Pyl.Tech
└── assets/                             # Assets statiques
```

## Prérequis

```bash
pip install pandas openpyxl python-docx python-pptx lxml
```

## Usage

```bash
# 1. Générer le catalogue enrichi
python3 src/generate_catalog.py

# 2. Générer le rapport Word
python3 src/generate_docx.py

# 3. Générer la présentation PowerPoint
python3 src/generate_pptx.py

# 4. Lancer les tests (220 tests, 100% coverage)
python3 -m pytest src/tests/ -v --cov=src
```

## Google Sheets (tableau de bord interactif)

1. Uploader `docs/use_cases_catalog.xlsx` sur Google Drive
2. Ouvrir avec Google Sheets → **Fichier → Enregistrer en tant que Google Sheets**
3. **Extensions → Apps Script** → coller le contenu de `src/create_analysis.gs`
4. Sauvegarder → le menu **🤖 AI Champions** apparaît automatiquement
5. Utiliser le menu pour générer les tableaux de synthèse et les graphiques

## Scoring des use cases

Chaque use case est scoré sur 5 dimensions (1–3 pts chacune) :

| Dimension | Critère |
|-----------|---------|
| Intégration technique | Nb d'outils, niveau d'intégration |
| Périmètre organisationnel | Local / Country / Group |
| Complexité data | Dépendances données, qualité requise |
| Maturité IA | Niveau d'expertise requis |
| Impact économique | ROI estimé |

**Tiers :**
- **Small** (5–7 pts) : Quick Win, < 2 semaines
- **Medium** (8–11 pts) : Use Case Structurant, 4–8 semaines
- **Large** (12–15 pts) : Projet Stratégique, 3–12 mois

## Charte graphique

Les livrables Word et PowerPoint suivent la **charte officielle Pyl.Tech** définie dans `Skill-Theme/`.
Couleurs principales : Navy `#0b132b`, Jaune `#F4BF46`, Turquoise `#208AAE`.
