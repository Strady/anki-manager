import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', case_sensitive=False)

    notes_archive_dir: pathlib.Path
    notes_cache_file: pathlib.Path
    rate: int


config = Configuration()
