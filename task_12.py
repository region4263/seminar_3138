"""
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
def calculate(n: int) -> int:
    """Рассчитывает элемент последовательности `3n + 1`"""
    return 3 * n + 1


if __name__ == "__main__":
    N = int(input('Введите N: '))
    # our_dict = {}
    our_dict = dict()
    for idx, v in enumerate(range(1, N + 1), start=1):
        # print(idx, v)
        our_dict[idx] = calculate(v)

    print(our_dict)
        
"""
Введите N: 6
{1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""