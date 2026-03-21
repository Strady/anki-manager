import json

import click
import sqlalchemy.exc

from database.session import get_session
import database.repositories.nouns as nouns_repo
import database.repositories.verbs as verbs_repo


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
    try:
        with get_session() as session:
            nouns_repo.create(session=session, singular=singular, plural=plural)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{singular or plural}" is already in database')
    click.echo(f'"{singular or plural}" was added to database')


def _parse_additional(ctx, param, value):
    if value is None:
        return value
    value = validate_nonempty(ctx, param, value)
    try:
        additional_forms = [form.strip() for form in value.split(',') if form.strip()]
        return json.dumps(additional_forms)
    except Exception:
        error_msg = f'{param.name} must be passed as a comma-separated list: <word1>,<word2>,<word3>'
        raise click.BadParameter(error_msg)


@add_word.command()
@click.option('-v1', '--base', type=str, callback=validate_nonempty)
@click.option('-3rd', '--third-person', type=str, callback=validate_nonempty)
@click.option('-v2', '--past-simple', type=str, callback=validate_nonempty)
@click.option('-v3', '--past-participle', type=str, callback=validate_nonempty)
@click.option('-ing', '--present-participle', type=str, callback=validate_nonempty, required=False)
@click.option('-a', '--additional', type=str, callback=_parse_additional, required=False)
def verb(base: str,
         third_person: str,
         past_simple: str,
         past_participle: str,
         present_participle: str | None,
         additional: list[str] | None
         ) -> None:
    try:
        with get_session() as session:
            verbs_repo.create(
                session=session,
                base=base,
                third_person=third_person,
                past_simple=past_simple,
                past_participle=past_participle,
                present_participle=present_participle,
                additional=additional
            )
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{base}" is already in database')
    click.echo(f'"{base}" was added to database')
