from pydantic import BaseModel, model_validator
from itertools import chain


class Adjective(BaseModel):

    positive: str
    comparative: str | None
    superlative: str | None
    exception: bool = False

    @model_validator(mode="after")
    def check_comparatives(self):
        if not self.exception:
            if self.comparative is not None and not self.comparative.endswith('er'):
                raise ValueError(f'Comparative for "{self.positive}" should end with "er"')
            if self.superlative is not None and not self.superlative.endswith('est'):
                raise ValueError(f'Comparative for "{self.positive}" should end with "est"')
        return self

    def __iter__(self):
        forms = [self.positive, self.comparative, self.superlative]
        return iter(forms)

    def __hash__(self):
        return hash(self.positive)

    def __lt__(self, other):
        return self.positive < other.positive

    def __str__(self) -> str:
        return self.positive


science = {
    Adjective(positive='scientific', comparative=None, superlative=None),
}

misc = {
    Adjective(positive='big', comparative='large', superlative='largest', exception=True),
    Adjective(positive='little', comparative='less', superlative='least', exception=True),
    Adjective(positive='bad', comparative='worse', superlative='worst', exception=True),
    Adjective(positive='good', comparative='better', superlative='best', exception=True),
    Adjective(positive='great', comparative='greater', superlative='greatest'),
    Adjective(positive='late', comparative='later', superlative='latest'),
    Adjective(positive='new', comparative='newer', superlative='newest'),
    Adjective(positive='old', comparative='older', superlative='oldest'),
    Adjective(positive='fresh', comparative='fresher', superlative='freshest'),
    Adjective(positive='strong', comparative='stronger', superlative='strongest'),
    Adjective(positive='crazy', comparative='crazier', superlative='craziest'),
    Adjective(positive='happy', comparative='happier', superlative='happiest'),
    Adjective(positive='fair', comparative='fairer', superlative='fairest'),
    Adjective(positive='peaceful', comparative=None, superlative=None),
    Adjective(positive='long', comparative='longer', superlative='longest'),
    Adjective(positive='hot', comparative='hotter', superlative='hottest'),
    Adjective(positive='steep', comparative='steeper', superlative='steepest'),
    Adjective(positive='romantic', comparative=None, superlative=None),
    Adjective(positive='nice', comparative='nicer', superlative='nicest'),
    Adjective(positive='suggestible', comparative=None, superlative=None),
    Adjective(positive='insane', comparative=None, superlative=None),
    Adjective(positive='dead', comparative=None, superlative=None),
    Adjective(positive='next', comparative=None, superlative=None),
    Adjective(positive='wrong', comparative=None, superlative=None),
    Adjective(positive='holy', comparative=None, superlative=None),
    Adjective(positive='whole', comparative=None, superlative=None),
    Adjective(positive='special', comparative=None, superlative=None),
    Adjective(positive='full', comparative=None, superlative=None),
    Adjective(positive='worthy', comparative=None, superlative=None),
    Adjective(positive='extreme', comparative=None, superlative=None),
    Adjective(positive='fast', comparative='faster', superlative='fastest'),
    Adjective(positive='alive', comparative=None, superlative=None),
    Adjective(positive='unclear', comparative=None, superlative=None),
    Adjective(positive='invisible', comparative=None, superlative=None),
    Adjective(positive='real', comparative=None, superlative=None),
    Adjective(positive='right', comparative=None, superlative=None),
    Adjective(positive='ideal', comparative=None, superlative=None),
    Adjective(positive='complete', comparative=None, superlative=None),
    Adjective(positive='last', comparative=None, superlative=None),
    Adjective(positive='sweet', comparative='sweeter', superlative='sweetest'),
    Adjective(positive='sweetie', comparative=None, superlative=None),
    Adjective(positive='important', comparative=None, superlative=None),
    Adjective(positive='unbelievable', comparative=None, superlative=None),
    Adjective(positive='impenetrable', comparative=None, superlative=None),
    Adjective(positive='unwitting', comparative=None, superlative=None),
    Adjective(positive='well-meaning', comparative=None, superlative=None),
    Adjective(positive='dilapidated', comparative=None, superlative=None),
}

adjective_objects = (
    *science, *misc
)

adjectives = {*chain.from_iterable(adjective_objects)}
