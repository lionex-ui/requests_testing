from enum import Enum


class RequestLinks(Enum):
    PING = "https://localhost/api_bot/ping"
    AUTH = "https://localhost/api_bot/auth"
    FILTERS = "https://localhost/api_bot/catalogs"
    STOCKS = "https://localhost/api_bot/stock"


class Errors(Enum):
    STATUS_CODE = "Received status_code [{status_code}] is not equals to expected [{expected}]."


class TestData(Enum):
    TEST_AUTHENTICATION = [
        [1234567890, "1234567890", "1234567890"],
        [0, "0", "0"],
        [-1, "olga", 123],
        [799682148, "yyyyy_sas_mislam", "+380680637527"],
        [799682148, "yyyyy_sas_mislam", "+380977692857"],
        [-1, "yyyy_sas_mislam", "+380977692857"],
        [799682148, "Null", "+380977692857"]
    ]

    TEST_FILTERS_PARAMS = [
        {"product_kit": True, "model": True, "size": True, "open": True},
        {"product_kit": True, "model": False, "size": False, "open": False},
        {"product_kit": False, "model": True, "size": False, "open": False},
        {"product_kit": False, "model": False, "size": True, "open": False},
        {"product_kit": False, "model": False, "size": False, "open": True},
        {"product_kit": False, "model": False, "size": True, "open": True},
        {"product_kit": False, "model": True, "size": False, "open": True},
        {"product_kit": True, "model": False, "size": False, "open": True},
        {"product_kit": True, "model": False, "size": True, "open": False},
        {"product_kit": True, "model": True, "size": False, "open": False},
        {"product_kit": False, "model": True, "size": True, "open": False},
        {"product_kit": False, "model": True, "size": True, "open": True},
        {"product_kit": True, "model": True, "size": False, "open": True},
        {"product_kit": True, "model": False, "size": True, "open": True},
        {"product_kit": True, "model": True, "size": True},
        {"product_kit": True, "model": True, "open": True},
        {"product_kit": True, "open": True, "size": True},
        {"model": True, "open": True, "size": True},
        {"product_kit": True, "model": True},
        {"product_kit": True, "size": True},
        {"product_kit": True, "open": True},
        {"size": True, "model": True},
        {"size": True, "open": True},
        {"model": True, "open": True},
        {"model": True, "size": True},
        {"product_kit": True},
        {"open": True},
        {"model": True},
        {"size": True},
        {}
    ]

    TEST_STOCK_PARAMS = [
        {"warehouse": "finished_products"},
        {"warehouse": "123"},
        {}
    ]

    @classmethod
    def fill_test_filters_data(cls):
        temp = []

        for param in cls.TEST_FILTERS_PARAMS.value:
            for auth in cls.TEST_AUTHENTICATION.value:
                temp.append(auth + [param])

        return temp

    @classmethod
    def fill_test_stocks_data(cls):
        temp = []

        for param in cls.TEST_STOCK_PARAMS.value:
            for auth in cls.TEST_AUTHENTICATION.value:
                print(auth)
                temp.append(auth + [param])

        return temp
