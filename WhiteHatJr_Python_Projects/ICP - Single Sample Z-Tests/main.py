import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics as stats
import plotly.graph_objects as go
import random

df = pd.read_csv("studentMarks.csv")
math_data = df["Math_score"].tolist()

def randomSetOFMeans():
    dataset = []

    for i in range(0, 100):
        random_index = random.randint(0, len(math_data) - 1)
        value = math_data[random_index]

        dataset.append(value)

    random_mean = stats.mean(dataset)

    return random_mean


mean_list = []

for i in range(0, 1000):
    mean = randomSetOFMeans()
    mean_list.append(mean)

sample_mean = stats.mean(mean_list)
sample_stdev = stats.stdev(mean_list)

print("Sample")
print(sample_mean, sample_stdev)

fig = ff.create_distplot([mean_list], ["Mean List"], show_hist=False)
fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 0.20], mode = "lines", name = "Mean"))


popul_mean = stats.mean(math_data)
popul_stdev = stats.stdev(math_data)

fsds, fsde = sample_mean - sample_stdev, sample_mean + sample_stdev
ssds, ssde = sample_mean - (2 * sample_stdev), sample_mean + (2 * sample_stdev)
tsds, tsde = sample_mean - (3 * sample_stdev), sample_mean + (3 * sample_stdev)


print("Population")
print(popul_mean, popul_stdev)


# df2 = pd.read_csv("data1.csv")
# data = df2["Math_score"].tolist()

# mean_of_sample_one = stats.mean(data)

# fig.add_trace(go.Scatter(x = [mean_of_sample_one, mean_of_sample_one], y = [0, 0.20], mode = "lines", name = "Mean Of Sample One"))
# fig.add_trace(go.Scatter(x = [fsde, fsde], y = [0, 0.20], mode="lines", name = "FSDE"))
# fig.show()

# fig.add_trace(go.Scatter(x=, y=, mode="lines", name=))

df2 = pd.read_csv("data3.csv")
data = df2["Math_score"].tolist()

mean_of_sample_one = stats.mean(data)

fig.add_trace(go.Scatter(x = [mean_of_sample_one, mean_of_sample_one], y = [0, 0.20], mode = "lines", name = "Mean Of Sample One"))
fig.add_trace(go.Scatter(x = [fsde, fsde], y = [0, 0.20], mode="lines", name = "FSDE"))
fig.add_trace(go.Scatter(x = [ssde, ssde], y = [0, 0.20], mode="lines", name = "SSDE"))
fig.add_trace(go.Scatter(x = [tsde, tsde], y = [0, 0.20], mode="lines", name = "TSDE"))
fig.show()

z_score = (sample_mean - mean_of_sample_one) / popul_stdev
print(z_score)