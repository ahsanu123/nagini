from typing import List
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from nagini.shared.databases.base_db import BaseDb


class FrequencyAndLotDb(BaseDb):
    __tablename__ = "frequency_and_lot"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    frequency: Mapped[BigInteger]
    lot: Mapped[BigInteger]


class TradebookDb(BaseDb):
    __tablename__ = "tradebook"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    buy: Mapped[List["frequency_and_lot"]] = relationship(back_populates="tradebook")
    sell: Mapped[List["frequency_and_lot"]] = relationship(back_populates="tradebook")
