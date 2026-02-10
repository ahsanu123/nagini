from datetime import datetime
from pydantic import BaseModel, Field
from typing import List


class Price(BaseModel):
    date: datetime = Field(validation_alias="formatted_date")
    xlabel: int
    value: int
    percentage: float
    change: int


class Prices(BaseModel):
    prices: List[Price]


class PricesData(BaseModel):
    data: Prices
