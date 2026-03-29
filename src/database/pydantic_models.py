import json

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class NoteData(BaseModel):
    expression: str
    explanation: str
    example: str

    def __eq__(self, other) -> bool:
        return self.expression == other.expression


class Noun(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    singular: str | None
    plural: str | None

    def __iter__(self):
        return iter(form.lower() for form in (self.singular, self.plural) if form is not None)

    def __hash__(self):
        return hash(self.singular)

    def __lt__(self, other):
        word = self.singular or self.plural
        other_word = other.singular or other.plural
        return word.lower() < other_word.lower()

    def __str__(self) -> str:
        return self.singular or self.plural


class Verb(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    base: str
    past_simple: str
    past_participle: str
    third_person: str
    present_participle: str | None
    additional: set[str] = set()

    @property
    def additional_json(self) -> str:
        return json.dumps(list(self.additional))

    @field_validator('present_participle')
    def check_v_ing(cls, value):
        if value is not None and not value.endswith('ing'):
            raise ValueError('Present participle form must end with "ing"')
        return value

    @field_validator('third_person')
    def check_v_s(cls, value):
        if not value.endswith('s'):
            raise ValueError('Third person form must end with "s"')
        return value

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

    def __iter__(self):
        forms = [
            self.base,
            self.third_person,
            self.past_simple,
            self.past_participle,
            *self.additional
        ]
        if self.present_participle:
            forms.append(self.present_participle)
        return iter(forms)

    def __hash__(self):
        return hash((self.base, self.past_simple, self.past_participle))

    def __lt__(self, other):
        return self.base.lower() < other.base.lower()

    def __str__(self) -> str:
        return self.base


class Adjective(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    positive: str
    comparative: str | None
    superlative: str | None

    def __iter__(self):
        forms = [self.positive, self.comparative, self.superlative]
        return iter(forms)

    def __hash__(self):
        return hash(self.positive)

    def __lt__(self, other):
        return self.positive < other.positive

    def __str__(self) -> str:
        return self.positive


class Adverb(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    positive: str
    comparative: str | None
    superlative: str | None

    def __iter__(self):
        forms = [self.positive, self.comparative, self.superlative]
        return iter(forms)

    def __hash__(self):
        return hash(self.positive)

    def __lt__(self, other):
        return self.positive < other.positive

    def __str__(self) -> str:
        return self.positive


class Pronoun(BaseModel):

    model_config = ConfigDict(from_attributes=True)

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
