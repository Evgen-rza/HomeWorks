import pytest


@pytest.fixture
def my_number():
    return "1234567891234567"


@pytest.fixture
def my_number_long():
    return "1234567891234567891"


@pytest.fixture
def my_number_empty():
    return ""


@pytest.fixture
def my_number_short():
    return "123"


@pytest.fixture
def my_number_list():
    return "Привет мир"


@pytest.fixture
def my_state_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def my_state_2():
    return [
        {"id": 49428829, "state": "EXECUTED", "date": "2020-07-09T18:35:29.512364"},
        {"id": 339719570, "state": "EXECUTED", "date": "2017-01-30T02:08:58.425572"},
        {"id": 594286727, "state": "CANCELED", "date": "2016-11-16T21:27:25.241689"},
        {"id": 615364591, "state": "CANCELED", "date": "2019-12-24T08:21:33.419441"},
    ]
