from sqlalchemy.orm import sessionmaker
from .engine import engine
from contextlib import contextmanager


SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
