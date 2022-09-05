from importlib.resources import path
import json
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent


data = {'test': 'test', 'text': 'Привет мир', 'data': {'test': 'test', 'text': 'Привет мир'}}

with open(ROOT_DIR / 'dataset' / 'json_example_1.json', 'w', encoding='utf-8') as fw:
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    fw.write(json_str)
    print(type(json_str))


with open(ROOT_DIR / 'dataset' / 'json_example_1.json', 'r', encoding='utf-8') as fr:
    data_str = fr.read()
    dataset = json.loads(data_str)
    print(dataset, type(dataset))
