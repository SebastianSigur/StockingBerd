from alpha_vantage.timeseries import TimeSeries
import csv
import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

api = '2ADBTDTCWZH4DVHG'
ticker = str('AAPL')
time_tik = 1
time = TimeSeries(key=api, output_format='csv')
data = time.get_intraday(symbol=ticker, interval='{}min'.format(time_tik), outputsize='full')[0]

with open('data.csv', 'a') as cf:
    for row in data:
        cf.write(','.join(row))
        cf.write('\n')
