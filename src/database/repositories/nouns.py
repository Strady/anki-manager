from sqlalchemy.orm import Session
from database.models import Noun


def create(session: Session, singular: str | None, plural: str | None) -> Noun:
    noun = Noun(singular=singular, plural=plural)
    session.add(noun)
    return noun


def get_all(session: Session) -> set[str]:
    nouns = session.query(Noun).all()
    result = set()
    for noun in nouns:
        if noun.singular:
            result.add(noun.singular)
        if noun.plural:
            result.add(noun.plural)
    return result


def count(session: Session) -> int:
    return session.query(Noun).count()
