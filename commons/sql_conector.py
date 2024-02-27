import contextlib
from typing import ContextManager

from sqlmodel import Session, create_engine, select
from commons.settings import settings
from model.radio import Radio

engine = create_engine(settings.mysql_uri, echo=True)


@contextlib.contextmanager
def connector() -> ContextManager[Session]:
    session = Session(engine)
    yield session
    session.close()
