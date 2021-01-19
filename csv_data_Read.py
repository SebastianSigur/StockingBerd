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
                dicty[row[0][0:10]]['high'].append(row[2])
                dicty[row[0][0:10]]['low'].append(row[3])
                dicty[row[0][0:10]]['close'].append(row[4])
                dicty[row[0][0:10]]['volume'].append(row[4])

    return dicty


def change_time(time: str, plus_time:int):
    if time[3] == '0' and time[4] != '9' and time[3:5] != '59':
            time = time[0:4] + str(int(time[4:5])+plus_time) + time[5:]
    elif time[3:5] == '59':
        if time[1:2] != '9':
            time = time[0] + str(int(time[1])+plus_time) + ':00:' + time[6:]
        else:
            time = str(int(time[0:2])+plus_time) + ':00:' + time[6:]
    else:
        time = time[0:3] + str(int(time[3:5])+plus_time) + time[5:]
    return time


def complete_data(dicty, begin_time: str, time_interval: int, end_time: str):
    dicty_new = dicty
    for key in dicty:
        for in_key in dicty[key]:
            dicty[key][in_key] = dicty[key][in_key][::-1]

        time = begin_time
        corrections = 0
        current_count = 0
        for count, currnet_time in enumerate(dicty[key]['time']):
            while True:
                if currnet_time != time:
                    dicty[key]['time'] = dicty[key]['time'][0:current_count] + [time] + dicty[key]['time'][current_count:]
                    dicty[key]['open'] = dicty[key]['open'][0:current_count] + [dicty[key]['open'][abs(current_count-1)]] + dicty[key]['open'][current_count:]
                    dicty[key]['high'] = dicty[key]['high'][0:current_count] + [dicty[key]['high'][abs(current_count-1)]] + dicty[key]['high'][current_count:]
                    dicty[key]['low'] = dicty[key]['low'][0:current_count] + [dicty[key]['low'][abs(current_count-1)]] + dicty[key]['low'][current_count:]
                    dicty[key]['close'] = dicty[key]['close'][0:current_count] + [dicty[key]['close'][abs(current_count-1)]] + dicty[key]['close'][current_count:]
                    dicty[key]['volume'] = dicty[key]['volume'][0:current_count] + [dicty[key]['volume'][abs(current_count-1)]] + dicty[key]['volume'][current_count:]
                    corrections += 1
                    assert current_count != 0 # Ef fyrsta callið er ekki byrjunar tíminn
                else:
                    time = change_time(time, time_interval)
                    current_count += 1
                    break
                time = change_time(time, time_interval)
                current_count += 1
    for key in dicty_new:
        row = 0
        for inner_key in dicty_new[key]:
            if row == 0:
                row += 1
                continue
            for count, value in enumerate(dicty[key][inner_key]):
                dicty_new[key][inner_key][count] = float(value)
    return dicty_new
