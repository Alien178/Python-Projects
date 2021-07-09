import csv
import pandas as pd

#* Project 130
# df = pd.read_csv("main.csv")
# df.drop(["Unnamed: 0", "Unnamed: 6", "Star_name.1", "Distance.1", "Mass.1", "Radius.1", "Luminosity"], axis = 1, inplace = True)
# print(df)
# df.to_csv("final.csv")

df = pd.read_csv("main.csv")
df.drop(["Unnamed: 0"], axis = 1, inplace = True)

df["Radius"] = df["Radius"].apply(lambda x: x.replace("$", "").replace(",", "")).astype("float")
print(df.dtypes)

radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
gravity = []

for i in range(0, len(radius)):
    radius[i] *= 6.957e+8
    mass[i] *= 1.989e+30

def calculate_gravity(radius, mass):
    G = 6.674e-11

    for index in range(0, len(mass)):
        g = (mass[index] * G) / ((radius[index]) ** 2)
        gravity.append(g)

calculate_gravity(radius, mass)

df["Gravity"] = gravity

df.to_csv("final.csv")

print(df)
