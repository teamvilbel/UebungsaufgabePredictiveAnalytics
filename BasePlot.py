import math

import pandas as pd
from matplotlib import pyplot
import missingno as msno

# CSV Collums TAA,TA,TIN,TIR,TSI,TIM,TIL,TIRE,TIP,TIT,TID,TSC,TAc
columns = ["TAA", "TA", "TIN", "TIR", "TSI", "TIM", "TIL", "TIRE", "TIP", "TIT", "TID", "TSC", "TAc"]

# TAA Alerts (@@ separated)
alertC = "TAA"

# TA Delay hour (before was in minutes) need to be compared with TIT column
delayHourC = "TA"

# TIN Train Model
trainModelC = "TIN"

# TIR Route
routeC = "TIR"

# TSI Station ID
stationIdC = "TSI"

# TIM Direction departura/arrival ==> can be converted to numbers
directionC = "TIM"

# TIL (http) Request with parameters
requestC = "TIL"

# TIRE Destination
destinationC = "TIRE"

# TIP Platform number
platformNumberC = "TIP"

# TIT Departure hour
departureHourC = "TIT"

# TID Date
dateC = "TID"

# TSC Station Name and ID
stationNameAndIdC = "TSC"

# TAc Delay in minutes ( TA - TIT, delayHourC - depatureHourC)
delayInMinutesC = "TAc"

# csv in einen dataframe einlesen
df = pd.read_csv("19.06.20_travels_Frankfurt.csv", header=0, index_col=0, na_values=[""])

 # löschen der ungültigen DS
df = df[dataset[delayInMinutesC] < -1]

# löschen der ausgefallenen Fahrten
df = df[dataset[alertC] != ' Fahrt fällt aus'] 

# print("x ", df[delayHourC])

# Show missing data as matrix
msno.matrix(df)
pyplot.show()

# Show missing data as bar-diagramm
msno.bar(df, color="green")
pyplot.show()

# Spalte mit TAc extrahieren und in eine Liste konvertieren
TAc = df["TAc"]
TAcList = TAc.values.tolist()
print(TAcList)

pyplot.scatter(TAcList, TAcList)
pyplot.show()
