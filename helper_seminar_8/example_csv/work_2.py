import csv
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent


with open(ROOT_DIR / 'dataset' / 'csv_example_1.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        print(row, ' - ', type(row))


with open(ROOT_DIR / 'dataset' / 'csv_example_2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    max_id = 1
    for row in reader:
        if max_id < int(row['id']):
            max_id = int(row['id'])
    
    with open(ROOT_DIR / 'dataset' / 'csv_example_2.csv', 'a') as csvfile:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writerow({'id': max_id + 1, 'second_name': "Иванович",
                         'first_name': "Иван",
                         'last_name': "Иванов"})
    