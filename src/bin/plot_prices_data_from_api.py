from nagini.https.price_history_httpx import insert_into_prices
from typing import Any
from time import sleep
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import List
from nagini.https.emiten_codes import EmitenCode
from nagini.https.price_history_httpx import PriceHistoryHttpx
from nagini.cli.nagini_cli_arg import NaginiCliArgsModel
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from nagini.shared.models.prices import PricesData


bearer = """
"""


def plot_prices_data_from_api():
    prices_data_list: List[PricesData] = []
    count = 25

    allCodes = EmitenCode.getAllCodes()
    for idx, code in enumerate(allCodes):
        args = NaginiCliArgsModel(credential=bearer, emitenCode=code)
        prices_data = PriceHistoryHttpx.getPriceHistory(args)

        print(f"{idx}/{len(allCodes)} -> {code.value}")
        prices_data_list.append(prices_data)

        print(f"inserting {code.value} to db. length -> {len(prices_data.data.prices)}")
        insert_into_prices(prices_data, code.value)

        if idx >= count:
            break

    # Grid dimensions
    n_cols = 5
    n_rows = 5

    fig, axes_ori = plt.subplots(n_rows, n_cols, figsize=(50, 10))

    # Flatten axes for easy indexing
    axes: List[Axes] = axes_ori.flatten().tolist()

    for idx, ax in enumerate(axes):
        data = prices_data_list[idx]
        x = [p.date for p in data.data.prices]
        y = [p.value for p in data.data.prices]

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax.set_title(allCodes[idx].value)
        ax.plot(x, y)  # pyright: ignore[reportArgumentType]

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_prices_data_from_api()
