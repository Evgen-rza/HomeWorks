# filename - определяет куда будут записываться логи: в файл или консоль
def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def wrapper(func):  # func - мы должны декорировать. Возвращает функцию-обертку wrapper
        def inner(*args, **kwargs):
            if not filename:  # логируем начало в консоли или в файле
                print(f"Функция {func.__name__} начала работу")
            else:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(f"Функция {func.__name__} начала работу\n")
            try:
                res = func(*args, **kwargs)
                if not filename:  # логиним успешную работу
                    print(f"Функция {func.__name__} выполнена успешно, результат: {res}")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Функция {func.__name__} выполнена успешно, результат: {res}\n")
                return res
            except Exception as e:
                if not filename:  # логиним ошибку
                    print(f"Ошибка в {func.__name__}: {e}")
                    print(f"Входные параметры: args={args}, kwargs={kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"Ошибка в {func.__name__}: {e}\n")
                        f.write(f"Входные параметры: args={args}, kwargs={kwargs}\n")
                raise

        return inner

    return wrapper

# @log()
# def my_function(x, y):
#     return x + y
#
#
# my_function(23, "10")
