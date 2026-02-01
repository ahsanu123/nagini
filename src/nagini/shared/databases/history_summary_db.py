# {
#     "date": "2026-01-30",
#     "close": 540,
#     "change": 15,
#     "value": 613606647000,
#     "volume": 11180500,
#     "frequency": 63076,
#     "foreign_buy": 109457431500,
#     "foreign_sell": 174634502000,
#     "net_foreign": -65177070500,
#     "open": 535,
#     "high": 580,
#     "low": 505,
#     "average": 549,
#     "change_percentage": 2.857142925262451
# },


from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from nagini.shared.databases.base_db import BaseDb


class HistorySummaryDb(BaseDb):
    __tablename__ = "history_summary"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[DateTime]
    open: Mapped[int]
    close: Mapped[int]
    change: Mapped[int]
    value: Mapped[BigInteger]
    volume: Mapped[BigInteger]
    frequency: Mapped[BigInteger]
    foreign_buy: Mapped[BigInteger]
    foreign_sell: Mapped[BigInteger]
    net_foreign: Mapped[BigInteger]
    high: Mapped[int]
    low: Mapped[int]
    average: Mapped[int]
    change_percentage: Mapped[float]
