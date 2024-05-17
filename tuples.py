# Una tupla es una colección ordenada e inmutable de elementos. Las tuplas se utilizan para agrupar varios elementos 
# en una sola estructura. A diferencia de las listas, una vez creada una tupla, sus elementos no se 
# pueden modificar (es inmutable). Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.
'''Características de las tuplas
Ordenadas: Los elementos tienen un orden definido y pueden ser accedidos mediante índices.
Inmutables: No se pueden cambiar después de su creación.
Permiten duplicados: Los elementos pueden repetirse.
Heterogéneas: Pueden contener elementos de diferentes tipos de datos (enteros, cadenas, listas, etc.).'''

# Creación de tuplas

# Tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# Tupla con elementos
tupla = (1, 2, 3)
print("Tupla con elementos:", tupla)

tupla_mixta = (1, "Hola", 3.4, [1, 2, 3])
print("Tupla mixta:", tupla_mixta)

# Tupla de un solo elemento (nota la coma al final)
tupla_un_elemento = (5,)
print("Tupla de un solo elemento:", tupla_un_elemento)

# Acceso a elementos
tupla = (1, 2, 3, 4)
print("Primer elemento:", tupla[0])  # Salida: 1
print("Tercer elemento:", tupla[2])  # Salida: 3

# Desempaquetado de tuplas
tupla = (1, 2, 3)
a, b, c = tupla
print("Desempaquetado:")
print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3

# Operaciones comunes con tuplas

# Concatenación
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print("Concatenación de tuplas:", tupla_concatenada)  # Salida: (1, 2, 3, 4)

# Repetición
tupla = (1, 2)
tupla_repetida = tupla * 3
print("Repetición de tupla:", tupla_repetida)  # Salida: (1, 2, 1, 2, 1, 2)

# Verificación de existencia
tupla = (1, 2, 3)
print("¿2 está en la tupla?:", 2 in tupla)  # Salida: True
print("¿5 está en la tupla?:", 5 in tupla)  # Salida: False

# Métodos de tuplas

# count()
tupla = (1, 2, 3, 1, 1)
print("Número de veces que aparece 1:", tupla.count(1))  # Salida: 3

# index()
tupla = (1, 2, 3)
print("Índice del elemento 2:", tupla.index(2))  # Salida: 1

# Usos comunes de las tuplas

# Devolución de múltiples valores desde una función
def dividir_y_restar(a, b):
    division = a / b
    resta = a - b
    return division, resta

resultado = dividir_y_restar(10, 2)
print("Resultado de la función (división, resta):", resultado)  # Salida: (5.0, 8)

# Almacenamiento de datos heterogéneos
persona = ("Juan", 28, "Ingeniero")
print("Datos de la persona:", persona)  # Salida: ('Juan', 28, 'Ingeniero')

# Ejemplo práctico

# Definir una tupla
punto = (2, 3)

# Acceder a los elementos de la tupla
x = punto[0]
y = punto[1]

print(f"Coordenadas del punto: x={x}, y={y}")

# Intentar modificar la tupla (esto generará un error)
# punto[0] = 5  # TypeError: 'tuple' object does not support item assignment
