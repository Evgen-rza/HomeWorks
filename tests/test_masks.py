import pytest

from src.masks import get_mask_account, get_mask_card_number


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
    return str([1])


def test_get_mask_card_number(my_number):
    assert get_mask_card_number(my_number) == "1234 56** **** 4567"
    assert get_mask_account(my_number) == "**4567"


def test_get_mask_card_number_long(my_number_long):
    assert get_mask_card_number(my_number_long) == "Ошибка, некорректный номер карты. Карта должна содержать 16 цифр"
    assert get_mask_account(my_number_long) == "**7891"


def test_get_mask_card_number_short(my_number_short):
    assert get_mask_card_number(my_number_short) == "Ошибка, некорректный номер карты. Карта должна содержать 16 цифр"
    assert (
        get_mask_account(my_number_short) == "Ошибка, некорректный номер счета. Счет должен содержать не менее 6 цифр"
    )


def test_get_mask_card_number_empty(my_number_empty):
    assert get_mask_card_number(my_number_empty) == "Ошибка, некорректный номер карты. Карта должна содержать 16 цифр"
    assert (
        get_mask_account(my_number_empty) == "Ошибка, некорректный номер счета. Счет должен содержать не менее 6 цифр"
    )


def test_get_mask_card_number_list(my_number_list):
    assert get_mask_card_number(my_number_list) == "Ошибка, некорректный номер карты. Карта должна содержать 16 цифр"
    assert (
        get_mask_account(my_number_list) == "Ошибка, некорректный номер счета. Счет должен содержать не менее 6 цифр"
    )
