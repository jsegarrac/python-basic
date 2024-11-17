'''
.loc: permite seleccionar datos basándose en etiquetas de filas y columnas.
df.loc[fila, columna]
- fila: la etiqueta de la fila o un rango de etiquetas.
- columna: la etiqueta de la columna o un rango de etiquetas.
'''

import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 25, 21],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)

print(df)

df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)

# Seleccionar una fila específica (por etiqueta)
print(df.loc['a'])
print(df.loc['c'])

# Seleccionar una columna específica
print(df.loc[:, 'Nombre'])

# Seleccionar una celda específica (por etiqueta de fila y columna)
print(df.loc['b', 'Edad'])

# Seleccionar múltiples filas y columnas
print(df.loc[['a', 'c'], ['Nombre', 'Ciudad']])