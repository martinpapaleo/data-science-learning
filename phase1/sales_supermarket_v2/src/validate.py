'''
No duplicate Invoice_ID
No nulls in required columns (your full list)
Unit_price > 0
Quantity >= 1
Total > 0
cogs > 0
0 <= Rating <= 10
Datetime is datetime dtype
'''
def value_pos_in_df(df_, col_name):
    if df_.loc[df_[col_name] <= 0].count().sum() != 0:
        return False
    return True

def valid_clean_data(data_):
    import pandas as pd
    # No duplicate Invoice_ID
    if data_['Invoice_ID'].shape != data_['Invoice_ID'].value_counts().shape:
        print('False1')
        return False

    # No nulls in required columns (your full list)
    if data_.isnull().sum().sum() != 0:
        print('False2')
        return False
    
    # Unit_price > 0 
    if not value_pos_in_df(data_, 'Unit_price'):
        print('False3')
        return False

    # Total > 0
    if not value_pos_in_df(data_, 'Total'):
        print('False4')
        return False

    # cogs > 0
    if not value_pos_in_df(data_, 'cogs'):
        print('False5')
        return False
    # I do know that Unit_price, Total and cogs could be chacked in one single line, but I'd want to differenciate with a differet print each possible fail

    # Quantity >= 1
    if data_.loc[data_['Quantity'] < 1].count().sum() != 0:
        print('False6')
        return False
    
    # 0 <= Rating <= 10
    if data_.loc[(data_['Rating'] > 10) | (data_['Rating'] < 0)].count().sum() != 0:
        print('False7')
        return False

    # Datetime type datetime[ns]
    if data_['Datetime'].dtypes != pd.to_datetime(pd.Series('12/12/2002')).dtype:
        print('False8')
        return False
    return True