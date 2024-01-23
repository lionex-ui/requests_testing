from typing import List, Any, Union
from pydantic import BaseModel, field_validator


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class PingRequest(BaseModel):
    status_code: int
    message: str
    data: list

    @field_validator("message")
    def message_content(cls, v: Any):
        if v != "Ok":
            raise ValueError("Received message [{message}] is not equals to \"Ok\"".format(
                message=v
            ))

        return v


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class DataAuth(BaseModel):
    result: str


class AuthRequest(BaseModel):
    status_code: int
    message: str
    data: List[DataAuth]


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

class DataModel(BaseModel):
    id: str
    name: str


class DataFilters(BaseModel):
    product_kit: List[DataModel] = None
    model: List[DataModel] = None
    size: List[DataModel] = None
    open: List[DataModel] = None


class FiltersRequest(BaseModel):
    status_code: int
    message: str
    data: List[DataFilters]


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class DataStocks(BaseModel):
    id: str
    name: str
    price: int
    quantity: Union[int, float]
    imageSrc: str


class StocksRequest(BaseModel):
    status_code: int
    message: str
    data: List[DataStocks]


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
