from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine("sqlite:///database.db", echo=False, future=True)
Base = declarative_base()
SessionFactory = sessionmaker(bind=engine, autoflush=False, future=True)
ScopedSession = scoped_session(SessionFactory)


@contextmanager
def session_scope(desktop: bool = False):
    sess = SessionFactory() if desktop else ScopedSession()
    try:
        yield sess
        sess.commit()
    except Exception:
        sess.rollback()
        raise
    finally:
        sess.close()
