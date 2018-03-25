import csv
import json

from pprint import pprint


data = {}

with open('csv/bairros.csv') as file:
    csvfile = csv.reader(file)

    for row in list(csvfile):
        if row[0] not in data.keys():
            data[row[0]] = {}

        if row[1] not in data[row[0]].keys():
            data[row[0]][row[1]] = []

        if row[2] not in data[row[0]][row[1]]:
            data[row[0]][row[1]].append(row[2])

with open('data.json', 'w') as file:
    json.dump(data, file, sort_keys=True, indent=2)
