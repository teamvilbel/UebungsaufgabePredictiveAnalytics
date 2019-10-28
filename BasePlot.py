import math

import pandas as pd
from matplotlib import pyplot

# csv in einen dataframe einlesen
ts = pd.read_csv("19.06.20_travels_Frankfurt.csv", header=0, index_col=0)
pyplot.plot(ts)
