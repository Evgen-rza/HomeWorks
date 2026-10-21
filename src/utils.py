import json
import os


def read_file(file_path: str) -> list:
    """Функция чтения файла со списком операций. Если файл пустой, содержит не список или не найден,
    возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []

            data_list = json.loads(content)

            if isinstance(data_list, list):
                return data_list
            return []
    except json.JSONDecodeError:
        return []
