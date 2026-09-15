import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Введите номер карты или счета"),
        ("Привет мир!", "Введите корректный номер карты или счета"),
        ("[1,2,3]", "Введите корректный номер карты или счета"),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "my_date,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-08-25T02:26:18.671407", "25.08.2022"),
        ("2020-05-20T02", "20.05.2020"),
    ],
)
def test_get_date(my_date, expected):
    assert get_date(my_date) == expected
