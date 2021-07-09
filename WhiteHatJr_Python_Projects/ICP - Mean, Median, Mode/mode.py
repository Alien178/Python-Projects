import csv
from collections import Counter

with open("HW-Data.csv", newline="") as f:
    data = csv.reader(f)
    fileData = list(data)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

n = len(newData)
data = Counter(newData)

dictData = dict(data)

modeOne = []
modeTwo = []
modeThree = []

for a, v in dictData.items():
    a = float(a)
    if 50 < a < 60:
        if v == max(list(data.values())):
            modeOne.append(a)
    elif 60 < a < 70:
        if v == max(list(data.values())):
            modeTwo.append(a)
    elif 70 < a < 80:
        if v == max(list(data.values())):
            modeThree.append(a)

if len(modeOne) > len(modeTwo) and len(modeThree):
    print(modeOne)
elif len(modeTwo) > len(modeOne) and len(modeThree):
    print(modeTwo)
elif len(modeThree) > len(modeOne) and len(modeTwo):
    print(modeThree)
