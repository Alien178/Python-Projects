import csv
import plotly.express as px
import pandas as pd

with open("class2.csv", newline="") as f:
    data = csv.reader(f)
    fileData = list(data)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))

n = len(newData)
sum = 0

for i in newData:
    sum = sum + i

mean = sum/n

df = pd.read_csv("class2.csv")
fig = px.scatter(df, x='Student Number', y="Marks")
fig.update_layout(shapes=[dict(type="line", y0=mean, y1=mean, x0=0, x1=n)])
fig.update_yaxes(rangemode="tozero")
fig.show()

print(mean)