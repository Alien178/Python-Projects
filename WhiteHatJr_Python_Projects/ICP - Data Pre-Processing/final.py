import csv

dataset_1 = []
dataset_2 = []

with open("1.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset_1.append(row)

with open("2_sorted_new.csv", "r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

main_headers = headers_1 + headers_2
main_planet_data = []

for index, data in enumerate(planet_data_1):
    main_planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("final_space.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(main_headers)
    csv_writer.writerows(main_planet_data)