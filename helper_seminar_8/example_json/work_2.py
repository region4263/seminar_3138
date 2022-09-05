from importlib.resources import path
import json
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent


data = {'test': 'test', 'text': 'Привет мир', 'data': ['test', 'test', 'text', 'Привет мир']}

with open(ROOT_DIR / 'dataset' / 'json_example_2.json', 'w', encoding='utf-8') as fw:
    json.dump(data, fw, ensure_ascii=False, indent=2)

with open(ROOT_DIR / 'dataset' / 'json_example_2.json', 'r', encoding='utf-8') as fr:
    dataset = json.load(fr)
    print(dataset, type(dataset))
    