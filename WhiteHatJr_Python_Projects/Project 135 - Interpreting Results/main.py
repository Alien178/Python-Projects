import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("main.csv")

# df.drop(["Unnamed: 0"], axis = 1, inplace = True)

# print(df.dtypes)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

plt.gcf().canvas.set_window_title("Figure One")
plt.bar(name, mass)
plt.title("Name vs Mass")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.show()

plt.gcf().canvas.set_window_title("Figure Two")
plt.bar(name, radius)
plt.title("Name vs Radius")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.show()

plt.gcf().canvas.set_window_title("Figure Three")
plt.bar(name, distance)
plt.title("Name vs Distance")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

plt.gcf().canvas.set_window_title("Figure Four")
plt.bar(name, gravity)
plt.title("Name vs Gravity")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.show()