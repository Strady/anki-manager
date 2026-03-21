from sqlalchemy.orm import Session
from database.models import Verb


def create(session: Session,
           base: str,
           third_person: str,
           past_simple: str,
           past_participle: str,
           present_participle: str | None,
           additional: str | None
           ) -> Verb:
    verb = Verb(
        base=base,
        third_person=third_person,
        past_simple=past_simple,
        past_participle=past_participle,
        present_participle=present_participle,
        additional=additional
    )
    session.add(verb)
    return verb


def get_all(session: Session) -> set[str]:
    nouns = session.query(Verb).all()
    result = set()
    for noun in nouns:
        result.add(noun.base)
        result.add(noun.third_person)
        result.add(noun.past_simple)
        result.add(noun.past_participle)
        if noun.present_participle:
            result.add(noun.present_participle)
    return result


def count(session: Session) -> int:
    return session.query(Verb).count()
