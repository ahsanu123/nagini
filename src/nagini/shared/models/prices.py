from datetime import datetime
from pydantic import AliasChoices, BaseModel, Field
from typing import Optional, List


class Price(BaseModel):
    date: datetime = Field(validation_alias="formatted_date")
    xlabel: int
    value: int
    percentage: float
    change: int

    model_config = {"extra": "ignore"}


class Prices(BaseModel):
    prices: List[Price]


class PricesData(BaseModel):
    data: Prices
