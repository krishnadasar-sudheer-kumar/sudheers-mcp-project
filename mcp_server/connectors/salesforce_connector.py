from simple_salesforce import Salesforce
from mcp_server.config.settings import settings

def get_salesforce_client():
    return Salesforce(
        username=settings.salesforce_username,
        password=settings.salesforce_password,
        security_token=settings.salesforce_security_token,
        domain=settings.salesforce_domain
    )

def query_salesforce(soql: str) -> list[dict]:
    sf = get_salesforce_client()
    result = sf.query_all(soql)
    return result['records']
