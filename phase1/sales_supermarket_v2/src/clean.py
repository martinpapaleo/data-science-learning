'''
Clean:

- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
- Ensure numeric columns are numeric (no silent object leftovers)
'''

import os
import pandas as pd

print("cwd:", os.getcwd())
print("__file__:", __file__)

src_dir = os.path.dirname(os.path.abspath(__file__))
print("src_dir:", src_dir)

'''
project_dir = os.path.dirname(src_dir)  # goes from /src to /sales_supermarket_v2
raw_path = os.path.join(project_dir, "data", "raw", "supermarket_sales.csv")
print("raw_path:", raw_path)
'''

df = pd.read_csv('c:/Users/marti/Desktop/DataScience/DataScience/phase1/sales_supermarket_v2/data/raw/supermarket_sales.csv') #obtained from scr_dir and modifying it properly.
print('loaded shape:',df.shape)
print(df.head())

# Applying 'Unknown' to NaN values in Gender column
df.loc[df['Gender'].isnull(), 'Gender'] = 'Unknown'

# Counting for validation
print(df['Gender'].value_counts())
print(df.head())

# Parsing Date and Time columns into Datetime column

df['Datetime'] = df['Date'] + ' ' + df['Time']
df['Datetime'] = pd.to_datetime(df['Datetime'])
print(df['Datetime'])

# Drop columns Time, Date, Tax 5% and gross margin percentage and verify

del df['Time']
del df['Date']
del df['Tax 5%']
del df['gross margin percentage']

print(df.columns)

# Ensure all numeric columns are indeed numeric
print(df.info())

# Deliverable outputs
df_clean = df
print(df_clean.head())
print(df_clean.isnull().sum().sort_values(ascending=False).head(5))