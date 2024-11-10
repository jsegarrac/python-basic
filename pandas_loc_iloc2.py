# loc & iloc
import pandas as pd

df1 = pd.read_json("supermarkets.json")

df1.set_index("ID")

df2=df1.loc[:,"Country"]

print(df2)

df3 = list(df2)
print(df3)