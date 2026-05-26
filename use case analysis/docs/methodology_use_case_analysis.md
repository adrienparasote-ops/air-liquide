# Méthodologie d'analyse — Use Cases AI Champions
**Fichier source :** `Advanced AI Champions - Action Monitoring.xlsx` — onglet `Use cases`  
**Volume :** 248 use cases · 14 clusters · 13 Job Families · 11 outils distincts  
**Date :** 2026-05-21 · **Statut :** Analyse sémantique v2 ✅ — marqueurs DONE intégrés

---

## Contexte & Objectif

Air Liquide a collecté 248 use cases IA portés par ses AI Champions (profils métiers, non-IT). La mission couvre 4 axes :

1. **Comprendre le corpus** → regroupement thématique des use cases
2. **Le qualifier** → matrice de complexité (Small / Medium / Large)
3. **Le projeter** → architecture cible Google-first par niveau de complexité
4. **Guider la pratique** → recommandations & bonnes pratiques pour structurer, stocker et pérenniser les réalisations des champions métiers

> [!NOTE]
> Le livrable final est un **document Word (.docx)**. Les références aux use cases dans le livrable utilisent uniquement des **UC_ID** (pas de noms de personnes).

---

## Phase 1 — Audit & Nettoyage des données

> Avant toute analyse, remettre les données en état. Toutes les lignes sont conservées.

### 1.1 Règles de traitement

| Problème détecté | Volume | Décision |
|-----------------|--------|----------|
| Valeurs `#REF!` dans `Cluster` et `Job Family` | 7 lignes | **Remplacer par `N/A`** (ne pas exclure) |
| Use cases sans `Stage` renseigné | 141 lignes | **Inclure** — valeur = `"A revoir avec le builder"` |
| Use cases sans `Economical Impact` | 193 lignes | **Inclure** — valeur = `"Non évalué"` |
| `Tools` = liste libre multi-valeurs | Toutes lignes | **Normaliser** en tags individuels (ex: `"Gemini, App Script"` → 2 tags) |
| Descriptions identiques, clusters différents | Ex: Voice Translation | **Grouper sous un UC_ID commun** — lignes conservées individuellement |

### 1.2 Système d'identifiants UC_ID

Chaque use case reçoit un identifiant unique `UC_XXXX`. Les lignes avec la même description partagent un `UC_ID` commun, ce qui permet :
- Le **regroupement analytique** (compter les instances d'un même use case)
- La **communication aux end users** sans exposer les données personnelles
- La **traçabilité** dans le livrable DOCX

```
UC_0001 → Voice Translation (instance Cluster SWE)
UC_0001 → Voice Translation (instance Corporate Functions)
UC_0002 → SFDC Gemini Reports
...
```

### 1.3 Catégorisation des outils (normalisation)

11 outils distincts → 4 niveaux de complexité technique :

| Niveau | Catégorie | Outils |
|--------|-----------|--------|
| L1 | **No-code** | Gemini (Prompts/Gems), NotebookLM |
| L2 | **Low-code** | AppSheet, Workspace Studio (ex Flows) |
| L3 | **Semi-code** | App Script, AI Studio (app), Power BI (app) |
| L4 | **Code custom** | Advance Coding, Web App/Internal Platform, Python on Power BI (Fabric), Python on DataStudio |

---

## Phase 2 — Regroupement thématique

> Identifier les grands patterns fonctionnels, indépendamment des silos organisationnels.

### 2.1 Méthode

Analyse sémantique des `Use Case Description (Long)` croisée avec `Job Family` et `Tools`. Classification manuelle assistée sur le corpus complet.

### 2.2 Taxonomie — 7 familles fonctionnelles

| # | Famille | Description fonctionnelle | Job Families principales | Exemples corpus |
|---|---------|--------------------------|--------------------------|-----------------|
| **F1** | **Automatisation documentaire** | Génération, rédaction, traduction, résumé de docs | Finance, HR, Legal, Operations | Voice Translation, rapport SFDC auto, synthèse contrats |
| **F2** | **Assistant BI & décisionnel** | Analyse données, lecture dashboards, alertes intelligentes | Finance, Digital & IT, R&ET | AI sur Power BI, analyse prédictive AVEVA, alertes DCS |
| **F3** | **Customer & Sales Intelligence** | Optimisation visites, analyse clients, recommandations | Sales & Business Mgmt, Marketing | Route optimizer SFDC, chatbot F&P, scoring clients |
| **F4** | **Monitoring & Maintenance industrielle** | Santé équipements, prédiction pannes, analyse capteurs | Operations, R&ET | Health monitor Streamlit, predictive maintenance ASU |
| **F5** | **Knowledge Management & Formation** | FAQ internes, onboarding, bases de connaissances | HR, Management/Admin, Marketing | NotebookLM knowledge bases, chatbot RH |
| **F6** | **Automatisation de workflows internes** | Scripts, flows, intégrations Google/Office | Digital & IT, Finance | App Script workflows, Workspace Studio flows |
| **F7** | **Data Engineering & Reporting** | Extraction, transformation, visualisation de données | Finance, Digital & IT, Procurement | Python Fabric, DataStudio pipelines, Power BI custom |

### 2.3 Répartition estimée (à consolider après classification)

```
F1 Automatisation documentaire    ████████████  ~25%
F2 Assistant BI & décisionnel     ████████      ~18%
F3 Customer & Sales Intelligence  ███████       ~15%
F4 Monitoring industriel          ██████        ~13%
F5 Knowledge Management           ██████        ~13%
F6 Workflow automation            █████         ~10%
F7 Data Engineering               ████          ~6%
```

---

## Phase 3 — Matrice de Complexité

> Scorer chaque use case sur 5 dimensions (poids égaux) pour le classer en Small / Medium / Large.

> [!IMPORTANT]
> **Règle DONE-marker (v2)** : L'analyse lit la description complète pour détecter les marqueurs de maturité explicites (`--DONE SO FAR`, `Already built`, `Already deployed`, etc.). La description est alors splitée en **partie faite** / **scope futur**. Le scoring porte sur le **scope futur uniquement**. Si aucun scope futur n'est identifié après le marqueur DONE, le use case est marqué `✅ Complet` et ses dimensions IA et Data sont réduites d'un niveau (l'effort est déjà consommé).

### 3.1 Grille de scoring (5 pts × 3 niveaux = score 5–15)

| Dimension | 🟢 Small (1 pt) | 🟡 Medium (2 pts) | 🔴 Large (3 pts) |
|-----------|----------------|------------------|-----------------|
| **Intégration technique** | 1 outil, L1/L2 (no-code) | 2-3 outils, L3 (semi-code) | 4+ outils, L4 (code custom) |
| **Périmètre organisationnel** | Team / équipe locale | Country / Cluster | Group (déploiement global) |
| **Complexité data** | Données statiques / manuelles | Données connectées (SFDC, Sheets, BI) | Données temps réel / industrielles (capteurs, DCS) |
| **Maturité IA requise** | Prompting / Gem / NotebookLM | API Gemini + RAG basique | Agent multi-étapes / ML / fine-tuning |
| **Impact économique déclaré** | Non évalué / Productivity | Cost Reduction | Revenue Growth / Sustainability |

**Règles d'application complémentaires :**

| Règle | Détail |
|-------|--------|
| **Outil L4 data → D3 ≥ 2** | Si `Python on Power BI (Fabric)`, `Python on DataStudio`, ou `BigQuery` dans les outils → D3 minimum = 2 (données connectées enterprise), même si la description ne le mentionne pas explicitement |
| **DONE + scope futur simple** | Si partie faite = systèmes enterprise (SFDC, SAP) et scope futur = slides/summary/corrective actions → D3 réduit à 1 (le futur est plus simple) |
| **DONE + pas de scope futur** | Use case complet → D4 (IA) et D3 (Data) réduits de 1 niveau (l'effort IA/Data est déjà investi) |
| **Stage Production/Scale-up + Small tier** | NON incohérent : des scripts App Script simples ou des Gems NotebookLM peuvent être en production tout en restant Small. Le tier reflète la complexité de l'effort, pas la valeur produite. |

### 3.2 Table de classification

| Tier | Score | Label | Time-to-value | Profil champion |
|------|-------|-------|---------------|-----------------|
| 🟢 **Small** | 5–7 | **Quick Win** | < 2 semaines | Champion seul, no-code |
| 🟡 **Medium** | 8–11 | **Use Case Structurant** | 4–8 semaines | Champion + support IT local |
| 🔴 **Large** | 12–15 | **Projet Stratégique** | 3–12 mois | Équipe projet IT + Champion métier |

### 3.2bis Résultats après analyse sémantique complète (248 UCs)

| Tier | Count | % | Observation |
|------|------:|--:|-------------|
| 🟢 Small | 110 | 44% | Quick Wins immédiatement mobilisables |
| 🟡 Medium | 130 | 52% | Cœur de portefeuille — championnat accompagné |
| 🔴 Large | 8 | 3% | Projets IT formels — budget et gouvernance dédiés |

> [!NOTE]
> La proportion de Large (3%) est volontairement faible : les champions IA sont des profils métiers, pas IT. Les use cases véritablement Large impliquent des architectures agents autonomes, du ML/fine-tuning, ou des intégrations enterprise multi-systèmes (SFDC + Power BI + Python).

### 3.3 Signalement et gouvernance des dépendances IT

La gouvernance technique repose sur la distinction entre deux indicateurs complémentaires pour assurer à la fois traçabilité et agilité :

* **`IT_Attention` (Visibilité passive)** : Moteur de recherche sémantique qui trace tous les mots-clés techniques sensibles (ex: `sap`, `sfdc`, `database`, `api`, `sql`) dans la description ou les outils, indépendamment de la taille du projet. Il offre à la DSI une visibilité passive complète sur le patrimoine technologique touché.
* **`IT_Flag` (Action et escalade obligatoire)** : Drapeau d'action (valeur = `⚠️ IT`) qui désigne les projets de complexité significatrice nécessitant un accompagnement technique et une validation formelle par la DSI avant tout déploiement.

> [!IMPORTANT]
> **Règle d'exemption pour les Quick Wins (Small)** : Afin de libérer l'innovation sur le terrain et d'éviter l'engorgement administratif de la DSI, tous les use cases classés dans la catégorie **`Small`** (Score Total <= 7) sont **exemptés d'IT_Flag** (qui reste vide), même s'ils contiennent des mots-clés techniques détectés dans `IT_Attention`. Ces petits projets locaux restent sous l'entière autonomie du champion.

Critères déclencheurs du point d'attention :
- Connexion à un système d'entreprise (ERP, CRM, SCADA, BI enterprise)
- Authentification / gestion des droits (SSO, API keys, OAuth)
- Hébergement hors Google Workspace (Cloud Run, Vertex AI, bases de données)
- Volume de données > ce qu'un Google Sheet peut supporter (> 100K lignes)


### 3.4 Corrélation Stage / Tier (signal de cohérence)

| Stage déclaré | Tier attendu | Signal |
|---------------|-------------|--------|
| Ideation | Small → Medium | À qualifier |
| POC | Small → Medium | Validation en cours |
| MVP | Medium → Large | Engagement fort |
| Testing / Eval | Medium | Recalibrage possible |
| In Development | Medium → Large | Investissement réel |
| Scale-up | Large | Traction prouvée |
| Production | Large | ROI mesurable |
| A revoir avec le builder | À scorer | Inclus dans l'analyse |

---

## Phase 4 — Architecture Cible (Google-first)

> Stack de référence par tier. **Rester dans l'écosystème Google Workspace / GCP**. Tout besoin dépassant cet écosystème est signalé comme point d'attention IT.

### 🟢 Small — "Prompting & Automation"

```
┌──────────────────────────────────────────────────────┐
│  USER  →  Gemini Gem / NotebookLM                    │
│           ↕                                           │
│  DATA  →  Google Drive / Sheets (statique)            │
│           ↕                                           │
│  OUTPUT → Google Docs / Gmail / Google Chat           │
└──────────────────────────────────────────────────────┘
```

| | |
|--|--|
| **Outils** | Gemini (Prompts/Gems), NotebookLM |
| **Compétence requise** | Prompt engineering |
| **Gouvernance** | Champion seul — aucune intervention IT |
| **Time-to-value** | < 2 semaines |
| **Point d'attention IT** | Aucun |

---

### 🟡 Medium — "App & Orchestration"

```
┌──────────────────────────────────────────────────────────────┐
│  TRIGGER  →  App Script (schedule / event)                   │
│              ↕                                                │
│  PROCESS  →  AI Studio (API Gemini) + Workspace Studio Flow  │
│              ↕                                                │
│  DATA     →  Google Sheets / AppSheet (données structurées)  │
│              ↓                            ↓                   │
│  OUTPUT   →  AppSheet App          Google Slides / Docs       │
└──────────────────────────────────────────────────────────────┘
```

| | |
|--|--|
| **Outils** | App Script, AppSheet, AI Studio, Workspace Studio |
| **Compétence requise** | Low-code + appels API basiques |
| **Gouvernance** | Champion + support IT local ponctuel |
| **Time-to-value** | 4–8 semaines |
| **Point d'attention IT** | Si connexion SFDC / BI enterprise → escalade IT requise |

---

### 🔴 Large — "Platform & Agent"

```
┌─────────────────────────────────────────────────────────────────┐
│  SOURCES  →  SFDC │ AVEVA │ DCS │ SAP │ Power BI (Fabric)       │
│              ↓                                                    │
│  INGESTION →  Python (Cloud Functions / BigQuery / DataStudio)   │
│              ↓                                                    │
│  AI ENGINE →  AI Studio / Vertex AI + RAG + Agents Gemini        │
│              ↓                                                    │
│  ORCHES.   →  Advance Coding (backend API / Cloud Run)           │
│              ↓                       ↓                           │
│  FRONT    →  Web App (AppSheet Pro)  Power BI Embedded           │
│               Internal Platform                                   │
└─────────────────────────────────────────────────────────────────┘
```

| | |
|--|--|
| **Outils** | Advance Coding, Python on Fabric, AI Studio/Vertex AI, Web App, Power BI |
| **Compétence requise** | Full-stack + ML engineering |
| **Gouvernance** | Projet IT formel + Champion métier + budget dédié |
| **Time-to-value** | 3–12 mois |
| **Point d'attention IT** | **Systématique** — hors portée du champion seul |

---

## Phase 5 — Recommandations & Bonnes Pratiques

> Cette section est centrale : les champions sont des **bidouilleurs métiers**, pas des développeurs. Sans cadre, leurs réalisations restent fragiles, non maintenables et impossibles à transmettre.

### 5.1 Gestion & Versioning des Prompts

Les prompts Gemini sont des **actifs métier** au même titre qu'une procédure opérationnelle. Ils doivent être traités comme tels.

**Pratiques recommandées :**

| Pratique | Comment faire (sans IT) |
|----------|------------------------|
| **Stocker les prompts** | Dans un Google Doc dédié par use case, pas dans le chat Gemini | 
| **Versionner** | Utiliser un naming clair : `Prompt_V1.0_AAAA-MM-JJ` dans le titre du Doc |
| **Documenter le contexte** | En-tête obligatoire : objectif, audience, exemples d'input/output attendus |
| **Centraliser** | Créer un Google Drive partagé `AI Champions / Prompts Library` accessible à l'équipe |
| **Tester avant de déployer** | Toujours tester avec 3 exemples réels avant de partager un Gem |

**Template d'en-tête prompt recommandé :**
```
# [Nom du Prompt] — v[X.Y] — [Date]
Objectif    : [Ce que fait ce prompt]
Audience    : [Qui l'utilise]
Outil       : [Gemini Gem / AI Studio / NotebookLM]
Use Case ID : UC_XXXX
Input type  : [Ex: texte libre / tableau / email]
Output type : [Ex: résumé 5 bullets / rapport structuré]
---
[Corps du prompt]
```

---

### 5.2 Bonnes Pratiques App Script

App Script est l'outil le plus utilisé (46 use cases). Sans discipline minimale, les scripts deviennent impossibles à maintenir.

**Règles de base pour les champions métiers :**

| Règle | Pourquoi |
|-------|----------|
| **1 script = 1 fichier Google Apps Script nommé** | Pas de scripts éparpillés dans des Sheets au hasard |
| **Commenter les blocs principaux** | Le champion suivant (ou vous dans 6 mois) doit comprendre |
| **Ne jamais mettre de mot de passe / clé API en clair dans le code** | Utiliser `PropertiesService.getScriptProperties()` pour stocker les secrets |
| **Créer un README dans le Doc associé** | Expliquer ce que fait le script, comment le lancer, ce qu'il touche |
| **Sauvegarder avant chaque modification** | Copier le script dans un Doc "Archive" avec la date |
| **Tester sur des données fictives** | Jamais directement sur la production |

**Structure de nommage recommandée :**
```
[Cluster]_[Famille]_[Fonction]_V[X]
Ex: SWE_F3_SFDC_RouteOptimizer_V2
```

---

### 5.3 Bonnes Pratiques NotebookLM

| Règle | Pourquoi |
|-------|----------|
| Documenter les sources chargées et leur date | NotebookLM n'est pas à jour automatiquement |
| Préférer des sources structurées (PDF, Doc bien formaté) | Améliore la qualité des réponses |
| Créer un Notebook par périmètre fonctionnel clair | Éviter les notebooks fourre-tout |
| Revoir et rafraîchir les sources tous les trimestres | Les sources obsolètes génèrent des réponses incorrectes |

---

### 5.4 Gouvernance Légère — Le "Kit Champion"

Pour chaque use case créé, le champion devrait maintenir un **Kit Champion** minimal :

```
📁 UC_XXXX — [Nom du Use Case]
├── 📄 README.md        → Description, audience, how-to, contacts
├── 📄 Prompts_Vx.x.md  → Historique des prompts versionnés
├── 📄 Script_Vx.x.gs   → Copie du App Script (si applicable)
├── 📄 Tests.md         → Exemples d'inputs / outputs validés
└── 📄 Changelog.md     → Historique des modifications
```

**Où stocker ce kit :** Google Drive partagé de l'équipe AI Champions du cluster.

---

### 5.5 Quand escalader vers l'IT ?

Les champions doivent savoir identifier les **signaux d'alerte** qui indiquent qu'un use case dépasse leur périmètre d'autonomie :

| Signal | Action recommandée |
|--------|-------------------|
| Besoin d'accéder à un système d'entreprise (SFDC, SAP, AVEVA…) | → Contacter l'IT pour une API / connexion sécurisée |
| Données sensibles (RH, financières, clients) | → Vérifier avec le DPO / Legal avant de construire |
| Le script plante régulièrement ou est "trop compliqué" | → Qualifier en Large, escalader |
| L'outil est utilisé par plus de 10 personnes | → Passer en Medium ou Large, documenter formellement |
| Besoin d'un accès 24/7 ou d'une fiabilité critique | → Hors périmètre champion → projet IT |

---

## Phase 6 — Livrables

> Tout le livrable final est en **DOCX**. Les références aux use cases utilisent les **UC_ID uniquement**.

| Livrable | Contenu | Audience |
|----------|---------|----------|
| **1. Synthèse du corpus** | Volume, répartition par famille / cluster / tier, Top outils | Cliente / CODIR |
| **2. Catalogue classifié** | Tableau UC_ID × Famille × Tier × Stage × Tools × Point d'attention | Champions AI |
| **3. Architectures de référence** | 3 schémas (Small / Medium / Large) commentés | DSI / Digital |
| **4. Roadmap de priorisation** | Matrice Impact / Effort — Top Quick Wins identifiés | Programme management |
| **5. Guide bonnes pratiques** | Sections 5.1 à 5.5 mises en forme pour les champions | Champions AI |

---

## Décisions validées

| # | Sujet | Décision |
|---|-------|----------|
| D1 | Valeurs `#REF!` | Remplacées par `N/A` — lignes conservées |
| D2 | Use cases sans Stage | Inclus — valeur `"A revoir avec le builder"` |
| D3 | Use cases sans Impact éco | Inclus — valeur `"Non évalué"` |
| D4 | Normalisation Tools | Tags individuels |
| D5 | Doublons | Lignes conservées + UC_ID partagé |
| D6 | Pondération complexité | Poids égaux sur les 5 dimensions |
| D7 | Stack cible | Google-first — dépendances IT signalées en point d'attention |
| D8 | Format livrable | DOCX |
| D9 | Confidentialité | UC_ID uniquement dans le livrable (pas de noms) |
| D10 | Nouvel axe | Section recommandations & bonnes pratiques ajoutée |
| **D11** | **Analyse sémantique DONE-marker** | **Les descriptions sont parsées pour détecter les marqueurs `--DONE SO FAR`, `Already built/deployed`, etc. Le scoring prospectif porte uniquement sur le scope futur. Implémenté en Python sur le corpus complet (248 UCs).** |
| **D12** | **Correction D3 — outils L4 data** | **Si `Python on Power BI (Fabric)` ou `Python on DataStudio` dans les outils → D3 ≥ 2 automatiquement (données enterprise connectées).** |
| **D13** | **Incohérence Stage/Tier** | **Production/Scale-up + Small tier = non incohérent. Le tier reflète l'effort de construction, pas le niveau de déploiement atteint.** |
| **D14** | **Extraction des Data Sources** | **Ajout d'une colonne `Data_Sources` extraite via règles regex unitaires sur la description et les outils (SAP, Salesforce, Power BI, BigQuery, etc.).** |
| **D15** | **Exemption IT Quick Wins** | **Les projets `Small` sont exemptés d' `IT_Flag` (visibilité passive conservée via `IT_Attention`) pour accélérer le déploiement des Quick Wins.** |

