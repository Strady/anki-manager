from sqlalchemy import Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Noun(Base):
    __tablename__ = 'nouns'

    __table_args__ = (
        UniqueConstraint('singular', 'plural', name='uq_single_plural'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    singular: Mapped[str | None]
    plural: Mapped[str | None]


class Verb(Base):
    __tablename__ = 'verbs'

    __table_args__ = (
        UniqueConstraint(
            'base',
            'third_person',
            'past_simple',
            'past_participle',
            'present_participle',
            name='uq_constraint'
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    base: Mapped[str]
    third_person: Mapped[str]
    past_simple: Mapped[str]
    past_participle: Mapped[str]
    present_participle: Mapped[str | None]
    additional: Mapped[str | None]
