import json
from nagini.shared.models.prices import PricesData


raw_string = """
{
    "data": {
        "cagr": "",
        "change": -45,
        "drawdown": "",
        "markingpoint": "{}",
        "percentage": "-7.89",
        "prices": [
            {
                "date": "0",
                "formatted_date": "2026-01-29 08:58:00",
                "xlabel": "0",
                "value": "510",
                "percentage": "-10.53",
                "change": -60,
                "open": "",
                "high": "",
                "low": "",
                "volume": ""
            },
            {
                "date": "1769652000000",
                "formatted_date": "2026-01-29 09:00:00",
                "xlabel": "1",
                "value": "496",
                "percentage": "-12.98",
                "change": -74,
                "open": "",
                "high": "",
                "low": "",
                "volume": ""
            },
            {
                "date": "0",
                "formatted_date": "2026-01-29 09:01:00",
                "xlabel": "2",
                "value": "490",
                "percentage": "-14.04",
                "change": -80,
                "open": "",
                "high": "",
                "low": "",
                "volume": ""
            }
        ]
    }
}
"""

raw_json = json.loads(raw_string)


def test_model_prices():
    prices_data = PricesData.model_validate(raw_json)
    print(prices_data.model_dump_json(indent=2))
