from mcp_server.connectors.snowflake_connector import query_snowflake
from mcp_server.connectors.salesforce_connector import query_salesforce
from mcp_server.connectors.databricks_connector import query_databricks

def route_query(question: str) -> dict:
    question_lower = question.lower()
    sources_used = []
    results = []

    if "pipeline" in question_lower or "forecast" in question_lower:
        # Salesforce
        sf_data = query_salesforce(
            "SELECT Name, StageName, Amount, CloseDate FROM Opportunity WHERE IsClosed = false"
        )
        total = sum(op["Amount"] for op in sf_data if "Amount" in op)
        results.append({"salesforce_summary": f"$ in open opportunities"})
        sources_used.append("Salesforce")

        # Snowflake
        sf_query = "SELECT region, total_pipeline FROM analytics.pipeline_forecast WHERE quarter = 'Q4'"
        snowflake_data = query_snowflake(sf_query)
        results.append({"snowflake_forecast": snowflake_data})
        sources_used.append("Snowflake")

    elif "prediction" in question_lower or "model" in question_lower:
        db_query = "SELECT * FROM predictions.q4_pipeline_model_outputs"
        db_data = query_databricks(db_query)
        results.append({"databricks_predictions": db_data})
        sources_used.append("Databricks")

    else:
        return {
            "answer": "Sorry, I could not determine which system to query.",
            "source_systems": [],
            "visualization": None,
            "data": []
        }

    return {
        "answer": "Here is your Q4 pipeline summary.",
        "source_systems": sources_used,
        "visualization": None,
        "data": results
    }
