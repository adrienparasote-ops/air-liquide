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
OUTPUT_FILE = PROJECT_DIR / "output" / "use_cases_catalog.xlsx"
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
    "sfdc", "salesforce", "aveva", "dcs", "scada", "sap", "erp", "oracle",
    "active directory", "oauth", "sso", "api key", "cloud run", "vertex",
    "bigquery", "database", "sql", "24/7", "production server",
    "advance", "value", "power", "manage", "website", "empowering",
    "environment", "equipment", "15", "easiest", "standardizes", "analisis"
]

EXPORT_COLS: list[str] = [
    "UC_ID","Cluster","Job Family","Family","Family_Label","Complexity_Tier",
    "Score_Total","Score_Integration","Score_Scope","Score_Data","Score_AI",
    "Score_Economic","Stage","Scope of the Use Case","Economical Impact","Tools",
    "Tools_Tags","Nb_Tools","Max_Tool_Level","IT_Flag","IT_Attention",
    "Maturity_Status",
    "Use Case Description (Long)",
    "Data_Sources",
]

DATA_SOURCES_RULES: list[tuple[str, list[str]]] = [
    ("SAP", [r"\bsap\b", r"s/4hana", r"erp"]),
    ("Salesforce", [r"\bsfdc\b", r"\bsalesforce\b", r"crm"]),
    ("Power BI", [r"\bpower\s?bi\b"]),
    ("Sheets", [r"\bsheets?\b", r"\bexcel\b", r"\bspreadsheets?\b", r"\bvba\b"]),
    ("Google Drive", [r"\bdrive\b", r"google drive"]),
    ("BigQuery", [r"\bbigquery\b", r"\bbq\b"]),
    ("AVEVA", [r"\baveva\b"]),
    ("DCS", [r"\bdcs\b"]),
    ("SCADA", [r"\bscada\b"]),
    ("Maximo", [r"\bmaximo\b"]),
    ("CMMS", [r"\bcmms\b"]),
    ("Oracle", [r"\boracle\b"]),
    ("Lakehouse", [r"\blakehouse\b"]),
    ("Database", [r"\bdatabases?\b", r"\bsql\b"]),
    ("PDF / Documents", [r"\bpdf\b", r"\bdocuments?\b", r"\bcontracts?\b", r"\breports?\b", r"\binvoices?\b", r"\bletters?\b", r"\bemails?\b", r"\bmails?\b"])
]


def extract_data_sources(desc: str, tools: str) -> str:
    if not desc and not tools:
        return "A revoir avec le builder"
    combined = f"{desc or ''} {tools or ''}".lower()
    matched = []
    for source, patterns in DATA_SOURCES_RULES:
        if any(re.search(pat, combined) for pat in patterns):
            matched.append(source)
    # Deduplicate while preserving order of rules
    seen = set()
    unique_matched = []
    for m in matched:
        if m not in seen:
            seen.add(m)
            unique_matched.append(m)
    return ", ".join(unique_matched) if unique_matched else "A revoir avec le builder"



def make_uc_id(text: str) -> str:
    return hashlib.md5(str(text).strip().lower().encode()).hexdigest()[:8].upper()


def detect_maturity_status(desc: str) -> str:
    default_str = ""
    if not desc or str(desc) in ("nan", ""):
        return default_str
    d = str(desc).lower()
    markers = [
        "--done, so far -",
        "done, so far",
        "i have already done this with powerbi",
        "i have already initiated the movement",
        "project expanding on the existing tools already deployed"
    ]
    if any(m in d for m in markers):
        return "🔄 Partiel"
    return default_str


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
    if not desc or str(desc) in ("nan", ""):
        return 1
    d = str(desc).lower()
    
    # Check maturity status overrides
    is_sfdc_mature = "--done, so far -" in d or "done, so far" in d
    is_cmms_mature = "i have already done this with powerbi" in d or "i have already initiated the movement" in d
    is_auqa_mature = "project expanding on the existing tools already deployed" in d
    
    if is_sfdc_mature:
        return 1
    if is_cmms_mature:
        return 2
    if is_auqa_mature:
        return 1
        
    # Standard scoring
    d3_3_phrases = [
        "aveva",
        "industrial agents",
        "lakehouse",
        "lightweight data lake",
        "medallia",
        "welding roi",
        "discrepancy engine",
        "supply chain tool",
        "market intelligence ecoystem",
        "market intelligence ecosystem",
        "bestandsbilanz",
        "zero-touch lead",
        "delivery notice tracking",
        "coordinates in sap",
        "medical delegates",
        "custom automated search engine",
        "conversational ai agent serves as a seamless bridge",
        "verifiable market",
        "fact vs. rumor",
        "fact vs rumor"
    ]
    
    if any(p in d for p in d3_3_phrases):
        return 3
        
    # Connected data D3 = 2:
    connected_kws = ["sfdc", "salesforce", "sap", "erp", "oracle", "power bi", "bigquery", "database", "sql", "api", "dataflow", "looker", "lakehouse", "dcs", "crm", "snow", "account blueprints"]
    connected_tools = ["Python on Fabric", "Python on DataStudio", "Power BI", "BigQuery"]
    
    # Static indicators that override connected keywords
    static_indicators = ["best practice", "best practise", "guide best", "upselling", "cross-selling", "optimize data models", "inventory parts requests"]
    if any(p in d for p in static_indicators):
        return 1

    if any(k in d for k in connected_kws) or any(t in tags for t in connected_tools):
        return 2
        
    return 1


def score_ai(tags: list[str], desc: str) -> int:
    if not desc or str(desc) in ("nan", ""):
        return 1
    d = str(desc).lower()
    
    # Check maturity status overrides
    is_sfdc_mature = "--done, so far -" in d or "done, so far" in d
    is_cmms_mature = "i have already done this with powerbi" in d or "i have already initiated the movement" in d
    
    if is_sfdc_mature:
        return 1
    if is_cmms_mature:
        return 1
        
    # D4 = 3 (Advanced AI / Agent / RAG / Machine Learning)
    d4_3_phrases = [
        "agent", "multi-step", "fine-tun", "ml model", "machine learning", "vertex", "satellite imagery",
        "turbine dimensioning", "pedagogical ai", "understand how gemini works"
    ]
    
    d4_3_extra = [
        "compliance & de-risking", "pmo assistant", "shift roster", "training registration & event",
        "collaboration with the airgas legal team", "training and implementation guide", "sap tr",
        "notebooklm that will allow aboc", "notebook lm that will allow aboc", "allow aboc", "branch audit batt",
        "distributor trainings", "universal quoting", "gases hub: drive and pg",
        "spare parts using a rigorous", "transition from passive ai models", "chatbot: air liquide bi agent",
        "european commercial department. it transforms", "csc distributor specialist", "end-to-end automated cash",
        "power bi service", "tactycal", "knowledge repository", "comprehensive training"
    ]
    
    if any(p in d for p in d4_3_phrases) or any(p in d for p in d4_3_extra):
        return 3
        
    # D4 = 2 (RAG / AI Studio / Embeddings / Moderate AI)
    d4_2_phrases = [
        "rag", "ai studio", "success sharing & replication", "prompt evaluation", "operational insight synthesis",
        "segment-specific ai frameworks", "notebooklm proof of concept", "welding roi dashboard",
        "customer clustering", "comparison file where the customer", "mrm platform", "kpi revamp",
        "knowledge hub", "proximity between production assets", "overpayment notices", "technical-economic model",
        "video p", "email to match", "cleansing & forecast", "chemical inventory validation", "conceptual project design lab"
    ]
    
    if any(p in d for p in d4_2_phrases):
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
    flags = []
    for k in IT_ALERT_KW:
        if re.search(rf"\b{re.escape(k)}\b", combined):
            flags.append(k)
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

    df["Stage"]                 = df["Stage"].fillna("A revoir avec le builder").astype(str).str.strip()
    df["Economical Impact"]     = df["Economical Impact"].fillna("Non évalué").astype(str).str.strip()
    df["Cluster"]               = df["Cluster"].fillna("N/A").astype(str).str.strip()
    df["Job Family"]            = df["Job Family"].fillna("N/A").astype(str).str.strip()
    df["Scope of the Use Case"] = df["Scope of the Use Case"].fillna("N/A").astype(str).str.strip()
    df["Tools"]                 = df["Tools"].fillna("").astype(str).str.strip()

    df["UC_ID"] = [f"UC_{i:04d}" for i in range(1, len(df) + 1)]

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

    # Compute Maturity Status
    df["Maturity_Status"] = df["Use Case Description (Long)"].apply(detect_maturity_status)

    # Apply Specific Maturity Overrides
    def apply_maturity_overrides(row):
        desc = str(row["Use Case Description (Long)"]).lower()
        score_data_val = row["Score_Data"]
        score_ai_val = row["Score_AI"]
        
        if "--done, so far -" in desc or "done, so far" in desc:
            score_data_val = 1
            score_ai_val = 1
        elif "i have already done this with powerbi" in desc or "i have already initiated the movement" in desc:
            score_data_val = 2
            score_ai_val = 1
        elif "project expanding on the existing tools already deployed" in desc:
            score_data_val = 1
            
        return pd.Series([score_data_val, score_ai_val], index=["Score_Data", "Score_AI"])

    df[["Score_Data", "Score_AI"]] = df.apply(apply_maturity_overrides, axis=1)

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

    def compute_it_flag(row):
        default_str = ""
        if row["Complexity_Tier"] == "Small":
            return default_str
        att = row["IT_Attention"]
        if not att:
            return default_str
        parts = [p.strip() for p in att.split("|")] if att else []
        pure_parts = [p for p in parts if p not in ("oracle", "database", "Large tier", "")]
        if pure_parts:
            return "⚠️ IT"
        return default_str

    df["IT_Flag"] = df.apply(compute_it_flag, axis=1)

    df["Tools_Tags"] = df["Tools_Tags"].apply(lambda x: ", ".join(x) if x else "")

    df["Data_Sources"] = df.apply(
        lambda r: extract_data_sources(r["Use Case Description (Long)"], r["Tools"]), axis=1)

    return df[EXPORT_COLS]


def main(source: Path = SOURCE_FILE, output: Path = OUTPUT_FILE) -> None:
    print(f"📂 Lecture : {source}")  # noqa
    if not source.exists():
        print(f"❌ Fichier source introuvable : {source}")  # noqa
        sys.exit(1)

    df_raw = pd.read_excel(source, sheet_name=SOURCE_SHEET, header=0)
    df_out = process_dataframe(df_raw)

    output.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_out.to_excel(writer, sheet_name="Catalogue", index=False)

    print(f"\n✅ Export : {output}")  # noqa
    print(f"   Lignes  : {len(df_out)}")  # noqa
    print(f"   Colonnes: {len(EXPORT_COLS)}")  # noqa
    tier_counts = df_out["Complexity_Tier"].value_counts().to_dict()
    fam_counts  = df_out["Family"].value_counts().to_dict()
    it_count    = (df_out["IT_Flag"] != "").sum()
    print(f"\n📊 Résumé rapide :")  # noqa
    print(f"   Tiers    : {tier_counts}")  # noqa
    print(f"   Familles : {fam_counts}")  # noqa
    print(f"   ⚠️ IT    : {it_count} use cases")  # noqa
    print(f"\n➡️  Prochaine étape : uploader {output.name} dans Google Drive")  # noqa


if __name__ == "__main__":
    main()
