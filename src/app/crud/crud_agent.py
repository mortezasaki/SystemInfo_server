from typing import List

from app.crud.base import CRUDBase
from app.models.agent import Agent
from app.schemas.agent_schema import AgentCreate, AgentUpdate
from sqlalchemy.orm import Session


class CRUDAgent(CRUDBase[Agent, AgentCreate, AgentUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Agent:
        return db.query(self.model).filter(self.model.name == name).first()
    

agent = CRUDAgent(Agent)
