# Definir una cadena
cadena = "¡Hola, mundo!"

# Imprimir la cadena
print("Cadena original:", cadena)

# Obtener la longitud de la cadena
longitud = len(cadena)
print("Longitud de la cadena:", longitud)

# Convertir la cadena a mayúsculas
mayusculas = cadena.upper()
print("Cadena en mayúsculas:", mayusculas)

# Convertir la cadena a minúsculas
minusculas = cadena.lower()
print("Cadena en minúsculas:", minusculas)

# Reemplazar parte de la cadena
nueva_cadena = cadena.replace("Hola", "Saludos")
print("Cadena con reemplazo:", nueva_cadena)

# Dividir la cadena en una lista de palabras
palabras = cadena.split(",")
print("Lista de palabras:", palabras)

# Comprobar si la cadena comienza con un cierto prefijo
comienza_con_hola = cadena.startswith("Hola")
print("¿La cadena comienza con 'Hola'?", comienza_con_hola)

# Comprobar si la cadena termina con un cierto sufijo
termina_con_mundo = cadena.endswith("mundo!")
print("¿La cadena termina con 'mundo!'?", termina_con_mundo)
