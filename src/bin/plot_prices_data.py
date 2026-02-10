from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from nagini.shared.models.prices import PricesData

BASE_DIR = Path(__file__).resolve().parent

schema_path = BASE_DIR / "../../schema/price_history.txt"


def plot_prices_data():
    with schema_path.open() as file:
        sample_json = json.load(file)
        prices_data = PricesData.model_validate(sample_json)

        x = [p.date for p in prices_data.data.prices]
        y = [p.value for p in prices_data.data.prices]

        _, ax = plt.subplots()
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        ax.plot(x, y)  # pyright: ignore[reportArgumentType]

        plt.show()


if __name__ == "__main__":
    plot_prices_data()
