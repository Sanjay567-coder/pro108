from pandas.core.arrays.categorical import factorize_from_iterables
import plotly_express as px
import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("mobile.csv")
fig = ff.create_distplot([df["Avg Rating"].to_list()],["Avg Rating"])
fig.show()