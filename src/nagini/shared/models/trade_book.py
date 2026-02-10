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


class TradeBookData(BaseModel):
    data: TradeBook
