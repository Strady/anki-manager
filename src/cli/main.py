import json
import pathlib

import click

from cli.add_note import add_note
from database.pydantic_models import NoteData
import words_archive.words_extractor
from cli.add_word import add_word

from words_archive.words_db import KNOWN_WORDS
import database.repositories.nouns as nouns_repo
import database.repositories.verbs as verbs_repo
import database.repositories.adjectives as adjectives_repo
import database.repositories.adverbs as adverbs_repo
import database.repositories.prepositions as prepositions_repo
from database.session import get_session


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


cli.add_command(add_word)
cli.add_command(add_note)


def _get_known_words():
    with get_session() as session:
        KNOWN_WORDS.update(nouns_repo.get_all(session=session))
        KNOWN_WORDS.update(verbs_repo.get_all(session=session))
        KNOWN_WORDS.update(adjectives_repo.get_all(session=session))
        KNOWN_WORDS.update(adverbs_repo.get_all(session=session))
        KNOWN_WORDS.update(prepositions_repo.get_all(session=session))
    return KNOWN_WORDS


def read_file(file: str) -> set[str]:
    try:
        with open(file) as f:
            return set(f.readlines())
    except (FileNotFoundError, IsADirectoryError) as e:
        raise SystemExit(e)


def get_excluded_words(file: str) -> set[str]:
    text = read_file(file)
    return {word.strip('\n').lower() for word in text}


@cli.command('extract-words')
@click.option('-f', '--file', required=True, help='Text file path')
@click.option('-e',
              '--extractor',
              type=click.Choice(['fallout', 'gachiakuta']),
              required=True,
              help='Extracting function'
              )
@click.option('-t', '--total', is_flag=True, help='To show total words count')
@click.option('--exclude', required=False, help='File with words that should be excluded')
def extract_words(file: str, extractor: str, total: bool, exclude: str | None) -> None:
    text = read_file(file)
    extraction_method = words_archive.words_extractor.extractors[extractor]
    words = extraction_method(text)
    words -= _get_known_words()
    if exclude is not None:
        words -= get_excluded_words(exclude)
    print(*words, sep='\n')
    if total:
        print(f'total: {len(words)}')


@cli.command('list-words')
@click.option('--noun', is_flag=True, help='Show nouns')
@click.option('--verb', is_flag=True, help='Show verbs')
@click.option('--adjective', is_flag=True, help='Show adjectives')
@click.option('--pronoun', is_flag=True, help='Show pronouns')
def list_words(noun: bool, verb: bool, adjective: bool, pronoun: bool) -> None:
    from src.words_archive.nouns import noun_objects
    from src.words_archive.verbs import verb_objects
    from src.words_archive.adjectives import adjective_objects
    from src.words_archive.pronouns import pronouns_objects, indefinite
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


@cli.command('count-words')
def count_words() -> None:
    with get_session() as session:
        nouns = nouns_repo.count(session)
        verbs = verbs_repo.count(session)
        adjectives = adjectives_repo.count(session)
        adverbs = adverbs_repo.count(session)
        prepositions = prepositions_repo.count(session)
    total = nouns + verbs + adjectives + adverbs + prepositions
    click.echo(f'nouns: {nouns}')
    click.echo(f'verbs: {verbs}')
    click.echo(f'adjectives: {adjectives}')
    click.echo(f'adverbs: {adverbs}')
    click.echo(f'prepositions: {prepositions}')
    click.echo(f'total: {total}')


def main():
    cli()


if __name__ == "__main__":
    main()
