import unittest
from unittest.mock import mock_open, patch

# Импорт чистый, так как путь к src задан в pytest.ini
from src.utils import read_file


class TestUtilsReadFile(unittest.TestCase):
    """Тесты для функции read_file из модуля utils.py."""

    @patch("os.path.exists")
    def test_file_not_found(self, mock_exists):
        """Файл не найден -> возвращает пустой список."""
        mock_exists.return_value = False
        self.assertEqual(read_file("data/operations.json"), [])

    @patch("os.path.exists")
    def test_file_is_empty(self, mock_exists):
        """Файл пустой -> возвращает пустой список."""
        mock_exists.return_value = True
        with patch("builtins.open", mock_open(read_data="")):
            self.assertEqual(read_file("data/operations.json"), [])

    @patch("os.path.exists")
    def test_file_contains_not_a_list(self, mock_exists):
        """В JSON передан словарь вместо списка -> пустой список."""
        mock_exists.return_value = True
        bad_json = '{"status": "success", "message": "not a list"}'
        with patch("builtins.open", mock_open(read_data=bad_json)):
            self.assertEqual(read_file("data/operations.json"), [])

    @patch("os.path.exists")
    def test_file_invalid_json(self, mock_exists):
        """JSON поврежден (синтаксическая ошибка) -> пустой список."""
        mock_exists.return_value = True
        corrupted_json = "[{'id': 1, 'amount': 100,]"
        with patch("builtins.open", mock_open(read_data=corrupted_json)):
            self.assertEqual(read_file("data/operations.json"), [])

    @patch("os.path.exists")
    def test_file_successful_load(self, mock_exists):
        """Успешное чтение валидного списка транзакций."""
        mock_exists.return_value = True
        valid_json = '[{"id": 1, "operationAmount": {"amount": "100.00"}}]'
        with patch("builtins.open", mock_open(read_data=valid_json)):
            result = read_file("data/operations.json")
            self.assertEqual(result, [{"id": 1, "operationAmount": {"amount": "100.00"}}])


# if __name__ == "__main__":
#     unittest.main()