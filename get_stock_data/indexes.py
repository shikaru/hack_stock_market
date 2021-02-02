def get_indexes(start=datetime.datetime(2020, 1, 1),end=datetime.datetime(2020, 12, 31),brand='1305.JP',n=14,):
  date=start-datetime.timedelta(days=40)
  stooq = StooqDailyReader(brand, start=date, end=end)
  data = stooq.read()
  #input data must be pandas dataframe
  diff=data["Close"].diff().sort_index(ascending=True)
  up=diff.copy()
  up[up<0]=0
  down=diff.copy()
  down[down>0]=0
  up_sma_14 = up.rolling(window=n, center=False).mean()
  down_sma_14 = down.abs().rolling(window=n, center=False).mean()
  RSI=(up_sma_14)/(down_sma_14+up_sma_14)

  #MacD
  short=data["Close"].sort_index(ascending=True).ewm(span=12,adjust=False).mean()
  long=data["Close"].sort_index(ascending=True).ewm(span=26,adjust=False).mean()
  macd=short-long
  signal = macd.ewm(span=9).mean()
  return RSI[30:]*100, macd.sort_index(ascending=True)[30:],signal.sort_index(ascending=True)[30:],data["Close"][:-30].sort_index(ascending=True)