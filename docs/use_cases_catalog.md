# Catalogue Classifié — Use Cases AI Champions Air Liquide
**Source :** `Advanced AI Champions - Action Monitoring.xlsx` — onglet `Use cases`  
**Volume :** 248 use cases analysés  
**Date :** 2026-05-21  
**Méthode :** Analyse sémantique des descriptions brutes + signaux de maturité explicites  

> [!IMPORTANT]
> Ce catalogue applique une **analyse sémantique en profondeur** des descriptions. Les marqueurs de maturité explicites (`--DONE SO FAR`, `Already built`, etc.) dans les descriptions sont détectés et réduisent le score de complexité prospectif : seul le travail **restant à faire** est scoré.

---

## Résumé exécutif

| Indicateur | Valeur |
|------------|--------|
| **Total use cases** | 248 |
| 🟢 Small (Quick Win) | 110 (44%) |
| 🟡 Medium (Use Case Structurant) | 130 (52%) |
| 🔴 Large (Projet Stratégique) | 8 (3%) |
| ⚠️ Attention IT requise | 81 (33%) |
| ✅ Avec marqueur DONE explicite | 3 |

---

## Répartition par Famille Fonctionnelle

| Famille | Small | Medium | Large | Total |
|---------|------:|-------:|------:|------:|
| **F1** Automatisation documentaire | 7 | 10 | 0 | 17 |
| **F2** Assistant BI & décisionnel | 14 | 22 | 1 | 37 |
| **F3** Customer & Sales Intelligence | 23 | 30 | 3 | 56 |
| **F4** Monitoring & Maintenance industrielle | 12 | 12 | 2 | 26 |
| **F5** Knowledge Management & Formation | 18 | 10 | 0 | 28 |
| **F6** Automatisation de workflows internes | 26 | 15 | 0 | 41 |
| **F7** Data Engineering & Reporting | 10 | 31 | 2 | 43 |

---

## Catalogue Complet par UC_ID

| UC_ID | Tier | Score | Stage | Famille | Cluster | Job Family | Outils | IT | Maturité |
|-------|------|------:|-------|---------|---------|-----------|-------|:--:|---------|
| UC_0001 | 🟡 Medium | 9/15 | Ideation | F6 | South-West Europe SWE | Operations | Advance Coding | ⚠️ |  |
| UC_0002 | 🟡 Medium | 9/15 | MVP | F6 | Corporate Functions | Operations | App Script (app) |  |  |
| UC_0003 | 🟢 Small | 7/15 | Ideation | F1 | South-West Europe SWE | Marketing | App Script (app), Gemini (Prompt... |  |  |
| UC_0004 | 🟡 Medium | 8/15 | MVP | F2 | South-West Europe SWE | Marketing | Gemini (Prompts / Gems), Appshee... | ⚠️ | 🔄 Partiel |
| UC_0005 | 🟡 Medium | 11/15 | MVP | F3 | South-West Europe SWE | Marketing | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0006 | 🟢 Small | 7/15 | N/A | F4 | South-West Europe SWE | Operations | App Script (app) |  |  |
| UC_0007 | 🟢 Small | 7/15 | N/A | F7 | South-West Europe SWE | Operations | Gemini (Prompts / Gems) |  |  |
| UC_0008 | 🟡 Medium | 9/15 | N/A | F4 | South-West Europe SWE | Operations | Python on Power BI (Fabric) | ⚠️ |  |
| UC_0009 | 🟡 Medium | 8/15 | N/A | F4 | South-West Europe SWE | Operations | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0010 | 🟡 Medium | 9/15 | N/A | F4 | North Central Europe NCE | Operations | App Script (app) | ⚠️ |  |
| UC_0011 | 🟢 Small | 6/15 | N/A | F4 | GBU HHC | Operations | App Script (app), Gemini (Prompt... |  |  |
| UC_0012 | 🟢 Small | 6/15 | Ideation | F6 | Digital & IT | Digital & IT | AI Studio (app), Gemini (Prompts... |  |  |
| UC_0013 | 🟢 Small | 7/15 | Ideation | F7 | Digital & IT | Digital & IT | Gemini (Prompts / Gems), AI Stud... |  |  |
| UC_0014 | 🟢 Small | 6/15 | N/A | F7 | Global Business Services | Finance & Controlling |  |  |  |
| UC_0015 | 🟡 Medium | 10/15 | N/A | F4 | East Asia Pacific EAP | Operations | Gemini (Prompts / Gems), AI Stud... | ⚠️ |  |
| UC_0016 | 🟡 Medium | 11/15 | N/A | F7 | GBU HHC | Digital & IT | Power BI (app), Advance Coding, ... | ⚠️ |  |
| UC_0017 | 🟡 Medium | 8/15 | N/A | F3 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), Noteboo... |  |  |
| UC_0018 | 🟡 Medium | 9/15 | POC | F2 | Corporate Functions | Digital & IT | App Script (app), Gemini (Prompt... | ⚠️ |  |
| UC_0019 | 🟢 Small | 6/15 | Scale-up | F6 | North Central Europe NCE | Digital & IT | AI Studio (app) |  |  |
| UC_0020 | 🟡 Medium | 8/15 | Scale-up | F1 | North Central Europe NCE | Digital & IT | App Script (app) |  |  |
| UC_0021 | 🟢 Small | 7/15 | Ideation | F6 | North Central Europe NCE | Digital & IT | AI Studio (app) |  |  |
| UC_0022 | 🟡 Medium | 10/15 | Ideation | F3 | North Central Europe NCE | Sales & Business Management | App Script (app), Web App/Intern... | ⚠️ |  |
| UC_0023 | 🟡 Medium | 11/15 | Scale-up | F7 | North Central Europe NCE | Sales & Business Management | App Script (app), Advance Coding... | ⚠️ |  |
| UC_0024 | 🟢 Small | 7/15 | Ideation | F3 | North Central Europe NCE | Sales & Business Management | App Script (app), Web App/Intern... |  |  |
| UC_0025 | 🟡 Medium | 11/15 | Scale-up | F3 | North Central Europe NCE | Sales & Business Management | App Script (app), Workspace Stud... | ⚠️ |  |
| UC_0026 | 🟡 Medium | 10/15 | Scale-up | F3 | North Central Europe NCE | Sales & Business Management | App Script (app), Web App/Intern... | ⚠️ |  |
| UC_0027 | 🟡 Medium | 8/15 | N/A | F5 | East Asia Pacific EAP | Operations | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0028 | 🟡 Medium | 9/15 | Draft | F7 | East Asia Pacific EAP | Management / Administration | Gemini (Prompts / Gems), AI Stud... |  |  |
| UC_0029 | 🟡 Medium | 9/15 | POC | F6 | GBU InnoTech | Research -Engineering -  Te... | App Script (app) |  |  |
| UC_0030 | 🟢 Small | 7/15 | N/A | F2 | East Asia Pacific EAP | HSE / Risk Mgt / IMS/ Quali... | Gemini (Prompts / Gems) |  |  |
| UC_0031 | 🟢 Small | 7/15 | N/A | F6 | Corporate Functions | Communication | App Script (app) |  |  |
| UC_0032 | 🟡 Medium | 9/15 | POC | F3 | Corporate Functions | Digital & IT | Advance Coding, Gemini (Prompts ... | ⚠️ |  |
| UC_0033 | 🟢 Small | 6/15 | MVP | F5 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), AI Stud... |  |  |
| UC_0034 | 🟢 Small | 7/15 | POC | F7 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), Workspa... |  |  |
| UC_0035 | 🟢 Small | 7/15 | POC | F7 | GBU InnoTech | Research -Engineering -  Te... | Workspace Studio (ex Flows), Gem... |  |  |
| UC_0036 | 🟡 Medium | 8/15 | N/A | F7 | Digital & IT | Digital & IT | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0037 | 🟡 Medium | 8/15 | N/A | F7 | Digital & IT | Digital & IT | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0038 | 🟡 Medium | 8/15 | Scale-up | F5 | North Central Europe NCE | Sales & Business Management | App Script (app), Gemini (Prompt... |  |  |
| UC_0039 | 🟡 Medium | 8/15 | MVP | F6 | North Central Europe NCE | Sales & Business Management | App Script (app) | ⚠️ |  |
| UC_0040 | 🟢 Small | 7/15 | POC | F2 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0041 | 🟢 Small | 6/15 | Scale-up | F7 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0042 | 🟡 Medium | 9/15 | N/A | F3 | GBU InnoTech | Research -Engineering -  Te... | NotebookLM, AI Studio (app), Gem... |  |  |
| UC_0043 | 🟡 Medium | 9/15 | N/A | F3 | GBU InnoTech | Research -Engineering -  Te... | AI Studio (app), NotebookLM, Gem... |  |  |
| UC_0044 | 🟢 Small | 7/15 | N/A | F6 | GBU InnoTech | Research -Engineering -  Te... | App Script (app), Gemini (Prompt... |  |  |
| UC_0045 | 🟡 Medium | 9/15 | N/A | F3 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), Noteboo... |  |  |
| UC_0046 | 🟡 Medium | 9/15 | N/A | F2 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), Noteboo... | ⚠️ |  |
| UC_0047 | 🟡 Medium | 8/15 | N/A | F3 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), Noteboo... |  |  |
| UC_0048 | 🟡 Medium | 8/15 | N/A | F1 | Procurement | Procurement | AI Studio (app), App Script (app) |  |  |
| UC_0049 | 🟢 Small | 6/15 | N/A | F1 | Procurement | Procurement | AI Studio (app), App Script (app) |  |  |
| UC_0050 | 🟡 Medium | 9/15 | N/A | F3 | Airgas | Digital & IT | Power BI (app), Python on Power ... | ⚠️ |  |
| UC_0051 | 🟡 Medium | 9/15 | N/A | F2 | GBU HHC | Digital & IT | Gemini (Prompts / Gems), AI Stud... |  |  |
| UC_0052 | 🟡 Medium | 8/15 | N/A | F2 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0053 | 🟡 Medium | 10/15 | N/A | F4 | North Central Europe NCE | Sales & Business Management | App Script (app) | ⚠️ |  |
| UC_0054 | 🟡 Medium | 8/15 | N/A | F3 | North Central Europe NCE | Sales & Business Management | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0055 | 🟡 Medium | 8/15 | N/A | F2 | North Central Europe NCE | Sales & Business Management | App Script (app) | ⚠️ |  |
| UC_0056 | 🟡 Medium | 10/15 | N/A | F7 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0057 | 🟢 Small | 7/15 | Ideation | F2 | GBU HHC | Finance & Controlling | Gemini (Prompts / Gems), Noteboo... |  |  |
| UC_0058 | 🟡 Medium | 9/15 | Ideation | F2 | Digital & IT | Digital & IT | App Script (app), Workspace Stud... |  |  |
| UC_0059 | 🟡 Medium | 11/15 | N/A | F7 | Airgas | Sales & Business Management | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0060 | 🟡 Medium | 8/15 | N/A | F2 | Airgas | Sales & Business Management | Gemini (Prompts / Gems) |  |  |
| UC_0061 | 🟡 Medium | 8/15 | N/A | F3 | Airgas | Sales & Business Management | NotebookLM |  |  |
| UC_0062 | 🟢 Small | 6/15 | N/A | F5 | Airgas | Sales & Business Management | Gemini (Prompts / Gems) |  |  |
| UC_0063 | 🟢 Small | 6/15 | N/A | F7 | Airgas | Sales & Business Management | Gemini (Prompts / Gems) |  |  |
| UC_0064 | 🟡 Medium | 9/15 | N/A | F7 | Airgas | Sales & Business Management | App Script (app) | ⚠️ |  |
| UC_0065 | 🟡 Medium | 9/15 | N/A | F7 | Airgas | Sales & Business Management | Workspace Studio (ex Flows) | ⚠️ |  |
| UC_0066 | 🟢 Small | 5/15 | N/A | F5 | Digital & IT | Digital & IT | NotebookLM |  |  |
| UC_0067 | 🟢 Small | 6/15 | N/A | F5 | Digital & IT | Digital & IT | Gemini (Prompts / Gems) |  |  |
| UC_0068 | 🟢 Small | 6/15 | N/A | F5 | Digital & IT | Digital & IT | App Script (app) |  |  |
| UC_0069 | 🟢 Small | 7/15 | N/A | F6 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0070 | 🟢 Small | 5/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0071 | 🟢 Small | 5/15 | N/A | F2 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0072 | 🟢 Small | 5/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0073 | 🟡 Medium | 9/15 | N/A | F3 | GBU HHC | Operations | App Script (app), Gemini (Prompt... |  |  |
| UC_0074 | 🟢 Small | 5/15 | N/A | F4 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0075 | 🟢 Small | 5/15 | N/A | F4 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0076 | 🟢 Small | 6/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0077 | 🟢 Small | 5/15 | N/A | F6 | LATAM | Finance & Controlling |  |  |  |
| UC_0078 | 🔴 Large | 12/15 | POC | F3 | South-West Europe SWE | Marketing | Python on Power BI (Fabric), Gem... | ⚠️ |  |
| UC_0079 | 🟢 Small | 5/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0080 | 🟡 Medium | 8/15 | N/A | F3 | Airgas | Management / Administration | NotebookLM |  |  |
| UC_0081 | 🟡 Medium | 8/15 | N/A | F4 | Airgas | Marketing | App Script (app) |  |  |
| UC_0082 | 🟡 Medium | 9/15 | N/A | F2 | Airgas | Management / Administration | NotebookLM | ⚠️ |  |
| UC_0083 | 🟢 Small | 5/15 | N/A | F4 | Airgas | Management / Administration | NotebookLM |  |  |
| UC_0084 | 🟢 Small | 7/15 | N/A | F3 | Airgas | Marketing | App Script (app) |  |  |
| UC_0085 | 🟡 Medium | 9/15 | N/A | F5 | Airgas | Management / Administration | NotebookLM | ⚠️ |  |
| UC_0086 | 🟢 Small | 7/15 | N/A | F5 | Airgas | Management / Administration | NotebookLM |  |  |
| UC_0087 | 🟡 Medium | 9/15 | N/A | F3 | Airgas | Management / Administration | NotebookLM | ⚠️ |  |
| UC_0088 | 🟢 Small | 7/15 | N/A | F3 | Airgas | Marketing | Power BI (app) |  |  |
| UC_0089 | 🟢 Small | 7/15 | N/A | F3 | Airgas | Marketing | Gemini (Prompts / Gems) |  |  |
| UC_0090 | 🟢 Small | 7/15 | N/A | F6 | Airgas | Management / Administration | App Script (app) |  |  |
| UC_0091 | 🟡 Medium | 9/15 | N/A | F3 | Airgas | Management / Administration | Python on Power BI (Fabric) | ⚠️ |  |
| UC_0092 | 🟢 Small | 7/15 | N/A | F2 | Airgas | Marketing | Power BI (app) |  |  |
| UC_0093 | 🟡 Medium | 10/15 | N/A | F7 | South-West Europe SWE | Operations | App Script (app), Python on Powe... | ⚠️ | 🔄 Partiel |
| UC_0094 | 🟡 Medium | 10/15 | N/A | F7 | South-West Europe SWE | Operations |  |  |  |
| UC_0095 | 🟢 Small | 7/15 | N/A | F5 | Airgas | Management / Administration | NotebookLM |  |  |
| UC_0096 | 🟢 Small | 5/15 | N/A | F1 | Airgas | Management / Administration | NotebookLM |  |  |
| UC_0097 | 🟢 Small | 6/15 | N/A | F2 | #REF! | #REF! | NotebookLM, App Script (app), Ge... |  |  |
| UC_0098 | 🟡 Medium | 8/15 | N/A | F7 | North Central Europe NCE | Digital & IT | AI Studio (app) |  |  |
| UC_0099 | 🟢 Small | 7/15 | N/A | F6 | Airgas | Digital & IT | AI Studio (app), App Script (app... |  |  |
| UC_0100 | 🟡 Medium | 9/15 | N/A | F5 | North Central Europe NCE | Digital & IT | App Script (app), Gemini (Prompt... |  |  |
| UC_0101 | 🟢 Small | 6/15 | Testing / Eval | F6 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) |  |  |
| UC_0102 | 🟢 Small | 7/15 | Testing / Eval | F5 | Airgas | Finance & Controlling | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0103 | 🟡 Medium | 8/15 | Production | F7 | Airgas | Finance & Controlling | App Script (app) |  |  |
| UC_0104 | 🟡 Medium | 10/15 | Draft | F7 | Airgas | Finance & Controlling | App Script (app), Web App/Intern... | ⚠️ | 🔄 Partiel |
| UC_0105 | 🟡 Medium | 9/15 | Production | F2 | Airgas | Finance & Controlling | App Script (app) |  |  |
| UC_0106 | 🟢 Small | 6/15 | N/A | F2 | Airgas | Finance & Controlling | App Script (app), AI Studio (app) |  |  |
| UC_0107 | 🟢 Small | 6/15 | N/A | F3 | GBU InnoTech | Digital & IT | App Script (app) |  |  |
| UC_0108 | 🟢 Small | 7/15 | N/A | F6 | Africa Middle-East Ind... | Operations | Appsheet, App Script (app), Work... |  |  |
| UC_0109 | 🟢 Small | 7/15 | N/A | F4 | Africa Middle-East Ind... | Operations | Appsheet, App Script (app), Work... |  |  |
| UC_0110 | 🟡 Medium | 10/15 | N/A | F7 | South-West Europe SWE | Operations | Workspace Studio (ex Flows), AI ... |  |  |
| UC_0111 | 🔴 Large | 12/15 | N/A | F4 | South-West Europe SWE | Operations | Workspace Studio (ex Flows), AI ... | ⚠️ |  |
| UC_0112 | 🟢 Small | 7/15 | Scale-up | F6 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0113 | 🟢 Small | 6/15 | N/A | F2 | GBU InnoTech | Research -Engineering -  Te... | NotebookLM |  |  |
| UC_0114 | 🟡 Medium | 9/15 | N/A | F7 | GBU InnoTech | Marketing | App Script (app), Appsheet |  |  |
| UC_0115 | 🟢 Small | 6/15 | Production | F6 | Global Business Services | Finance & Controlling | App Script (app) |  |  |
| UC_0116 | 🟢 Small | 5/15 | Production | F5 | Global Business Services | Finance & Controlling | Gemini (Prompts / Gems) |  |  |
| UC_0117 | 🟢 Small | 6/15 | N/A | F2 | Airgas | Digital & IT | App Script (app) |  |  |
| UC_0118 | 🟢 Small | 7/15 | N/A | F7 | Airgas | Digital & IT | App Script (app) |  |  |
| UC_0119 | 🟢 Small | 7/15 | N/A | F7 | Airgas | Digital & IT | App Script (app) |  |  |
| UC_0120 | 🟡 Medium | 8/15 | N/A | F7 | Airgas | Digital & IT | App Script (app) |  |  |
| UC_0121 | 🟡 Medium | 10/15 | Scale-up | F6 | Digital & IT | Digital & IT | NotebookLM |  |  |
| UC_0122 | 🟡 Medium | 8/15 | Scale-up | F6 | Digital & IT | Digital & IT | NotebookLM |  |  |
| UC_0123 | 🟡 Medium | 10/15 | MVP | F7 | Digital & IT | Digital & IT | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0124 | 🟡 Medium | 9/15 | POC | F2 | Airgas | Finance & Controlling | NotebookLM, Gemini (Prompts / Ge... |  |  |
| UC_0125 | 🟡 Medium | 9/15 | Scale-up | F5 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0126 | 🟡 Medium | 8/15 | N/A | F6 | Procurement | Procurement | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0127 | 🟡 Medium | 9/15 | Scale-up | F3 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0128 | 🟡 Medium | 9/15 | Scale-up | F3 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) |  |  |
| UC_0129 | 🟡 Medium | 8/15 | Scale-up | F3 | Airgas | Finance & Controlling | NotebookLM | ⚠️ |  |
| UC_0130 | 🟢 Small | 7/15 | Scale-up | F5 | Airgas | Finance & Controlling | NotebookLM |  |  |
| UC_0131 | 🟡 Medium | 10/15 | N/A | F4 | Airgas | Marketing | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0132 | 🟢 Small | 7/15 | POC | F1 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding |  |  |
| UC_0133 | 🟢 Small | 6/15 | POC | F4 | GBU InnoTech | Research -Engineering -  Te... | App Script (app) |  |  |
| UC_0134 | 🟡 Medium | 9/15 | POC | F3 | Corporate Functions | Marketing | App Script (app), Gemini (Prompt... | ⚠️ |  |
| UC_0135 | 🟢 Small | 7/15 | N/A | F2 | Global Business Services | Finance & Controlling | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0136 | 🟡 Medium | 10/15 | Ideation | F7 | Global Business Services | Finance & Controlling | Power BI (app), Python on Power ... | ⚠️ |  |
| UC_0137 | 🟡 Medium | 10/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0138 | 🟡 Medium | 9/15 | POC | F2 | Airgas | Finance & Controlling | Web App/Internal Platform, Advan... | ⚠️ |  |
| UC_0139 | 🟡 Medium | 9/15 | Scale-up | F3 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0140 | 🟡 Medium | 9/15 | N/A | F2 | #REF! | #REF! | NotebookLM, Gemini (Prompts / Gems) |  |  |
| UC_0141 | 🟡 Medium | 8/15 | N/A | F2 | #REF! | #REF! | NotebookLM, Gemini (Prompts / Gems) |  |  |
| UC_0142 | 🟡 Medium | 9/15 | N/A | F5 | #REF! | #REF! | NotebookLM, Gemini (Prompts / Gems) |  |  |
| UC_0143 | 🟢 Small | 6/15 | N/A | F2 | South-West Europe SWE | Marketing |  |  |  |
| UC_0144 | 🟢 Small | 7/15 | Testing / Eval | F5 | Global Business Services | Finance & Controlling | Gemini (Prompts / Gems), NotebookLM |  |  |
| UC_0145 | 🟡 Medium | 8/15 | Production | F7 | North Central Europe NCE | Operations | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0146 | 🟢 Small | 7/15 | Testing / Eval | F3 | North Central Europe NCE | Marketing | NotebookLM, Gemini (Prompts / Gems) |  |  |
| UC_0147 | 🟢 Small | 6/15 | In Development | F6 | Global Business Services | Finance & Controlling | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0148 | 🟢 Small | 7/15 | In Development | F3 | Global Business Services | Finance & Controlling | Gemini (Prompts / Gems), Noteboo... |  |  |
| UC_0149 | 🟢 Small | 7/15 | In Development | F2 | Procurement | Procurement | NotebookLM |  |  |
| UC_0150 | 🟢 Small | 5/15 | Testing / Eval | F5 | Procurement | Procurement | NotebookLM |  |  |
| UC_0151 | 🟡 Medium | 9/15 | Testing / Eval | F3 | North Central Europe NCE | Marketing | NotebookLM | ⚠️ |  |
| UC_0152 | 🟡 Medium | 8/15 | MVP | F7 | GBU InnoTech | Research -Engineering -  Te... | App Script (app), Advance Coding | ⚠️ |  |
| UC_0153 | 🟢 Small | 5/15 | Testing / Eval | F3 | North Central Europe NCE | Marketing | Gemini (Prompts / Gems) |  |  |
| UC_0154 | 🟢 Small | 7/15 | MVP | F6 | LATAM | Digital & IT | App Script (app) |  |  |
| UC_0155 | 🟢 Small | 6/15 | Production | F3 | GBU InnoTech | Sales & Business Management | App Script (app) |  |  |
| UC_0156 | 🟢 Small | 6/15 | Production | F3 | GBU InnoTech | Sales & Business Management | App Script (app), Gemini (Prompt... |  |  |
| UC_0157 | 🟢 Small | 7/15 | Production | F3 | GBU InnoTech | Sales & Business Management | App Script (app), Gemini (Prompt... |  |  |
| UC_0158 | 🟢 Small | 6/15 | Production | F3 | GBU InnoTech | Sales & Business Management | App Script (app) |  |  |
| UC_0159 | 🟢 Small | 7/15 | MVP | F3 | East Asia Pacific EAP | Marketing | App Script (app) |  |  |
| UC_0160 | 🟡 Medium | 8/15 | Ideation | F2 | East Asia Pacific EAP | Marketing | Power BI (app), Advance Coding | ⚠️ |  |
| UC_0161 | 🟡 Medium | 9/15 | MVP | F7 | East Asia Pacific EAP | Marketing | Gemini (Prompts / Gems), Power B... | ⚠️ |  |
| UC_0162 | 🟢 Small | 7/15 | MVP | F4 | East Asia Pacific EAP | Marketing | Power BI (app) |  |  |
| UC_0163 | 🟢 Small | 6/15 | Ideation | F6 | Digital & IT | Digital & IT | Workspace Studio (ex Flows), App... |  |  |
| UC_0164 | 🟡 Medium | 8/15 | MVP | F7 | GBU InnoTech | Research -Engineering -  Te... | App Script (app), Advance Coding | ⚠️ |  |
| UC_0165 | 🟢 Small | 6/15 | POC | F6 | East Asia Pacific EAP | Operations | App Script (app) |  |  |
| UC_0166 | 🟡 Medium | 8/15 | POC | F5 | North Central Europe NCE | Sales & Business Management | NotebookLM |  |  |
| UC_0167 | 🟡 Medium | 8/15 | Ideation | F6 | GBU HHC | Finance & Controlling | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0168 | 🟡 Medium | 8/15 | MVP | F4 | Corporate Functions | Digital & IT | App Script (app), Appsheet |  |  |
| UC_0169 | 🟡 Medium | 8/15 | Ideation | F7 | #REF! | #REF! |  | ⚠️ |  |
| UC_0170 | 🟡 Medium | 8/15 | Ideation | F6 | GBU HHC | Digital & IT |  |  |  |
| UC_0171 | 🔴 Large | 12/15 | Ideation | F3 | North Central Europe NCE | Finance & Controlling | Python on DataStudio |  |  |
| UC_0172 | 🟡 Medium | 8/15 | Ideation | F2 | North Central Europe NCE | Legal & Intellectual Property | Appsheet, Gemini (Prompts / Gems... |  |  |
| UC_0173 | 🟢 Small | 6/15 | Ideation | F3 | North Central Europe NCE | Legal & Intellectual Property | App Script (app), Gemini (Prompt... |  |  |
| UC_0174 | 🟢 Small | 6/15 | POC | F5 | GBU HHC | Finance & Controlling | App Script (app), Workspace Stud... |  |  |
| UC_0175 | 🟡 Medium | 9/15 | MVP | F6 | LATAM | Digital & IT | Advance Coding | ⚠️ |  |
| UC_0176 | 🟡 Medium | 8/15 | N/A | F3 | Airgas | Sales & Business Management | NotebookLM, App Script (app) |  |  |
| UC_0177 | 🟡 Medium | 10/15 | POC | F2 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems) |  |  |
| UC_0178 | 🟡 Medium | 9/15 | Ideation | F6 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding | ⚠️ |  |
| UC_0179 | 🟡 Medium | 8/15 | Ideation | F6 | East Asia Pacific EAP | Finance & Controlling |  |  |  |
| UC_0180 | 🟡 Medium | 8/15 | N/A | F5 | GBU HHC | Digital & IT | AI Studio (app) |  |  |
| UC_0181 | 🟡 Medium | 8/15 | N/A | F5 | GBU HHC | Digital & IT | AI Studio (app), Advance Coding | ⚠️ |  |
| UC_0182 | 🔴 Large | 12/15 | POC | F3 | GBU HHC | Digital & IT | Advance Coding, AI Studio (app) | ⚠️ |  |
| UC_0183 | 🔴 Large | 12/15 | MVP | F4 | Global Business Services | Digital & IT | AI Studio (app), Advance Coding,... | ⚠️ |  |
| UC_0184 | 🟡 Medium | 10/15 | POC | F7 | Global Business Services | Digital & IT | AI Studio (app), Advance Coding,... | ⚠️ |  |
| UC_0185 | 🟡 Medium | 10/15 | Ideation | F6 | Global Business Services | Digital & IT | AI Studio (app), Advance Coding,... | ⚠️ |  |
| UC_0186 | 🟢 Small | 7/15 | N/A | F6 | East Asia Pacific EAP | Sales & Business Management | App Script (app) |  |  |
| UC_0187 | 🟢 Small | 7/15 | POC | F4 | Digital & IT | Digital & IT | App Script (app) |  |  |
| UC_0188 | 🟡 Medium | 9/15 | Ideation | F7 | N/A | Finance & Controlling | Python on Power BI (Fabric), Pow... | ⚠️ |  |
| UC_0189 | 🔴 Large | 14/15 | MVP | F7 | Airgas | Digital & IT | Power BI (app), Advance Coding | ⚠️ |  |
| UC_0190 | 🟡 Medium | 9/15 | POC | F1 | #REF! | #REF! | App Script (app) |  |  |
| UC_0191 | 🟡 Medium | 11/15 | Ideation | F1 |   | N/A | Advance Coding | ⚠️ |  |
| UC_0192 | 🟢 Small | 7/15 | Scale-up | F6 | Global Business Services | HR | Advance Coding |  |  |
| UC_0193 | 🟡 Medium | 8/15 | Scale-up | F2 | Global Business Services | HR | Advance Coding | ⚠️ |  |
| UC_0194 | 🟢 Small | 6/15 | Scale-up | F6 | Global Business Services | HR | App Script (app) |  |  |
| UC_0195 | 🟢 Small | 7/15 | Scale-up | F1 | Global Business Services | HR | Advance Coding |  |  |
| UC_0196 | 🟢 Small | 7/15 | Scale-up | F5 | Global Business Services | HR | Advance Coding |  |  |
| UC_0197 | 🟢 Small | 6/15 | Scale-up | F5 | Global Business Services | HR | NotebookLM, Gemini (Prompts / Gems) |  |  |
| UC_0198 | 🟢 Small | 7/15 | Scale-up | F6 | Global Business Services | HR | Advance Coding |  |  |
| UC_0199 | 🟡 Medium | 10/15 | MVP | F7 | NAM | Operations | App Script (app), Advance Coding... | ⚠️ |  |
| UC_0200 | 🟡 Medium | 10/15 | POC | F3 | Airgas | Finance & Controlling | App Script (app) | ⚠️ |  |
| UC_0201 | 🟡 Medium | 10/15 | Scale-up | F7 | NAM | Operations | App Script (app), Gemini (Prompt... | ⚠️ |  |
| UC_0202 | 🟢 Small | 6/15 | MVP | F1 | GBU InnoTech | Procurement | Gemini (Prompts / Gems) |  |  |
| UC_0203 | 🟡 Medium | 10/15 | POC | F4 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding, Gemini (Prompts ... | ⚠️ |  |
| UC_0204 | 🟢 Small | 6/15 | POC | F6 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems) |  |  |
| UC_0205 | 🟡 Medium | 8/15 | POC | F3 | GBU HHC | Digital & IT | Gemini (Prompts / Gems), Web App... | ⚠️ |  |
| UC_0206 | 🟢 Small | 5/15 | N/A | F3 | GBU HHC | Digital & IT |  |  |  |
| UC_0207 | 🟢 Small | 5/15 | N/A | F3 | GBU HHC | Sales & Business Management | NotebookLM |  |  |
| UC_0208 | 🟢 Small | 6/15 | POC | F6 | GBU InnoTech | Research -Engineering -  Te... | Workspace Studio (ex Flows) |  |  |
| UC_0209 | 🟢 Small | 7/15 | POC | F5 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems) |  |  |
| UC_0210 | 🟢 Small | 7/15 | POC | F7 | GBU InnoTech | Research -Engineering -  Te... | NotebookLM |  |  |
| UC_0211 | 🟡 Medium | 9/15 | POC | F2 | GBU InnoTech | Research -Engineering -  Te... | App Script (app), Advance Coding | ⚠️ |  |
| UC_0212 | 🟢 Small | 6/15 | Ideation | F2 | NAM | Operations | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0213 | 🟢 Small | 6/15 | Ideation | F4 | NAM | Operations | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0214 | 🔴 Large | 12/15 | MVP | F2 | GBU HHC | Marketing | Gemini (Prompts / Gems), App Scr... | ⚠️ |  |
| UC_0215 | 🟢 Small | 7/15 | MVP | F3 | North Central Europe NCE | Sales & Business Management | App Script (app) |  |  |
| UC_0216 | 🟡 Medium | 8/15 | Scale-up | F3 | GBU InnoTech | Research -Engineering -  Te... | Web App/Internal Platform, Advan... | ⚠️ |  |
| UC_0217 | 🟡 Medium | 9/15 | MVP | F6 | GBU HHC | Finance & Controlling | App Script (app) |  |  |
| UC_0218 | 🟡 Medium | 10/15 | POC | F2 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0219 | 🔴 Large | 12/15 | Scale-up | F7 | Airgas | Finance & Controlling | Gemini (Prompts / Gems) | ⚠️ |  |
| UC_0220 | 🟡 Medium | 10/15 | POC | F3 | Airgas | Finance & Controlling | App Script (app), Appsheet, Adva... | ⚠️ |  |
| UC_0221 | 🟡 Medium | 11/15 | Scale-up | F3 | North Central Europe NCE | Sales & Business Management | App Script (app), Web App/Intern... | ⚠️ |  |
| UC_0222 | 🟡 Medium | 9/15 | Ideation | F2 | Airgas | Finance & Controlling | Advance Coding | ⚠️ |  |
| UC_0223 | 🟡 Medium | 9/15 | Ideation | F2 | GBU InnoTech | Procurement | App Script (app), Advance Coding | ⚠️ |  |
| UC_0224 | 🟡 Medium | 8/15 | POC | F5 | GBU InnoTech | Research -Engineering -  Te... | App Script (app) |  |  |
| UC_0225 | 🟡 Medium | 9/15 | Ideation | F1 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding | ⚠️ |  |
| UC_0226 | 🟢 Small | 7/15 | POC | F2 | #REF! | #REF! | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0227 | 🟢 Small | 7/15 | MVP | F6 | GBU InnoTech | Research -Engineering -  Te... | Gemini (Prompts / Gems), App Scr... |  |  |
| UC_0228 | 🟡 Medium | 8/15 | POC | F7 | East Asia Pacific EAP | Operations | Web App/Internal Platform, Advan... | ⚠️ |  |
| UC_0229 | 🟢 Small | 7/15 | Ideation | F3 | East Asia Pacific EAP | Operations | Advance Coding |  |  |
| UC_0230 | 🟢 Small | 7/15 | POC | F4 | LATAM | Digital & IT | App Script (app) |  |  |
| UC_0231 | 🟡 Medium | 8/15 | N/A | F6 | East Asia Pacific EAP | Finance & Controlling | App Script (app) |  |  |
| UC_0232 | 🟢 Small | 7/15 | Scale-up | F6 | South-West Europe SWE | Marketing | App Script (app) |  |  |
| UC_0233 | 🟡 Medium | 9/15 | N/A | F4 | North Central Europe NCE | Operations | App Script (app) | ⚠️ |  |
| UC_0234 | 🟡 Medium | 8/15 | N/A | F1 | North Central Europe NCE | Operations | App Script (app) |  |  |
| UC_0235 | 🟡 Medium | 8/15 | N/A | F1 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0236 | 🟡 Medium | 8/15 | N/A | F1 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0237 | 🟡 Medium | 9/15 | N/A | F1 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0238 | 🟢 Small | 6/15 | N/A | F3 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0239 | 🟢 Small | 5/15 | N/A | F1 | Airgas | Management / Administration | Gemini (Prompts / Gems) |  |  |
| UC_0240 | 🟢 Small | 7/15 | Ideation | F4 | North Central Europe NCE | Operations | Workspace Studio (ex Flows), Gem... |  |  |
| UC_0241 | 🟡 Medium | 9/15 | Ideation | F4 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding | ⚠️ |  |
| UC_0242 | 🟡 Medium | 8/15 | POC | F7 | Airgas | Finance & Controlling | App Script (app), Gemini (Prompt... | ⚠️ |  |
| UC_0243 | 🟢 Small | 7/15 | POC | F6 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding, App Script (app)... |  |  |
| UC_0244 | 🟡 Medium | 9/15 | Ideation | F7 | South-West Europe SWE | Sales & Business Management | Python on Power BI (Fabric) | ⚠️ |  |
| UC_0245 | 🟡 Medium | 11/15 | POC | F1 | GBU InnoTech | Research -Engineering -  Te... | Advance Coding, Web App/Internal... | ⚠️ |  |
| UC_0246 | 🟢 Small | 5/15 | N/A | F5 | GBU InnoTech | Research -Engineering -  Te... | Workspace Studio (ex Flows) |  |  |
| UC_0247 | 🟢 Small | 7/15 | Scale-up | F5 | North Central Europe NCE | Sales & Business Management | App Script (app), Web App/Intern... |  |  |
| UC_0248 | 🟡 Medium | 8/15 | Scale-up | F4 | Airgas | Operations | App Script (app), Web App/Intern... | ⚠️ |  |

---

## Détail de Scoring — Dimensions

| UC_ID | D1 Integration | D2 Périmètre | D3 Data | D4 IA | D5 Impact | Total | Tier |
|-------|---------------|-------------|--------|-------|-----------|-------|------|
| UC_0001 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0002 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0003 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0004 | 3 | 2 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0005 | 3 | 3 | 2 | 1 | 2 | 11 | 🟡 Medium |
| UC_0006 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0007 | 1 | 2 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0008 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0009 | 1 | 2 | 3 | 1 | 1 | 8 | 🟡 Medium |
| UC_0010 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0011 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0012 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0013 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0014 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0015 | 3 | 3 | 2 | 1 | 1 | 10 | 🟡 Medium |
| UC_0016 | 3 | 3 | 2 | 2 | 1 | 11 | 🟡 Medium |
| UC_0017 | 3 | 1 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0018 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0019 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0020 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0021 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0022 | 3 | 2 | 1 | 1 | 3 | 10 | 🟡 Medium |
| UC_0023 | 3 | 2 | 2 | 1 | 3 | 11 | 🟡 Medium |
| UC_0024 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0025 | 3 | 1 | 3 | 1 | 3 | 11 | 🟡 Medium |
| UC_0026 | 3 | 1 | 2 | 1 | 3 | 10 | 🟡 Medium |
| UC_0027 | 2 | 1 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0028 | 2 | 2 | 2 | 2 | 1 | 9 | 🟡 Medium |
| UC_0029 | 2 | 3 | 1 | 2 | 1 | 9 | 🟡 Medium |
| UC_0030 | 1 | 2 | 1 | 2 | 1 | 7 | 🟢 Small |
| UC_0031 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0032 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0033 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0034 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0035 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0036 | 2 | 1 | 3 | 1 | 1 | 8 | 🟡 Medium |
| UC_0037 | 2 | 1 | 3 | 1 | 1 | 8 | 🟡 Medium |
| UC_0038 | 2 | 1 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0039 | 2 | 2 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0040 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0041 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0042 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0043 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0044 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0045 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0046 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0047 | 2 | 1 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0048 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0049 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0050 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0051 | 3 | 1 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0052 | 2 | 1 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0053 | 2 | 2 | 3 | 2 | 1 | 10 | 🟡 Medium |
| UC_0054 | 2 | 2 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0055 | 2 | 1 | 3 | 1 | 1 | 8 | 🟡 Medium |
| UC_0056 | 2 | 2 | 2 | 3 | 1 | 10 | 🟡 Medium |
| UC_0057 | 2 | 1 | 1 | 2 | 1 | 7 | 🟢 Small |
| UC_0058 | 2 | 3 | 1 | 2 | 1 | 9 | 🟡 Medium |
| UC_0059 | 1 | 3 | 2 | 2 | 3 | 11 | 🟡 Medium |
| UC_0060 | 1 | 1 | 2 | 3 | 1 | 8 | 🟡 Medium |
| UC_0061 | 1 | 3 | 1 | 2 | 1 | 8 | 🟡 Medium |
| UC_0062 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0063 | 1 | 1 | 2 | 1 | 1 | 6 | 🟢 Small |
| UC_0064 | 2 | 1 | 3 | 2 | 1 | 9 | 🟡 Medium |
| UC_0065 | 1 | 3 | 3 | 1 | 1 | 9 | 🟡 Medium |
| UC_0066 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0067 | 1 | 1 | 2 | 1 | 1 | 6 | 🟢 Small |
| UC_0068 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0069 | 1 | 3 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0070 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0071 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0072 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0073 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0074 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0075 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0076 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0077 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0078 | 3 | 2 | 2 | 2 | 3 | 12 | 🔴 Large |
| UC_0079 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0080 | 1 | 2 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0081 | 2 | 2 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0082 | 1 | 2 | 2 | 3 | 1 | 9 | 🟡 Medium |
| UC_0083 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0084 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0085 | 1 | 2 | 2 | 3 | 1 | 9 | 🟡 Medium |
| UC_0086 | 1 | 3 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0087 | 1 | 2 | 2 | 3 | 1 | 9 | 🟡 Medium |
| UC_0088 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0089 | 1 | 2 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0090 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0091 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0092 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0093 | 3 | 3 | 2 | 1 | 1 | 10 | 🟡 Medium |
| UC_0094 | 1 | 3 | 2 | 3 | 1 | 10 | 🟡 Medium |
| UC_0095 | 1 | 1 | 1 | 3 | 1 | 7 | 🟢 Small |
| UC_0096 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0097 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0098 | 2 | 1 | 2 | 2 | 1 | 8 | 🟡 Medium |
| UC_0099 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0100 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0101 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0102 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0103 | 2 | 2 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0104 | 3 | 2 | 1 | 3 | 1 | 10 | 🟡 Medium |
| UC_0105 | 2 | 2 | 1 | 3 | 1 | 9 | 🟡 Medium |
| UC_0106 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0107 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0108 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0109 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0110 | 2 | 3 | 1 | 3 | 1 | 10 | 🟡 Medium |
| UC_0111 | 2 | 3 | 3 | 3 | 1 | 12 | 🔴 Large |
| UC_0112 | 2 | 1 | 1 | 1 | 2 | 7 | 🟢 Small |
| UC_0113 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0114 | 2 | 2 | 2 | 2 | 1 | 9 | 🟡 Medium |
| UC_0115 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0116 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0117 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0118 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0119 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0120 | 2 | 1 | 3 | 1 | 1 | 8 | 🟡 Medium |
| UC_0121 | 1 | 3 | 1 | 3 | 2 | 10 | 🟡 Medium |
| UC_0122 | 1 | 3 | 1 | 1 | 2 | 8 | 🟡 Medium |
| UC_0123 | 1 | 3 | 2 | 1 | 3 | 10 | 🟡 Medium |
| UC_0124 | 3 | 1 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0125 | 1 | 3 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0126 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0127 | 1 | 3 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0128 | 1 | 3 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0129 | 1 | 2 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0130 | 1 | 1 | 1 | 1 | 3 | 7 | 🟢 Small |
| UC_0131 | 3 | 2 | 3 | 1 | 1 | 10 | 🟡 Medium |
| UC_0132 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0133 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0134 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0135 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0136 | 3 | 1 | 3 | 2 | 1 | 10 | 🟡 Medium |
| UC_0137 | 3 | 2 | 3 | 1 | 1 | 10 | 🟡 Medium |
| UC_0138 | 3 | 1 | 3 | 1 | 1 | 9 | 🟡 Medium |
| UC_0139 | 1 | 3 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0140 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0141 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0142 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0143 | 1 | 2 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0144 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0145 | 2 | 1 | 2 | 2 | 1 | 8 | 🟡 Medium |
| UC_0146 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0147 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0148 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0149 | 1 | 3 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0150 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0151 | 1 | 2 | 2 | 3 | 1 | 9 | 🟡 Medium |
| UC_0152 | 3 | 1 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0153 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0154 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0155 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0156 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0157 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0158 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0159 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0160 | 3 | 2 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0161 | 2 | 2 | 2 | 2 | 1 | 9 | 🟡 Medium |
| UC_0162 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0163 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0164 | 3 | 1 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0165 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0166 | 1 | 2 | 1 | 3 | 1 | 8 | 🟡 Medium |
| UC_0167 | 2 | 2 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0168 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0169 | 1 | 3 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0170 | 1 | 2 | 2 | 2 | 1 | 8 | 🟡 Medium |
| UC_0171 | 3 | 3 | 2 | 3 | 1 | 12 | 🔴 Large |
| UC_0172 | 2 | 1 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0173 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0174 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0175 | 3 | 1 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0176 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0177 | 1 | 3 | 2 | 2 | 2 | 10 | 🟡 Medium |
| UC_0178 | 3 | 3 | 1 | 1 | 1 | 9 | 🟡 Medium |
| UC_0179 | 1 | 2 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0180 | 2 | 2 | 1 | 2 | 1 | 8 | 🟡 Medium |
| UC_0181 | 3 | 2 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0182 | 3 | 3 | 2 | 2 | 2 | 12 | 🔴 Large |
| UC_0183 | 3 | 3 | 2 | 3 | 1 | 12 | 🔴 Large |
| UC_0184 | 3 | 3 | 2 | 1 | 1 | 10 | 🟡 Medium |
| UC_0185 | 3 | 3 | 2 | 1 | 1 | 10 | 🟡 Medium |
| UC_0186 | 2 | 1 | 1 | 1 | 2 | 7 | 🟢 Small |
| UC_0187 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0188 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0189 | 3 | 2 | 3 | 3 | 3 | 14 | 🔴 Large |
| UC_0190 | 2 | 3 | 1 | 1 | 2 | 9 | 🟡 Medium |
| UC_0191 | 3 | 3 | 1 | 1 | 3 | 11 | 🟡 Medium |
| UC_0192 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0193 | 3 | 1 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0194 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0195 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0196 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0197 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0198 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0199 | 3 | 1 | 2 | 2 | 2 | 10 | 🟡 Medium |
| UC_0200 | 2 | 2 | 3 | 1 | 2 | 10 | 🟡 Medium |
| UC_0201 | 3 | 1 | 2 | 2 | 2 | 10 | 🟡 Medium |
| UC_0202 | 1 | 1 | 1 | 1 | 2 | 6 | 🟢 Small |
| UC_0203 | 3 | 1 | 1 | 3 | 2 | 10 | 🟡 Medium |
| UC_0204 | 1 | 1 | 1 | 1 | 2 | 6 | 🟢 Small |
| UC_0205 | 3 | 1 | 1 | 1 | 2 | 8 | 🟡 Medium |
| UC_0206 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0207 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0208 | 1 | 1 | 1 | 1 | 2 | 6 | 🟢 Small |
| UC_0209 | 1 | 1 | 1 | 3 | 1 | 7 | 🟢 Small |
| UC_0210 | 1 | 1 | 2 | 1 | 2 | 7 | 🟢 Small |
| UC_0211 | 3 | 2 | 1 | 1 | 2 | 9 | 🟡 Medium |
| UC_0212 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0213 | 2 | 1 | 1 | 1 | 1 | 6 | 🟢 Small |
| UC_0214 | 3 | 2 | 3 | 3 | 1 | 12 | 🔴 Large |
| UC_0215 | 2 | 1 | 1 | 1 | 2 | 7 | 🟢 Small |
| UC_0216 | 3 | 1 | 1 | 1 | 2 | 8 | 🟡 Medium |
| UC_0217 | 2 | 3 | 1 | 1 | 2 | 9 | 🟡 Medium |
| UC_0218 | 1 | 3 | 2 | 1 | 3 | 10 | 🟡 Medium |
| UC_0219 | 1 | 3 | 2 | 3 | 3 | 12 | 🔴 Large |
| UC_0220 | 3 | 1 | 2 | 1 | 3 | 10 | 🟡 Medium |
| UC_0221 | 3 | 2 | 2 | 1 | 3 | 11 | 🟡 Medium |
| UC_0222 | 3 | 1 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0223 | 3 | 1 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0224 | 2 | 1 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0225 | 3 | 1 | 1 | 1 | 3 | 9 | 🟡 Medium |
| UC_0226 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0227 | 2 | 1 | 1 | 1 | 2 | 7 | 🟢 Small |
| UC_0228 | 3 | 1 | 2 | 1 | 1 | 8 | 🟡 Medium |
| UC_0229 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0230 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0231 | 2 | 1 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0232 | 2 | 2 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0233 | 2 | 3 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0234 | 2 | 3 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0235 | 1 | 2 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0236 | 1 | 2 | 1 | 1 | 3 | 8 | 🟡 Medium |
| UC_0237 | 1 | 2 | 2 | 1 | 3 | 9 | 🟡 Medium |
| UC_0238 | 1 | 1 | 2 | 1 | 1 | 6 | 🟢 Small |
| UC_0239 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0240 | 2 | 1 | 2 | 1 | 1 | 7 | 🟢 Small |
| UC_0241 | 3 | 1 | 2 | 2 | 1 | 9 | 🟡 Medium |
| UC_0242 | 3 | 2 | 1 | 1 | 1 | 8 | 🟡 Medium |
| UC_0243 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0244 | 3 | 2 | 2 | 1 | 1 | 9 | 🟡 Medium |
| UC_0245 | 3 | 3 | 2 | 1 | 2 | 11 | 🟡 Medium |
| UC_0246 | 1 | 1 | 1 | 1 | 1 | 5 | 🟢 Small |
| UC_0247 | 3 | 1 | 1 | 1 | 1 | 7 | 🟢 Small |
| UC_0248 | 3 | 1 | 1 | 1 | 2 | 8 | 🟡 Medium |