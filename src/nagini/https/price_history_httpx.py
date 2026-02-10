from string import Template
from typing import Final
from nagini.cli.nagini_cli_arg import NaginiCliArgsModel
import httpx

from nagini.shared.models.prices import PricesData


class PriceHistoryHttpx:
    endpoint: Final[str] = (
        "https://exodus.stockbit.com/charts/${CODE}/daily?timeframe=today"
    )

    @classmethod
    def getPriceHistory(cls, arg: NaginiCliArgsModel):
        template = Template(cls.endpoint)

        parsedEndpoint = template.substitute(CODE=arg.emitenCode.value)

        response = httpx.get(
            parsedEndpoint, headers={"authorization": arg.credential.strip()}
        )

        response.raise_for_status()
        prices = PricesData.model_validate(response.json())

        print(prices.model_dump_json(indent=2))
