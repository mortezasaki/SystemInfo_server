from typing import Any, List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[schemas.Agent])
def get_agents(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve agents.
    """
    agents = crud.agent.get_multi(db, skip=skip, limit=limit)
    return agents

@router.post("/", response_model=schemas.Agent)
def create_agent(
    *,
    db: Session = Depends(deps.get_db),
    agent_in: schemas.AgentIn,
) -> Any:
    """
    Create new agent.
    """
    agent = crud.agent.get_by_name(db, name=agent_in.name)
    if agent:
        raise HTTPException(status_code=400, detail="The agent with this name already exists in the system.")
    
    
    new_agent = schemas.AgentCreate(name=agent_in.name)
    
    agent = crud.agent.create(db, obj_in=new_agent)
    return agent
