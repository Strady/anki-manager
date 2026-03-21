from pydantic import BaseModel, Field
import requests
from constants import Fields


class NotePublishError(Exception):

    """
    Raised in case response "error" field if not null
    """


class Base64Data(BaseModel):

    data: str
    filename: str
    fields: list[str]


class Note(BaseModel):

    deck_name: str = Field(alias='deckName')
    model_name: str = Field(alias='modelName')
    fields: dict[str, str]
    audio: list[Base64Data]

    def __str__(self):
        return f'Note: "{self.fields[Fields.TEXT_FRONT]}"'


class NoteParams(BaseModel):

    note: Note


class NoteCreateRequest(BaseModel):

    action: str = 'addNote'
    version: int = 6
    params: NoteParams


class AnkiConnectClient:

    ignored_errors = {
        'cannot create note because it is a duplicate'
    }

    def __init__(self, url):
        self._url = url

    def _check_error(self, response: requests.Response) -> None:
        response_body = response.json()
        error = response_body['error']
        if error is not None and error not in self.ignored_errors:
            raise NotePublishError(error)

    def publish_note(self, note: Note) -> None:
        note_params = NoteParams(note=note)
        note_request = NoteCreateRequest(params=note_params)
        response = requests.post(self._url, json=note_request.model_dump(by_alias=True))
        self._check_error(response)
