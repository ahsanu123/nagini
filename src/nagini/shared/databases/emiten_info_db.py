from sqlalchemy.orm import Mapped, mapped_column
from nagini.shared.databases.base_db import BaseDb


class EmitenInfoDb(BaseDb):
    __tablename__ = "emiten_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    symbol: Mapped[str]
    sector: Mapped[str]
    name: Mapped[str]
    icon_url: Mapped[str]
    uma: Mapped[bool]
    previous: Mapped[int]
    price: Mapped[int]
    percentage: Mapped[float]
    sub_sector: Mapped[str]
