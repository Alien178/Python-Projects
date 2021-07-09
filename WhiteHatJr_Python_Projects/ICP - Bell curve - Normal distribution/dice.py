import random
import plotly.express as px
import plotly.figure_factory as pff

result = []
count = []

for i in range(0, 100):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)

    result.append(dice_one + dice_two)
    count.append(i)

#fig = px.bar(x=result, y=count)
#fig.show()

fig = pff.create_distplot([result], ["Dice Result Graph"], show_hist=False)
fig.show()