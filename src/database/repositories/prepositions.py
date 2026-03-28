import typing

from sqlalchemy.orm import Session
import database.sa_models as sa_models


def create(session: Session, preposition: str) -> sa_models.Preposition:
    db_preposition = sa_models.Preposition(word=preposition)
    session.add(db_preposition)
    return db_preposition


def get_all(session: Session) -> set[str]:
    return set(
        typing.cast(str, preposition.word)
        for preposition in session.query(sa_models.Preposition).all()
    )


def count(session: Session) -> int:
    return session.query(sa_models.Preposition).count()
