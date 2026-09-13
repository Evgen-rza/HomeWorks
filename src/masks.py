def get_mask_card_number(num_card: str) -> str:
    """Функция которая маскирует номер карты пользователя"""

    if num_card.isdigit() and len(num_card) == 16:
        source_string = num_card.replace(num_card[6:-4], "******")
    else:
        return "Ошибка, некорректный номер карты. Карта должна содержать 16 цифр"

    new_list_nums = []
    for i in range(0, len(source_string), 4):
        new_list_nums.append(source_string[i : i + 4])
    return " ".join(new_list_nums)


def get_mask_account(bank_account: str) -> str:
    """Функция которая маскирует номер счета пользователя"""
    if len(bank_account) >= 6:
        bank_account_mask = bank_account.replace(bank_account[:-4], "**")

    elif len(bank_account) < 6:
        bank_account_mask = "Ошибка, некорректный номер счета. Счет должен содержать не менее 6 цифр"

    return bank_account_mask
