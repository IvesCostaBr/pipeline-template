from sqlalchemy import Column, Integer, String, DateTime, JSON
# from sqlalchemy.orm import relationship
from src.infra.database import db_config
from datetime import datetime
from pydantic import BaseModel


class Log(db_config.Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    content = Column(JSON)
    call_method = Column(String)


class LogModel(BaseModel):
    """Log Model Representation."""

    id: int = None
    created_at: datetime = datetime.now()
    content: dict
    call_method: str

    class Config:
        orm_model = True
