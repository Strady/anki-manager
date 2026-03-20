import json
from typing import TypedDict

from configuration import Configuration
from anki_client.constants import Fields
from models import NoteData
from utils import generate_audio_from_text, base64_encode


config = Configuration()


class BinaryDataDict(TypedDict):

    data: str
    filename: str
    fields: list[str]


def get_audio_front(card_name: str, text: str) -> BinaryDataDict:
    audio_front_name = f'{card_name}-{Fields.AUDIO_FRONT.value}.mp3'
    audio_front_bytes = generate_audio_from_text(text, rate=config.rate)
    audio_front_data = base64_encode(audio_front_bytes)
    return {
        'data': audio_front_data,
        'filename': audio_front_name,
        'fields': [str(Fields.AUDIO_FRONT.value)]
    }


def get_audio_back(card_name: str, explanation: str, example: str) -> dict:
    audio_back_name = f'{card_name}-{Fields.AUDIO_BACK.value}.mp3'
    text = f'{explanation}. Example: {example}'
    audio_back_bytes = generate_audio_from_text(text, rate=config.rate)
    audio_back_data = base64_encode(audio_back_bytes)
    return {
        'data': audio_back_data,
        'filename': audio_back_name,
        'fields': [str(Fields.AUDIO_BACK.value)]
    }


def get_image(card_name: str, filename: str) -> BinaryDataDict:
    images_file = config.images_dir / filename
    return {
        'data': base64_encode(images_file.read_bytes()),
        'filename': f'{card_name}-{filename}',
        'fields': [str(Fields.IMAGE.value)]
    }


def generate_note_payload(note_name: str, note_data: NoteData) -> dict:
    payload = {
        'deckName': config.deck,
        'modelName': config.model,
        'fields': {
            Fields.TEXT_FRONT.value: note_data.expression,
            Fields.TEXT_BACK.value: note_data.explanation,
            Fields.TEXT_EXAMPLE.value: note_data.example
        },
        'audio': [
            get_audio_front(note_name, note_data.expression),
            get_audio_back(note_name, note_data.explanation, note_data.example),
        ]
        # 'picture': [get_image(note_name, note_data.image)]
    }
    return payload


def get_nodes_data() -> list[NoteData]:
    return [
        NoteData.model_validate(note_data)
        for note_data
        in json.loads(config.notes_source.read_text())
    ]
