import pandas as pd
import plotly.express as px
import csv
import numpy as np

# with open("Data/dataTwo.csv") as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x="sleep in hours", y="Coffee in ml")
#     fig.show()

def getDataSource(DataPath):
    SleepInHours = []
    CoffeeInMl = []

    with open(DataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            SleepInHours.append(float(row["sleep in hours"]))
            CoffeeInMl.append(float(row["Coffee in ml"]))

    return {"x":SleepInHours, "y":CoffeeInMl}

def findCorrelation(DataSource):
    correlation = np.corrcoef(DataSource["x"], DataSource["y"])
    print(correlation[0, 1])

def main():
    DataPath = "Data/dataTwo.csv"
    DataSource = getDataSource(DataPath)
    findCorrelation(DataSource)

main()