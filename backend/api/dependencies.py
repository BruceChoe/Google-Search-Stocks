from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from api import models
from api.config import settings

#  if settings.dbsocket is None:
#      connection_string = (
#          f"postgresql://{settings.dbuser}:{settings.dbpassword}"
#          f"@{settings.dbhost}/{settings.appdb}"
#      )
#  else:
#      connection_string = (
#          f"postgresql://{settings.dbuser}:{settings.dbpassword}"
#          f"@/{settings.appdb}?host={settings.dbsocket}"
#      )

connection_string = "sqlite+pysqlite:///database.db"

engine = create_engine(connection_string, echo=True, future=True)

models.Base.metadata.create_all(engine)


def get_engine():
    return engine


def get_session(engine_: get_engine = Depends()):
    session = Session(engine_)

    try:
        yield session
    finally:
        session.close()
