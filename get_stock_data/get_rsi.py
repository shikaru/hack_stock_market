from pandas_datareader.stooq import StooqDailyReader
from datetime import datetime
import pandas as pd

def get_rsi(start=datetime(2020, 1, 1),end=datetime(2020, 12, 31),brand='1305.JP',n=14,):
  stooq = StooqDailyReader(brand, start=start, end=end)
  data = stooq.read()
  #input data must be pandas dataframe
  diff=data["Close"].diff()
  up=diff.copy()
  up[up<0]=0
  down=diff.copy()
  down[down>0]=0
  up_sma_14 = up.rolling(window=n, center=False).mean()
  
  down_sma_14 = down.abs().rolling(window=n, center=False).mean()
  RSI=(up_sma_14)/(down_sma_14+up_sma_14)
  return RSI*100, data["Close"]