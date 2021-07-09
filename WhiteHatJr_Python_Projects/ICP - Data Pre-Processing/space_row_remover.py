import csv

with open("final_space.csv") as input, open("final.csv", "w", newline = '') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)