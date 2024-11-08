# set columns name
import pandas as pd

df1 = pd.read_csv("csv_header.csv", header = None)

df1.columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7"]

print(df1)