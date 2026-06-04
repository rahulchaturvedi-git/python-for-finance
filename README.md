# Python for Finance

This repository contains Python-based finance experiments, and visualizations created while learning financial data analysis, stock market concepts, and quantitative finance using Python. The goal is to continuously build and upload finance-related scripts, models, and visualizations while documenting the learning process through practical implementations.

---

# Candle Stick Charts

- This project demonstrates how to fetch historical stock market data using Python and visualize it using candlestick charts. 
- The script uses the `yfinance` library to download stock data from Yahoo Finance and `mplfinance`/`matplotlib` for financial chart visualization.
- It helps in understanding stock price movement, including open, high, low, and close values over time. 
- To run the project, install the required libraries using `pip install yfinance mplfinance pandas matplotlib`, then execute the Python file normally using `python filename.py`.

---

# Portfolio Visualizer

- This script (`stock_visualizer.py`) tracks the value of a stock portfolio and visualizes its composition.
- It fetches real-time closing prices for a predefined list of tickers (AAPL, TSLA, META, NVDA, AMZN, GOOGL) and calculates the total portfolio value.
- The visualization is presented as a donut chart, showing the percentage and USD value of each holding.
- **Key Features**: Portfolio tracking, real-time data fetching, and clear data visualization using `matplotlib`.
- **/modfications** - **Institutional Shareholding Visualizer**: (`company-investors-shareholding.py`)
- Allows users to explore the institutional ownership of any publicly traded company of the USA.
- It provides an interactive menu to view a table of top institutional holders or visualize the shareholding distribution in a pie chart.
- **Key Features**: Dynamic ticker input, interactive console menu, and data grouping for clear visualization of major vs. minor institutional investors.

---

