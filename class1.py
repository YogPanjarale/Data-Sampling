import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
file1 = pd.read_csv("./data.csv")
noEntries = 1000
list1 = file1["average"].to_list()
list2 = []
# random.choices(list1,100)
for i in range(0, noEntries):
    v = random.randint(0, len(list1))
    list2.append(list1[v])
print(f"Length L1: {len(list1)}\nLength L2: {len(list2)}")
mean = stats.mean(list1)
stdev = stats.stdev(list1)
print(f"Mean: {mean} Standard Deviation: {stdev}")
plot = ff.create_distplot([list1], ["Averavge"], show_hist=False)
plot.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
plot.add_trace(go.Scatter(x=[stdev, stdev], y=[0, 1],
                          mode="lines", name=" Standard Deviation"))
plot.show()
