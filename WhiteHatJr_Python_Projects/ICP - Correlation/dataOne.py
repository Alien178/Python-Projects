import pandas as pd
import plotly.express as px
import csv
import numpy as np

# with open("Data/dataOne.csv") as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x="Temperature", y="Ice-cream Sales")
#     fig.show()

def getDataSource(DataPath):
    Temperature = []
    IceCreamSales = []

    with open(DataPath) as f:
        df = csv.DictReader(f)
        for row in df:
            Temperature.append(float(row["Temperature"]))
            IceCreamSales.append(float(row["Ice-cream Sales"]))

    return {"x":IceCreamSales, "y":Temperature}

def findCorrelation(DataSource):
    correlation = np.corrcoef(DataSource["x"], DataSource["y"])
    print(correlation[0, 1])

def main():
    DataPath = "Data/dataOne.csv"
    DataSource = getDataSource(DataPath)
    findCorrelation(DataSource)

main()