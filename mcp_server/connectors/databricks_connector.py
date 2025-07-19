import requests
from mcp_server.config.settings import settings

def query_databricks(sql: str) -> list[dict]:
    endpoint = f"{settings.databricks_host}/api/2.0/sql/statements"
    headers = {
        "Authorization": f"Bearer {settings.databricks_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "statement": sql,
        "warehouse_id": "YOUR_WAREHOUSE_ID",  # Replace with real warehouse ID
        "wait_timeout": "30s"
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    response.raise_for_status()
    return [{"placeholder": "Databricks results would go here"}]
