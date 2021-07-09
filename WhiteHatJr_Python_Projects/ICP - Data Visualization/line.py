import pandas as pd
import plotly.express as px

df = pd.read_csv("CSV-Files/line_chart.csv")

fig = px.line(df, x="Year", y="Per capita income", title="Per capita income", color="Country")

fig.show()
