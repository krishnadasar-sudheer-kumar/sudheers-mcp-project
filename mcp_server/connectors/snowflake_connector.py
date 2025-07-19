import snowflake.connector
from mcp_server.config.settings import settings

def query_snowflake(sql: str) -> list[dict]:
    conn = snowflake.connector.connect(
        user=settings.snowflake_user,
        account=settings.snowflake_account,
        warehouse=settings.snowflake_warehouse,
        database=settings.snowflake_database,
        schema=settings.snowflake_schema,
        authenticator='externalbrowser'
    )
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()
