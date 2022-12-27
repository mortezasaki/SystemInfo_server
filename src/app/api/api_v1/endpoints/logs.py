from typing import List

import sqlalchemy
from app import crud, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{agent_id}", response_model=List[schemas.LogsOut])
def get_logs(
    *,
    db: Session = Depends(deps.get_db),
    agent_id: str,
    skip: int = 0,
    limit: int = 100,
) -> List[schemas.LogsOut]:
    """
    Retrieve logs.
    """
    logs = crud.logs.get_multi(db, agent_id, skip=skip, limit=limit)
    result = []
    for log in logs:
        result.append(schemas.LogsOut(logs=log.logs, timestamp=log.timestamp))
    return result

@router.post("/", response_model=schemas.LogsOut)
def create_logs(
    *,
    db: Session = Depends(deps.get_db),
    logs_in: schemas.LogsIn,
) -> schemas.LogsOut:
    """
    Create new logs.
    """
    logs_schema = schemas.LogsCreate(agent_id=logs_in.agent_id, logs=logs_in.logs, timestamp=logs_in.timestamp)
    try:
        new_logs = crud.logs.create(db, obj_in=logs_schema)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail="Agent ID does not exist")
    result = schemas.LogsOut(logs=new_logs.logs, timestamp=new_logs.timestamp)
    return result
    
