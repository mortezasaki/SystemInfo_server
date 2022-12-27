from datetime import datetime

from pydantic import BaseModel


class AgentBase(BaseModel):
    name: str

class AgentCreate(AgentBase):
    pass

class AgentUpdate(AgentBase):
    pass

class AgentInDBBase(AgentBase):
    id: str
    date_created: datetime
    class Config:
        orm_mode = True
        
class Agent(AgentInDBBase):
    pass

class AgentIn(AgentBase):
    pass
