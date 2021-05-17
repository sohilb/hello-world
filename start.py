import numpy as np
import pandas as pd
import yfinance as yf

tick = yf.download('AAPL', '2021-01-01', '2021-04-30')

data  = tick[['Open', 'High', 'Low', 'Close']]

data[2]