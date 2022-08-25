# Сгенерировать файл из чисел в диапазоне [-2, 2], используя утилиту utils/gen_4_30.py. Написать программу,
# считывающую все значения чисел из сгенерированного файла и выводящую в stdout только уникальные значения.

import os

file_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file_dir, "data_4_30.txt")


result = set()
with open(file_path, 'r') as fr:
    for i in fr:
        x, y = i.split()
        result.add(int(x))
        result.add(int(y))

print(result)  # {0, 1, 2, -1, -2}