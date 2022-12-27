from datetime import datetime

from pydantic import BaseModel


class LogsBase(BaseModel):
    agent_id: str
    logs: dict
    timestamp: datetime

class LogsCreate(LogsBase):
    pass

class LogsUpdate(LogsBase):
    pass

class LogsInDBBase(LogsBase):
    id: str
    class Config:
        orm_mode = True
        
class Logs(LogsInDBBase):
    pass

class LogsIn(LogsBase):
    pass

class LogsOut(BaseModel):
    logs: dict
    timestamp: datetime
