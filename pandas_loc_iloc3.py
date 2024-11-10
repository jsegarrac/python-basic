# loc & iloc 2
import pandas as pd

df1 = pd.read_json("supermarkets.json")

df1.set_index("ID")

print(df1)

df2=df1.iloc[3, 1:4]

print(df2)



