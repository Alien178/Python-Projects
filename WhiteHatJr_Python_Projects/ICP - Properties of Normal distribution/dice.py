import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics as stats
import plotly.graph_objects as go

result = []
count = []

for i in range(0, 1000):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)

    result.append(dice_one + dice_two)
    count.append(i)

mean = stats.mean(result)
median = stats.median(result)
mode = stats.mode(result)
stdev = stats.stdev(result)

print(mean, median, mode, stdev)

fsds, fsde = mean - stdev, mean + stdev
ssds, ssde = mean - (2 * stdev), mean + (2 * stdev)
tsds, tsde = mean - (3 * stdev), mean + (3 * stdev)

fig = ff.create_distplot([result], ["Dice Result Graph"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))

#fsds
fig.add_trace(go.Scatter(x = [fsds, fsds], y = [0, 0.17], mode = "lines", name = "fsds"))
fig.add_trace(go.Scatter(x = [fsde, fsde], y = [0, 0.17], mode = "lines", name = "fsde"))

#ssds
fig.add_trace(go.Scatter(x = [ssds, ssds], y = [0, 0.17], mode = "lines", name = "ssds"))
fig.add_trace(go.Scatter(x = [ssde, ssde], y = [0, 0.17], mode = "lines", name = "ssde"))

#tsds
fig.add_trace(go.Scatter(x = [tsds, tsds], y = [0, 0.17], mode = "lines", name = "tsds"))
fig.add_trace(go.Scatter(x = [tsde, tsde], y = [0, 0.17], mode = "lines", name = "tsde"))

fig.show()

#List 1
list_of_data_in_stdev_one = [data for data in result if data > fsds and data < fsde]

#List 2
list_of_data_in_stdev_two = [data for data in result if data > ssds and data < ssde]

#List 3
list_of_data_in_stdev_three = [data for data in result if data > tsds and data < tsde]

print("List One: " + str((len(list_of_data_in_stdev_one) * 100) / len(result)))
print("List Two: " + str((len(list_of_data_in_stdev_two) * 100) / len(result)))
print("List Three: " + str((len(list_of_data_in_stdev_three) * 100) / len(result)))