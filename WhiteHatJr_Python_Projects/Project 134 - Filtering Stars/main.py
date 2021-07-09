import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('main.csv')

print(df)

df["Distance"] = df["Distance"].apply(lambda x: x.replace("$", "").replace(",", "")).astype("float")

distances = []

print(df.dtypes)

for i in df.Distance:
    if i <= 100:
        distances.append(True)
    else:
        distances.append(False)

ISDistance = pd.Series(distances)
print(ISDistance.head())

star_distance = df[ISDistance]
star_distance.reset_index(inplace = True, drop = True)
print(star_distance.head())
print(star_distance.shape)

gravity = []

for i in star_distance.Gravity:
    if i >= 150 and i <= 350:
        gravity.append(True)
    else:
        gravity.append(False)

ISGravity = pd.Series(gravity)
print(ISGravity.head())

filteredData = star_distance[ISGravity]
print(filteredData.head())
print(filteredData.shape)

filteredData.reset_index(inplace = True, drop = True)
print(filteredData.head())

filteredData.to_csv("filtered.csv")