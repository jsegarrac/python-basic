# Trabajando con tuplas. Las tuplas son inmutables, no se pueden cambiar, solo eliminar
# Creación de una tupla
mi_tupla = (1, 2, 3, 4, 5) # el deliminatod es la , pero se puede cambiar
mi_tupla_nueva = (mi_tupla[0], 666, mi_tupla[4])

# Accediendo a elementos individuales de la tupla
primer_elemento = mi_tupla[0]
print("Primer elemento de la tupla:", primer_elemento)

# Longitud de una tupla
longitud_tupla = len(mi_tupla)
print("Longitud de la tupla:", longitud_tupla)

# Tupla nueva copiando datos de otra
print("Nueva tupla:", mi_tupla_nueva)

# Borrar tupla
del mi_tupla_nueva

# Iterando sobre los elementos de la tupla
for elemento in mi_tupla:
    print(elemento)



# Trabajando con diccionarios. Clave - valor, son similares a las listas y son mutables
# Creación de un diccionario
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print ("Mi diccionario:", mi_diccionario)

# Accediendo a valores individuales del diccionario
nombre = mi_diccionario['nombre']
print("Nombre:", nombre)
print(mi_diccionario['nombre'])

edad = mi_diccionario['edad']
print("Edad:", edad)

ciudad = mi_diccionario['ciudad']
print("Ciudad:", ciudad)

# Modificando valores en el diccionario
mi_diccionario['edad'] = 35
print("Diccionario después de modificar la edad:", mi_diccionario)

# Agregando nuevos pares clave-valor al diccionario
mi_diccionario['profesion'] = 'Ingeniero'
print("Diccionario después de agregar una nueva clave-valor:", mi_diccionario)

# Eliminando una clave-valor del diccionario
del mi_diccionario['ciudad']
print("Diccionario después de eliminar la clave 'ciudad':", mi_diccionario)

#
# Iterando sobre las claves y valores del diccionario
for clave, valor in mi_diccionario.items():
    print(clave + ":", valor)

# Limpia el diccionario
mi_diccionario.clear()
# Elimina el diccionario
del mi_diccionario


