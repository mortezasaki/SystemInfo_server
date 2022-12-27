from app.config import settings
from app.db import base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def init_db(db: Session) -> None:
    engine = create_engine(settings.SQLITE_URL)
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    base.metadata.create_all(bind=engine)
