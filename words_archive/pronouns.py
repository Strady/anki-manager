from pydantic import BaseModel, field_validator
from itertools import chain


class Pronoun(BaseModel):

    subject: str
    object: str
    dependent_possessive: str
    independent_possessive: str
    reflexive: str

    def __iter__(self):
        return iter((
            self.subject,
            self.object,
            self.dependent_possessive,
            self.independent_possessive,
            self.reflexive
        ))

    def __hash__(self):
        return hash(self.subject)

    def __lt__(self, other) -> bool:
        return self.subject < other.subject

    def __str__(self) -> str:
        return self.subject


personal = {
    Pronoun(subject='i', object='me', dependent_possessive='my', independent_possessive='mine', reflexive='myself'),
    Pronoun(subject='you', object='you', dependent_possessive='your', independent_possessive='yours', reflexive='yourself'),
    Pronoun(subject='he', object='him', dependent_possessive='his', independent_possessive='his', reflexive='himself'),
    Pronoun(subject='she', object='her', dependent_possessive='her', independent_possessive='hers', reflexive='herself'),
    Pronoun(subject='it', object='it', dependent_possessive='its', independent_possessive='its', reflexive='itself'),
    Pronoun(subject='we', object='us', dependent_possessive='our', independent_possessive='ours', reflexive='ourself'),
    Pronoun(subject='they', object='them', dependent_possessive='their', independent_possessive='theirs', reflexive='themself'),
}

indefinite = {
    'someone', 'anyone', 'noone', 'everyone',
    'somebody', 'anybody', 'nobody', 'everybody',
    'something', 'anything', 'nothing', 'everything',
}

pronouns_objects = (*personal,)

pronouns = {*chain.from_iterable(pronouns_objects), *indefinite}
