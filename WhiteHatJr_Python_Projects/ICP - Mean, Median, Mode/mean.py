import csv

with open("HW-Data.csv", newline="") as f:
    data = csv.reader(f)
    fileData = list(data)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

n = len(newData)
sum = 0

for i in newData:
    sum = sum + i

mean = sum/n

print(mean)