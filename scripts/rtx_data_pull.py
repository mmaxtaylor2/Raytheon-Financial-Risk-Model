import yfinance as yf
import pandas as pd

# RTX, peers, and sector ETF benchmark
tickers = ["RTX", "LMT", "GD", "NOC", "ITA"]  # ITA = iShares US Aerospace & Defense ETF

print("Downloading market data...")

# 5-year price history
prices = yf.download(tickers, period="5y")["Adj Close"]
prices.to_csv("data/prices.csv")

# Basic fundamental metrics
data = {}
for t in tickers:
    stock = yf.Ticker(t)
    info = stock.info
    data[t] = {
        "Market Cap": info.get("marketCap"),
        "EV/EBITDA": info.get("enterpriseToEbitda"),
        "P/FCF": info.get("priceToFreeCashflow"),
        "5Y Revenue CAGR": info.get("revenueGrowth"),
    }

financials = pd.DataFrame(data).T
financials.to_csv("data/financials.csv")

print("Data pull complete. Files saved in /data/")

