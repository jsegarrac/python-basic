# Asignación de valores
a = 10
b = 5
c = a + b
print("El valor de c es:", c)

var = 10
print ("var: ", var)
var = var + 10
print ("var: ", var)
var += 10
print ("var: ", var)

# Operaciones a nivel de bits
# AND bitwise
resultado_and = a & b
print("AND Bitwise de", a, "y", b, "es:", resultado_and)

# OR bitwise
resultado_or = a | b
print("OR Bitwise de", a, "y", b, "es:", resultado_or)

# XOR bitwise
resultado_xor = a ^ b
print("XOR Bitwise de", a, "y", b, "es:", resultado_xor)

# Desplazamiento a la izquierda
resultado_desplazamiento_izquierda = a << 2
print("Desplazamiento a la izquierda de", a, "es:", resultado_desplazamiento_izquierda)

# Desplazamiento a la derecha
resultado_desplazamiento_derecha = a >> 2
print("Desplazamiento a la derecha de", a, "es:", resultado_desplazamiento_derecha)

print("\n\n\n\n")
#
#
#

# Operaciones a nivel de bits con números binarios

# Convertir números enteros a binario
num1 = bin(10)  # Convertir el número 10 a binario
num2 = bin(5)   # Convertir el número 5 a binario

print("Número binario de 10:", num1)
print("Número binario de 5:", num2)

# Operaciones a nivel de bits con números binarios
# AND
resultado_and = bin(int(num1, 2) & int(num2, 2))
print("AND Bitwise de", num1, "y", num2, "es:", resultado_and)

# OR
resultado_or = bin(int(num1, 2) | int(num2, 2))
print("OR Bitwise de", num1, "y", num2, "es:", resultado_or)

# XOR
resultado_xor = bin(int(num1, 2) ^ int(num2, 2))
print("XOR Bitwise de", num1, "y", num2, "es:", resultado_xor)

# Desplazamiento a la izquierda
resultado_desplazamiento_izquierda = bin(int(num1, 2) << 2)
print("Desplazamiento a la izquierda de", num1, "es:", resultado_desplazamiento_izquierda)

# Desplazamiento a la derecha
resultado_desplazamiento_derecha = bin(int(num1, 2) >> 2)
print("Desplazamiento a la derecha de", num1, "es:", resultado_desplazamiento_derecha)
