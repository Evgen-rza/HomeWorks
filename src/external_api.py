import os
from typing import Any, Dict
import requests
from dotenv import load_dotenv

# Ищем .env на один уровень выше, так как этот файл лежит в папке src
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

# Адрес для Exchange Rates Data API
API_URL = "https://apilayer.com"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Принимает транзакцию и возвращает её сумму в рублях.
    Если валюта отличная от RUB, обращается к Exchange Rates Data API.
    """
    # Извлекаем данные из вложенной структуры транзакции
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount", "0")
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    # Переводим строковую сумму в float
    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        return 0.0

    # Если транзакция уже в рублях, возвращаем сумму без вызова API
    if currency_code == "RUB":
        return amount

    # Проверяем наличие ключа доступа
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("API ключ EXCHANGE_RATES_API_KEY не найден в переменных окружения.")

    params = {"from": currency_code, "to": "RUB", "amount": amount}
    headers = {"apikey": api_key}

    try:
        response = requests.get(API_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            return float(data["result"])
        else:
            # Вместо падения приложения возвращаем 0.0 при ошибке API
            return 0.0

    except (requests.RequestException, KeyError, ValueError):
        # Возвращаем 0.0, если пропал интернет или API недоступен
        return 0.0