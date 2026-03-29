import typing

from sqlalchemy.orm import Session
import database.sa_models as sa_models


def create(session: Session, conjunction: str) -> sa_models.Conjunction:
    db_conjunction = sa_models.Conjunction(word=conjunction)
    session.add(db_conjunction)
    return db_conjunction


def get_all(session: Session) -> set[str]:
    return set(
        typing.cast(str, conjunction.word)
        for conjunction in session.query(sa_models.Conjunction).all()
    )


def count(session: Session) -> int:
    return session.query(sa_models.Conjunction).count()
