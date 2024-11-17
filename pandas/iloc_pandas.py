'''
.iloc: El método .iloc se usa cuando queremos acceder a los datos usando posiciones numéricas (índices).
df.iloc[fila, columna]
- fila: índice de la fila o rango de índices.
- columna: índice de la columna o rango de índices.
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

# Seleccionar una fila específica (por posición)
print(df.iloc[0])  # Primer fila

# Seleccionar una columna específica (por posición)
print(df.iloc[:, 1])  # Segunda columna

# Seleccionar una celda específica (por posición de fila y columna)
print(df.iloc[1, 1])  # Segunda fila, segunda columna

# Seleccionar múltiples filas y columnas
print(df.iloc[[0, 2], [0, 2]])  # Primera y tercera fila, primera y tercera columna