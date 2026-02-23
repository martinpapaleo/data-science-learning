'''
Clean:
- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
- Ensure numeric columns are numeric (no silent object leftovers)
'''
from ingest import load_raw_data
import pandas as pd
df_raw_ = load_raw_data()
def clean_raw_data(df_raw):
    # Applying 'Unknown' to NaN values in Gender column
    df_raw.loc[df_raw['Gender'].isnull(), 'Gender'] = 'Unknown'

    # Counting for validation
    print(df_raw['Gender'].value_counts())
    print(df_raw.head())

    # Parsing Date and Time columns into Datetime column

    df_raw['Datetime'] = df_raw['Date'] + ' ' + df_raw['Time']
    df_raw['Datetime'] = pd.to_datetime(df_raw['Datetime'])
    print(df_raw['Datetime'])

    # Drop columns Time, Date, Tax 5% and gross margin percentage and verify

    del df_raw['Time']
    del df_raw['Date']
    del df_raw['Tax 5%']
    del df_raw['gross margin percentage']

    print(df_raw.columns)

    # Ensure all numeric columns are indeed numeric
    print(df_raw.info())

    # Deliverable outputs
    df_clean = df_raw
    print(df_clean.head())
    print(df_clean.isnull().sum().sort_values(ascending=False).head(5))
    return df_clean
clean_raw_data(df_raw_)