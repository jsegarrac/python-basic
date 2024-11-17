# uso de funciones, control de excepciones y gestion de ficheros

def leer_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:  # Abre el archivo en modo lectura
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{ruta}'.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
    finally:
        print("La clausaula finally siempre se ejecuta - leer_archivo")

def escribir_archivo(ruta, texto):
    try:
        with open(ruta, 'a') as archivo:  # Abre el archivo en modo de agregar ('append')
            archivo.write(texto)
            print("Texto agregado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en el archivo '{ruta}'.")
    except Exception as e:
        print(f"Error inesperado al escribir en el archivo: {e}")
    finally:
        print("La clausaula finally siempre se ejecuta - escribir_archivo")

# Ejemplo de uso
ruta_archivo = 'archivo_ejemplo.txt'

# Leer el archivo
leer_archivo(ruta_archivo)

# Escribir en el archivo
texto_a_agregar = "\nEste es un nuevo texto para agregar."
escribir_archivo(ruta_archivo, texto_a_agregar)

# Volver a leer el archivo para ver el cambio
leer_archivo(ruta_archivo)