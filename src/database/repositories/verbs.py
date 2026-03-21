from itertools import chain

from sqlalchemy.orm import Session
import database.sa_models as sa_models
import database.pydantic_models as pydantic_models


def create(session: Session, verb: pydantic_models.Verb) -> sa_models.Verb:
    verb = sa_models.Verb(
        base=verb.base,
        past_simple=verb.past_simple,
        past_participle=verb.past_participle,
        third_person=verb.third_person,
        present_participle=verb.present_participle,
        additional=verb.additional_json
    )
    session.add(verb)
    return verb


def get_all(session: Session) -> set[str]:
    verbs = [
        pydantic_models.Verb.model_validate(verb)
        for verb in session.query(sa_models.Verb).all()
    ]
    return set(chain.from_iterable(verbs))


def count(session: Session) -> int:
    return session.query(sa_models.Verb).count()
