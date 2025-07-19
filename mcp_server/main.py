from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mcp_server.services.query_router import route_query

app = FastAPI(title="MCP Server")

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    source_systems: list[str]
    visualization: str | None = None
    data: list[dict] | None = None

@app.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    try:
        result = route_query(request.question)
        return AskResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
