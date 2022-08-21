import random


def get_double_args(N: int) -> str:
    """ Возвращает строку из двух случайных целых чисел из
        диапазона [-N, N], разделенных пробелом 
        
        example: '34 -13' """
    n = abs(N)
    return f'{random.randint(-n, n)} {random.randint(-n, n)}'


def main(count: int, n: int, filename: str = 'data_4_30.txt'):
    """ Генерирует файл 'data_4_30.txt' с кол-вом строк count
        count - кол-во строк в файле
        n - верхняя граница случайных чисел ([-n, n])
        filename - имя генерируемого файла"""
    if not isinstance(count, int):
        raise ValueError(f'count должен быть целым числом')
    count_rows = abs(count)
    with open(filename, 'w', encoding='utf-8') as fw:
        for _ in range(count_rows):
            fw.write(f'{get_double_args(n)}\n')


if __name__ == "__main__":
    # пример использования
    main(10, 100)
