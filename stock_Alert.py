import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import time

yf.pdr_override()
start = dt.datetime(2020, 12, 29)
now = dt.datetime.now()

#stock : target
stock_list = {}
new_stock = 'y'


#Add stocks by entering ticker symbol with target price
while new_stock == 'y':
  new_stock = input('Add new Stock & Target (y or n): ')
  if new_stock == 'y':
    key = input('Enter Stock: ')
    value = float(input('Enter Target: '))
    stock_list[key] = value
  print(stock_list)
  print()


delete_list = []

#For case of one user loop stops once all stocks alerted
while len(stock_list) > 0:

  for j in delete_list:
    del stock_list[j]
  delete_list.clear()

  print(stock_list)
  for k, v in stock_list.items():
    df = pdr.get_data_yahoo(k, start, now)
    currentClose = df["Adj Close"][-1]
    
    condition = (currentClose - .001) <= v

    if(condition):

      message = k +" has dropped under "+ str(v) +\
      "\nCurrent Price: "+ str(currentClose)

      print(message)
      print("\n")
      delete_list.append(k)

    time.sleep(5)