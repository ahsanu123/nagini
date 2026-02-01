# {
#     "date": "0",
#     "formatted_date": "2026-01-29 08:58:00",
#     "xlabel": "0",
#     "value": "510",
#     "percentage": "-10.53",
#     "change": -60,
#     "open": "",
#     "high": "",
#     "low": "",
#     "volume": ""
# },

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from nagini.shared.databases.base_db import BaseDb


class PriceDb(BaseDb):
    __tablename__ = "price"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    formatted_date: Mapped[DateTime] = mapped_column(DateTime)
    xlabel: Mapped[int]
    value: Mapped[int]
    percentage: Mapped[float]
    change: Mapped[int]
