import csv
import pandas as pd

df = pd.read_csv("main.csv")

df.drop(["Unnamed: 0", "Unnamed: 6", "Star_name.1", "Distance.1", "Mass.1", "Radius.1", "Luminosity"], axis = 1, inplace = True)

print(df)

df.to_csv("final.csv")