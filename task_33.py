"""
Написать функцию, принимающую один позиционных аргумент N (целое число). 
Функция должна возвращать словарь где ключами будут индексы от 1 до N включительно, 
а значениями для этих ключей являются строки, образованные из случайных чисел диапазона [10, 99], 
преобразованных в строку по формату <первое число> <второе число>. 
В режиме дозаписи сохранять вывод функции в файле dict_park.txt
"""
import random
import os

file_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file_dir, "dict_park.txt")


def make_dict(n: int) -> dict:
    result = {}
    for i in range(1, n + 1):
        x = random.randint(10, 99)
        result[i] = f"{x // 10} {x % 10}"
    return result


if __name__ == "__main__":
    n = int(input("Введите количество значений: "))
    with open("dict_park.txt", "a") as fout:
        fout.write(f"{make_dict(n)}\n")
