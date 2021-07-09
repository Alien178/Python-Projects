import csv
import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].tolist()


fig = pff.create_distplot([height_list], ["Height List"], show_hist=False)
fig.show()