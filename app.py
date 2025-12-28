from analysis import get_data  # import our data function
import numpy as np
import matplotlib.pyplot as plt

# Define the tickers we want
tickers = ["AAPL", "MSFT", "SPY"]

# Download prices and compute returns
prices, returns = get_data(tickers)

# Print the last 5 rows of prices
print("=== Prices ===")
print(prices.tail())

# Print the last 5 rows of returns
print("\n=== Daily Returns ===")
print(returns.tail())

# #daily volatitly = std(dev)(returns)
# daily_vol= returns.std()
# print("\n=== Daily Volatility ===")
# print(daily_vol)

annual_vol = daily_vol * np.sqrt(252)
print("\n=== Annualized Volatility ===")
print(annual_vol)

#Plot closing prices
plt.figure(figsize=(10,6))
for ticker in tickers:
    plt.plot(prices[ticker], label= ticker)
plt.title("Stock Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.tight_layout()
plt.show()

#plotting the daily returns
plt.figure(figsize= (10,6))
for ticker in tickers:
    plt.plot(returns[ticker], label= ticker)
plt.title("Daily returns")
plt.xlabel("Date")
plt.ylabel("Daily return")
plt.legend()
plt.tight_layout()
plt.show() #seperate script runs

#plot a bar chart for annual volatility
plt.figure(figsize= (8,5))
plt.bar(annual_vol.index, annual_vol.values, color= ['blue', 'green', 'orange'])
plt.title("Annualized Volatility")
plt.ylabel("Volatility (Decimal)")
plt.tight_layout()
plt.show()

