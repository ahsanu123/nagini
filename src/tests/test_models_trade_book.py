from nagini.shared.models.trade_book import TradeBookData
import json


raw_string = """
{
    "message": "Successfully loaded tradebook data chart",
    "data": {
        "buy": [
            {
                "frequency": {
                    "raw": "930",
                    "formatted": "930"
                },
                "lot": {
                    "raw": "156892",
                    "formatted": "156,892"
                },
                "time": "09:00"
            },
            {
                "frequency": {
                    "raw": "1295",
                    "formatted": "1,295"
                },
                "lot": {
                    "raw": "238635",
                    "formatted": "238,635"
                },
                "time": "09:01"
            },
            {
                "frequency": {
                    "raw": "1609",
                    "formatted": "1,609"
                },
                "lot": {
                    "raw": "289016",
                    "formatted": "289,016"
                },
                "time": "09:02"
            }
        ],

        "sell": [
            {
                "frequency": {
                    "raw": "930",
                    "formatted": "930"
                },
                "lot": {
                    "raw": "156892",
                    "formatted": "156,892"
                },
                "time": "09:00"
            },
            {
                "frequency": {
                    "raw": "1295",
                    "formatted": "1,295"
                },
                "lot": {
                    "raw": "238635",
                    "formatted": "238,635"
                },
                "time": "09:01"
            },
            {
                "frequency": {
                    "raw": "1609",
                    "formatted": "1,609"
                },
                "lot": {
                    "raw": "289016",
                    "formatted": "289,016"
                },
                "time": "09:02"
            }
        ]
    }
}
"""

raw_json = json.loads(raw_string)


def test_model_trade_book():
    trade_book_data = TradeBookData.model_validate(raw_json)
    print(trade_book_data.model_dump_json(indent=2))
