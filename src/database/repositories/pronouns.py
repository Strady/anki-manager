from itertools import chain

from sqlalchemy.orm import Session
import database.sa_models as sa_models
import database.pydantic_models as pydantic_models


def create(session: Session, pronoun: pydantic_models.Pronoun) -> sa_models.Pronoun:
    pronoun = sa_models.Pronoun(
        subject=pronoun.subject,
        object=pronoun.object,
        dependent_possessive=pronoun.dependent_possessive,
        independent_possessive=pronoun.independent_possessive,
        reflexive=pronoun.reflexive,
        additional=pronoun.additional_json
    )
    session.add(pronoun)
    return pronoun


def get_all(session: Session) -> set[str]:
    pronouns = [
        pydantic_models.Pronoun.model_validate(pronoun)
        for pronoun in session.query(sa_models.Pronoun).all()
    ]
    return set(chain.from_iterable(pronouns))


def count(session: Session) -> int:
    return session.query(sa_models.Pronoun).count()
