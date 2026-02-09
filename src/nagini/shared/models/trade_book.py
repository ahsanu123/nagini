from datetime import time
from pydantic import BaseModel
from typing import List


class TradeValue(BaseModel):
    raw: int
    formatted: str


class TradeBookAction(BaseModel):
    lot: TradeValue
    frequency: TradeValue
    time: time


class TradeBook(BaseModel):
    buy: List[TradeBookAction]
    sell: List[TradeBookAction]

    model_config = {"extra": "ignore"}


class TradeBookData(BaseModel):
    data: TradeBook

    model_config = {"extra": "ignore"}
