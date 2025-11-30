import yfinance as yf

# Download EUR/USD 1-minute data for the last 7 days
data = yf.download("EURUSD=X", interval="1m", period="7d")

# Show first few rows
print(data.head())

# Save to CSV
data.to_csv("eurusd_1m.csv")

print("✅ 1-minute data saved to 'eurusd_1m.csv'")


