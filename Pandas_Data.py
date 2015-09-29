__author__ = 'jwintzar'

import os
import pandas
import csv
from collections import defaultdict
import dateutil.parser
import matplotlib.pyplot as plt
import pprint
import functools
from GetDataURLs import GetDataURLs
import numpy as np
import matplotlib
import datetime

def DownloadAndProcessRawData(directory="/Users/jennilee09/desktop/"):
    #linkList = GetDataURLs(rawHTMLdataURLs)
    #fileList = [link.split("/")[-1] for link in linkList]
    raw_readings = {}


    for f in os.listdir(directory):
        if f.endswith(".txt"):
            f = directory + f
            with open(f,"r") as csvfile:
                reader = csv.reader(csvfile)
                rows = [[cell.strip() for cell in row] for row in reader]

            assert rows.pop(0) == ['C/A', 'UNIT', 'SCP', 'STATION', 'LINENAME',
                           'DIVISION', 'DATE', 'TIME', 'DESC', 'ENTRIES',
                           'EXITS']

            for row in rows:
                raw_readings.setdefault(tuple([row[0], row[1], row[2], row[3] + " - " + "".join(sorted([c for c in row[4]]))]), []).append(row[4:])
    return(raw_readings)

#d = DownloadAndProcessRawData()

def ConvertRawDictToDatetimeEntryDict(d):
    """
    d = Old dictionary to convert to new dictionary format

    Return completely new dict with date and time strings combined,
    and turnstile entries count to integer
    """

    newDict = defaultdict()

    for k, lst in d.items():

        newDict[k] = []

        for dataRow in lst:
            # Find dates and time data points and combine into one
            datetimeStr = str(dataRow[2]) + " " + str(dataRow[3])

            # Use dateutil to convert to datetime
            newDate = dateutil.parser.parse(datetimeStr)

            #Get turnstile entries count and convert to integer
            entries = int(dataRow[5])

            # Append datetime and entries to new data row list
            newDataRow = []
            newDataRow.append(newDate)
            newDataRow.append(entries)

            # Append new data row list to new dict. under the key
            newDict[k].append(newDataRow)

    for k, lst in newDict.items():
        lst = sorted(lst, key=lambda x: x[0])

        for i, dataRow in enumerate(lst):
            if i == 0:
                dataRow.append(0)
            else:
                dataRow.append(lst[i][1] - lst[i-1][1])

        for dataRow in lst:
            dataRow.pop(-2)

    #return newDict

    data=[]

    for key,value in newDict.items():
            for item in value:
                x=[key[0],key[1],key[2],key[3],item[0],item[1]]

                data.append(x)

    return(data)

def weekday(x):
    test=datetime.datetime.weekday(x)
    return test



def create_df(d):
    df = pandas.DataFrame(d)
    df.columns =["C/A","UNIT","SCP","STATION","Date-Time","Entries"]

    df["Hour"] =df["Date-Time"].map(lambda x: int(x.strftime('%H')))
    df["Weekday"] = df["Date-Time"].map(lambda x: int(weekday(x)))
    df["Month"] = df["Date-Time"].map(lambda x: int(x.strftime('%d')))
    df=df.set_index("Date-Time")
    df=df[df['Entries']>0]
    df=df[df['Entries']<5000]
    df=df[df['Hour']>16]    ##rushhour slice
    df=df[df['Hour']<21]   ##rushhour slice
    df=df[df["Weekday"]<5] ##weekday slice
    df=df[df["Month"]==24]
    #df=df[df["Month"]<6]
    df=df.drop(["C/A","UNIT","SCP","Hour","Weekday","Month"],axis=1)

    grouped=df.groupby(["STATION"])

    #grouped = grouped['Entries'].agg([np.sum, np.median, np.mean, np.std])
    #grouped = grouped['Entries'].agg([np.sum])

     ###problems here
    #df=pandas.DataFrame(grouped)
    #df.columns=["sum","median","mean","std"]
    grouped.columns=["STATION","Entries","Date-Time"]



    df = grouped.aggregate(np.sum)
    df=df.sort("Entries", ascending=False)
    df=pandas.DataFrame(df)
    #df=df.sort()
    df=df[0:50]
    df.plot(title="Station Sum - Weekday Evening Rushour")

    plt.show()
    #print(df.tail())




create_df(
ConvertRawDictToDatetimeEntryDict(
DownloadAndProcessRawData(directory="/Users/jennilee09/Desktop/")
)
)