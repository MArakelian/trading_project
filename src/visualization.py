import matplotlib.pyplot as plt
import pandas as pd


def plot_stock_vs_sma(df: pd.DataFrame):
    """Plot stock price and 50-day moving average."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Close"], label="Stock Price", color="blue")
    plt.plot(df["SMA_50"], label="50-Day Moving Average", color="red")
    plt.legend()
    plt.title("Stock Price vs. 50-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.show()


def plot_strategy_performance(df: pd.DataFrame):
    """Plot cumulative returns of strategy."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Cumulative Returns"], label="Strategy Performance", color="green")
    plt.legend()
    plt.title("Trading Strategy Performance")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.show()


if __name__ == "__main__":
    import fetch_data, strategy, backtest

    df = fetch_data.get_stock_data("AAPL")
    df = strategy.apply_sma_strategy(df)
    df = backtest.backtest_strategy(df)

    plot_stock_vs_sma(df)
    plot_strategy_performance(df)
