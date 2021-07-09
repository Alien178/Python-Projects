import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

##Data Frame##
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()


##Variables##
mean = sum(data) / len(data)
stdev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)


##Standard Deviation 1, 2, 3 (Start and End)##
first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)


##Displot with Traces##
fig = ff.create_distplot([data], ["reading scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 (START)"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 (END)"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 (START)"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 (END)"))
fig.show()


##List##
list_of_data_within_1_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_2_stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_3_stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]


##Percent##
percent_of_data_within_1_stdev = len(list_of_data_within_1_stdev) * 100.0 / len(data)
percent_of_data_within_2_stdev = len(list_of_data_within_2_stdev) * 100.0 / len(data)
percent_of_data_within_3_stdev = len(list_of_data_within_3_stdev) * 100.0 / len(data)


##Printing##
print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))
print("Standard Deviation: " + str(stdev))
print(str(percent_of_data_within_1_stdev) + "% of data within standard deviation 1")
print(str(percent_of_data_within_2_stdev) + "% of data within standard deviation 2")
print(str(percent_of_data_within_3_stdev) + "% of data within standard deviation 3")