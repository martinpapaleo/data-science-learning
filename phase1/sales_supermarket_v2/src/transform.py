import pandas as pd
def transform_data(data_):
    data_['Year'] = data_['Datetime'].dt.year
    data_['Month'] = data_['Datetime'].dt.month
    data_['Day'] = data_['Datetime'].dt.day
    data_['Weekday'] = data_['Datetime'].dt.day_name()
    data_['Hour'] = data_['Datetime'].dt.hour
    return data_
