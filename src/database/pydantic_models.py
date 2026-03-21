from pydantic import BaseModel, ConfigDict


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
