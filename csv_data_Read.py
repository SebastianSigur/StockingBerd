import numpy as np
import pandas as pd
# Make numpy values easier to read.
import csv

def csv_to_dict(file_name):
    line = 0
    dicty = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if line == 0:
                line += 1
                continue
            if row[0][0:10] not in dicty:
                #open,high,low,close,volume
                dicty[row[0][0:10]] = {'time': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

            else:
                dicty[row[0][0:10]]['time'].append(row[0][11:20])
                dicty[row[0][0:10]]['open'].append(row[1])
                dicty[row[0][0:10]]['close'].append(row[2])
                dicty[row[0][0:10]]['open'].append(row[3])
                dicty[row[0][0:10]]['open'].append(row[4])
    return dicty


def complete_data(dicty, begin_time, time_interval, end_time):
    dicty_new = dicty
    for key in dicty:
        for in_key in dicty[key]:
            dicty[key][in_key] = dicty[key][in_key][::-1]
    return dicty_new

dicty = csv_to_dict('data.csv')
dicty_new = complete_data(dicty,1 , 1, 1)
print(dicty)
for i in dicty:
    for j in dicty[i]:
        print(len(dicty[i][j]))
