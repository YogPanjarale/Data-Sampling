import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
# no of entries
noE = 100
file1 = pd.read_csv("./hw_25000.csv")
print(file1.keys())
hf_ = file1['Height(Inches)'].to_list()
hf = []
wf_ = file1['Weight(Pounds)'].to_list()
wf = []
for i in range(0, noE):
    vh = random.randint(0, len(hf_))
    hf.append(hf_[vh])
    vw = random.randint(0, len(wf_))
    # print(wf_[vw])
    wf.append(wf_[vw])
print(f"Length L1: {len(hf_)}\nLength L2: {len(hf)}")
print(wf)
plot = ff.create_distplot([wf, hf], ["Weight", "Height"], show_hist=False)
meanw = stats.mean(wf)
meanh = stats.mean(hf)
stdevW = stats.stdev(wf)
stdevH = stats.stdev(hf)
print(f"Mean: {meanw} {meanh} Standard Deviation: {stdevW} {stdevH}")
plot.add_trace(go.Scatter(x=[meanh, meanh], y=[
               0, 1], mode="lines", name="Mean Height"))
plot.add_trace(go.Scatter(x=[meanw, meanw], y=[
               0, 1], mode="lines", name="Mean Weight"))
plot.add_trace(go.Scatter(x=[stdevH, stdevH], y=[0, 1],
                          mode="lines", name=" Standard Deviation Height"))
plot.add_trace(go.Scatter(x=[stdevW, stdevW], y=[0, 1],
                          mode="lines", name=" Standard Deviation Weight"))
plot.show()
