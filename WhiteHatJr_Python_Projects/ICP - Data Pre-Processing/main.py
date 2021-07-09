import csv

data = []

with open("2.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for value in planet_data:
    value[0] = value[0].lower()

planet_data.sort(key = lambda planet_data: planet_data[0])

with open("2_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)