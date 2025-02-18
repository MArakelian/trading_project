import pandas as pd


def apply_sma_strategy(df: pd.DataFrame, window: int = 50) -> pd.DataFrame:
    """Apply a simple moving average (SMA) strategy."""
    df["SMA_50"] = df["Close"].rolling(window=window).mean()
    df["Signal"] = 0  # Default: No action
    df.loc[df["Close"] < df["SMA_50"], "Signal"] = 1  # Buy
    df.loc[df["Close"] > df["SMA_50"], "Signal"] = -1  # Sell
    return df


if __name__ == "__main__":
    import fetch_data

    df = fetch_data.get_stock_data("AAPL")
    df = apply_sma_strategy(df)
    print(df[["Close", "SMA_50", "Signal"]].tail(10))
