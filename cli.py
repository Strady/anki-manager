import json
import pathlib

import click

from configuration import config
from models import NoteData
import words_archive.words_extractor


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
@click.option('-d', '--deck', required=True, help='Deck name (e.g., fallout)')
def add_note(deck):
    deck_file = config.notes_archive_dir / f'{deck}.json'
    note = NoteData(
        expression=click.prompt('expression').strip(),
        explanation=click.prompt('explanation').strip(),
        example=click.prompt('example').strip()
    )
    add_note_to_deck(deck_file, note)


@cli.command('extract-words')
@click.option('-f', '--file', required=True, help='Text file path')
@click.option('-e',
              '--extractor',
              type=click.Choice(['fallout', 'gachiakuta']),
              required=True,
              help='Extracting function'
              )
@click.option('-t', '--total', is_flag=True, help='To show total words count')
def extract_words(file: str, extractor: str, total: bool) -> None:
    try:
        with open(file) as f:
            text = f.readlines()
    except (FileNotFoundError, IsADirectoryError) as e:
        raise SystemExit(e)
    extraction_method = words_archive.words_extractor.extractors[extractor]
    words = extraction_method(text)
    print(*extraction_method(text), sep='\n')
    if total:
        print(f'total: {len(words)}')


@cli.command('list-words')
@click.option('--noun', is_flag=True, help='Show nouns')
@click.option('--verb', is_flag=True, help='Show verbs')
@click.option('--adjective', is_flag=True, help='Show adjectives')
@click.option('--pronoun', is_flag=True, help='Show pronouns')
def list_words(noun: bool, verb: bool, adjective: bool, pronoun: bool) -> None:
    from words_archive.nouns import noun_objects
    from words_archive.verbs import verb_objects
    from words_archive.adjectives import adjective_objects
    from words_archive.pronouns import pronouns_objects, indefinite
    if noun:
        print(f'Nouns in archive (total {len(noun_objects)}):')
        for word in sorted(noun_objects):
            print(word)
    if verb:
        print(f'Verbs in archive (total {len(verb_objects)}):')
        for word in sorted(verb_objects):
            print(word)
    if adjective:
        print(f'Adjectives in archive (total {len(adjective_objects)}):')
        for word in sorted(adjective_objects):
            print(word)
    if pronoun:
        print(f'Pronouns in archive (total {len(pronouns_objects) + len(indefinite)}):')
        complex_pronouns = list(str(pronoun) for pronoun in pronouns_objects)
        for word in sorted(complex_pronouns + list(indefinite)):
            print(word)


if __name__ == '__main__':
    cli()
