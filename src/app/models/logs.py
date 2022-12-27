from datetime import datetime as dt

from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON


class Log(Base):
    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(String(64), ForeignKey("agent.id"), nullable=False)
    logs = Column(JSON, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    agent = relationship("Agent", back_populates="logs")
