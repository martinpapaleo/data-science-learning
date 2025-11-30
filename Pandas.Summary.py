import csv
import pandas as pd

# How to read csv with pandas (with the read_ functions) :
sales = pd.read_csv("supermarket_sales - Sheet1.csv")

# Visualize  DataFrame:
print(sales, "\n\nSales info: ")

# Visualize  all columns information:
print(sales.info(), "\n")

# Column == Series when talking about dataframes

# Visualize certain statistics about each series of the dataframe:
print(sales.describe(), '\n')

# Visualize the first or last x amount of rows:
print(sales.head(8), '\n')
print(sales.tail(3), '\n')

# Show the max or min of any Series:
print(f'The max amount of Quantity from the sales dataframe is: {sales["Quantity"].max()}', '\n')

# Shows all columns data types, this info is also available with .info() :
print(sales.dtypes, '\n')

# Show all the DataFrame's Rows or Series:
'''
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None) 
print(sales)
'''

# Visualize specific Series of the DataFrame:
custom_id = sales['Invoice_ID']
gender_quant = sales[["Gender", "Quantity"]]

# Visualize DataFrame values based on conditions (& == and, | == or):
c_over_5 = sales[sales['Quantity'] > 5]

# while displaying more than one condition () are needed to separate each one of them:
males_over_5 = sales[(sales['Quantity'] > 5) & (sales['Gender'] == 'Male')]

# .isin() conditional function returns a True for each row the values are in the provided list:
c_1_2 = sales[sales['Quantity'].isin([1, 2])]

# .isnull() is the opposite of .notna()
# Visualize Invoice_id of all customers whose gender is empty or whose gender is not empty:
gender_inc = sales[sales['Gender'].isnull()]['Invoice_ID']
g_complete = sales[sales['Gender'].notna()][['Invoice_ID', 'Total']]

# Transform DataFrame to Excel or others (with .to_ functions):
# index = False makes the sales row indexes not to be saved
sales.to_excel('Super-Sales.xlsx', sheet_name="Super", index=False)
excel_sales = pd.read_excel('Super-Sales.xlsx', sheet_name='Super')

# Visualize specific rows and series of a dataframe (.loc[] / .iloc[])
# .loc[] allows to separate first the conditions and then with a ',' the Series you need to see
m_under_3 = excel_sales.loc[(excel_sales['Quantity'] < 3) & (excel_sales['Gender'] == 'Male'), ['Gender', 'Invoice_ID']]
# .iloc[] allows to adjust directly by range of columns and rows (first the range of rows, then the range of columns):
new_data = excel_sales.iloc[2:3, 2:5]
# how to assign the costumer type (4th column) the value 'anonymous' to the first 3 elements:
excel_sales.iloc[0:3, 3] = 'anonymous'
pd.set_option('display.max_columns', None)
#print(excel_sales.head(5))

# Remove all rows that have null values:
excel_sales = excel_sales.dropna()


