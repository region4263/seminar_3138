# получение данных от пользователя - view
def get_rational() -> str:
    return input("Введите выражение (example: 6/10+1.5): ")


def get_complex() -> str:
    pass


# выбор типа чисел для работы  -> view
def show_menu() -> str:
    result = input("Выберите тип чисел для работы (Q - рациональные, C - комплексные): ")
    return result.upper()


# вывод результата
def show_result(result: float):
    print(f'Результат вычислений {result:.2f}')