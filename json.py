# load json
import pandas as pd

df1 = pd.read_json("supermarkets.json")
df1.set_index("ID")

print(df1)