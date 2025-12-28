import yfinance as yf
import pandas as pd

def get_data(tickers, start="2023-01-01"):
    all_data = {}  # store each ticker's closing prices

    for ticker in tickers:
        print(f"Downloading {ticker}...")
        data = yf.download(ticker, start=start) #historical data for that ticker
        
        # Make sure we have data
        if "Close" in data.columns and not data.empty: # only keep it if the "close" price exists
            all_data[ticker] = data["Close"]
        else:
            print(f"Warning: {ticker} data missing or empty.")

    if not all_data:
        raise ValueError("No data downloaded. Check tickers or network.")

    # Combine into one DataFrame
    prices = pd.concat(all_data, axis=1)  # safer than pd.DataFrame(all_data)
    prices.columns = tickers  # ensure column names match tickers

    # Compute daily returns
    returns = prices.pct_change().dropna() #.pct_change is a method part of pandas (calculates percentage change between consecutive rows) .dropna() removes rows or colums that have missing values

    return prices, returns

