from src.generators import filter_by_currency, transaction_descriptions


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


def test_filter_by_currency_empty(my_list_empty):
    iteration = filter_by_currency(my_list_empty, "USD")
    result = next(iteration, None)  # Если элементов нет, next() вернет None вместо ошибки
    assert result is None  # Проверяем, что вернулся именно None


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


def test_transaction_descriptions_empty(my_list_empty):
    iteration = transaction_descriptions(my_list_empty)
    result = next(iteration, None)  # Если элементов нет, next() вернет None вместо ошибки
    assert result is None  # Проверяем, что вернулся именно None
