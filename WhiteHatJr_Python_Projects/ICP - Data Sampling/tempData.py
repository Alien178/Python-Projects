import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics as stats
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
temp_data = df["temp"].tolist()

def randomSetOfMeans():
    data_temp = []

    for i in range(0, 100):
        random_index = random.randint(0, len(temp_data) - 1)
        value = temp_data[random_index]

        data_temp.append(value)

    temp_mean = stats.mean(data_temp)

    return temp_mean

def showFig(mean_list):

    sample_mean = stats.mean(mean_list)
    sample_stdev = stats.stdev(mean_list)

    print("Sample")
    print(sample_mean, sample_stdev)

    fig = ff.create_distplot([mean_list], ["Sample Distribution"], show_hist=False)
    fig.show()

def main():
    mean_list = []

    for i in range(0, 1000):
        mean = randomSetOfMeans()
        mean_list.append(mean)
    
    showFig(mean_list)

popul_mean = stats.mean(temp_data)
popul_sd = stats.stdev(temp_data)

print("Popul")
print(popul_mean, popul_sd)

main()

# fig = ff.create_distplot([temp_data], ["Temp Data"], show_hist=False)
# fig.add_trace(go.Scatter(x=[popul_mean, popul_mean], y=[0, 0.1], mode="lines", name="Mean"))
# fig.show()