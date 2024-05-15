# Concatenación
saludo = "Hola"
nombre = "Juan"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)  # Output: Hola, Juan!

# Repetición
cadena = "Hola "
cadena_repetida = cadena * 3
print(cadena_repetida)  # Output: Hola Hola Hola

# Indexación y Slicing
cadena = "Python"
print(cadena[0])     # Output: P
print(cadena[-1])    # Output: n
print(cadena[2:5])   # Output: tho

# Longitud
cadena = "Hola"
longitud = len(cadena)
print(longitud)  # Output: 4

# Métodos de formato
nombre = "Juan"
edad = 30
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Output: Hola, me llamo Juan y tengo 30 años.

# Métodos de manipulación
cadena = "   Hola Mundo   "
print(cadena.strip())          # Output: "Hola Mundo"
print(cadena.upper())          # Output: "   HOLA MUNDO   "
print(cadena.split())          # Output: ["Hola", "Mundo"]
print(cadena.replace("Mundo", "Amigo"))  # Output: "   Hola Amigo   "
