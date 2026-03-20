from pydantic import BaseModel


class NoteData(BaseModel):
    expression: str
    explanation: str
    example: str

    def __eq__(self, other) -> bool:
        return self.expression == other.expression
