from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2018, 12, 31)
BAC = data.DataReader('BAC', 'iex', start, end)
CITI = data.DataReader('C', 'iex', start, end)
GS = data.DataReader('GS', 'iex', start, end)
JPM = data.DataReader('JPM', 'iex', start, end)
MS = data.DataReader('MS', 'iex', start, end)
WFC = data.DataReader('WFC', 'iex', start, end)

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks = pd.concat([BAC, CITI, GS, JPM, MS, WFC], axis=1, keys=tickers )
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
#bank_stocks.to_csv('bank_stocks.csv')

print(bank_stocks.head())
print(bank_stocks.xs(('BAC','close'), axis=1).max())
for stock in tickers:
  print("%s max close:" %(stock))
  print(bank_stocks.xs((stock,'close'), axis=1).max())
  print('\n')

print(bank_stocks.xs(key='close',axis=1,level='Stock Info').max())

bank_returns = pd.DataFrame()

for stock in tickers:
  bank_returns[stock] = bank_stocks.xs((stock,'close'), axis=1).pct_change()

bank_returns.to_csv('bank_returns.csv')

#sns.set(style="ticks", color_codes=True)
#plt.tight_layout()
#sns.pairplot(bank_returns[1:], height=1.5 )
#plt.show()

print("****************** \n")

for stock in tickers:
  print("%s Index of min close:" %(stock))
  print(bank_returns.index[bank_returns[stock] == bank_returns[stock].min()])
  print(bank_returns[stock].min())

print("****************** \n")

for stock in tickers:
  print("%s Index of max close:" %(stock))
  print(bank_returns.index[bank_returns[stock] == bank_returns[stock].max()])
  print(bank_returns[stock].max())

print("****************** \n")

for stock in tickers:
  print("%s std close:" %(stock))
  print(bank_returns[stock].std())

print("****************** \n")
print(bank_returns.idxmin())
print("****************** \n")
print(bank_returns.idxmax())
print("****************** \n")
print(bank_returns.std())
print("****************** \n")
print(bank_returns.loc['2015-01-01':'2015-12-31'].std())

#sns.distplot(bank_returns.loc['2015-01-01':'2015-12-31']['BAC'], bins=50)
#plt.show()

#fig, axes = plt.subplots(figsize=(12,6))
#axes.set_xlabel('Time')
#axes.set_ylabel('Price')
#axes.plot(bank_stocks.index, bank_stocks.xs(('BAC','close'), axis=1), color = "red", lw = 0.5, label = 'BAC')
#axes.plot(bank_stocks.index, bank_stocks.xs(('C','close'), axis=1), color = "blue", lw = 0.5, label = 'C')
#axes.plot(bank_stocks.index, bank_stocks.xs(('GS','close'), axis=1), color = "green", lw = 0.5, label = 'GS')
#axes.plot(bank_stocks.index, bank_stocks.xs(('JPM','close'), axis=1), color = "purple", lw = 0.5, label = 'JPM')
#axes.plot(bank_stocks.index, bank_stocks.xs(('MS','close'), axis=1), color = "black", lw = 0.5, label = 'MS')
#axes.plot(bank_stocks.index, bank_stocks.xs(('WFC','close'), axis=1), color = "yellow", lw = 0.5, label = 'WFC')
#axes.legend(loc=0)
#plt.show()


#for stock in tickers:
#    bank_stocks[stock]['close'].plot(figsize=(12,4),label=stock)
#plt.legend()
#plt.show()


#plt.figure(figsize=(12,6))
#BAC['close'].loc['2015-01-01':'2015-12-31'].rolling(window=30).mean().plot(label='30 Day Avg')
#BAC['close'].loc['2015-01-01':'2015-12-31'].plot(label='BAC CLOSE')
#plt.legend()
#plt.show()

sns.heatmap(bank_stocks.xs(key='close',axis=1,level='Stock Info').corr(),annot=True)
plt.show()


