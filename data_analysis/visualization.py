# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
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


labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()

