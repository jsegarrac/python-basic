# load fichero plan (;)

import pandas as pd

df1 = pd.read_csv("supermarkets-semi-colons.txt", sep=';')

print(df1)

df2 = pd.read_csv("supermarkets-semi-colons.txt")

print(df2)