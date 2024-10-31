# load csv
import pandas as pd

df1 = pd.read_csv("supermarkets.csv")

df1.set_index("ID")

print(df1)