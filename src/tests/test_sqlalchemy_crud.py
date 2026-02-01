from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import now

from nagini.shared.databases.base_db import BaseDb
from nagini.shared.databases.price_db import PriceDb


db_engine = create_engine("sqlite:///test_db", echo=True)
_sessionFactory = sessionmaker(bind=db_engine)


def session_factory():
    BaseDb.metadata.create_all(db_engine)
    return _sessionFactory()


def test_create_price_db():
    price = PriceDb(
        formatted_date=datetime.now(), xlabel=0, value=129, percentage=2.8, change=19
    )
    with session_factory() as session:
        session.add(price)
        session.commit()
        pass


def test_read_price_db():
    pass


def test_update_price_db():
    pass


def test_delete_price_db():
    pass
