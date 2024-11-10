# update 
import pandas as pd

df1 = pd.read_json("supermarkets.json")

df2=df1.set_index("ID")

print(df2)