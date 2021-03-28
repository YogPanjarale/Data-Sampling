import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
# function to return mean of random sample of data


def random_set_of_mean(no: int):
    dataset = []
    for i in range(0, no):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean
# function to plot the mean on the graph


def show_fig(mean_list, mean: float, stdev: float):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[
                  0, 1], mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[stdev, stdev], y=[
                  0, 1], mode="lines", name="Standard Deviation"))
    fig.show()
# function to find the standard deviation of the sample data


def standard_deviation(no: int):
    mean_list = []
    for i in range(0, no):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = stats.stdev(mean_list)
    return std_deviation
    # print("sampling mean :- ", std_deviation)


def setup(no: int):
    mean_list = []
    for i in range(0, no):
        setOfMeans = random_set_of_mean(100)
        mean_list.append(setOfMeans)
    return mean_list
    # show_fig(mean_list)
    # mean = stats.mean(mean_list)
    # print("Mean of sampling distribution : ", mean)


if __name__ == "__main__":
    l = setup(100)
    mmean = random_set_of_mean(100)
    print(f"Mean of sample of data: {mmean}")
    stdev = standard_deviation(100)
    print(f"Standard Deviation of sample of data: {stdev}")
    show_fig(l, mmean, stdev)


population_mean = stats.mean(data)
print("population mean:- ", population_mean)
