from pydantic import BaseModel


class NoteData(BaseModel):
    expression: str
    explanation: str
    example: str
