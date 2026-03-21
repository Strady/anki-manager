import click
import sqlalchemy.exc

from database.session import get_session
import database.repositories.nouns as nouns_repo
import database.repositories.verbs as verbs_repo
import database.pydantic_models as db_pydantic_models


@click.group()
def add_word():
    pass


def validate_nonempty(ctx, param, value):
    if isinstance(value, str) and not value.strip():
        raise click.BadParameter(f"{param.name} cannot be empty")
    return value


@add_word.command()
@click.option('-s', '--singular', type=str, callback=validate_nonempty)
@click.option('-p', '--plural', type=str, callback=validate_nonempty)
def noun(singular: str | None, plural: str | None) -> None:
    click.echo(f'Input: {singular = } and {plural = }')
    if singular is None and plural is None:
        raise click.UsageError('Either singular or plural form must be specified')
    noun_model = db_pydantic_models.Noun(singular=singular, plural=plural)
    try:
        with get_session() as session:
            nouns_repo.create(session=session, noun=noun_model)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{noun_model}" is already in database')
    click.echo(f'"{noun_model}" was added to database')


def _parse_additional(ctx, param, value):
    if value is None:
        return set()
    value = validate_nonempty(ctx, param, value)
    try:
        return {form.strip() for form in value.split(',') if form.strip()}
    except Exception:
        error_msg = f'{param.name} must be passed as a comma-separated list: <word1>,<word2>,<word3>'
        raise click.BadParameter(error_msg)


@add_word.command()
@click.option('-v1', '--base', type=str, callback=validate_nonempty)
@click.option('-v2', '--past-simple', type=str, callback=validate_nonempty)
@click.option('-v3', '--past-participle', type=str, callback=validate_nonempty)
@click.option('-s', '--third-person', type=str, callback=validate_nonempty)
@click.option('-ing', '--present-participle', type=str, callback=validate_nonempty, required=False)
@click.option('-a', '--additional', type=str, callback=_parse_additional, required=False)
def verb(base: str,
         past_simple: str,
         past_participle: str,
         third_person: str,
         present_participle: str | None,
         additional: set[str]
         ) -> None:
    verb_model = db_pydantic_models.Verb(
        base=base,
        third_person=third_person,
        past_simple=past_simple,
        past_participle=past_participle,
        present_participle=present_participle,
        additional=additional
    )
    print(repr(verb_model))
    try:
        with get_session() as session:
            verbs_repo.create(session=session, verb=verb_model)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{verb_model}" is already in database')
    click.echo(f'"{verb_model}" was added to database')
