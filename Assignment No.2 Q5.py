import csv
import json

vars = []

with open("Q5.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        vars.append(row)

# Convert to JSON
json_data = json.dumps(vars, indent=4)

print(json_data)