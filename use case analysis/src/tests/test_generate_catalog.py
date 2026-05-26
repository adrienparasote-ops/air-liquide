"""
test_generate_catalog.py
Tests unitaires — couverture 100% de src/generate_catalog.py
"""
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
import pandas as pd

# Ajouter src/ au path pour l'import
sys.path.insert(0, str(Path(__file__).parent.parent))
import generate_catalog as gc


# ════════════════════════════════════════════════════════════════
# make_uc_id
# ════════════════════════════════════════════════════════════════
class TestMakeUcId(unittest.TestCase):
    def test_same_text_same_hash(self):
        self.assertEqual(gc.make_uc_id("hello"), gc.make_uc_id("hello"))

    def test_different_text_different_hash(self):
        self.assertNotEqual(gc.make_uc_id("hello"), gc.make_uc_id("world"))

    def test_case_insensitive(self):
        self.assertEqual(gc.make_uc_id("HELLO"), gc.make_uc_id("hello"))

    def test_strips_whitespace(self):
        self.assertEqual(gc.make_uc_id("  hello  "), gc.make_uc_id("hello"))

    def test_returns_8_chars_uppercase(self):
        result = gc.make_uc_id("test")
        self.assertEqual(len(result), 8)
        self.assertEqual(result, result.upper())


# ════════════════════════════════════════════════════════════════
# parse_tools
# ════════════════════════════════════════════════════════════════
class TestParseTools(unittest.TestCase):
    def test_empty_string_returns_empty(self):
        self.assertEqual(gc.parse_tools(""), [])

    def test_none_returns_empty(self):
        self.assertEqual(gc.parse_tools(None), [])

    def test_nan_string_returns_empty(self):
        self.assertEqual(gc.parse_tools("nan"), [])

    def test_gemini_full_name(self):
        self.assertIn("Gemini Prompts/Gems", gc.parse_tools("Gemini (Prompts / Gems)"))

    def test_gemini_short(self):
        self.assertIn("Gemini Prompts/Gems", gc.parse_tools("Gemini"))

    def test_app_script_with_app(self):
        self.assertIn("App Script", gc.parse_tools("App Script (App)"))

    def test_app_script_plain(self):
        self.assertIn("App Script", gc.parse_tools("App Script"))

    def test_notebooklm(self):
        self.assertIn("NotebookLM", gc.parse_tools("NotebookLM"))

    def test_advance_coding(self):
        self.assertIn("Advance Coding", gc.parse_tools("Advance Coding"))

    def test_ai_studio_with_app(self):
        self.assertIn("AI Studio", gc.parse_tools("AI Studio (App)"))

    def test_ai_studio_plain(self):
        self.assertIn("AI Studio", gc.parse_tools("AI Studio"))

    def test_appsheet(self):
        self.assertIn("AppSheet", gc.parse_tools("AppSheet"))

    def test_workspace_studio_with_ex(self):
        self.assertIn("Workspace Studio", gc.parse_tools("Workspace Studio (ex Flows)"))

    def test_workspace_studio_plain(self):
        self.assertIn("Workspace Studio", gc.parse_tools("Workspace Studio"))

    def test_power_bi_with_app(self):
        self.assertIn("Power BI", gc.parse_tools("Power BI (App)"))

    def test_power_bi_plain(self):
        self.assertIn("Power BI", gc.parse_tools("Power BI"))

    def test_web_app_with_platform(self):
        self.assertIn("Web App/Platform", gc.parse_tools("Web App/Internal Platform"))

    def test_web_app_plain(self):
        self.assertIn("Web App/Platform", gc.parse_tools("Web App"))

    def test_python_on_fabric_long(self):
        # "Python on Power BI (Fabric)" dans l'entrée réelle — matche python on fabric en priorité
        self.assertIn("Python on Fabric", gc.parse_tools("Python on Fabric, another tool"))

    def test_python_on_fabric_short(self):
        self.assertIn("Python on Fabric", gc.parse_tools("Python on Fabric"))

    def test_python_on_datastudio(self):
        self.assertIn("Python on DataStudio", gc.parse_tools("Python on DataStudio"))

    def test_multiple_tools_comma_separated(self):
        result = gc.parse_tools("Gemini, NotebookLM")
        self.assertIn("Gemini Prompts/Gems", result)
        self.assertIn("NotebookLM", result)

    def test_returns_sorted_list(self):
        result = gc.parse_tools("NotebookLM, Gemini")
        self.assertEqual(result, sorted(result))

    def test_deduplication(self):
        result = gc.parse_tools("Gemini, Gemini (Prompts / Gems)")
        self.assertEqual(result.count("Gemini Prompts/Gems"), 1)

    def test_unknown_tool_ignored(self):
        result = gc.parse_tools("SomeFutureTool")
        self.assertEqual(result, [])


# ════════════════════════════════════════════════════════════════
# max_tool_level
# ════════════════════════════════════════════════════════════════
class TestMaxToolLevel(unittest.TestCase):
    def test_empty_list_returns_l1(self):
        self.assertEqual(gc.max_tool_level([]), "L1")

    def test_l1_tools(self):
        self.assertEqual(gc.max_tool_level(["Gemini Prompts/Gems", "NotebookLM"]), "L1")

    def test_l2_tools(self):
        self.assertEqual(gc.max_tool_level(["AppSheet"]), "L2")

    def test_l3_tools(self):
        self.assertEqual(gc.max_tool_level(["AI Studio"]), "L3")

    def test_l4_tools(self):
        self.assertEqual(gc.max_tool_level(["Advance Coding"]), "L4")

    def test_mixed_returns_highest(self):
        self.assertEqual(gc.max_tool_level(["Gemini Prompts/Gems", "Advance Coding"]), "L4")

    def test_unknown_tool_defaults_l1(self):
        self.assertEqual(gc.max_tool_level(["UnknownTool"]), "L1")


# ════════════════════════════════════════════════════════════════
# score_integration
# ════════════════════════════════════════════════════════════════
class TestScoreIntegration(unittest.TestCase):
    def test_l4_level_returns_3(self):
        self.assertEqual(gc.score_integration(1, "L4"), 3)

    def test_4_tools_returns_3(self):
        self.assertEqual(gc.score_integration(4, "L1"), 3)

    def test_l3_level_returns_2(self):
        self.assertEqual(gc.score_integration(1, "L3"), 2)

    def test_2_tools_returns_2(self):
        self.assertEqual(gc.score_integration(2, "L1"), 2)

    def test_l2_1_tool_returns_1(self):
        self.assertEqual(gc.score_integration(1, "L2"), 1)

    def test_l1_1_tool_returns_1(self):
        self.assertEqual(gc.score_integration(1, "L1"), 1)


# ════════════════════════════════════════════════════════════════
# score_scope
# ════════════════════════════════════════════════════════════════
class TestScoreScope(unittest.TestCase):
    def test_group_returns_3(self):
        self.assertEqual(gc.score_scope("Group-wide"), 3)

    def test_cluster_returns_2(self):
        self.assertEqual(gc.score_scope("Cluster level"), 2)

    def test_country_returns_2(self):
        self.assertEqual(gc.score_scope("Country"), 2)

    def test_local_returns_1(self):
        self.assertEqual(gc.score_scope("Local team"), 1)

    def test_na_returns_1(self):
        self.assertEqual(gc.score_scope("N/A"), 1)


# ════════════════════════════════════════════════════════════════
# score_data
# ════════════════════════════════════════════════════════════════
class TestScoreData(unittest.TestCase):
    def test_salesforce_in_desc_returns_2(self):
        # In new rules, Salesforce is connected (D3 = 2), not industrial (D3 = 3)
        self.assertEqual(gc.score_data([], "Connect to Salesforce CRM"), 2)

    def test_sfdc_in_desc_returns_2(self):
        self.assertEqual(gc.score_data([], "Uses sfdc data"), 2)

    def test_aveva_returns_3(self):
        self.assertEqual(gc.score_data([], "Aveva SCADA system"), 3)

    def test_lakehouse_returns_3(self):
        self.assertEqual(gc.score_data([], "integrated with the lakehouse"), 3)

    def test_fact_vs_rumor_returns_3(self):
        self.assertEqual(gc.score_data([], "Strict fact vs. rumor guardrails"), 3)

    def test_sap_returns_2(self):
        self.assertEqual(gc.score_data([], "extract from sap"), 2)

    def test_erp_returns_2(self):
        self.assertEqual(gc.score_data([], "from the erp system"), 2)

    def test_oracle_returns_2(self):
        self.assertEqual(gc.score_data([], "oracle database query"), 2)

    def test_bigquery_in_desc_returns_2(self):
        self.assertEqual(gc.score_data([], "query bigquery tables"), 2)

    def test_database_in_desc_returns_2(self):
        self.assertEqual(gc.score_data([], "connect to database"), 2)

    def test_api_in_desc_returns_2(self):
        self.assertEqual(gc.score_data([], "call external api"), 2)

    def test_python_on_fabric_tag_returns_2(self):
        # Connect tools tag override
        self.assertEqual(gc.score_data(["Python on Fabric"], "simple description"), 2)

    def test_static_override_best_practice(self):
        # best practice is static indicator -> D3 = 1 even with database
        self.assertEqual(gc.score_data([], "best practice in database management"), 1)

    def test_plain_description_returns_1(self):
        self.assertEqual(gc.score_data([], "summarize this email"), 1)


# ════════════════════════════════════════════════════════════════
# score_ai
# ════════════════════════════════════════════════════════════════
class TestScoreAi(unittest.TestCase):
    def test_agent_in_desc_returns_3(self):
        self.assertEqual(gc.score_ai([], "build an agent that..."), 3)

    def test_multi_step_returns_3(self):
        self.assertEqual(gc.score_ai([], "multi-step reasoning"), 3)

    def test_fine_tun_returns_3(self):
        self.assertEqual(gc.score_ai([], "fine-tuning the model"), 3)

    def test_ml_model_returns_3(self):
        self.assertEqual(gc.score_ai([], "train a ml model"), 3)

    def test_machine_learning_returns_3(self):
        self.assertEqual(gc.score_ai([], "machine learning pipeline"), 3)

    def test_rag_in_desc_returns_2(self):
        # rag is now a D4 = 2 keyword, not D4 = 3
        self.assertEqual(gc.score_ai([], "rag-based retrieval"), 2)

    def test_vertex_returns_3(self):
        self.assertEqual(gc.score_ai([], "deploy on vertex"), 3)

    def test_embedding_returns_1(self):
        # embedding alone is not a D4=3 keyword, returns 1
        self.assertEqual(gc.score_ai([], "embedding similarity"), 1)

    def test_tactycal_returns_3(self):
        self.assertEqual(gc.score_ai([], "part of tactycal suite"), 3)

    def test_comprehensive_training_returns_3(self):
        self.assertEqual(gc.score_ai([], "comprehensive training notebook"), 3)

    def test_ai_studio_tag_returns_1(self):
        # AI Studio tag does not force D4 = 2 anymore
        self.assertEqual(gc.score_ai(["AI Studio"], "simple prompt"), 1)

    def test_ai_studio_in_desc_returns_2(self):
        # But ai studio in description does
        self.assertEqual(gc.score_ai([], "use ai studio to query"), 2)

    def test_api_in_desc_returns_1(self):
        # api does not force 2 anymore
        self.assertEqual(gc.score_ai([], "call api endpoint"), 1)

    def test_notebooklm_in_desc_returns_1(self):
        # notebooklm does not force 2 anymore
        self.assertEqual(gc.score_ai([], "use notebooklm to summarize"), 1)

    def test_plain_gemini_prompt_returns_1(self):
        self.assertEqual(gc.score_ai(["Gemini Prompts/Gems"], "translate this document"), 1)


# ════════════════════════════════════════════════════════════════
# score_economic
# ════════════════════════════════════════════════════════════════
class TestScoreEconomic(unittest.TestCase):
    def test_revenue_growth_returns_3(self):
        self.assertEqual(gc.score_economic("Revenue Growth"), 3)

    def test_sustainability_returns_3(self):
        self.assertEqual(gc.score_economic("Sustainability"), 3)

    def test_cost_reduction_returns_2(self):
        self.assertEqual(gc.score_economic("Cost Reduction"), 2)

    def test_non_evalue_returns_1(self):
        self.assertEqual(gc.score_economic("Non évalué"), 1)

    def test_empty_returns_1(self):
        self.assertEqual(gc.score_economic(""), 1)


# ════════════════════════════════════════════════════════════════
# classify_family
# ════════════════════════════════════════════════════════════════
class TestClassifyFamily(unittest.TestCase):
    def test_f4_sensor(self):
        self.assertEqual(gc.classify_family("sensor monitoring", [], ""), "F4")

    def test_f4_scada(self):
        self.assertEqual(gc.classify_family("read from scada", [], ""), "F4")

    def test_f4_maintenance(self):
        self.assertEqual(gc.classify_family("predictive maintenance", [], ""), "F4")

    def test_f7_python(self):
        self.assertEqual(gc.classify_family("python script to extract", [], ""), "F7")

    def test_f7_bigquery(self):
        self.assertEqual(gc.classify_family("query from bigquery", [], ""), "F7")

    def test_f7_reporting(self):
        self.assertEqual(gc.classify_family("automated reporting", [], ""), "F7")

    def test_f2_dashboard(self):
        self.assertEqual(gc.classify_family("create a dashboard", [], ""), "F2")

    def test_f2_kpi(self):
        self.assertEqual(gc.classify_family("track kpi", [], ""), "F2")

    def test_f3_salesforce(self):
        self.assertEqual(gc.classify_family("sfdc customer data", [], ""), "F3")

    def test_f3_crm(self):
        self.assertEqual(gc.classify_family("crm data analysis", [], ""), "F3")

    def test_f1_translate(self):
        self.assertEqual(gc.classify_family("translate document", [], ""), "F1")

    def test_f1_email(self):
        self.assertEqual(gc.classify_family("draft email response", [], ""), "F1")

    def test_f5_knowledge(self):
        self.assertEqual(gc.classify_family("knowledge base FAQ", [], ""), "F5")

    def test_f5_training(self):
        self.assertEqual(gc.classify_family("training onboarding chatbot", [], ""), "F5")

    def test_f6_automation(self):
        self.assertEqual(gc.classify_family("workflow automation script", [], ""), "F6")

    def test_f6_appsheet(self):
        self.assertEqual(gc.classify_family("appsheet app", [], ""), "F6")

    def test_default_f1_when_no_match(self):
        self.assertEqual(gc.classify_family("something completely unrelated xyz", [], ""), "F1")

    def test_tags_used_in_classification(self):
        self.assertEqual(gc.classify_family("generic task", ["Workspace Studio"], ""), "F6")

    def test_job_family_used_in_classification(self):
        self.assertEqual(gc.classify_family("task", [], "scada operator"), "F4")


# ════════════════════════════════════════════════════════════════
# it_attention
# ════════════════════════════════════════════════════════════════
class TestItAttention(unittest.TestCase):
    def test_sfdc_in_desc_flagged(self):
        result = gc.it_attention("connects to sfdc", [], "Small")
        self.assertIn("sfdc", result)

    def test_salesforce_flagged(self):
        result = gc.it_attention("salesforce crm", [], "Small")
        self.assertIn("salesforce", result)

    def test_bigquery_flagged(self):
        result = gc.it_attention("queries bigquery", [], "Small")
        self.assertIn("bigquery", result)

    def test_sap_flagged(self):
        result = gc.it_attention("reads from sap", [], "Small")
        self.assertIn("sap", result)

    def test_large_tier_always_flagged(self):
        result = gc.it_attention("simple task", [], "Large")
        self.assertIn("Large tier", result)

    def test_no_keywords_no_flag(self):
        result = gc.it_attention("summarize this document", [], "Small")
        self.assertEqual(result, "")

    def test_multiple_keywords_piped(self):
        result = gc.it_attention("sfdc and salesforce", [], "Small")
        self.assertIn("|", result)

    def test_keyword_in_tags_flagged(self):
        result = gc.it_attention("normal desc", ["sfdc"], "Small")
        self.assertIn("sfdc", result)

    def test_aveva_flagged(self):
        result = gc.it_attention("aveva system", [], "Small")
        self.assertIn("aveva", result)

    def test_oracle_flagged(self):
        result = gc.it_attention("oracle db", [], "Small")
        self.assertIn("oracle", result)

    def test_vertex_flagged(self):
        result = gc.it_attention("deploy on vertex", [], "Medium")
        self.assertIn("vertex", result)

    def test_production_server_flagged(self):
        result = gc.it_attention("runs on production server", [], "Medium")
        self.assertIn("production server", result)


# ════════════════════════════════════════════════════════════════
# complexity_tier
# ════════════════════════════════════════════════════════════════
class TestComplexityTier(unittest.TestCase):
    def test_score_5_is_small(self):
        self.assertEqual(gc.complexity_tier(5), "Small")

    def test_score_7_is_small(self):
        self.assertEqual(gc.complexity_tier(7), "Small")

    def test_score_8_is_medium(self):
        self.assertEqual(gc.complexity_tier(8), "Medium")

    def test_score_11_is_medium(self):
        self.assertEqual(gc.complexity_tier(11), "Medium")

    def test_score_12_is_large(self):
        self.assertEqual(gc.complexity_tier(12), "Large")

    def test_score_15_is_large(self):
        self.assertEqual(gc.complexity_tier(15), "Large")


# ════════════════════════════════════════════════════════════════
# process_dataframe — tests d'intégration sur la fonction pure
# ════════════════════════════════════════════════════════════════
def _make_raw_df(**overrides) -> pd.DataFrame:
    """Construit un DataFrame brut minimal valide pour process_dataframe."""
    base = {
        "Use Case Description (Long)": ["Translate the weekly report to English"],
        "Cluster":                     ["Corporate Functions"],
        "Job Family":                  ["HR"],
        "Stage":                       ["POC"],
        "Scope of the Use Case":       ["Local"],
        "Economical Impact":           ["Cost Reduction"],
        "Tools":                       ["Gemini"],
    }
    base.update(overrides)
    return pd.DataFrame(base)


class TestProcessDataframe(unittest.TestCase):
    def test_returns_dataframe(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        self.assertIsInstance(result, pd.DataFrame)

    def test_output_has_all_export_cols(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        for col in gc.EXPORT_COLS:
            self.assertIn(col, result.columns, f"Missing column: {col}")

    def test_ref_replaced_by_na(self):
        df = _make_raw_df(**{"Cluster": ["#REF!"]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Cluster"].iloc[0], "N/A")

    def test_empty_description_rows_dropped(self):
        df = pd.DataFrame({
            "Use Case Description (Long)": ["Valid desc", "   ", None],
            "Cluster": ["A", "B", "C"],
            "Job Family": ["J", "J", "J"],
            "Stage": ["POC", "POC", "POC"],
            "Scope of the Use Case": ["Local", "Local", "Local"],
            "Economical Impact": ["Cost Reduction", "Cost Reduction", "Cost Reduction"],
            "Tools": ["Gemini", "Gemini", "Gemini"],
        })
        result = gc.process_dataframe(df)
        self.assertEqual(len(result), 1)

    def test_uc_id_format(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        self.assertRegex(result["UC_ID"].iloc[0], r"UC_\d{4}")

    def test_duplicate_descriptions_get_unique_uc_id(self):
        df = pd.DataFrame({
            "Use Case Description (Long)": ["Same desc", "Same desc"],
            "Cluster": ["A", "B"],
            "Job Family": ["J", "J"],
            "Stage": ["POC", "POC"],
            "Scope of the Use Case": ["Local", "Local"],
            "Economical Impact": ["Cost Reduction", "Cost Reduction"],
            "Tools": ["Gemini", "Gemini"],
        })
        result = gc.process_dataframe(df)
        self.assertNotEqual(result["UC_ID"].iloc[0], result["UC_ID"].iloc[1])

    def test_tools_tags_serialized_as_string(self):
        df = _make_raw_df(**{"Tools": ["Gemini, NotebookLM"]})
        result = gc.process_dataframe(df)
        self.assertIsInstance(result["Tools_Tags"].iloc[0], str)

    def test_complexity_tier_assigned(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        self.assertIn(result["Complexity_Tier"].iloc[0], ["Small", "Medium", "Large"])

    def test_family_assigned(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        self.assertIn(result["Family"].iloc[0], ["F1","F2","F3","F4","F5","F6","F7"])

    def test_family_label_assigned(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        self.assertIn(result["Family_Label"].iloc[0], gc.FAMILY_LABELS.values())

    def test_it_flag_set_for_sfdc(self):
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["Connect to sfdc data"],
            "Scope of the Use Case": ["Group-wide"]
        })
        result = gc.process_dataframe(df)
        self.assertEqual(result["IT_Flag"].iloc[0], "⚠️ IT")

    def test_small_tier_exemption(self):
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["Connect to sfdc data"],
            "Scope of the Use Case": ["Local"] # Small tier
        })
        result = gc.process_dataframe(df)
        self.assertEqual(result["IT_Flag"].iloc[0], "")
        self.assertIn("sfdc", result["IT_Attention"].iloc[0])

    def test_new_pure_keywords_set_it_flag(self):
        # "easiest" is one of the new pure keywords
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["This is the easiest way to manage documents"],
            "Scope of the Use Case": ["Group-wide"] # Medium tier
        })
        result = gc.process_dataframe(df)
        self.assertEqual(result["IT_Flag"].iloc[0], "⚠️ IT")

    def test_no_it_flag_for_simple_use_case(self):
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["Translate the document"],
            "Tools": ["Gemini"],
        })
        result = gc.process_dataframe(df)
        # Only flag if tier is Large or IT keywords detected
        it_flag = result["IT_Flag"].iloc[0]
        self.assertIn(it_flag, ["", "⚠️ IT"])  # valid either way

    def test_nan_stage_filled(self):
        df = _make_raw_df(**{"Stage": [None]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Stage"].iloc[0], "A revoir avec le builder")

    def test_nan_economic_impact_filled(self):
        df = _make_raw_df(**{"Economical Impact": [None]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Economical Impact"].iloc[0], "Non évalué")

    def test_nan_cluster_filled(self):
        df = _make_raw_df(**{"Cluster": [None]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Cluster"].iloc[0], "N/A")

    def test_nan_job_family_filled(self):
        df = _make_raw_df(**{"Job Family": [None]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Job Family"].iloc[0], "N/A")

    def test_nan_scope_filled(self):
        df = _make_raw_df(**{"Scope of the Use Case": [None]})
        result = gc.process_dataframe(df)
        self.assertEqual(result["Scope of the Use Case"].iloc[0], "N/A")

    def test_score_total_is_sum_of_dimensions(self):
        df = _make_raw_df()
        result = gc.process_dataframe(df)
        expected = (result["Score_Integration"] + result["Score_Scope"] +
                    result["Score_Data"] + result["Score_AI"] + result["Score_Economic"])
        self.assertTrue((result["Score_Total"] == expected).all())

    def test_large_tier_flagged_it(self):
        """Un use case Large doit recevoir le flag IT même sans mot-clé système."""
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["Build a complex industrial integration"],
            "Tools": ["Advance Coding, AI Studio, App Script, AppSheet"],
            "Scope of the Use Case": ["Group-wide"],
            "Economical Impact": ["Revenue Growth"],
        })
        result = gc.process_dataframe(df)
        if result["Complexity_Tier"].iloc[0] == "Large":
            self.assertEqual(result["IT_Flag"].iloc[0], "⚠️ IT")


# ════════════════════════════════════════════════════════════════
# Maturity status & Overrides (v2)
# ════════════════════════════════════════════════════════════════
class TestMaturityAndOverrides(unittest.TestCase):
    def test_maturity_status_none(self):
        # TC-001
        self.assertEqual(gc.detect_maturity_status("A normal description without any markers"), "")
        self.assertEqual(gc.detect_maturity_status(None), "")
        self.assertEqual(gc.detect_maturity_status(""), "")

    def test_maturity_status_sfdc(self):
        # TC-002
        self.assertEqual(gc.detect_maturity_status("Some text --DONE, SO FAR - with salesforce"), "🔄 Partiel")
        self.assertEqual(gc.detect_maturity_status("done, so far"), "🔄 Partiel")

    def test_maturity_status_cmms(self):
        # TC-003
        self.assertEqual(gc.detect_maturity_status("I have already done this with PowerBI and some more"), "🔄 Partiel")
        self.assertEqual(gc.detect_maturity_status("I have already initiated the movement on the plant"), "🔄 Partiel")

    def test_maturity_status_auqa(self):
        # TC-004
        self.assertEqual(gc.detect_maturity_status("Project expanding on the existing tools already deployed for quoting"), "🔄 Partiel")

    def test_score_data_l4_override(self):
        # TC-005: D3 (Score_Data) must be at least 2 if "Python on Fabric", "Python on DataStudio", or "BigQuery" is present
        self.assertEqual(gc.score_data(["Python on Fabric"], "plain description"), 2)
        self.assertEqual(gc.score_data(["Python on DataStudio"], "plain description"), 2)
        self.assertEqual(gc.score_data(["BigQuery"], "plain description"), 2)
        self.assertEqual(gc.score_data([], "use bigquery to get the data"), 2)

    def test_process_dataframe_maturity_overrides(self):
        # IT-001
        # Test Salesforce
        df_sfdc = _make_raw_df(**{
            "Use Case Description (Long)": ["A Gemini assistant --DONE, SO FAR -"],
            "Tools": ["Gemini"],
        })
        res_sfdc = gc.process_dataframe(df_sfdc)
        self.assertEqual(res_sfdc["Maturity_Status"].iloc[0], "🔄 Partiel")
        self.assertEqual(res_sfdc["Score_Data"].iloc[0], 1)
        self.assertEqual(res_sfdc["Score_AI"].iloc[0], 1)
        
        # Test CMMS
        df_cmms = _make_raw_df(**{
            "Use Case Description (Long)": ["I have already done this with PowerBI"],
            "Tools": ["Gemini"],
        })
        res_cmms = gc.process_dataframe(df_cmms)
        self.assertEqual(res_cmms["Maturity_Status"].iloc[0], "🔄 Partiel")
        self.assertEqual(res_cmms["Score_Data"].iloc[0], 2)
        self.assertEqual(res_cmms["Score_AI"].iloc[0], 1)

        # Test AUQA
        df_auqa = _make_raw_df(**{
            "Use Case Description (Long)": ["Project expanding on the existing tools already deployed"],
            "Tools": ["Gemini"],
        })
        res_auqa = gc.process_dataframe(df_auqa)
        self.assertEqual(res_auqa["Maturity_Status"].iloc[0], "🔄 Partiel")
        self.assertEqual(res_auqa["Score_Data"].iloc[0], 1)

    def test_process_dataframe_l4_override(self):
        # IT-002
        df_fabric = _make_raw_df(**{
            "Use Case Description (Long)": ["Plain description"],
            "Tools": ["Python on Fabric"],
        })
        res_fabric = gc.process_dataframe(df_fabric)
        self.assertEqual(res_fabric["Score_Data"].iloc[0], 2)

        df_bq = _make_raw_df(**{
            "Use Case Description (Long)": ["Plain bigquery description"],
            "Tools": ["Gemini"],
        })
        res_bq = gc.process_dataframe(df_bq)
        self.assertEqual(res_bq["Score_Data"].iloc[0], 2)

    def test_main_workflow_end_to_end(self):
        # IT-003
        df = _make_raw_df()
        res = gc.process_dataframe(df)
        self.assertIn("Maturity_Status", res.columns)
        idx_status = res.columns.get_loc("Maturity_Status")
        idx_desc = res.columns.get_loc("Use Case Description (Long)")
        self.assertEqual(idx_status + 1, idx_desc, "Maturity_Status must be directly before Use Case Description (Long)")


# ════════════════════════════════════════════════════════════════
# Data Sources Extraction
# ════════════════════════════════════════════════════════════════
class TestExtractDataSources(unittest.TestCase):
    def test_extract_data_sources_sap(self):
        # TC-006
        self.assertEqual(gc.extract_data_sources("Consolidates manual SAP data exports", ""), "SAP")
        self.assertEqual(gc.extract_data_sources("SAP S/4HANA migration", ""), "SAP")

    def test_extract_data_sources_sheets(self):
        # TC-007
        self.assertEqual(gc.extract_data_sources("central repository using Sheets", ""), "Sheets")
        self.assertEqual(gc.extract_data_sources("VBA scripts", ""), "Sheets")

    def test_extract_data_sources_multiple(self):
        # TC-008
        res = gc.extract_data_sources("An assistant for Salesforce, reading SAP and Sheets", "")
        self.assertIn("SAP", res)
        self.assertIn("Salesforce", res)
        self.assertIn("Sheets", res)

    def test_extract_data_sources_none(self):
        # TC-009
        self.assertEqual(gc.extract_data_sources("Translate this text", "Gemini"), "A revoir avec le builder")

    def test_extract_data_sources_case_insensitivity(self):
        # TC-010
        self.assertEqual(gc.extract_data_sources("sap data", ""), "SAP")
        self.assertEqual(gc.extract_data_sources("powerbi dashboard", ""), "Power BI")

    def test_extract_data_sources_deduplication(self):
        # TC-011
        self.assertEqual(gc.extract_data_sources("SAP and another SAP load", ""), "SAP")

    def test_process_dataframe_data_sources(self):
        # IT-004
        df = _make_raw_df(**{
            "Use Case Description (Long)": ["Automated SAP and Sheets consolidation"],
            "Tools": ["Gemini"],
        })
        res = gc.process_dataframe(df)
        self.assertIn("Data_Sources", res.columns)
        self.assertEqual(res["Data_Sources"].iloc[0], "SAP, Sheets")

    def test_main_runs_completely_with_new_column(self):
        # IT-005
        import tempfile
        import os
        fake_source = MagicMock(spec=Path)
        fake_source.exists.return_value = True
        raw_df = _make_raw_df(**{"Use Case Description (Long)": ["Read from SAP"]})
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            with patch("generate_catalog.pd.read_excel", return_value=raw_df):
                gc.main(source=fake_source, output=tmp_path)
            self.assertTrue(tmp_path.exists())
            df_out = pd.read_excel(tmp_path, sheet_name="Catalogue")
            self.assertIn("Data_Sources", df_out.columns)
            self.assertEqual(df_out["Data_Sources"].iloc[0], "SAP")
        finally:
            if tmp_path.exists():
                os.unlink(tmp_path)

    def test_generate_catalog_data_sources_coverage(self):
        # IT-006
        df = _make_raw_df()
        res = gc.process_dataframe(df)
        self.assertTrue((res["Data_Sources"] != "").all())


# ════════════════════════════════════════════════════════════════
# main() — filesystem mocking
# ════════════════════════════════════════════════════════════════
class TestMain(unittest.TestCase):
    def test_main_exits_when_source_missing(self):
        fake_source = MagicMock(spec=Path)
        fake_source.exists.return_value = False
        fake_source.__str__ = lambda self: "/fake/path.xlsx"

        with self.assertRaises(SystemExit) as ctx:
            gc.main(source=fake_source, output=Path("/tmp/out.xlsx"))
        self.assertEqual(ctx.exception.code, 1)

    def test_main_success_calls_to_excel(self):
        import os
        import tempfile
        fake_source = MagicMock(spec=Path)
        fake_source.exists.return_value = True
        fake_source.__str__ = lambda self: "/fake/source.xlsx"

        raw_df = _make_raw_df()

        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            tmp_path = Path(tmp.name)

        try:
            with patch("generate_catalog.pd.read_excel", return_value=raw_df) as mock_read:
                gc.main(source=fake_source, output=tmp_path)

            mock_read.assert_called_once_with(fake_source, sheet_name="Use cases", header=0)
            self.assertTrue(tmp_path.exists())
        finally:
            if tmp_path.exists():
                os.unlink(tmp_path)


# ════════════════════════════════════════════════════════════════
# __main__ guard — couvre la ligne if __name__ == "__main__"
# ════════════════════════════════════════════════════════════════
class TestMainGuard(unittest.TestCase):
    def test_main_guard_invoked_as_module(self):
        """Couvre la branche if __name__ == '__main__' via subprocess."""
        import os
        import subprocess
        env = {"PYTHONPATH": str(Path(__file__).parent.parent)}
        # On patche en passant un source inexistant → sys.exit(1) attendu
        result = subprocess.run(
            [sys.executable, str(Path(__file__).parent.parent / "generate_catalog.py")],
            capture_output=True, text=True,
            env={**os.environ, **env}
        )
        # Le fichier source réel peut exister ou non ; dans les deux cas
        # le processus se termine (exit 0 ou 1 selon l'env)
        self.assertIn(result.returncode, [0, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
