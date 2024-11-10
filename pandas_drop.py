# drop index and columns
import pandas as pd

df1 = pd.read_json("supermarkets.json")

df1.set_index("ID")

print(df1)

df1 = df1.drop("City",axis=1)

print(df1)

df1 = df1.drop("California",axis=0)

print(df1)




