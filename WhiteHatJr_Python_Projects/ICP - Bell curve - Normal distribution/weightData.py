import csv
import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv("data.csv")
weight_list = df["Weight(Pounds)"].tolist()


fig = pff.create_distplot([weight_list], ["Weight List"], show_hist=False)
fig.show()