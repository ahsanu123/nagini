from pathlib import Path
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

FILE_PATH = Path(__file__).resolve().parent

# TODO: chnage this to use config
db_path = FILE_PATH / "../../../../test_db"
db_engine = create_engine(f"sqlite:///{db_path.absolute()}", echo=True)

_sessionFactory = sessionmaker(bind=db_engine)


def create_session() -> Session:
    return _sessionFactory()
