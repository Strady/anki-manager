import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', case_sensitive=False)

    notes_archive_dir: pathlib.Path
    notes_cache_file: pathlib.Path
    rate: int
    words_db_path: pathlib.Path
    db_echo: bool
    anki_desktop_url: str = 'http://localhost:8765'
    note_model: str = 'FalloutModel'


config = Configuration()
