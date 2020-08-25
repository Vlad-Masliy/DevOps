import csv
import json


def convert_csv_to_json(path_to_csv, path_to_json):
    cars_list = list()

    with open(path_to_csv) as cars:
        reader = csv.DictReader(cars)
        for row in reader:
            cars_list.append({'Year': row['Year'], 'Make': row['Make'], 'Model': row['Model']})

    with open(path_to_json, 'w+') as result_file:
        json.dump(cars_list, result_file, indent=2)


convert_csv_to_json('', '')
