# if
# Recuerda que la indentación es fundamental en Python, ya que determina el bloque de código que se ejecutará dentro de cada condición.

x = 10

# Ejemplo de condicional 1
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")


# Ejemplo de condicional 2

x = 10
y = 5

if x > 5:
    if y > 2:
        print("Tanto x como y son mayores que 5 y 2 respectivamente.")
    else:
        print("x es mayor que 5, pero y no es mayor que 2.")
else:
    print("x no es mayor que 5.")
