# Write Three Functions That Are Able to Add, Subtract, and Multiply Two Numbers
# Write a Function to Divide Two Numbers and Implement a Check for Division by 0

def suma (a, b):
    resultado = a + b
    return(resultado)

def resta(a, b):
    resultado = a - b
    return(resultado)

def multi(a, b):
    resultado = a * b
    return (resultado)

def divi (a, b):
    if b == 0:
        return "Error: Cannot divide by ZERO!"
    else:
        resultado = a / b
    return (resultado)

sumar = suma (10, 20)
print("suma:", sumar)

restar = resta (10, 20)
print("resta:", restar)

multiplicar = multi (10, 20)
print("multi:", multiplicar)

dividir = divi (10, 0)
print("divi:", dividir)
