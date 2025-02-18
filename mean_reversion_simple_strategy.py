"""
Prototype of a simple mean reversion 
trading strategy using a 50-day Simple 
Moving Average (SMA).
"""

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Fetch Historical Stock Data (AAPL - Apple)
stock = yf.Ticker("AAPL")  # Change to any stock symbol
df = stock.history(period="1y")  # 1 year of data

# Calculate 50-Day Simple Moving Average (SMA)
df["SMA_50"] = df["Close"].rolling(window=50).mean()

# Define Trading Signals
df["Signal"] = 0  # Default: No action
df.loc[df["Close"] < df["SMA_50"], "Signal"] = 1  # Buy when price < SMA
df.loc[df["Close"] > df["SMA_50"], "Signal"] = -1  # Sell when price > SMA

# Backtest the Strategy
initial_capital = 10000  # Starting money ($10,000)
df["Daily Returns"] = df["Close"].pct_change()  # Daily % returns
df["Strategy Returns"] = df["Signal"].shift(1) * df["Daily Returns"]  # Apply signals
df["Cumulative Returns"] = (
    1 + df["Strategy Returns"]
).cumprod() * initial_capital  # Portfolio growth

# Plot Stock Price and Moving Average
plt.figure(figsize=(12, 6))
plt.plot(df["Close"], label="Stock Price", color="blue")
plt.plot(df["SMA_50"], label="50-Day Moving Average", color="red")
plt.legend()
plt.title("AAPL Stock Price vs. 50-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.show()

# Plot Strategy Performance
plt.figure(figsize=(12, 6))
plt.plot(df["Cumulative Returns"], label="Strategy Performance", color="green")
plt.legend()
plt.title("Trading Strategy Performance (Starting Capital: $10,000)")
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($)")
plt.show()

# Print last 10 rows to check signals
print(df[["Close", "SMA_50", "Signal", "Cumulative Returns"]].tail(10))
