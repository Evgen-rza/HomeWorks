def get_mask_card_number(num_card: str) -> str:
    """Функция которая маскирует номер карты пользователя"""

    if num_card.isdigit() and len(num_card) == 16:
        source_string = num_card.replace(num_card[6:-4], "******")
    else:
        return "Ошибка. Необходимо ввести 16 цифр. Проверьте правильность ввода номера карты"

    new_list_nums = []
    for i in range(0, len(source_string), 4):
        new_list_nums.append(source_string[i : i + 4])
    return " ".join(new_list_nums)


print(get_mask_card_number("9994567891234552"))


def get_mask_account(bank_account: str) -> str:
    """Функция которая маскирует номер счета пользователя"""
    if len(bank_account) >= 6:
        bank_account_mask = bank_account.replace(bank_account[:-4], "**")

    elif len(bank_account) == 5:
        bank_account_mask = bank_account.replace(bank_account[:-4], "*")

    elif len(bank_account) <= 4:
        bank_account_mask = bank_account.replace(bank_account[:-4], "")

    return bank_account_mask


print(get_mask_account("459446512123"))
