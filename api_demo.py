# api

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)

type(df)

df.head()

print(df)

df1=df.mean()

print(df1)
