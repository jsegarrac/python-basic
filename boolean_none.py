# En Python, los tipos booleanos representan dos valores: Verdadero (True) y Falso (False)

# Comparaciones simples:
x = 5
y = 10
es_mayor = x > y
print(es_mayor)  # Output: False


# Operadores lógicos:
llueve = True
hace_sol = False
es_verano = True

si_salir = es_verano and hace_sol and not llueve
print(si_salir)  # Output: False

# Valores de retorno de funciones:
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))  # Output: True

#Condiciones en bucles:
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

# Comprobaciones de igualdad:
nombre = "Alice"
es_igual = nombre == "Alice"
print(es_igual)  # Output: True

# none in python = nil = null = undefined
'''
En Python, None es un valor especial que se utiliza para representar la ausencia de un valor válido. Esencialmente, es un tipo de objeto único que se utiliza para denotar la falta de cualquier otro valor. Algunos conceptos clave sobre None incluyen:
Ausencia de valor: None se utiliza cuando una variable o una expresión no tiene un valor asignado o cuando una función no devuelve explícitamente ningún valor.
Comparación: None es considerado falso cuando se evalúa en un contexto booleano, pero no es igual a False. Es importante tener en cuenta la diferencia entre None y False.
Ningún objeto: None es un objeto único en Python y no es lo mismo que una cadena vacía '', una lista vacía [], un diccionario vacío {}, o cualquier otro valor vacío de otro tipo de datos.
Valor por defecto: A menudo se utiliza como valor por defecto para parámetros de función cuando se quiere indicar que el parámetro es opcional y no tiene un valor predefinido.
'''
def saludar(nombre=None):
    if nombre is None:
        print("¡Hola, mundo!")
    else:
        print(f"¡Hola, {nombre}!")

saludar()          # Output: ¡Hola, mundo!
saludar("Juan")    # Output: ¡Hola, Juan!

# En resumen, None es un valor especial en Python que se utiliza para indicar la falta de un valor válido y se puede 
# utilizar en una variedad de contextos para representar la ausencia de datos.
