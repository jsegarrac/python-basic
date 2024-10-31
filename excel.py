# load excel
# pip install openpyxl -> para  ficheros excel xlsx
# pip install xlrd -> para  ficheros excel xls

import pandas as pd

df1 = pd.read_excel("supermarkets.xlsx")

print(df1)