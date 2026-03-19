import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):

    model_config = SettingsConfigDict(env_file='../.env', case_sensitive=False)

    images_dir: pathlib.Path
    notes_source: pathlib.Path
    cache_file: pathlib.Path
    model: str
    deck: str
    rate: int


config = Configuration()
