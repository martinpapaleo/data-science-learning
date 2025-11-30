import pandas as pd

# Load the 1-minute EUR/USD data
data = pd.read_csv("eurusd_1m.csv", parse_dates=["Datetime"], index_col="Datetime")

# Show basic structure
print("Columns:", data.columns)
print("\nFirst 5 rows:")
print(data.head())

# Show date range
print(f"\n Date Range: {data.index.min()} to {data.index.max()}")
