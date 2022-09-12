from operator import add, sub, mul, truediv


def operation(a: float, op: str, b: float) -> float:
    """ Считает арифметические операции для двух чисел и вернёт
        округлённый результат """
    opers = {'+': add, '-': sub, '*': mul, '/': truediv}
    callback = opers.get(op)
    if not callback:
        raise ArithmeticError('operator unknown')
    return round(callback(a, b), 2)


def get_list_elements(expression: str) -> list:
    """ Преобразует строку в список элементов
        example: '(1+2.2)*3' -> ['(', 1.0, '+', 2.2, ')', '*', 3.0]"""
    spam = ''
    massiv = []
    for simbol in expression:
        if simbol in '+-*/()':
            if spam:
                massiv.extend([float(spam), simbol])
            else:
                massiv.append(simbol)
            spam = ''
        elif simbol.isnumeric() or simbol == '.':
            spam += simbol
    else:
        if spam:
            massiv.append(float(spam))
    return massiv


def mass_operation(arr: list):
    """ Получает выражения уже без скобок и рекурсивно
        считает до конечного результата """
    for s in '*/+-':
        start = 0
        while s in arr:
            finish = len(arr) - 1
            try:
                idx = arr.index(s, start, finish)
                a, op, b = arr[idx - 1:idx + 2]
                result = operation(a, op, b)
                arr = arr[:idx - 1] + [result] + arr[idx + 2:]
                start = idx + 1
            except ValueError:
                break
    if not len(arr) > 1:
        return arr[0]
    return mass_operation(arr)


def doing_simple(massiv: list) -> list:
    """ Извлекает из списка выражение в скобках, считает и заменяет
        результатом всё выражение в исходном списке """
    while '(' in massiv:
        for i in range(len(massiv) - 1, -1, -1):
            if not massiv[i] == '(':
                continue
            for j in range(i, len(massiv)):
                if not massiv[j] == ')':
                    continue
                result = mass_operation(massiv[i + 1:j])
                massiv = massiv[:i] + [result] + massiv[j+1:]
                break
    return massiv
