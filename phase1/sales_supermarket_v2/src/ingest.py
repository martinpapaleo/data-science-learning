'''
Returns df_raw
'''
def load_raw_data():
    import os
    import pandas as pd

    print("cwd:", os.getcwd())
    print("__file__:", __file__)

    src_dir = os.path.dirname(os.path.abspath(__file__))
    print("src_dir:", src_dir)


    project_dir = os.path.dirname(src_dir)  # goes from /src to /sales_supermarket_v2
    print(project_dir)

    raw_path = os.path.join(project_dir, "data", "raw", "supermarket_sales.csv")
    print("raw_path:", raw_path)


    df_raw = pd.read_csv(raw_path) #obtained from scr_dir and modifying it properly.
    print('loaded shape:',df_raw.shape)
    print(df_raw.head())
    return(df_raw)

#load_raw_data()