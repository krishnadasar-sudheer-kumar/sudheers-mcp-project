from pydantic import BaseSettings

class Settings(BaseSettings):
    # Snowflake
    snowflake_user: str
    snowflake_password: str = ""
    snowflake_account: str
    snowflake_warehouse: str
    snowflake_database: str
    snowflake_schema: str

    # Salesforce
    salesforce_username: str
    salesforce_password: str
    salesforce_security_token: str
    salesforce_domain: str

    # Databricks
    databricks_host: str
    databricks_token: str

    class Config:
        env_file = ".env"

settings = Settings()
