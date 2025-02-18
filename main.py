from src import fetch_data
from src import strategy
from src import backtest
from src import visualization


def main():
    ticker = "AAPL"  # Change to any stock
    df = fetch_data.get_stock_data(ticker)
    df = strategy.apply_sma_strategy(df)
    df = backtest.backtest_strategy(df)

    print(df[["Close", "SMA_50", "Signal", "Cumulative Returns"]].tail(10))

    visualization.plot_stock_vs_sma(df)
    visualization.plot_strategy_performance(df)


if __name__ == "__main__":
    main()
