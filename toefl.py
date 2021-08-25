import csv
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")

toefl = df["TOEFL Score"].tolist()
chances = df["Chance of Admit"].tolist()

toefl2 = np.array(toefl)
chances2 = np.array(chances)

m,c = np.polyfit(toefl, chances2, 1)
x = 250
y = []

line = (m*x) + c
print("Chances of getting admission on 250 TOEFL is: " + str(line))
for x in toefl2:
    yvalue = (m*x)+c
    y.append(yvalue)


fig = px.scatter(x=toefl2, y=chances2)
fig.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y),
        y1 = max(y),
        x0 = min(toefl2),
        x1 = max(toefl2),
    )
])
fig.show()