from nagini.shared.databases.session_factory import create_session
from nagini.shared.databases.price_db import PriceDb
from string import Template
from typing import Final, List
from nagini.cli.nagini_cli_arg import NaginiCliArgsModel
import httpx

from nagini.shared.models.prices import PricesData


class PriceHistoryHttpx:
    endpoint: Final[str] = (
        "https://exodus.stockbit.com/charts/${CODE}/daily?timeframe=today"
    )

    @classmethod
    def getPriceHistory(cls, arg: NaginiCliArgsModel) -> PricesData:
        template = Template(cls.endpoint)

        parsedEndpoint = template.substitute(CODE=arg.emitenCode.value)

        response = httpx.get(
            parsedEndpoint, headers={"authorization": arg.credential.strip()}
        )

        response.raise_for_status()
        prices = PricesData.model_validate(response.json())

        return prices


def insert_into_prices(prices: PricesData, code: str):
    pricesDb: List[PriceDb] = []

    for price in prices.data.prices:
        pdb = PriceDb(
            price.date, price.xlabel, price.value, price.percentage, price.change, code
        )
        pricesDb.append(pdb)

    with create_session() as session:
        session.add_all(pricesDb)
        session.commit()
