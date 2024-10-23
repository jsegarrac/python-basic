# NOTA: El uso de la estructura with es preferido porque garantiza que el archivo se cierre automáticamente, incluso si ocurre un error durante su manejo.

# Abrir y leer un archivo

# Abrir el archivo en modo lectura
archivo = open('archivo.txt', 'r')

# Leer todo el contenido del archivo
contenido = archivo.read()
print(contenido)

# Cerrar el archivo
archivo.close()

# Abrir y leer un archivo por lineas en modo lectura
# COn la clausula with, no tenemos que cerrar el fichero!!! se hace automaticamente

with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # `strip()` elimina saltos de línea adicionales


# escribir en fichero
with open('archivo.txt', 'w') as archivo:
    archivo.write('Esta es una nueva línea de texto.\n')
    archivo.write('Este contenido sobrescribe el archivo existente.\n')


# añadir contenido a fichero existente
# Abrir el archivo en modo añadir (append)
with open('archivo.txt', 'a') as archivo:
    archivo.write('Esta línea se añade al final del archivo.\n')


# Leer y escribir en el mismo archivo (modo lectura/escritura)
# Abrir el archivo en modo lectura y escritura
with open('archivo.txt', 'r+') as archivo:
    contenido = archivo.read()  # Leer el contenido
    print(contenido)
    
    # Mover el cursor al final del archivo para escribir
    archivo.write('\nEsta línea se escribe al final del archivo. Modo r+')

