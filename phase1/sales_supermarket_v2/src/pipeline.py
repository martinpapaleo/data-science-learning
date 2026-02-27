from ingest import load_raw_data
from clean import clean_raw_data
from validate import valid_clean_data
from transform import transform_data
import pandas as pd
df_raw_ = load_raw_data(debug=False)
df_clean = clean_raw_data(df_raw_, debug=False)

valid_clean_data(df_clean)
print('DF Valid')
df_trans = transform_data(df_clean)
print(df_trans.head(5))