# Dictionnaire des colonnes — use_cases_catalog.xlsx

**Fichier :** `docs/use_cases_catalog.xlsx`  
**Lignes :** 248 use cases · **Colonnes :** 22  
**Généré le :** 2026-05-21

---

> [!NOTE]
> Le fichier est organisé en 4 groupes logiques de colonnes. Utilisez les filtres Excel sur `Complexity_Tier`, `Family` et `IT_Flag` pour naviguer efficacement.

---

## Groupe 1 — Identifiants & Origine

Ces colonnes viennent du fichier source ou ont été calculées pour identifier chaque ligne de façon unique.

---

### `UC_ID`
| | |
|--|--|
| **Source** | Calculé (hash MD5 des 8 premiers caractères de la description) |
| **Type** | Texte — format `UC_XXXX` |
| **Valeurs possibles** | `UC_0001` à `UC_0245` |
| **Unicité** | Un même UC_ID peut apparaître sur **plusieurs lignes** si le même use case a été soumis par des champions différents (instances multiples du même use case) |

**Comment l'utiliser :** Filtrer sur un UC_ID pour retrouver toutes les instances d'un même use case. Compter les doublons d'un UC_ID pour mesurer la popularité d'un use case.

**Exemple :** `UC_0001` → Voice Translation, soumis par SWE Cluster et Corporate Functions

---

### `Cluster`
| | |
|--|--|
| **Source** | Fichier source — colonne `Cluster` |
| **Type** | Texte |
| **Valeurs possibles** | `Airgas Cluster`, `North Central Europe (NCE) Cluster`, `GBU InnoTech`, `South-West Europe (SWE) Cluster`, `Global Business Services`, `GBU HHC`, `East Asia Pacific (EAP) Cluster`, `Digital & IT`, `Corporate Functions`, `Procurement`, `LATAM Cluster`, `NAM Cluster`, `Africa Middle-East India (AMEI) Cluster`, `N/A` |
| **Note** | Les 7 valeurs `#REF!` du fichier source ont été remplacées par `N/A` |

**Comment l'utiliser :** Filtrer pour comparer le niveau de maturité et le type d'use cases par entité.

---

### `Job Family`
| | |
|--|--|
| **Source** | Fichier source — colonne `Job Family` |
| **Type** | Texte |
| **Valeurs possibles** | `Digital & IT`, `Finance & Controlling`, `Sales & Business Management`, `Research - Engineering - Technology`, `Operations`, `Management / Administration`, `Marketing`, `Procurement`, `HR`, `Legal & Intellectual Property`, `HSE / Risk Mgt`, `Communication`, `N/A` |
| **Note** | Les `#REF!` remplacés par `N/A` |

**Comment l'utiliser :** Identifier quelles fonctions métiers sont les plus actives et quels types d'IA elles sollicitent.

---

### `Stage`
| | |
|--|--|
| **Source** | Fichier source — colonne `Stage` |
| **Type** | Texte |
| **Valeurs possibles** | `Ideation`, `POC`, `MVP`, `Testing / Eval`, `In Development`, `Scale-up`, `Production`, `A revoir avec le builder` |
| **Note** | Les valeurs vides du fichier source sont remplacées par `"A revoir avec le builder"` (141 cas) |

**Comment l'utiliser :** Combiner avec `Complexity_Tier` — un use case Large en `Ideation` est un signal d'alerte (sous-estimation probable). Un use case Small en `Production` est un Quick Win validé.

---

### `Scope of the Use Case`
| | |
|--|--|
| **Source** | Fichier source — colonne `Scope of the Use Case` |
| **Type** | Texte |
| **Valeurs possibles** | `Team(s)`, `Country`, `Cluster`, `Group` |

---

## Groupe 2 — Classification analytique

Ces colonnes ont été **calculées et ajoutées** lors de l'analyse. Elles n'existaient pas dans le fichier source.

---

### `Family`
| | |
|--|--|
| **Source** | Calculé — classification sémantique de la description |
| **Type** | Texte — code court |
| **Valeurs possibles** | `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7` |

| Code | Famille |
|------|---------|
| `F1` | Automatisation documentaire |
| `F2` | Assistant BI & décisionnel |
| `F3` | Customer & Sales Intelligence |
| `F4` | Monitoring & Maintenance industrielle |
| `F5` | Knowledge Management & Formation |
| `F6` | Automatisation de workflows internes |
| `F7` | Data Engineering & Reporting |

**Comment l'utiliser :** Utiliser le code court pour les tableaux croisés dynamiques. Voir `Family_Label` pour l'affichage lisible.

---

### `Family_Label`
| | |
|--|--|
| **Source** | Calculé — libellé long de `Family` |
| **Type** | Texte |
| **Valeurs possibles** | Voir tableau ci-dessus |

---

### `Complexity_Tier`
| | |
|--|--|
| **Source** | Calculé — basé sur `Score_Total` |
| **Type** | Texte |
| **Valeurs possibles** | `Small`, `Medium`, `Large` |

| Tier | Score | Signification |
|------|-------|---------------|
| `Small` | 5–7 | Quick Win — champion seul, no-code, < 2 semaines |
| `Medium` | 8–11 | Use Case Structurant — 4–8 semaines, support IT léger |
| `Large` | 12–15 | Projet Stratégique — 3–12 mois, projet IT formel |

**Comment l'utiliser :** Premier filtre pour prioriser. Commencer par les `Small` pour les Quick Wins, escalader les `Large` vers l'IT.

---

### `Tools`
| | |
|--|--|
| **Source** | Fichier source — colonne `Tools` (conservée telle quelle) |
| **Type** | Texte libre — liste séparée par des virgules |
| **Note** | Valeur brute originale — non normalisée. Utiliser `Tools_Tags` pour l'analyse |

**Exemple :** `"Gemini (Prompts / Gems), App Script (app), Web App/Internal Platform, Appsheet, Advance Coding"`

---

### `Tools_Tags`
| | |
|--|--|
| **Source** | Calculé — normalisation de `Tools` |
| **Type** | Liste Python (ex: `['App Script', 'Gemini Prompts/Gems']`) |
| **Valeurs possibles** | `Gemini Prompts/Gems`, `NotebookLM`, `AppSheet`, `Workspace Studio`, `App Script`, `AI Studio`, `Power BI`, `Advance Coding`, `Web App/Platform`, `Python on Fabric`, `Python on DataStudio` |

**Comment l'utiliser :** Colonne technique — utiliser `Tools` (brut) pour la lecture humaine, `Tools_Tags` pour les filtres et les tableaux croisés via Python/scripts.

---

### `Nb_Tools`
| | |
|--|--|
| **Source** | Calculé — nombre d'outils distincts dans `Tools_Tags` |
| **Type** | Entier |
| **Valeurs possibles** | 0 à 5+ |

**Comment l'utiliser :** Proxy direct de la complexité d'intégration. `Nb_Tools = 1` → Quick Win potentiel. `Nb_Tools ≥ 4` → projet complexe, vérifier `IT_Flag`.

---

### `Max_Tool_Level`
| | |
|--|--|
| **Source** | Calculé — niveau max des outils utilisés |
| **Type** | Texte |
| **Valeurs possibles** | `L1`, `L2`, `L3`, `L4` |

| Niveau | Signification | Outils |
|--------|--------------|--------|
| `L1` | No-code | Gemini Prompts/Gems, NotebookLM |
| `L2` | Low-code | AppSheet, Workspace Studio |
| `L3` | Semi-code | App Script, AI Studio, Power BI |
| `L4` | Code custom | Advance Coding, Web App, Python on Fabric/DataStudio |

**Comment l'utiliser :** Un champion non-IT devrait rester sur `L1`–`L2`. Un `L4` dans un scope `Team` est un signal que le use case risque de ne pas être maintenu.

---

### `Economical Impact`
| | |
|--|--|
| **Source** | Fichier source — colonne `Economical Impact` |
| **Type** | Texte |
| **Valeurs possibles** | `Cost Reduction`, `Revenue Growth`, `Sustainability`, combinaisons de ces 3, `Non évalué` |
| **Note** | Les valeurs vides remplacées par `"Non évalué"` (193 cas — majorité du corpus) |

**Comment l'utiliser :** Attention — la grande majorité des champions n'ont pas renseigné cette valeur. Son absence ne signifie pas l'absence d'impact.

---

### `Data_Sources`
| | |
|--|--|
| **Source** | Calculé — classification sémantique de la description et des outils |
| **Type** | Texte (liste séparée par des virgules) |
| **Valeurs possibles** | `SAP`, `Salesforce`, `Power BI`, `Sheets`, `Google Drive`, `BigQuery`, `AVEVA`, `DCS`, `SCADA`, `Maximo`, `CMMS`, `Oracle`, `Lakehouse`, `Database`, `PDF / Documents`, `A revoir avec le builder` |

**Comment l'utiliser :** Identifier les systèmes d'information et les environnements de données requis pour chaque use case. Permet de dresser la cartographie unitaire des besoins par famille fonctionnelle.

---

## Groupe 3 — Scoring de complexité

Chaque colonne représente le score (1, 2 ou 3) d'une dimension du scoring. **La somme de ces 5 scores = `Score_Total`.**

---

### `Score_Total`
| | |
|--|--|
| **Source** | Calculé — somme des 5 scores |
| **Type** | Entier |
| **Plage** | 5 (minimum possible) à 15 (maximum possible) |

---

### `Score_Integration`
| | |
|--|--|
| **Source** | Calculé |
| **Ce que mesure** | Complexité de l'intégration technique (nombre et niveau des outils) |
| **1 pt** | 1 outil, niveau L1 ou L2 (no-code/low-code) |
| **2 pts** | 2–3 outils ou niveau L3 (semi-code) |
| **3 pts** | 4+ outils ou niveau L4 (code custom) |

---

### `Score_Scope`
| | |
|--|--|
| **Source** | Calculé depuis `Scope of the Use Case` |
| **Ce que mesure** | Périmètre organisationnel visé |
| **1 pt** | `Team(s)` — équipe locale |
| **2 pts** | `Country` ou `Cluster` |
| **3 pts** | `Group` — déploiement global |

---

### `Score_Data`
| | |
|--|--|
| **Source** | Calculé depuis la description + les outils |
| **Ce que mesure** | Complexité et nature des données mobilisées |
| **1 pt** | Données statiques ou manuelles (fichiers Drive, Sheets figés) |
| **2 pts** | Données connectées (SFDC, Power BI, Google Sheets dynamiques) |
| **3 pts** | Données temps réel ou industrielles (capteurs, DCS, SCADA, AVEVA, SAP) |

---

### `Score_AI`
| | |
|--|--|
| **Source** | Calculé depuis la description + les outils |
| **Ce que mesure** | Niveau de maturité IA nécessaire pour implémenter le use case |
| **1 pt** | Prompting simple, Gem, NotebookLM |
| **2 pts** | Appel API Gemini via AI Studio, RAG basique |
| **3 pts** | Agent multi-étapes, fine-tuning, ML custom, Vertex AI |

---

### `Score_Economic`
| | |
|--|--|
| **Source** | Calculé depuis `Economical Impact` |
| **Ce que mesure** | Ambition de l'impact économique déclaré |
| **1 pt** | `Non évalué` ou Productivity seulement |
| **2 pts** | `Cost Reduction` |
| **3 pts** | `Revenue Growth` et/ou `Sustainability` |

> [!NOTE]
> Le score économique reflète uniquement **ce que le champion a déclaré**, pas l'impact réel. Un use case Small avec un impact non évalué peut avoir un fort ROI non quantifié.

---

## Groupe 4 — Alertes IT

---

### `IT_Flag`
| | |
|--|--|
| **Source** | Calculé |
| **Type** | Texte |
| **Valeurs possibles** | `⚠️ IT` ou vide |

**Comment l'utiliser :** Filtrer sur `⚠️ IT` pour identifier les use cases qui nécessitent un accompagnement IT. Ces use cases ne peuvent pas être menés à bien par un champion seul.

> [!WARNING]
> **Implementation Note:** External systems (like Google Apps Script) reading this column must use substring matching (e.g., `.indexOf("IT") !== -1` or `.includes("IT")`) instead of exact string matching. Unicode variation selectors on the warning emoji (`\ufe0f`) are often dropped or normalized differently when importing Excel files into Google Sheets, causing strict equality checks (`=== "⚠️ IT"`) to fail silently.

---

### `IT_Attention`
| | |
|--|--|
| **Source** | Calculé — détail des signaux déclencheurs |
| **Type** | Texte — liste de flags séparés par `\|` |
| **Valeurs possibles (flags)** | `sfdc`, `salesforce`, `aveva`, `dcs`, `scada`, `sap`, `erp`, `oracle`, `active directory`, `oauth`, `sso`, `api key`, `cloud run`, `vertex`, `bigquery`, `database`, `sql`, `24/7`, `production server`, `Large tier` |

**Exemple :** `"sfdc | sap | Large tier"` → Le use case se connecte à SFDC et SAP, et est classé Large — escalade IT obligatoire.

---

### `Maturity_Status`
| | |
|--|--|
| **Source** | Calculé — analyse sémantique des marqueurs de maturité |
| **Type** | Texte |
| **Valeurs possibles** | `🔄 Partiel` ou vide |

**Description :** Cette colonne indique si un use case a déjà été partiellement implémenté ou déployé (par exemple avec Power BI, App Script, ou s'il est noté `--DONE, SO FAR -` dans la description).

**Comment l'utiliser :** Permet d'isoler les use cases qui ont déjà fait l'objet d'un premier développement partiel. Pour ces cas, l'analyse de complexité a été ajustée pour ne scorer que l'effort prospectif restant (le futur scope).

**Exemple :** `UC_0004` (Salesforce Dashboards Assistant) contient la mention `--DONE, SO FAR -`. Son statut est donc `🔄 Partiel`, et ses scores D3 (Data) et D4 (IA) ont été réduits pour refléter uniquement la suite de la roadmap (génération de Slides automatique).

---

## Groupe 5 — Description source

---

### `Use Case Description (Long)`
| | |
|--|--|
| **Source** | Fichier source — colonne `Use Case Description (Long)` |
| **Type** | Texte long (description complète rédigée par le champion) |
| **Note** | Colonne en lecture seule — ne pas modifier. C'est la source de vérité pour la classification. |

**Comment l'utiliser :** En lecture pour comprendre le détail d'un use case identifié par son `UC_ID`. Ne pas utiliser pour les filtres — préférer les colonnes calculées.

---

## Guide de lecture rapide

### Filtres recommandés pour démarrer

| Objectif | Filtre à appliquer |
|----------|-------------------|
| Voir tous les Quick Wins | `Complexity_Tier = Small` |
| Identifier les risques IT | `IT_Flag = ⚠️ IT` |
| Focus sur une famille | `Family = F3` (ex: Customer & Sales) |
| Cluster spécifique | `Cluster = Airgas Cluster` |
| Use cases prêts à scaler | `Stage = Scale-up` ou `Production` |
| Use cases à fort impact | `Score_Economic = 3` |
| Cas sans données manquantes | `Stage ≠ A revoir avec le builder` |

### Tableaux croisés utiles (Excel → Insertion → Tableau croisé dynamique)

| Lignes | Colonnes | Valeurs | Ce que ça montre |
|--------|----------|---------|-----------------|
| `Family_Label` | `Complexity_Tier` | Nombre | Densité par famille × tier |
| `Cluster` | `Complexity_Tier` | Nombre | Maturité par cluster |
| `Job Family` | `Family_Label` | Nombre | Alignement fonction × usage IA |
| `Stage` | `Complexity_Tier` | Nombre | Cohérence déclarée vs réelle |
| `Max_Tool_Level` | `Complexity_Tier` | Nombre | Niveau technique vs ambition |
