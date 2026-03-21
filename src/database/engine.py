from sqlalchemy import create_engine

from configuration import config


engine = create_engine(
    url=f'sqlite:///{config.words_db_path}',
    echo=config.db_echo
)
