import json

from pydantic import BaseModel, field_validator, ConfigDict
from itertools import chain


class Pronoun(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    subject: str
    object: str
    dependent_possessive: str
    independent_possessive: str
    reflexive: str
    additional: set[str] = set()

    def __iter__(self):
        return iter((
            self.subject,
            self.object,
            self.dependent_possessive,
            self.independent_possessive,
            self.reflexive,
            *self.additional
        ))

    def __hash__(self):
        return hash(self.subject)

    def __lt__(self, other) -> bool:
        return self.subject < other.subject

    def __str__(self) -> str:
        return self.subject

    @property
    def additional_json(self) -> str:
        return json.dumps(list(self.additional))

    @field_validator('additional', mode='before')
    @classmethod
    def parse_additional_arg(cls, v):
        if isinstance(v, str):
            validation_error = '"additional" must be either a set of stings or a JSON-array with strings'
            try:
                additional_list = json.loads(v)
            except json.JSONDecodeError:
                raise ValueError(validation_error)
            if not all(isinstance(word, str) for word in additional_list):
                raise ValueError(validation_error)
            return set(additional_list)
        return v



personal = {
    Pronoun(subject='i', object='me', dependent_possessive='my', independent_possessive='mine', reflexive='myself'),
    Pronoun(subject='you', object='you', dependent_possessive='your', independent_possessive='yours', reflexive='yourself', additional={'yourselves'}),
    Pronoun(subject='he', object='him', dependent_possessive='his', independent_possessive='his', reflexive='himself'),
    Pronoun(subject='she', object='her', dependent_possessive='her', independent_possessive='hers', reflexive='herself'),
    Pronoun(subject='it', object='it', dependent_possessive='its', independent_possessive='its', reflexive='itself'),
    Pronoun(subject='we', object='us', dependent_possessive='our', independent_possessive='ours', reflexive='ourself'),
    Pronoun(subject='they', object='them', dependent_possessive='their', independent_possessive='theirs', reflexive='themselves', additional={'themself'}),
}

indefinite = {
    'someone', 'anyone', 'noone', 'everyone',
    'somebody', 'anybody', 'nobody', 'everybody',
    'something', 'anything', 'nothing', 'everything',
}

pronouns_objects = (*personal,)

pronouns = {
    # *chain.from_iterable(pronouns_objects),
    *indefinite
}
