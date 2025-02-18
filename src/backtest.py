import pandas as pd


def backtest_strategy(df: pd.DataFrame, initial_capital: float = 10000) -> pd.DataFrame:
    """Backtest the strategy by calculating portfolio value over time."""
    df["Daily Returns"] = df["Close"].pct_change()  # % daily returns
    df["Strategy Returns"] = (
        df["Signal"].shift(1) * df["Daily Returns"]
    )  # Apply trading signal
    df["Cumulative Returns"] = (1 + df["Strategy Returns"]).cumprod() * initial_capital
    return df


if __name__ == "__main__":
    import fetch_data, strategy

    df = fetch_data.get_stock_data("AAPL")
    df = strategy.apply_sma_strategy(df)
    df = backtest_strategy(df)
    print(df[["Close", "SMA_50", "Signal", "Cumulative Returns"]].tail(10))
