import pandas as pd

# Ruta del archivo Excel
ruta_archivo = 'file_example_XLSX_10.xlsx'

# Leer el archivo Excel
df = pd.read_excel(ruta_archivo)

# Mostrar el DataFrame
print(df)
