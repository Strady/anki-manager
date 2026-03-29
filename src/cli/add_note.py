import click

from anki_client.anki_connect_client import AnkiConnectClient, Note
from anki_client.notes_generation import generate_note_payload
from configuration import config
from database.pydantic_models import NoteData


def get_note_data() -> NoteData:
    return NoteData(
        expression=input('expression: ').strip(),
        explanation=input('explanation: ').strip(),
        example=input('example: ').strip()
    )


def get_existing_notes(deck: str) -> set[str]:
    client = AnkiConnectClient(url=config.anki_desktop_url)
    notes = client.get_notes(deck=deck)
    return {note['fields']['Text Front']['value'].lower() for note in notes}


def check_note_exists(note_data: NoteData, deck: str) -> None:
    click.echo('Checking note does not exist...')
    existing_notes = get_existing_notes(deck)
    if note_data.expression.lower() in existing_notes:
        raise click.ClickException(f'{note_data.expression.lower()} is already exists in "{deck}" deck')


def publish_note(note_data: NoteData, deck: str) -> None:
    client = AnkiConnectClient(url=config.anki_desktop_url)
    click.echo('Generating note payload...')
    note_payload = generate_note_payload(note_data=note_data, deck=deck)
    note = Note.model_validate(note_payload)
    click.echo('Publishing note...')
    client.publish_note(note=note)
    click.echo(f'Note "{note_data.expression}" is published')


@click.command("add-note")
@click.option('-d', '--deck', required=True, help='Deck name (e.g., fallout)')
def add_note(deck):
    note_data = get_note_data()
    check_note_exists(note_data, deck)
    publish_note(note_data, deck)
