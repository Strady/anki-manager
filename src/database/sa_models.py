from sqlalchemy import Integer, String, UniqueConstraint, Index, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Noun(Base):
    __tablename__ = 'nouns'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    singular: Mapped[str | None] = mapped_column(String, nullable=True)
    plural: Mapped[str | None] = mapped_column(String, nullable=True)

    __table_args__ = (
        Index(
            "uq_constraint",
            func.coalesce(singular, ""),
            func.coalesce(plural, ""),
            unique=True
        ),
    )


class Verb(Base):
    __tablename__ = 'verbs'

    __table_args__ = (
        UniqueConstraint(
            'base',
            'past_simple',
            'past_participle',
            'third_person',
            name='uq_constraint'
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    base: Mapped[str]
    past_simple: Mapped[str]
    past_participle: Mapped[str]
    third_person: Mapped[str]
    present_participle: Mapped[str | None]
    additional: Mapped[str | None]


class Adjective(Base):
    __tablename__ = 'adjectives'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    positive: Mapped[str] = mapped_column(String, unique=True)
    comparative: Mapped[str | None]
    superlative: Mapped[str | None]


class Adverb(Base):
    __tablename__ = 'adverbs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    positive: Mapped[str] = mapped_column(String, unique=True)
    comparative: Mapped[str | None]
    superlative: Mapped[str | None]


class Preposition(Base):
    __tablename__ = 'prepositions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    word: Mapped[str] = mapped_column(String, unique=True)


class Pronoun(Base):
    __tablename__ = 'pronouns'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    subject: Mapped[str] = mapped_column(String, unique=True)
    object: Mapped[str]
    dependent_possessive: Mapped[str]
    independent_possessive: Mapped[str]
    reflexive: Mapped[str] = mapped_column(String, nullable=True)


class Determiner(Base):
    __tablename__ = 'determiners'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    word: Mapped[str] = mapped_column(String, unique=True)


class Conjunction(Base):
    __tablename__ = 'conjunctions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    word: Mapped[str] = mapped_column(String, unique=True)

