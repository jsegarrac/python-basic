# El anidamiento de bucles en Python se refiere a la práctica de colocar un bucle dentro de otro bucle. Esto es útil cuando necesitas repetir una acción dentro de otra acción repetida. Aquí tienes un ejemplo simple de cómo funciona

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Este código imprimirá:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1

lenght = 10
astr="*"
for i in range(lenght):
    for j in range(lenght-i):
        print (" ", end='')
    print(astr)
    astr +="**"

