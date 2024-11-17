import pandas as pd
import matplotlib.pyplot as plt

# Convertir el diccionario en un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 25, 21],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data)

# Gráfico de barras para visualizar la edad de cada persona
plt.figure(figsize=(8, 5))
plt.bar(df['Nombre'], df['Edad'], color='skyblue', edgecolor='black')
plt.title('Edades de las Personas')
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.show()