#!/usr/bin/env python3
"""
generate_catalog.py
Lit le fichier source Air Liquide et génère use_cases_catalog.xlsx.
Usage : python3 src/generate_catalog.py
"""
import sys
import hashlib
import re
from pathlib import Path
import pandas as pd

_SRC_DIR    = Path(__file__).parent
PROJECT_DIR = _SRC_DIR.parent
SOURCE_FILE = PROJECT_DIR / "assets" / "Advanced AI Champions - Action Monitoring.xlsx"
OUTPUT_FILE = PROJECT_DIR / "docs" / "use_cases_catalog.xlsx"
SOURCE_SHEET = "Use cases"

TOOL_MAP: dict[str, str] = {
    "gemini (prompts / gems)":     "Gemini Prompts/Gems",
    "gemini":                      "Gemini Prompts/Gems",
    "app script (app)":            "App Script",
    "app script":                  "App Script",
    "notebooklm":                  "NotebookLM",
    "advance coding":              "Advance Coding",
    "ai studio (app)":             "AI Studio",
    "ai studio":                   "AI Studio",
    "appsheet":                    "AppSheet",
    "workspace studio (ex flows)": "Workspace Studio",
    "workspace studio":            "Workspace Studio",
    "python on power bi (fabric)": "Python on Fabric",
    "python on fabric":            "Python on Fabric",
    "power bi (app)":              "Power BI",
    "power bi":                    "Power BI",
    "web app/internal platform":   "Web App/Platform",
    "web app":                     "Web App/Platform",
    "python on datastudio":        "Python on DataStudio",
}

TOOL_LEVEL: dict[str, str] = {
    "Gemini Prompts/Gems": "L1",
    "NotebookLM":          "L1",
    "AppSheet":            "L2",
    "Workspace Studio":    "L2",
    "App Script":          "L3",
    "AI Studio":           "L3",
    "Power BI":            "L3",
    "Advance Coding":      "L4",
    "Web App/Platform":    "L4",
    "Python on Fabric":    "L4",
    "Python on DataStudio":"L4",
}

FAMILY_RULES: list[tuple[str, list[str]]] = [
    ("F4", ["sensor","capteur","equipment","maintenance","predictive",
            "alarm","dcs","scada","aveva","plant","process control","monitoring equipment"]),
    ("F7", ["python","bigquery","fabric","datastudio","etl","pipeline",
            "data engineering","power bi","reporting","extraction","transformation"]),
    ("F2", ["dashboard","power bi","analytics","decision","forecast",
            "kpi","alert","bi ","analyse"]),
    ("F3", ["sfdc","salesforce","customer","visit","route","sales",
            "commercial","client","crm","churn"]),
    ("F1", ["translat","document","contract","report","summar",
            "résum","rédact","draft","email","letter","génér"]),
    ("F5", ["knowledge","faq","onboarding","formation","training",
            "chatbot","notebook","base de connaissance","wiki"]),
    ("F6", ["script","flow","automation","workflow","trigger",
            "schedule","appsheet","spreadsheet","workspace studio"]),
]

FAMILY_LABELS: dict[str, str] = {
    "F1": "Automatisation documentaire",
    "F2": "Assistant BI & décisionnel",
    "F3": "Customer & Sales Intelligence",
    "F4": "Monitoring & Maintenance industrielle",
    "F5": "Knowledge Management & Formation",
    "F6": "Automatisation de workflows internes",
    "F7": "Data Engineering & Reporting",
}

IT_ALERT_KW: list[str] = [
    "sfdc","salesforce","aveva","dcs","scada","sap","erp","oracle",
    "active directory","oauth","sso","api key","cloud run","vertex",
    "bigquery","database","sql","24/7","production server",
]

EXPORT_COLS: list[str] = [
    "UC_ID","Cluster","Job Family","Family","Family_Label","Complexity_Tier",
    "Score_Total","Score_Integration","Score_Scope","Score_Data","Score_AI",
    "Score_Economic","Stage","Scope of the Use Case","Economical Impact","Tools",
    "Tools_Tags","Nb_Tools","Max_Tool_Level","IT_Flag","IT_Attention",
    "Use Case Description (Long)",
]


def make_uc_id(text: str) -> str:
    return hashlib.md5(str(text).strip().lower().encode()).hexdigest()[:8].upper()


def parse_tools(raw: str) -> list[str]:
    if not raw or str(raw) in ("nan", ""):
        return []
    tags: set[str] = set()
    for part in re.split(r",", str(raw)):
        part = part.strip().lower()
        for key, val in TOOL_MAP.items():
            if key in part:
                tags.add(val)
                break
    return sorted(tags)


def max_tool_level(tags: list[str]) -> str:
    levels = [TOOL_LEVEL.get(t, "L1") for t in tags]
    return max(levels) if levels else "L1"


def score_integration(nb_tools: int, level: str) -> int:
    if level == "L4" or nb_tools >= 4:
        return 3
    if level == "L3" or nb_tools >= 2:
        return 2
    return 1


def score_scope(scope: str) -> int:
    s = str(scope).lower()
    if "group" in s:
        return 3
    if "cluster" in s or "country" in s:
        return 2
    return 1


def score_data(tags: list[str], desc: str) -> int:
    d = str(desc).lower()
    industrial = ["sfdc","salesforce","aveva","dcs","scada","sap",
                  "real-time","sensor","capteur","erp","oracle"]
    connected  = ["power bi","sheets","bigquery","database","api","pipeline","dataflow"]
    if any(k in d for k in industrial):
        return 3
    if any(k in d for k in connected) or "Python on Fabric" in tags:
        return 2
    return 1


def score_ai(tags: list[str], desc: str) -> int:
    d = str(desc).lower()
    advanced = ["agent","multi-step","fine-tun","ml model","machine learning",
                "rag","vertex","embedding"]
    medium   = ["api","ai studio","notebooklm","rag"]
    if any(k in d for k in advanced):
        return 3
    if "AI Studio" in tags or any(k in d for k in medium):
        return 2
    return 1


def score_economic(impact: str) -> int:
    s = str(impact).lower()
    if "revenue growth" in s or "sustainability" in s:
        return 3
    if "cost reduction" in s:
        return 2
    return 1


def classify_family(desc: str, tags: list[str], job_family: str) -> str:
    combined = f"{desc} {' '.join(tags)} {job_family}".lower()
    for fam, keywords in FAMILY_RULES:
        if any(k in combined for k in keywords):
            return fam
    return "F1"


def it_attention(desc: str, tags: list[str], tier: str) -> str:
    combined = f"{desc} {' '.join(tags)}".lower()
    flags = [k for k in IT_ALERT_KW if k in combined]
    if tier == "Large":
        flags.append("Large tier")
    return " | ".join(flags)


def complexity_tier(score: int) -> str:
    if score <= 7:
        return "Small"
    if score <= 11:
        return "Medium"
    return "Large"


def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline complet d'enrichissement. Fonction pure — ne touche pas le filesystem."""
    df = df.copy()
    df.replace("#REF!", "N/A", inplace=True)
    df = df[df["Use Case Description (Long)"].notna()]
    df = df[df["Use Case Description (Long)"].astype(str).str.strip() != ""]
    df = df.reset_index(drop=True)

    df["Stage"]                 = df["Stage"].fillna("Non renseigné").astype(str).str.strip()
    df["Economical Impact"]     = df["Economical Impact"].fillna("Non évalué").astype(str).str.strip()
    df["Cluster"]               = df["Cluster"].fillna("N/A").astype(str).str.strip()
    df["Job Family"]            = df["Job Family"].fillna("N/A").astype(str).str.strip()
    df["Scope of the Use Case"] = df["Scope of the Use Case"].fillna("N/A").astype(str).str.strip()
    df["Tools"]                 = df["Tools"].fillna("").astype(str).str.strip()

    hash_to_id: dict[str, str] = {}
    counter = [1]
    def get_uc_id(text: str) -> str:
        h = make_uc_id(text)
        if h not in hash_to_id:
            hash_to_id[h] = f"UC_{counter[0]:04d}"
            counter[0] += 1
        return hash_to_id[h]
    df["UC_ID"] = df["Use Case Description (Long)"].apply(get_uc_id)

    df["Tools_Tags"]     = df["Tools"].apply(parse_tools)
    df["Nb_Tools"]       = df["Tools_Tags"].apply(len)
    df["Max_Tool_Level"] = df["Tools_Tags"].apply(max_tool_level)

    df["Score_Integration"] = df.apply(
        lambda r: score_integration(r["Nb_Tools"], r["Max_Tool_Level"]), axis=1)
    df["Score_Scope"]       = df["Scope of the Use Case"].apply(score_scope)
    df["Score_Data"]        = df.apply(
        lambda r: score_data(r["Tools_Tags"], r["Use Case Description (Long)"]), axis=1)
    df["Score_AI"]          = df.apply(
        lambda r: score_ai(r["Tools_Tags"], r["Use Case Description (Long)"]), axis=1)
    df["Score_Economic"]    = df["Economical Impact"].apply(score_economic)
    df["Score_Total"]       = df[["Score_Integration","Score_Scope","Score_Data",
                                  "Score_AI","Score_Economic"]].sum(axis=1)
    df["Complexity_Tier"]   = df["Score_Total"].apply(complexity_tier)

    df["Family"]       = df.apply(
        lambda r: classify_family(
            r["Use Case Description (Long)"], r["Tools_Tags"], r["Job Family"]), axis=1)
    df["Family_Label"] = df["Family"].map(FAMILY_LABELS)

    df["IT_Attention"] = df.apply(
        lambda r: it_attention(
            r["Use Case Description (Long)"], r["Tools_Tags"], r["Complexity_Tier"]), axis=1)
    df["IT_Flag"] = df["IT_Attention"].apply(lambda x: "⚠️ IT" if x else "")

    df["Tools_Tags"] = df["Tools_Tags"].apply(lambda x: ", ".join(x) if x else "")

    return df[EXPORT_COLS]


def main(source: Path = SOURCE_FILE, output: Path = OUTPUT_FILE) -> None:
    print(f"📂 Lecture : {source}")
    if not source.exists():
        print(f"❌ Fichier source introuvable : {source}")
        sys.exit(1)

    df_raw = pd.read_excel(source, sheet_name=SOURCE_SHEET, header=0)
    df_out = process_dataframe(df_raw)

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_out.to_excel(writer, sheet_name="Catalogue", index=False)

    print(f"\n✅ Export : {output}")
    print(f"   Lignes  : {len(df_out)}")
    print(f"   Colonnes: {len(EXPORT_COLS)}")
    tier_counts = df_out["Complexity_Tier"].value_counts().to_dict()
    fam_counts  = df_out["Family"].value_counts().to_dict()
    it_count    = (df_out["IT_Flag"] != "").sum()
    print(f"\n📊 Résumé rapide :")
    print(f"   Tiers    : {tier_counts}")
    print(f"   Familles : {fam_counts}")
    print(f"   ⚠️ IT    : {it_count} use cases")
    print(f"\n➡️  Prochaine étape : uploader {output.name} dans Google Drive")


if __name__ == "__main__":
    main()
