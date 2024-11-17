# set index colum
import pandas as pd

df1 = pd.read_csv("supermarkets.csv")

#df1.columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7"]

df1.set_index("ID", inplace = True)

#df2 = df1.set_index("ID")
#print(df2)

print(df1)