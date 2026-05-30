import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Define Time frame
start = dt.datetime(2026, 1, 1)
end = dt.datetime.now()

# Load Data
ticker = 'GOOGL'
data = yf.download(ticker, start=start, end=end)

#print(data.columns)

#Restructure Data
data = data[['Open','High','Low','Close']]

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

#print(data.head())

# Vizualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title(ticker + ' Share Price',color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')
ax.xaxis_date()

candlestick_ohlc(ax,data.values,width=0.6,colorup='#00ff00',colordown='#ff0000')
plt.show()
