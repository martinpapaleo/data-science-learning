from ingest import load_raw_data
from clean import clean_raw_data
from transform import transform_data
from validate import valid_data
import pandas as pd

df_raw_ = load_raw_data(debug=False)
df_clean = clean_raw_data(df_raw_, debug=False)
df_trans = transform_data(df_clean)
valid_data(df_trans)

print('DF Valid')
print(df_trans.head(5))