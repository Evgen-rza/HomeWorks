import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# проверяем что функция корректно работает если установлена валюта USD
def test_filter_by_currency_usd(my_list):
    iteration = filter_by_currency(my_list, "USD")
    first_transaction = next(iteration)
    assert first_transaction == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


# проверяем что функция корректно работает если установлена валюта RUB
def test_filter_by_currency_rub(my_list):
    iteration = filter_by_currency(my_list, "RUB")
    first_transaction = next(iteration)
    assert first_transaction == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


# проверяем что функция корректно работает если передан пустой список
def test_filter_by_currency_empty(my_list_empty):
    iteration = filter_by_currency(my_list_empty, "USD")
    result = next(iteration, None)  # Если элементов нет, next() вернет None вместо ошибки
    assert result is None  # Проверяем, что вернулся именно None


# проверка вывода описания транзакции
def test_transaction_descriptions(my_list):
    iteration = transaction_descriptions(my_list)
    first_transaction = next(iteration)
    second_transaction = next(iteration)
    third_transaction = next(iteration)
    fourth_transaction = next(iteration)
    fifth_transaction = next(iteration)
    sixth_transaction = next(iteration, None)
    assert first_transaction == "Перевод организации"
    assert second_transaction == "Перевод со счета на счет"
    assert third_transaction == "Перевод со счета на счет"
    assert fourth_transaction == "Перевод с карты на карту"
    assert fifth_transaction == "Перевод организации"
    assert sixth_transaction is None


# проверка вывода описания транзакции если передан пустой список
def test_transaction_descriptions_empty(my_list_empty):
    iteration = transaction_descriptions(my_list_empty)
    result = next(iteration, None)  # Если элементов нет, next() вернет None вместо ошибки
    assert result is None  # Проверяем, что вернулся именно None


# проверка поочередного вывода номеров карт, преобразовали генератор в список.
@pytest.mark.parametrize(
    "start, stop, expected_list",
    [(2, 5, ["0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"])],
)
def test_card_number_generator_list(start, stop, expected_list):
    gen = card_number_generator(start, stop)
    assert list(gen) == expected_list


# проверка корректности вывода номеров карт
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1025, 1256, "0000 0000 0000 1025"),
        (200, 500, "0000 0000 0000 0200"),
        (25655555, 577777888, "0000 0000 2565 5555"),
        (9999999999999997, 9999999999999999, "9999 9999 9999 9997"),
    ],
)
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    assert next(gen) == expected


@pytest.mark.parametrize(
    "start, stop, match_message",
    [
        (15, 5, "Некорректно задан диапазон"),
        (-10, 30, "Числа должны быть больше нуля."),
        (3, -5, "Числа должны быть больше нуля."),
        (9999999999999997, 99999999999999999, "Число не может содержать более 16 цифр."),
    ],
)
def test_card_number_generator_errors(start, stop, match_message):
    # pytest.raises проверяет, что внутри блока кода упал именно ValueError
    # параметр match проверяет, что в тексте ошибки есть указанная подстрока
    with pytest.raises(ValueError, match=match_message):
        list(card_number_generator(start, stop))  # Вызываем генератор, чтобы он выполнил проверки
