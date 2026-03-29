from database.base import Base
from database.engine import engine


if __name__ == '__main__':
    from database.sa_models import Noun, Verb, Adjective, Adverb, Preposition, Pronoun
    Base.metadata.create_all(engine)
