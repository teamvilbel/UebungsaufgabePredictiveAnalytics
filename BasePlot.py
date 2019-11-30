import math

import pandas as pd
from matplotlib import pyplot
import missingno as msno
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import numpy as np  # linear algebra

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
# df = pd.read_csv("19.06.20_travels_Frankfurt.csv", header=0, index_col=0, na_values=[""])
'''
0 TAA   Nicht relevant
1 TA    Nur für die Berechnung fehlender Werte 
2 TIN   One-Hot-Encoding für die Linien (BSP.)
3 TIR   Nur relevant für erweiterte Auswertungen (Verspätungen anhand von Zwichenstationen)
4 TSI   Nicht relevant da alle Daten von uns immer von Frankfurt aus sind
5 TIM   One-Hot-Encoding für die arr = 0 dep = 1(BSP.)
6 TIL   Nicht relevant denke ich (HELP WANTED)
7 TIRE  One-Hot-Encoding für die Bahnhöfe (BSP.)
8 TIP   Entfernen vom ORT Gleisnummer / ID ist aussreichen ⇒ nur Gleise in FFM
9 TIT
10 TID
11 TSC  Nicht relevant da alle Daten von uns immer von Frankfurt aus sind
12 TAc  Fehler-Findung  / Neuberechnung
'''
df = pd.read_csv("19.06.20_travels_Frankfurt.csv",
                 header=0,
                 usecols=[0, 1, 2, 5, 7, 8, 9, 10, 11, 12],
                 parse_dates=["TID"],
                 na_values=[''],
                 names=columns
                 );

df.dataframeName = "19.06.20_travels_Frankfurt.csv";
# Vor dem Preprocessing
nRow, nCol = df.shape;
print("Befor preprocessing:");
print(f'There are {nRow} rows and {nCol} columns');

# Format Times ?
# df['TA'] = pd.to_datetime(df['TA'], format='%H:%M:%S').dt.time
# df['TIT'] = pd.to_datetime(df['TIT'], format='%H:%M:%S').dt.time

# löschen der ungültigen DS
df[delayInMinutesC] = df[delayInMinutesC].astype(int);
df[delayInMinutesC] = df[df[delayInMinutesC] >= 0];

# löschen der ausgefallenen Fahrten
# df = df[df["TAA"] != ' Fahrt fällt aus'];
df = df[df.TAA != ' Fahrt fällt aus'];
df.drop('TAA', axis=1);



nRow, nCol = df.shape;
print("After preprocessing:");
print(f'There are {nRow} rows and {nCol} columns');
print(df)
# plotPerColumnDistribution(df)

df.boxplot();
pyplot.show();