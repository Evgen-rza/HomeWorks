import pytest

from src.decorators import log


def test_console_logging_success(capsys):
    """Проверяет логирование успешного выполнения в консоль."""

    @log()
    def add(a, b):
        return a + b

    res = add(6, 11)

    assert res == 17  # Проверяем результат работы функции

    # Перехватываем вывод в консоль через capsys
    captured = capsys.readouterr()

    assert "Функция add начала работу" in captured.out
    assert "Функция add выполнена успешно, результат: 17" in captured.out


def test_console_logging_error(capsys):
    """Проверяет логирование ошибки и входных параметров в консоль."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):  # Проверяем, что ошибка пробрасывается дальше
        divide(26, 0)

    captured = capsys.readouterr()

    assert "Функция divide начала работу" in captured.out
    assert "Ошибка в divide: division by zero" in captured.out
    assert "Входные параметры: args=(26, 0), kwargs={}" in captured.out


def test_file_logging_success(tmp_path):
    """Проверяет логирование успешного выполнения в файл."""
    # Создаем путь к временному файлу, который pytest удалит сам
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def greet(name):
        return f"Hello, {name}"

    greet("Alice")

    content = log_file.read_text(encoding="utf-8")  # Читаем содержимое файла

    assert "Функция greet начала работу\n" in content
    assert "Функция greet выполнена успешно, результат: Hello, Alice\n" in content


def test_file_logging_error(tmp_path):
    """Проверяет логирование ошибки и входных параметров в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def fail_func():
        raise ValueError("Wrong value")

    with pytest.raises(ValueError):
        fail_func()

    content = log_file.read_text(encoding="utf-8")

    assert "Функция fail_func начала работу\n" in content
    assert "Ошибка в fail_func: Wrong value\n" in content
    assert "Входные параметры: args=(), kwargs={}\n" in content
