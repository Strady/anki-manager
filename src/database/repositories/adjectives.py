from itertools import chain

from sqlalchemy.orm import Session
import database.sa_models as sa_models
import database.pydantic_models as pydantic_models


def create(session: Session, adjective: pydantic_models.Adjective) -> sa_models.Adjective:
    db_adjective = sa_models.Adjective(
        positive=adjective.positive,
        comparative=adjective.comparative,
        superlative=adjective.superlative
    )
    session.add(db_adjective)
    return db_adjective


def get_all(session: Session) -> set[str]:
    adjectives = [
        pydantic_models.Adjective.model_validate(adjective)
        for adjective in session.query(sa_models.Adjective).all()
    ]
    return set(chain.from_iterable(adjectives))


def count(session: Session) -> int:
    return session.query(sa_models.Adjective).count()
