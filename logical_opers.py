# Realización de operaciones lógicas y precedencia de operadores
# Performing Logical Operations and Operator Precedence

# operaciones logicas
#and
a = True
b = False

resultado = a and b
print(resultado)  # Output: False


#or
a = True
b = False

resultado = a or b
print(resultado)  # Output: True

#not (no)
a = True

resultado = not a
print(resultado)  # Output: False

# Precedencia de operadores
#parentesis()

resultado = (2 + 3) * 4
print(resultado)  # Output: 20

#**Exponente
resultado = 2 ** 3 * 2
print(resultado)  # Output: 16

#Multiplicación (*) y División (/):

resultado = 10 * 2 / 5
print(resultado)  # Output: 4.0

#Suma (+) y Resta (-):
resultado = 10 + 5 - 3
print(resultado)  # Output: 12

#Operaciones con variables:
x = 5
y = 3

resultado = (x + 2) * y
print(resultado)  # Output: 21

# OPERADOR IN en listas y diccionarios
# El operador in se utiliza para verificar si un valor está presente en una secuencia (como una lista, una cadena o un diccionario) y devuelve True si el valor está presente y False si no lo está.

lista = [1, 2, 3, 4, 5]

# Verificar si un elemento está en la lista
resultado = 3 in lista
print(resultado)  # Output: True

resultado = 6 in lista
print(resultado)  # Output: False

# Verificar si un carácter está en una cadena
cadena = "Hola Mundo"
resultado = 'a' in cadena
print(resultado)  # Output: True

resultado = 'x' in cadena
print(resultado)  # Output: False

# Verificar si una clave está en un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
resultado = 'a' in diccionario
print(resultado)  # Output: True

resultado = 'd' in diccionario
print(resultado)  # Output: False

# ver mas operadeores en la dopcu de python