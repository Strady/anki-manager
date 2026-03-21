from sqlalchemy import create_engine

# TODO: move to configuration
DATABASE_URL = "sqlite:////var/anki_manager/words.db"

engine = create_engine(DATABASE_URL, echo=True)
