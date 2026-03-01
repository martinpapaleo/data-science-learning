from ingest import load_raw_data
from clean import clean_raw_data
from transform import transform_data
from validate import valid_data
from persist import save_data
import pandas as pd

def main():

    df_raw_ = load_raw_data(debug=False)
    df_clean = clean_raw_data(df_raw_, debug=False)
    df_trans = transform_data(df_clean)
    valid_data(df_trans)
    save_data(df_trans, debug=False)
    print('Pipeline finished succesfully.')
    print(df_trans.head(5))

if __name__ == "__main__":
    main()