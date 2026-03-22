import click
import sqlalchemy.exc

from database.session import get_session
import database.repositories.nouns as nouns_repo
import database.repositories.verbs as verbs_repo
import database.repositories.adjectives as adjectives_repo
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
    if singular is None and plural is None:
        raise click.UsageError('Either singular or plural form must be specified')
    noun_model = db_pydantic_models.Noun(singular=singular, plural=plural)
    try:
        with get_session() as session:
            nouns_repo.create(session=session, noun=noun_model)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{noun_model}" is already in database')
    click.echo(f'"{noun_model}" was added to database')


def parse_additional(ctx, param, value):
    if value is None:
        return set()
    value = validate_nonempty(ctx, param, value)
    try:
        return {form.strip() for form in value.split(',') if form.strip()}
    except Exception:
        error_msg = f'{param.name} must be passed as a comma-separated list: <word1>,<word2>,<word3>'
        raise click.BadParameter(error_msg)


def validate_third_person(ctx, param, value):
    value: str = validate_nonempty(ctx, param, value)
    if not value.endswith('s'):
        raise click.BadParameter(f'third person form must ends with "s"')
    return value


def validate_present_participle(ctx, param, value):
    if value is None:
        return value
    value: str = validate_nonempty(ctx, param, value)
    if not value.endswith('ing'):
        raise click.BadParameter(f'present participle form must ends with "ing"')
    return value


def validate_past_forms(irregular: bool, past_simple: str, past_participle: str) -> None:
    if irregular:
        return
    error_template = '{field} form must end with "ed"'
    if not past_simple.endswith('ed'):
        raise click.BadParameter(error_template.format(field='past simple'))
    if not past_participle.endswith('ed'):
        raise click.BadParameter(error_template.format(field='past participle'))


@add_word.command()
@click.option('-v1', '--base', type=str, callback=validate_nonempty)
@click.option('-v2', '--past-simple', type=str, callback=validate_nonempty)
@click.option('-v3', '--past-participle', type=str, callback=validate_nonempty)
@click.option('-s', '--third-person', type=str, callback=validate_third_person)
@click.option('-ing', '--present-participle', type=str, callback=validate_present_participle, required=False)
@click.option('-a', '--additional', type=str, callback=parse_additional, required=False)
@click.option('-i', '--irregular', is_flag=True, required=False)
def verb(base: str,
         past_simple: str,
         past_participle: str,
         third_person: str,
         present_participle: str | None,
         additional: set[str],
         irregular: bool
         ) -> None:
    validate_past_forms(irregular, past_simple, past_participle)
    verb_model = db_pydantic_models.Verb(
        base=base,
        third_person=third_person,
        past_simple=past_simple,
        past_participle=past_participle,
        present_participle=present_participle,
        additional=additional
    )
    try:
        with get_session() as session:
            verbs_repo.create(session=session, verb=verb_model)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{verb_model}" is already in database')
    click.echo(f'"{verb_model}" was added to database')


def validate_comparison_forms(exception: bool, comparative: str | None, superlative: str | None) -> None:
    if bool(comparative) ^ bool(superlative):   # check with XOR either both None or both not None:
        error_msg = 'comparative and superlative form must either both be specified or neither of them is specified'
        raise click.BadParameter(error_msg)
    if exception:
        return None
    if comparative is not None and not comparative.endswith('er'):
        raise click.BadParameter(f'comparative form must end with "er"')
    if superlative is not None and not superlative.endswith('est'):
        raise click.BadParameter(f'superlative form must end with "est"')


@add_word.command()
@click.option('-p', '--positive', type=str, callback=validate_nonempty)
@click.option('-c', '--comparative', type=str, callback=validate_nonempty)
@click.option('-s', '--superlative', type=str, callback=validate_nonempty)
@click.option('-e', '--exception', is_flag=True)
def adjective(positive: str, comparative: str, superlative: str, exception: bool) -> None:
    if not exception:
        validate_comparison_forms(exception, comparative, superlative)
    adjective_model = db_pydantic_models.Adjective(
        positive=positive,
        comparative=comparative,
        superlative=superlative
    )
    try:
        with get_session() as session:
            adjectives_repo.create(session=session, adjective=adjective_model)
    except sqlalchemy.exc.IntegrityError:
        raise click.ClickException(f'"{adjective_model}" is already in database')
    click.echo(f'"{adjective_model}" was added to database')
