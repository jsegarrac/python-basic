# Comprobar si un archivo existe antes de abrirlo
# Para evitar errores, puedes comprobar si un archivo existe antes de abrirlo usando el módulo os.

# NOTA: El uso de la estructura with es preferido porque garantiza que el archivo se cierre automáticamente, incluso si ocurre un error durante su manejo.

import os

if os.path.exists('archivo1.txt'):
    with open('archivo1.txt', 'r') as archivo:
        print(archivo.read())
else:
    print('El archivo no existe')



# Leer y escribir archivos binarios
# Para trabajar con archivos binarios (imágenes, archivos de audio, etc.), puedes usar los modos 'rb' (lectura binaria) y 'wb' (escritura binaria).

# Leer archivo binario
with open('imagen.jpg', 'rb') as archivo:
    datos = archivo.read()
    print(datos[:20])  # Imprimir los primeros 20 bytes


# Escribir archivo binario
with open('copia_imagen.jpg', 'wb') as archivo:
    archivo.write(datos)  # Escribir los datos leídos previamente