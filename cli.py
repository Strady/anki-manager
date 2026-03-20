import json
import pathlib

import click

from configuration import config
from models import NoteData


class DeckReadError(Exception):
    pass


def load_deck(deck_file: pathlib.Path) -> list[NoteData]:
    if not deck_file.exists():
        return []
    text = deck_file.read_text()
    try:
        deck = json.loads(text)
    except json.JSONDecodeError:
        raise DeckReadError(f'{deck_file} is not valid JSON')
    if not isinstance(deck, list):
        raise DeckReadError(f'{deck_file} is not a JSON list')
    return [NoteData.model_validate(note) for note in deck]


def save_deck(deck_file: pathlib.Path, notes: list[NoteData]) -> None:
    notes_list = [note.model_dump() for note in notes]
    deck_file.write_text(json.dumps(notes_list, indent=2))


def add_note_to_deck(deck_file: pathlib.Path, note: NoteData) -> None:
    try:
        deck_data = load_deck(deck_file)
    except Exception as e:
        raise SystemExit(e)
    if any(existing_note == note for existing_note in deck_data):
        click.echo(f'\nNote "{note.expression}" already exists in {deck_file}')
    else:
        deck_data.append(note)
        save_deck(deck_file, deck_data)
        click.echo(f'\nNote "{note.expression}" added to {deck_file}')


@click.group()
def cli():
    pass


@cli.command('add-note')
@click.option('--deck', required=True, help='Deck name (e.g., fallout)')
def add_note(deck):
    deck_file = config.notes_archive_dir / f'{deck}.json'
    note = NoteData(
        expression=click.prompt('expression').strip(),
        explanation=click.prompt('explanation').strip(),
        example=click.prompt('example').strip()
    )
    add_note_to_deck(deck_file, note)


if __name__ == '__main__':
    cli()
