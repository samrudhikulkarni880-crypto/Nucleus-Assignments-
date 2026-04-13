import csv
from collections import Counter

def analyze_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    print("There are", len(data), "elements in CSV which has attributes:")
    print("->", ", ".join(reader.fieldnames))

    missing_age = []
    missing_country = []

    names = []
    ages = []
    countries = []

    for row in data:
        sr = row['sr.no']

        # Check missing
        if row['Age'].strip() == "":
            missing_age.append(sr)
        if row['Country'].strip() == "":
            missing_country.append(sr)

        # Collect data
        names.append(row['Name'])
        if row['Age'].strip() != "":
            ages.append(row['Age'])
        if row['Country'].strip() != "":
            countries.append(row['Country'])

    print("\nThere are", len(missing_age) + len(missing_country), "missing values:")
    if missing_age:
        print("-> Age of sr.no", ", ".join(missing_age))
    if missing_country:
        print("-> Country of sr.no", ", ".join(missing_country))

    # Duplicate check
    rows = [(row['Name'], row['Age'], row['Country']) for row in data]
    seen = {}
    duplicates = []

    for i, r in enumerate(rows):
        if r in seen:
            duplicates.append((seen[r], i+1))
        else:
            seen[r] = i+1

    print("\nThere are", len(duplicates), "duplicate values:")
    for d in duplicates:
        print("->", d[0], "AND", d[1])

    # Max frequency
    print("\nMAX in Name ->", Counter(names).most_common(1)[0])
    print("MAX in Age ->", Counter(ages).most_common(1)[0])
    print("MAX in Country ->", Counter(countries).most_common(1)[0])


# Run
analyze_csv("Q6.csv")