import typing

from sqlalchemy.orm import Session
import database.sa_models as sa_models


def create(session: Session, determiner: str) -> sa_models.Determiner:
    db_determiner = sa_models.Determiner(word=determiner)
    session.add(db_determiner)
    return db_determiner


def get_all(session: Session) -> set[str]:
    return set(
        typing.cast(str, determiner.word)
        for determiner in session.query(sa_models.Determiner).all()
    )


def count(session: Session) -> int:
    return session.query(sa_models.Determiner).count()
