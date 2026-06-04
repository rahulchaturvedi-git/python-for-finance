import datetime as dt
import yfinance as yf

tickers = ['AAPL', 'TSLA', 'META', 'NVDA', 'AMZN', 'GOOGL']
amounts = [7, 5, 12, 16, 2, 4]

prices = []
total = []

for ticker, amount in zip(tickers, amounts):
    df = yf.download(
        ticker,
        start="2026-01-01",
        end=dt.datetime.now().strftime("%Y-%m-%d"),
        progress=False
    )

    price = df['Close'].iloc[-1].item()
    prices.append(price)
    total.append(price * amount)

#print("Prices:")
#print(prices)

#print("\nPortfolio Value:")
#print(total)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16,8))

ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')

ax.tick_params(axis='x',color='white')
ax.tick_params(axis='y',color='white')
ax.set_title('Portfolio Value',color='white',fontsize = 20)

_, texts, _ = ax.pie(total,labels=tickers,autopct='%1.1f%%',pctdistance=0.8)
[text.set_color('white') for text in texts]

my_circle = plt.Circle((0,0),0.6,color="Black")
ax.add_artist(my_circle)

ax.text(-2,1, 'Portfolio Overview', fontsize = 14, color='#FFF536',verticalalignment='center',horizontalalignment='center')
ax.text(-2,0.85, f'Total USD Value: ${sum(total):.2f}', fontsize = 14, color='#FFF536',verticalalignment='center',horizontalalignment='center')
counter = 0.15
for ticker in tickers:
  ax.text(-2, 0.85 - counter, f'{ticker}: {total[tickers.index(ticker)]:.2f}' + '$', fontsize = 14, color='white',verticalalignment='center',horizontalalignment='center')
  counter += 0.15

#ax.bar(tickers, total)

plt.show()
