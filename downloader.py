from pathlib import Path
import pandas as pd
import yfinance as yf

tickers = [
    "AAPL", "MSFT", "NVDA", "GOOGL",  # Technology and communication
    "AMZN", "HD",                    # Consumer discretionary
    "KO", "PG", "WMT",               # Consumer staples
    "JPM", "GS", "V",                # Financials
    "JNJ", "MRK",                    # Healthcare
    "XOM", "CVX",                    # Energy
    "CAT", "UPS",                    # Industrials
    "NEE",                          # Utilities
    "AMT",                          # Real estate
]
start = "2020-01-01"
end = "2026-01-01"

# Include the stocks and dates in the filename
file = Path(f"data/{'_'.join(tickers)}_{start}_{end}_adjusted.csv")

if file.exists():
    prices = pd.read_csv(file, index_col=0, parse_dates=True)
    print("Loaded saved prices.")

    print("File destination:\n" \
    f"data/{'_'.join(tickers)}_{start}_{end}_adjusted.csv")

else:
    data = yf.download(
        tickers,
        start=start,
        end=end,
        interval="1d",
        auto_adjust=True,
    )

    prices = data["Close"].reindex(columns=tickers)

    # Avoid saving a failed or incomplete download
    if prices.empty or prices.isna().any().any():
        raise ValueError("Download has missing data. Check before saving.")

    file.parent.mkdir(parents=True, exist_ok=True)
    prices.to_csv(file)
    print("Downloaded and saved prices.")

    print("File destination:\n" \
    f"data/{'_'.join(tickers)}_{start}_{end}_adjusted.csv")

prices.head()