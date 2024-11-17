import json
import os

directorio_actual = os.getcwd()
print("El directorio actual es:", directorio_actual)

# Leer datos de un archivo JSON

with open("file.json", 'r') as fichero:
    datos = json.load(fichero)

print(datos)
print ("\n\n")

# Escribir en  un archivo JSON

# Datos que queremos guardar en un archivo JSON
datos = {
    "nombre": "JSC",
    "edad": 56,
    "ciudad": "Collbato"
}

# Guardar los datos en un archivo JSON
with open('salida.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)  # Indent para formateo bonito

    
with open("salida.json", 'r') as fichero:
    datos = json.load(fichero)

print(datos)
print ("\n\n")