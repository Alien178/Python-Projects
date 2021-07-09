import csv
import pandas as pd

data_1 = []
data_2 = []

with open("1.csv", "r") as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data_1.append(i)
        
with open("2_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        data_2.append(i)

headers_1 = data_1[0]
stars_data_1 = data_1[1:]

headers_2 = data_2[0]
stars_data_2 = data_2[1:]

h = headers_1 + headers_2

main_stars_data =[]

for index, data in enumerate(stars_data_1):
    main_stars_data.append(stars_data_1[index] + stars_data_2[index])

with open("finall.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(main_stars_data)