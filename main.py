from anki_client.constants import URL
from anki_client.notes_generation import get_nodes_data, generate_note_payload, NoteData
from anki_client.anki_connect_client import AnkiConnectClient, Note
from configuration import Configuration


config = Configuration()


def get_cache() -> list[str]:
    return config.cache_file.read_text().splitlines()


def update_cache(note_title: str) -> None:
    with open(config.cache_file, 'a') as f:
        f.write(f'{note_title}\n')


def get_note_name(note_data: NoteData) -> str:
    return note_data.expression.lower().replace(' ', '_')


def main() -> None:
    anki_client = AnkiConnectClient(url=URL)
    cache = get_cache()
    for note_data in get_nodes_data():
        note_name = get_note_name(note_data)
        if note_name not in cache:
            note_payload = generate_note_payload(note_name, note_data)
            note = Note.model_validate(note_payload)
            print(f'Publishing "{note_name}"')
            anki_client.publish_note(note=note)
            update_cache(note_name)
        else:
            print(f'Note "{note_name}" already exists')


if __name__ == '__main__':
    main()
