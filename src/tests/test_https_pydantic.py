from pydantic import BaseModel
from pydantic.types import datetime


class HttpxWithPydanticDatetime(BaseModel):
    httpxDate: datetime


def test_pydantic_date():
    json_response = {"httpxDate": "2026-01-29 16:14:00"}

    data = HttpxWithPydanticDatetime.model_validate(json_response)
    print(data)
