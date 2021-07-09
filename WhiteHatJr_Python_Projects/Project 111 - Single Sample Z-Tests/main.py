import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()


# fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
# fig.show()


mean = stats.mean(data)
stdev = stats.stdev(data)
# print("Mean of Popultion: ", mean)
# print("Standard Deviation of Popultion:- ", stdev)


def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    
    mean = stats.mean(dataset)
    return mean


mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)


stdev = stats.stdev(mean_list)
# mean = stats.mean(mean_list)
# print("Mean of Sampling Distribution: ", mean)
# print("Standard Deviation of Sampling Distribution: ", stdev)


# fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = "MEAN"))
# fig.show()

# print("Standard Deviation of Sampling Distribution: ", stdev)


first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)

# print("stdev_one", first_stdev_start, first_stdev_end)
# print("stdev_two", second_stdev_start, second_stdev_end)
# print("stdev_three", third_stdev_start, third_stdev_end)


# fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
# fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
# fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3 START"))
# fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
# fig.show()


# df = pd.read_csv("data1.csv")
# data = df["Math_score"].tolist()

# mean_of_sample_one = stats.mean(data)
# print("Mean of Sample One: ", mean_of_sample_one)

# fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [mean_of_sample_one, mean_of_sample_one], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
# fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
# fig.show()


# df = pd.read_csv("data2.csv")
# data = df["Math_score"].tolist()

# mean_of_sample_two = stats.mean(data)
# print("Mean of Sample Two", mean_of_sample_two)

# fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [mean_of_sample_two, mean_of_sample_two], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO HAD EXTRA CLASSES"))
# fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
# fig.show()


df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean_of_sample_three = stats.mean(data)
print("Mean of Sample Three", mean_of_sample_three)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_three, mean_of_sample_three], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()
