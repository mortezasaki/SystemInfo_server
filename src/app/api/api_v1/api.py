from app.api.api_v1.endpoints import agent, logs
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
