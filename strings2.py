# Concatenación de cadenas:
cadena1 = "Hola"
cadena2 = "mundo"
concatenacion = cadena1 + ", " + cadena2 + "!"
print("Cadena concatenada:", concatenacion)

# Formateo de cadenas utilizando f-strings:
nombre = "Juan"
edad = 30
saludo = f"Hola, me llamo {nombre} y tengo {edad} años."
print(saludo)

# Eliminación de espacios en blanco alrededor de una cadena:
cadena_con_espacios = "   Hola, mundo!   "
cadena_sin_espacios = cadena_con_espacios.strip()
print("Cadena sin espacios:", cadena_sin_espacios)

# Búsqueda de subcadenas:
cadena = "¡Hola, mundo!"
indice = cadena.find("mundo")
print("Índice de 'mundo':", indice)

# Conteo de ocurrencias de una subcadena:
cadena = "La casa de Juan es grande y la casa de María también es grande."
conteo = cadena.count("casa")
print("Número de veces que aparece 'casa':", conteo)

# Verificación de tipo de caracteres:
cadena = "123abc"
es_alnum = cadena.isalnum()  # Alfanumérico (letras y números)
es_alpha = cadena.isalpha()  # Alfabético (solo letras)
es_digit = cadena.isdigit()  # Dígitos (solo números)
print("¿Alfanumérico?", es_alnum)
print("¿Alfabético?", es_alpha)
print("¿Dígitos?", es_digit)

