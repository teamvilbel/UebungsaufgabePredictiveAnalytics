import math

import pandas as pd
from matplotlib import pyplot
import missingno as msno

# csv in einen dataframe einlesen
ts = pd.read_csv("19.06.20_travels_Frankfurt.csv", header=0, index_col=0)

msno.matrix(ts)
pyplot.show()

# Spalte mit Passagieren extrahieren und in eine Liste konvertieren
TAc = ts["TAc"]
TAcList = TAc.values.tolist()

pyplot.plot(TAcList)
pyplot.show()

