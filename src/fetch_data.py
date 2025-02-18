import yfinance as yf
import pandas as pd


def get_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Fetch historical stock data from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df


if __name__ == "__main__":
    df = get_stock_data("AAPL")
    print(df.tail())  # Print last 5 rows
