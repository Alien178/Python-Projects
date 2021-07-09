from collections import Counter
import csv

def getMean(totalWeight, totalEntries):

    mean = totalWeight / totalEntries
    print(f"Mean (Average) is -> {mean:2f}")

def getMedian(totalEntries, sortedData):

    if totalEntries % 2 == 0:

        median1 = float(sortedData[totalEntries//2])
        median2 = float(sortedData[totalEntries//2 - 1])
        median = (median1 + median2) / 2

    else:
        median = float(sortedData[totalEntries//2])
    
    print(f"Median is -> {median:2f}")

def getMode(sortedData):

    data = Counter(sortedData)

    modeDataRange = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }

    for weight, occurence in data.items():

        if 75 < weight < 85:
            modeDataRange["75-85"] += occurence

        elif 85 < weight < 95:
            modeDataRange["85-95"] += occurence

        elif 95 < weight < 105:
            modeDataRange["95-105"] += occurence

        elif 105 < weight < 115:
            modeDataRange["105-115"] += occurence

        elif 115 < weight < 125:
            modeDataRange["115-125"] += occurence

        elif 125 < weight < 135:
            modeDataRange["125-135"] += occurence

        elif 135 < weight < 145:
            modeDataRange["135-145"] += occurence

        elif 145 < weight < 155:
            modeDataRange["145-155"] += occurence

        elif 155 < weight < 165:
            modeDataRange["155-165"] += occurence

        elif 165 < weight < 175:
            modeDataRange["165-175"] += occurence

    modeRange, modeOccurence = 0, 0

    for range, occurence in modeDataRange.items():

        if occurence > modeOccurence:
            modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

    mode = float((modeRange[0] + modeRange[1]) / 2)
    print(f"Mode is -> {mode:2f}")

with open('HWData.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)


fileData.pop(0)

totalWeight = 0
totalEntries = len(fileData)
sortedData = []

for person_data in fileData:
    totalWeight += float(person_data[2])
    sortedData.append(float(person_data[2]))

sortedData.sort()

getMean(totalWeight, totalEntries)
getMedian(totalEntries, sortedData)
getMode(sortedData)