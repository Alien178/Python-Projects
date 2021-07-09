import csv
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats

df = pd.read_csv("data2.csv")
average_data = df["average"].tolist()

def randomSetOFMeans():
    dataset = []

    for i in range(0, 100):
        random_index = random.randint(0, len(average_data) - 1)
        value = average_data[random_index]

        dataset.append(value)

    random_mean = stats.mean(dataset)

    return random_mean

def showFig(mean_list):

    average_mean = stats.mean(mean_list)
    average_stdev = stats.stdev(mean_list)

    print("Sample")
    print(average_mean, average_stdev)

    fig = ff.create_distplot([mean_list], ["Sample Distribution"], show_hist=False)
    fig.show()

def main():
    mean_list = []

    for i in range(0, 1000):
        mean = randomSetOFMeans()
        mean_list.append(mean)

    showFig(mean_list)

print("Popul")
popul_mean = stats.mean(average_data)
popul_stdev = stats.stdev(average_data)

print(popul_mean, popul_stdev)

main()