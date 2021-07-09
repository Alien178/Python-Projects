import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random
import pandas as pd
import csv


df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()


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
mean = stats.mean(mean_list)
print("Mean of Sampling Distribution: ", mean)
print("Standard deviation of sampling distribution: ", stdev)


first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)
# print("stdev1",first_stdev_start, first_stdev_end)
# print("stdev2",second_stdev_start, second_stdev_end)
# print("stdev3",third_stdev_start,third_stdev_end)


df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()

mean_of_sample_one = stats.mean(data)
print("Mean of Sample One: ", mean_of_sample_one)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_one, mean_of_sample_one], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()


df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()

mean_of_sample_two = stats.mean(data)
print("Mean of Sample Two: ", mean_of_sample_two)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_two, mean_of_sample_two], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()


df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()

mean_of_sample_three = stats.mean(data)
print("Mean of Sample Three: ", mean_of_sample_three)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample_three, mean_of_sample_three], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()


z_score = (mean - mean_of_sample_two) / stdev
print("The z score is = ", z_score)