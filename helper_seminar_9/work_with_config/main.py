"""
Информация по configparse:
    https://docs.python.org/3/library/configparser.html
"""
import pathlib
from configparser import ConfigParser


BASE_DIR = pathlib.Path(__file__).parent
CONFIG_PATH = BASE_DIR / 'my_values.conf'

config = ConfigParser()
config.read(CONFIG_PATH)

print(f"Секции в конфигурационном файле - {config.sections()}")

TOKEN = config.get('base', 'TOKEN')
DEBUG = config.getboolean('base', 'DEBUG')
PORT = config.getint('database', 'PORT')
EMPTY = config.getint('database', 'EMPTY', fallback='666')

print(f"TOKEN = {TOKEN}, type = {type(TOKEN)}\n"
      f"DEBUG = {DEBUG}, type = {type(DEBUG)}\n"
      f"PORT = {PORT}, type = {type(PORT)}\n"
      f"EMPTY = {EMPTY}, type = {type(EMPTY)}")