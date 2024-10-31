# use of loc & iloc

# let us import the Pandas Library
import pandas as pd


#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000], 'new data': [1, 2, 3, 4]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

# access the value on the first row and the firs column
df.iloc[0,0]

# access the column using the name
df.loc[0,'Salary']

# copy a dataset

df1 = df
