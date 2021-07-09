import csv

# with open("scrapper.csv") as in_file:
#     with open("scrapper_new.csv", 'w') as out_file:
#         writer = csv.writer(out_file)
#         for row in csv.reader(in_file):
#             if any(row):
#                 writer.writerow(row)

with open('scrapper.csv') as input, open('scrapper_new.csv', 'w', newline = '') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)