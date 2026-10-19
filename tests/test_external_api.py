import unittest
from unittest.mock import patch
import requests

# 1. Изменили импорт
from src.external_api import convert_to_rub


class TestExternalAPI(unittest.TestCase):
    """Тесты для функции convert_to_rub из модуля external_api.py."""

    def test_currency_rub_no_api_call(self):
        tx = {"operationAmount": {"amount": "150.50", "currency": {"code": "RUB"}}}
        result = convert_to_rub(tx)
        self.assertEqual(result, 150.50)
        self.assertIsInstance(result, float)

    # 2. Указали полный путь src.external_api в patch
    @patch("src.external_api.os.getenv")
    @patch("requests.get")
    def test_currency_usd_success(self, mock_get, mock_getenv):
        mock_getenv.return_value = "fake_api_key"
        tx = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "result": 9500.75}

        result = convert_to_rub(tx)

        mock_get.assert_called_once_with(
            "https://apilayer.com",
            params={"from": "USD", "to": "RUB", "amount": 100.0},
            headers={"apikey": "fake_api_key"},
            timeout=10,
        )
        self.assertEqual(result, 9500.75)

    # 3. Указали полный путь src.external_api в patch
    @patch("src.external_api.os.getenv")
    @patch("requests.get")
    def test_api_returns_success_false(self, mock_get, mock_getenv):
        mock_getenv.return_value = "fake_api_key"
        tx = {"operationAmount": {"amount": "50.00", "currency": {"code": "EUR"}}}

        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": False, "error": {"info": "Invalid API key"}}

        result = convert_to_rub(tx)
        self.assertEqual(result, 0.0)

    # 4. Указали полный путь src.external_api в patch
    @patch("src.external_api.os.getenv")
    @patch("requests.get")
    def test_api_network_error(self, mock_get, mock_getenv):
        mock_getenv.return_value = "fake_api_key"
        tx = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}

        mock_get.side_effect = requests.RequestException("Timeout")

        result = convert_to_rub(tx)
        self.assertEqual(result, 0.0)


# if __name__ == "__main__":
#     unittest.main()