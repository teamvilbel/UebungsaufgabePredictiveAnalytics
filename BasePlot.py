import math
import sys

import pandas as pd
from matplotlib import pyplot
import numpy as np  # linear algebra
# OneHotEncoder
from pandas import Series
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# keine truncation für numpy
np.set_printoptions(threshold=sys.maxsize)
# keine truncation für pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

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
9 TIT   In lesbares Zeitformat übertragen
10 TID  In lesbares Zeitformat übertragen
11 TSC  Nicht relevant da alle Daten von uns immer von Frankfurt aus sind
12 TAc  Fehler-Findung  / Neuberechnung
'''
df = pd.read_csv("19.06.20_travels_Frankfurt.csv",
                 header=0,
                 usecols=[0, 1, 2, 5, 7, 8, 9, 12],
                 na_values=[''],
                 names=columns
                 );

df.dataframeName = "19.06.20_travels_Frankfurt.csv";
# Vor dem Preprocessing
nRow, nCol = df.shape;
print("Befor preprocessing:");
print(f'There are {nRow} rows and {nCol} columns');

# TAA   Nicht relevant / entfallende Fahrten entfernen
df = df[df.TAA != ' Fahrt fällt aus'];  # Löschen der Zeilen mit ausgefallenen Fahrten
df = df[df.TAA != ' Es verkehrt'];      # Löschen der Zeilen mit  Es verkehrt
df = df.drop('TAA', axis=1);  # Löschen der Spalte TAA

# TA    Nur für die Berechnung fehlender Werte
df['TA'] = pd.to_datetime(df['TA'], format='%H:%M').dt.time

# TIN   One-Hot-Encoding für die Linien
# le = LabelEncoder()  # LabelEncoder for TIN
# tin_le = le.fit_transform(df['TIN'].to_numpy(dtype=str))
#
# ohe = OneHotEncoder(sparse=False)  # OneHotEncoder for TIN
# Data_ohe = ohe.fit_transform(tin_le.reshape(-1, 1))
# print(Data_ohe)

# TIR   Nur relevant für erweiterte Auswertungen (Verspätungen anhand von Zwichenstationen)
# siehe einlesen der datei
# df = df.drop('TIR', axis=1);  # Löschen der Spalte TIR

# TSI   Nicht relevant da alle Daten von uns immer von Frankfurt aus sind
# siehe einlesen der datei
# df = df.drop('TSI', axis=1);  # Löschen der Spalte TSI

# TIM   One-Hot-Encoding für die arr = 0 dep = 1
le = LabelEncoder() # LabelEncoder for TIM
tim_le = le.fit_transform(df['TIM'].to_numpy(dtype=str))

ohe = OneHotEncoder(sparse=False) # OneHotEncoder for TIM
tim_ohe = ohe.fit_transform(tim_le.reshape(-1, 1))
# print(tim_ohe)

# TIL   Nicht relevant denke ich (HELP WANTED)
# siehe einlesen der datei
# df = df.drop('TIL', axis=1);  # Löschen der Spalte TIL

# TIRE  One-Hot-Encoding für die Bahnhöfe

# TIP   Entfernen vom ORT Gleisnummer / ID ist aussreichen ⇒ nur Gleise in FFM
# ds_TIP = df["TIP"]
# df["TIP"] = ds_TIP.replace(value='', inplace=True, regex=r'Frankfurt Hbf (tief)')
# df["TIP"] = ds_TIP.replace(value='', inplace=True, to_replace='Frankfurt Hbf (tief)')

# TIT   In lesbares Zeitformat übertragen
df['TIT'] = pd.to_datetime(df['TIT'], format='%H:%M').dt.time

#  TID  In lesbares Zeitformat übertragen
# siehe einlesen der Datei

#  TSC  Nicht relevant da alle Daten von uns immer von Frankfurt aus sind
# siehe einlesen der Datei

#  TAc  Fehler-Findung  / Neuberechnung

# löschen der ungültigen DS
df[delayInMinutesC] = df[delayInMinutesC].astype(int);
df[delayInMinutesC] = df[df[delayInMinutesC] >= 0];



nRow, nCol = df.shape;
print("After preprocessing:");
print(f'There are {nRow} rows and {nCol} columns');
x = df.describe(include='all')
print('Description:');
print(x)
# # Anz Fahrten pro End-Bahnhof
# df['TIRE'].hist(bins=12, xrot=90, xlabelsize=10, figsize=(20,10))
# pyplot.title("tire");
# pyplot.savefig("img/TIRE", bbox_inches="tight")
# pyplot.show()
#
# # Anz Fahrten pro Gleis
# df['TIP'].hist(bins=12, xrot=90, xlabelsize=10, figsize=(20,10))
# pyplot.title("TIP");
# pyplot.savefig("img/TIP", bbox_inches="tight")
# pyplot.show()

max_tin = df['TIN'].value_counts().max()
min_tin = df['TIN'].value_counts().min()
idxmax_tin = df['TIN'].value_counts().idxmax()
idxmin_tin = df['TIN'].value_counts().idxmin()

print("max_tin: ", max_tin)
print("min_tin: ", min_tin)
print("idxmax_tin: ", idxmax_tin)
print("idxmin_tin: ", idxmin_tin)


df['TIN'].value_counts().plot()
pyplot.show()
res = df['TIN'].value_counts()
print(res[1])
# result[res['Value'] > 10]  .plot.pie()
pyplot.show()
