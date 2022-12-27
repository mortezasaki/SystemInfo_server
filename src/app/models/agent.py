from datetime import datetime as dt
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship


def generate_id():
    new_id = str(uuid4())
    return new_id

class Agent(Base):
    id = Column(String(64), primary_key=True, index=True, default=generate_id)
    name = Column(String(128), nullable=False, unique=True)
    date_created = Column(DateTime, nullable=False, default=dt.now)
    logs = relationship("Log", back_populates="agent")
    