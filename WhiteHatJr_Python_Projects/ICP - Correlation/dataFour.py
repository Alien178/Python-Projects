import pandas as pd
import plotly.express as px
import csv
import numpy as np

# with open("Data/dataFour.csv") as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x="Size of TV", y="Average time spent watching TV in a week (hours)")
#     fig.show()

def getDataSource(DataPath):
    SizeOfTV = []
    AverageTimeSpentWatchingTvInAWeek = []

    with open(DataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            SizeOfTV.append(float(row["Size of TV"]))
            AverageTimeSpentWatchingTvInAWeek.append(float(row["Average time spent watching TV in a week (hours)"]))

    return {"x":SizeOfTV, "y":AverageTimeSpentWatchingTvInAWeek}

def findCorrelation(DataSource):
    correlation = np.corrcoef(DataSource["x"], DataSource["y"])
    print(correlation[0, 1])

def main():
    DataPath = "Data/dataFour.csv"
    DataSource = getDataSource(DataPath)
    findCorrelation(DataSource)

main()