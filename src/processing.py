def filter_by_state(list_of_dict: list, key_state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    result_list = []  # итоговый список
    for i in list_of_dict:
        if i["state"] == key_state:
            result_list.append(i)
    return result_list


def sort_by_date(list_of_dict: list, sort_order: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание) и возвращает новый список, отсортированный по дате"""
    sorted_list_dict = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sorted_list_dict


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        True,
    )
)
