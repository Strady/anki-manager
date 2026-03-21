from itertools import chain

from sqlalchemy.orm import Session
import database.sa_models as sa_models
import database.pydantic_models as pydantic_models


def create(session: Session, noun: pydantic_models.Noun) -> sa_models.Noun:
    db_noun = sa_models.Noun(singular=noun.singular, plural=noun.plural)
    session.add(db_noun)
    return db_noun


def get_all(session: Session) -> set[str]:
    nouns = [
        pydantic_models.Noun.model_validate(noun)
        for noun in session.query(sa_models.Noun).all()
    ]
    return set(chain.from_iterable(nouns))
    #
    # result = set()
    # for noun in nouns:
    #     if noun.singular:
    #         result.add(noun.singular)
    #     if noun.plural:
    #         result.add(noun.plural)
    # return result


def count(session: Session) -> int:
    return session.query(sa_models.Noun).count()
