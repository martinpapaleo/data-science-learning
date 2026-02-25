def t_valid_data(data_):
    import pandas as pd          #delete block before finishing file

    t_data = data_
    return t_data
import pandas as pd 
from datetime import date
print(pd.to_datetime(pd.Series('12/12/2002')).dtype)