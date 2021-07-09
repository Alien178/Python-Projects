import math
import csv

global total
total = 0
global mean

with open("data.csv", newline="") as f:
    data = csv.reader(f)
    fileData = list(data)

data = fileData[0]

def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total/n

    return mean

squaredList = []

for i in data:
    a = int(i) - mean(data)
    a = a ** 2
    squaredList.append(a)

for j in squaredList:
    total = total + j

result = total / len(data)

standardDeviation = math.sqrt(result)

print(standardDeviation)
print(mean(data))