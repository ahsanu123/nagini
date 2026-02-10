from nagini.cli.nagini_cli_arg import NaginiCliArgsModel
from nagini.https.emiten_codes import EmitenCode
from nagini.https.price_history_httpx import PriceHistoryHttpx


bearer = """
"""


def test_emiten_info():
    args = NaginiCliArgsModel(credential=bearer, emitenCode=EmitenCode.BUMI)

    PriceHistoryHttpx.getPriceHistory(args)
