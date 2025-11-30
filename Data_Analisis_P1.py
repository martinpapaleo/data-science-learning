import pandas as pd
from charset_normalizer import from_path

# Get the encoding for properly opening the CSV file
results = from_path('sales_data_sample.csv').best()
print(results.encoding)

# Get info from the CSV into a variable
sales = pd.read_csv(
    'sales_data_sample.csv',
    encoding='cp1250',
    parse_dates=['ORDERDATE']
)

# Show always all the columns and rows available
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Show relevant information
print(sales.iloc[:3])
price_extremes = sales.groupby('ORDERLINENUMBER').PRICEEACH.agg(['min', 'max'])
print(price_extremes)

sorted_values = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_values)

