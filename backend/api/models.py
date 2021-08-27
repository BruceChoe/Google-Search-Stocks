from dustyapi.db import SQLAlchemyUniverse
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Dummy(Base):
    __tablename__ = "dummies"

    id = Column(Integer, primary_key=True)
    size = Column(String(30), nullable=False)


class DummyUniverse(SQLAlchemyUniverse):
    model_cls = Dummy
