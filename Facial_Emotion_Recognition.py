import csv
import pandas as pd
'''
data_ = pd.read_csv('anime.recomendation.2020.csv')
data_.to_excel('Anime.Rec.2020.xlsx', sheet_name='Sheet_1', index=False)
'''
#pd.set_option('display.max_columns', None)
data_excel = pd.read_excel('Anime.Rec.2020.xlsx', 'Sheet_1')
print(data_excel.info())
data_desc = data_excel.describe()
print(data_excel.head(10))
fav_mean = data_desc['Favorites'].iloc[1]
print(fav_mean)


