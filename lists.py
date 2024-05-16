# En las listas se pueden mezclar tipso de datos
# Las listas son MUTABLES, pueden cambiar!

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]

# Acceder a elementos de la lista por su índice
print(mi_lista[0])  # Imprime el primer elemento de la lista, en este caso, 1
print(mi_lista[-1])  # Imprime el ultimo elemento de la lista, en este caso, 5

# Modificar elementos de la lista
mi_lista[2] = 10  # Modifica el tercer elemento de la lista a 10
print(mi_lista)   # Imprime la lista modificada: [1, 2, 10, 4, 5]

# Agregar elementos a la lista
mi_lista.append(6)  # Agrega el número 6 al final de la lista
print(mi_lista)     # Imprime la lista actualizada: [1, 2, 10, 4, 5, 6]

# Eliminar elementos de la lista
del mi_lista[3]  # Elimina el cuarto elemento de la lista
# mi_lista.remove <elemento> [index] or (element)
print(mi_lista)  # Imprime la lista actualizada: [1, 2, 10, 5, 6]

# Iterar sobre una lista
for elemento in mi_lista:
    print(elemento)

# Longitud de la lista
print(len(mi_lista))  # Imprime la longitud de la lista, en este caso, 5

# Se pueden especificar rangos y posiciones concretas: ejemplo: [0:2], [1:], [0:-1:1] ...
# las operaciones de suma y acumulacion son validas en las listas: my_lista + [8, 9, 10] or my_lista += [8, 9, 10]

# el método pop() en Python se usa para eliminar y devolver el último elemento de una lista. 
# Definir una lista
mi_lista = [1, 2, 3, 4, 5]

# Eliminar y obtener el último elemento de la lista
elemento_eliminado = mi_lista.pop()

# Imprimir el elemento eliminado y la lista actualizada
print("Elemento eliminado:", elemento_eliminado)
print("Lista actualizada:", mi_lista)

# También puedes pasar un índice específico al método pop() para eliminar y devolver un elemento en ese índice particular de la lista. Por ejemplo:
elemento_eliminado = mi_lista.pop(2)  # Eliminar y devolver el elemento en el índi