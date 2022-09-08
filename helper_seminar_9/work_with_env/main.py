"""
Информация по os:
    https://docs.python.org/3/library/os.html
    https://pythonworld.ru/moduli/modul-os.html
Информация по python-dotenv:
    https://pypi.org/project/python-dotenv/
"""
import os
import pathlib
from dotenv import load_dotenv, dotenv_values


BASE_DIR = pathlib.Path(__file__).parent
ENV_FILE_PATH = BASE_DIR / '.env'
config = None

if ENV_FILE_PATH.exists():
    load_dotenv(ENV_FILE_PATH)
    config = dotenv_values(ENV_FILE_PATH)

# LOGIN = os.environ.get('LOGIN')

print(f"Мой логин - {os.environ.get('LOGIN')}")
print(f"Мой токен - {os.environ.get('TOKEN')}")
print(f"Конфиг переменных из моего файла - {config}")
print(dict(config))  # преобразовать в словарь и извлекать по ключам
