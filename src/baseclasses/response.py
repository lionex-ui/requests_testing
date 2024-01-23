import requests
from typing import Union

from src.enums.global_enums import *
from src.pydantic_schemas.post import *


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class Main:
    def __init__(self, response: Union[requests.models.Response]):
        self.response = response
        self.Global: Global = Global(self)


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class Global(Main):
    def __init__(self, main: Main):
        self.main = main

    def assert_status_code(self, status_code: Union[int, list]):
        response_status_code = self.main.response.status_code

        if isinstance(status_code, list):
            assert response_status_code in status_code, Errors.STATUS_CODE.value.format(
                status_code=response_status_code,
                expected=status_code
            )
        elif isinstance(status_code, int):
            assert response_status_code == status_code, Errors.STATUS_CODE.value.format(
                status_code=response_status_code,
                expected=status_code
            )
        else:
            raise TypeError("Unsupported type of status_code")

        return self.main

    def assert_structure(self, schema):
        response_json = self.main.response.json()

        schema.model_validate(response_json)

        return self.main


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
