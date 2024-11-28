''' 
Data Analysis
In this section, you will learn how to approach data acquisition in various ways and obtain necessary insights from a dataset. By the end of this lab, you will successfully load the data into Jupyter Notebook and gain some fundamental insights via the Pandas Library.

In our case, the Diabetes Dataset is an online source and it is in CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.

About this Dataset
Context: This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years of age of Pima Indian heritage.

Content: The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

We have 768 rows and 9 columns. The first 8 columns represent the features and the last column represent the target/label.

'''
import pandas as pd
import requests

# URL del archivo CSV
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# Descargar el archivo CSV
response = requests.get(url)
if response.status_code == 200:
    # Guardar el archivo localmente
    with open("diabetes.csv", "wb") as file:
        file.write(response.content)
    print("Archivo CSV descargado como 'diabetes.csv'")
else:
    print(f"Error al descargar el archivo: {response.status_code}")

# Leer el archivo CSV con pandas
df = pd.read_csv("diabetes.csv")

# Mostrar las primeras filas del DataFrame
print(df.head())

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
print(df.head(15))
print(df.shape)
print(df.info())
print(df.describe())

missing_data = df.isnull()
print(missing_data)
missing_data.head(5)
print(missing_data)


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    