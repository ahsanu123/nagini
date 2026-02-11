from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from nagini.shared.databases.base_db import BaseDb
from nagini.shared.databases.price_db import PriceDb


db_engine = create_engine("sqlite:///test_db", echo=True)
_sessionFactory = sessionmaker(bind=db_engine)


def session_factory():
    BaseDb.metadata.create_all(db_engine)
    return _sessionFactory()


def test_create_price_db():
    price = PriceDb(
        date=datetime.now(), xlabel=0, value=129, percentage=2.8, change=19, code="BUMI"
    )
    with session_factory() as session:
        session.add(price)
        session.commit()


def test_read_price_db():
    with session_factory() as session:
        all_prices = session.query(PriceDb).all()
        print(all_prices)
        print("len of data", len(all_prices))
        assert len(all_prices) > 0


def test_update_price_db():
    with session_factory() as session:
        price = session.query(PriceDb).first()
        print("initial price", price)

        if price is not None:
            price.date = datetime.now()
            session.commit()
            print("updated price", price)


def test_delete_price_db():
    with session_factory() as session:
        price = session.query(PriceDb).first()
        print(price)

        if price is not None:
            session.delete(price)
            session.commit()


def test_crud_price():
    print("=========================================")
    test_create_price_db()

    print("=========================================")
    test_read_price_db()

    print("=========================================")
    test_update_price_db()

    print("=========================================")
    test_delete_price_db()
