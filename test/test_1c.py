import pytest
import requests

from src.enums.global_enums import *
from src.baseclasses.response import *


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class TestRequests:
    def test_ping(self):
        r = requests.get(RequestLinks.PING.value, verify=False)
        response_proc = Main(r)

        response_proc.Global.assert_status_code(200)
        response_proc.Global.assert_structure(PingRequest)

    @pytest.mark.parametrize(
        "user_id, user_username, user_phone",
        # map(lambda el: tuple(el), test_authentication)
        TestData.TEST_AUTHENTICATION.value
    )
    def test_auth(self, user_id, user_username, user_phone):
        body = {
            "from": {
                "id": user_id,
                "username": user_username
            },
            "params": {
                "number": user_phone
            }
        }

        r = requests.get(RequestLinks.AUTH.value, json=body, verify=False)
        response_proc = Main(r)

        response_proc.Global.assert_status_code(200)
        response_proc.Global.assert_structure(AuthRequest)

    @pytest.mark.parametrize(
        "user_id, user_username, user_phone, params",
        TestData.fill_test_filters_data()
    )
    def test_filters(self, user_id, user_username, user_phone, params):
        body = {
            "from": {
                "id": user_id,
                "username": user_username
            },
            "params": params
        }

        r = requests.get(RequestLinks.FILTERS.value, json=body, verify=False)
        response_proc = Main(r)

        response_proc.Global.assert_status_code(200)
        response_proc.Global.assert_structure(FiltersRequest)

    @pytest.mark.parametrize(
        "user_id, user_username, user_phone, params",
        TestData.fill_test_stocks_data()
    )
    def test_stocks(self, user_id, user_username, user_phone, params):
        body = {
            "from": {
                "id": user_id,
                "username": user_username
            },
            "params": params
        }

        r = requests.get(RequestLinks.STOCKS.value, json=body, verify=False)
        response_proc = Main(r)

        response_proc.Global.assert_status_code(200)
        response_proc.Global.assert_structure(StocksRequest)
