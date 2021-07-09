import pandas as pd
import plotly.express as px
import csv
import numpy as np

# with open("Data/dataThree.csv") as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
#     fig.show()

def getDataSource(DataPath):
    MarksInPercentage = []
    DaysPresent = []

    with open(DataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))

    return {"x":MarksInPercentage, "y":DaysPresent}

def findCorrelation(DataSource):
    correlation = np.corrcoef(DataSource["x"], DataSource["y"])
    print(correlation[0, 1])

def main():
    DataPath = "Data/dataThree.csv"
    DataSource = getDataSource(DataPath)
    findCorrelation(DataSource)

main()