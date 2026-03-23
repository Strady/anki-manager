from itertools import chain

from sqlalchemy.orm import Session
import database.sa_models as sa_models
import database.pydantic_models as pydantic_models


def create(session: Session, adverb: pydantic_models.Adverb) -> sa_models.Adverb:
    db_adverb = sa_models.Adverb(
        positive=adverb.positive,
        comparative=adverb.comparative,
        superlative=adverb.superlative
    )
    session.add(db_adverb)
    return db_adverb


def get_all(session: Session) -> set[str]:
    adverbs = [
        pydantic_models.Adverb.model_validate(Adverb)
        for Adverb in session.query(sa_models.Adverb).all()
    ]
    return set(chain.from_iterable(adverbs))


def count(session: Session) -> int:
    return session.query(sa_models.Adverb).count()
