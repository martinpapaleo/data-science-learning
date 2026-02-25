'''
Clean:
- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
- Ensure numeric columns are numeric (no silent object leftovers)
'''
import pandas as pd
def clean_raw_data(df_raw):
    df = df_raw.copy()
    # Applying 'Unknown' to NaN values in Gender column
    df.loc[df['Gender'].isnull(), 'Gender'] = 'Unknown'

    # Counting for validation
    
    print(df['Gender'].value_counts())
    print(df.head())

    # Parsing Date and Time columns into Datetime column

    df['Datetime'] = df['Date'] + ' ' + df['Time']
    df['Datetime'] = pd.to_datetime(df['Datetime'], format='MM-DD-YYYY HH:MM')
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
    return df_clean
