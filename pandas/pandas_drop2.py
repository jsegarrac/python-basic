# drop index and columns
'''
El método .drop() en Pandas se utiliza para eliminar filas o columnas de un DataFrame. Es muy útil cuando quieres limpiar datos eliminando información irrelevante o duplicada. A continuación, te explico cómo usar .drop() para ambas opciones:

Sintaxis básica de .drop()

df.drop(labels, axis, inplace)

- labels: el nombre o lista de nombres de filas o columnas a eliminar.
- axis: indica si eliminar filas (axis=0, por defecto) o columnas (axis=1).
- inplace: si se establece en True, modifica el DataFrame original. Si es False (por defecto), devuelve un nuevo 
    DataFrame con las filas o columnas eliminadas sin modificar el original.
    ej: df.drop('Edad', axis=1, inplace=True)
- Para eliminar filas usando su posición en lugar de su nombre o índice, puedes combinar .drop() con .index o utilizar .iloc.
    ej: df_sin_primera = df.drop(df.index[0])

'''
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 25, 21],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

print (df)

# filas
# Eliminar una fila específica por índice
df_sin_a = df.drop('a')  # Elimina la fila con índice 'a' sin modificar el original
print(df_sin_a)

# Eliminar múltiples filas
df_sin_ac = df.drop(['a', 'c'])
print(df_sin_ac)

# columnas
# Eliminar una columna específica
df_sin_edad = df.drop('Edad', axis=1)
print(df_sin_edad)

# Eliminar múltiples columnas
df_sin_edadyciudad = df.drop(['Edad', 'Ciudad'], axis=1)
print(df_sin_edadyciudad)
