from masks import get_mask_card_number, get_mask_account

def mask_account_card(my_string: str) -> str:
    '''Функция обработки информации номеров карт и счетов'''
    result = '' # Определяем текст/название карт или счета
    list_simbols = my_string.split() # разбиваем строку на отдельные элементы списка
    if len(list_simbols[-1]) == 16: # для номера карты
        if len(list_simbols) == 3:
            result += " ".join(list_simbols[0:2])
        elif len(list_simbols) == 2:
            result += " ".join(list_simbols[0:1])
        return f"{result} {get_mask_card_number(list_simbols[-1])}"
    else: # для номера счета
        result += list_simbols[0]
        return f"{result} {get_mask_account(list_simbols[-1])}"


print(mask_account_card("Platinum 8990922113665229")) # Возвращать строку с замаскированным номером

from datetime import datetime
'''Функция возвращает дату в формате: день.месяц.год'''
def get_date(date_string: str) -> str:
  result = datetime.fromisoformat(date_string) # читает строку с датой, временем и микросекундами
  return result.strftime("%d.%m.%Y") # метод strftime форматирует полученную дату в нужный вид

print(get_date("2024-03-11T02:26:18.671407")) # Вернуть в формате "ДД.ММ.ГГГГ"