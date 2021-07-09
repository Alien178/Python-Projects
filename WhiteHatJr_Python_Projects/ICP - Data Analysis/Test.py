import pandas as pd
import plotly.express as px
import csv
import plotly.graph_objects as go


df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=['Level1', 'Level2', 'Level3', 'Level4'],
    orientation='h'
))

fig.show()