'''
Clean:
- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
- Ensure numeric columns are numeric (no silent object leftovers)
'''
import pandas as pd
def clean_raw_data(df_raw, debug):
    df = df_raw.copy()
    # Applying 'Unknown' to NaN values in Gender column
    df.loc[df['Gender'].isnull(), 'Gender'] = 'Unknown'

    # Counting for validation
    if debug:
        print(df['Gender'].value_counts())
        print(df.head())

    # Parsing Date and Time columns into Datetime column

    df['Datetime'] = df['Date'] + ' ' + df['Time']
    df['Datetime'] = pd.to_datetime(df['Datetime'], format='mixed')
    if debug:
        print(df['Datetime'])

    # Drop columns Time, Date, Tax 5% and gross margin percentage and verify
    columns_to_drop = ['Time', 'Date', 'Tax 5%', 'gross margin percentage']
    df = df.drop(columns= columns_to_drop, axis=1)
    if debug:
        print(df.columns)

    # Ensure all numeric columns are indeed numeric
    if debug:
        print(df.info())

    # Deliverable outputs
    df_clean = df
    print('DF Clean:')
    print(df_clean.head())
    print(df_clean.isnull().sum().sort_values(ascending=False).head(5))
    return df_clean
