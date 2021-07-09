import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics as stats
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = stats.mean(height_list)
weight_mean = stats.mean(weight_list)

height_median = stats.median(height_list)
weight_median = stats.median(weight_list)

height_mode = stats.mode(height_list)
weight_mode = stats.mode(weight_list)

height_stdev = stats.stdev(height_list)
weight_stdev = stats.stdev(weight_list)

print(height_mean, height_median, height_mode, height_stdev)
print(weight_mean, weight_median, weight_mode, weight_stdev)

hfsds, hfsde = height_mean - height_stdev, height_mean + height_stdev
hssds, hssde = height_mean - (2 * height_stdev), height_mean + (2 * height_stdev)
htsds, htsde = height_mean - (3 * height_stdev), height_mean + (3 * height_stdev)

wfsds, wfsde = weight_mean - weight_stdev, weight_mean + weight_stdev
wssds, wssde = weight_mean - (2 * weight_stdev), weight_mean + (2 * weight_stdev)
wtsds, wtsde = weight_mean - (3 * weight_stdev), weight_mean + (3 * weight_stdev)

#Height Lists
height_list_of_data_in_stdev_one = [data for data in height_list if data > hfsds and data < hfsde]
height_list_of_data_in_stdev_two = [data for data in height_list if data > hssds and data < hssde]
height_list_of_data_in_stdev_three = [data for data in height_list if data > htsds and data < htsde]

#Weight Lists
weight_list_of_data_in_stdev_one = [data for data in weight_list if data > wfsds and data < wfsde]
weight_list_of_data_in_stdev_two = [data for data in weight_list if data > wssds and data < wssde]
weight_list_of_data_in_stdev_three = [data for data in weight_list if data > wtsds and data < wtsde]

#Height Percentage
print("Height:")
print("List One: " + str((len(height_list_of_data_in_stdev_one) * 100) / len(height_list)))
print("List Two: " + str((len(height_list_of_data_in_stdev_two) * 100) / len(height_list)))
print("List Three: " + str((len(height_list_of_data_in_stdev_three) * 100) / len(height_list)))

#Weight Percentage
print("Weight:")
print("List One: " + str((len(weight_list_of_data_in_stdev_one) * 100) / len(weight_list)))
print("List Two: " + str((len(weight_list_of_data_in_stdev_two) * 100) / len(weight_list)))
print("List Three: " + str((len(weight_list_of_data_in_stdev_three) * 100) / len(weight_list)))