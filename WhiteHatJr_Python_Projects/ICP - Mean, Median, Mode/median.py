import csv

with open("HW-Data.csv", newline="") as f:
    data = csv.reader(f)
    fileData = list(data)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num =  fileData[i][1]
    newData.append(float(num))

newData.sort()
dataLen = len(newData)

if dataLen % 2 == 0:
    medianOne = float(newData[dataLen // 2])
    medianTwo = float(newData[dataLen // 2 - 1])
    median = medianOne + medianTwo / 2
    print(median)
else:
    median = float(newData[dataLen // 2])
    print(median)

print(dataLen)