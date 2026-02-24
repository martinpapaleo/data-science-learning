from ingest import load_raw_data
from clean import clean_raw_data
from validate import valid_clean_data
from validate import value_pos_in_df
import pandas as pd
df_raw_ = load_raw_data()
df_clean = clean_raw_data(df_raw_)

if valid_clean_data(df_clean):
    print('Yes')
else:
    print('No')