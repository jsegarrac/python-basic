# let us import the Pandas Library
import pandas as pd


#Define a dictionary 'x'
x = {'Student': ['David','Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Country': ['UK', 'Canada', 'China', 'USA'], 
      'Course':['py', 'dc', 'ml', 'w'], 'Marks': [85, 72, 89, 76]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#retrieve de "Marks" column and assigning it to a variable y
y = df[['Marks']]
print(y)
print(type(y))

# to view the columns as a series, just use one bracket
y = df['Marks']
print(y)
print(type(y))

y = df['Student']
print(y)
print(type(y))