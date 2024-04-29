# WHILE
# Este ejemplo muestra cómo utilizar un bucle while para imprimir los números del 1 al 5:
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# dibuja triangulo desdendente de *
count = 10
while(count > 0):
    print("*" * count)
    count -= 1

# Validación de entrada
numero = 0
while numero < 1 or numero > 10:
    numero = int(input("Por favor ingresa un número entre 1 y 10: "))
print("¡Has ingresado un número válido!")

# Suma acumulativa
suma = 0
contador = 1
while contador <= 10:
    suma += contador
    contador += 1
print("La suma acumulativa es:", suma)

# Búsqueda en una lista
numeros = [1, 2, 3, 4, 5]
busqueda = int(input("Ingresa un número para buscar en la lista: "))
encontrado = False
indice = 0
while indice < len(numeros):
    if numeros[indice] == busqueda:
        encontrado = True
        break
    indice += 1

if encontrado:
    print("El número", busqueda, "ha sido encontrado en la lista.")
else:
    print("El número", busqueda, "no ha sido encontrado en la lista.")

# FOR
# Iteración sobre una lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

lista2 = ["lista 1", "lista 2", "lista 3", "lista 4", "lista 5"]
for elemento in lista:
    print(elemento)    

# Iteración sobre una cadena
cadena = "Hola"
for caracter in cadena:
    print(caracter)

# Iteración sobre un rango
for i in range(5):
    print(i)
# Este bucle imprimirá los números del 0 al 4.

# Iteración sobre un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in diccionario:
    print("Clave:", clave, "- Valor:", diccionario[clave])
# Este bucle iterará sobre las claves del diccionario e imprimirá cada clave y su valor correspondiente.

# Iteración sobre una lista de tuplas
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
for numero, letra in pares:
    print("Número:", numero, "- Letra:", letra)
#Este bucle iterará sobre cada tupla en la lista y desempaquetará los elementos en las variables numero y letra, luego imprimirá ambos.

#el comando break dentro de un bucle, rompe la ejecucion de este!
for i in range(0,10):
    if i == 8:
        break
        print ("In IF:", i)
    print(i)
#el comando continue, hace lo contrario de brake
    