import enum
from datetime import datetime

from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, Enum, DateTime, Text

Base = declarative_base()


class Project(Base):
    """Project Model."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    create_date = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'{self.number}'
