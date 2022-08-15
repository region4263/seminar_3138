"""
Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
"""

def search(source: str, research: str) -> int:
    s_1 = source.lower()
    s_2 = research.lower()
    return s_1.count(s_2)


if __name__ == '__main__':
    s1 = input('Введите большую строку: ')
    s2 = input('Введите искомую строку: ')
    print(f'Найдено вхождений: {search(s1, s2)}')
