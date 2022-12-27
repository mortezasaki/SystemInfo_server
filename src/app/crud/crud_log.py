from typing import List

from app.crud.base import CRUDBase
from app.models.logs import Log
from app.schemas.logs_schema import LogsCreate, LogsUpdate
from sqlalchemy.orm import Session


class CRUDLogs(CRUDBase[Log, LogsCreate, LogsUpdate]):
    def get_multi(self, db: Session, agent_id: str, *, skip: int = 0, limit: int = 100) -> List[Log]:
        return db.query(self.model).order_by(self.model.timestamp.desc()).filter(self.model.agent_id == agent_id).offset(skip).limit(limit).all()

logs = CRUDLogs(Log)
