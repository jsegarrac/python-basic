# ejemplos con clases

# En Python, las clases y los objetos son conceptos fundamentales en la programación orientada a objetos. Una clase es como un plano o molde que define las 
# características y comportamientos de los objetos que se crearán a partir de ella. Un objeto es una instancia de una clase.
# Continuación, te muestro ejemplos básicos y avanzados de cómo crear y trabajar con clases y objetos en Python.

# 1. Ejemplo básico de una clase y objeto
# Definir una clase llamada 'Perro'
class Perro:
    # Constructor (método especial que inicializa el objeto)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

    # Método para que el perro ladre
    def ladrar(self):
        print(f'{self.nombre} dice: ¡Guau!')

    # Método para mostrar la edad del perro
    def mostrar_edad(self):
        print(f'{self.nombre} tiene {self.edad} años.')

# Crear un objeto de la clase Perro
mi_perro = Perro('Rex', 5)

# Llamar a los métodos del objeto
mi_perro.ladrar()  # Rex dice: ¡Guau!
mi_perro.mostrar_edad()  # Rex tiene 5 años.


# 2. Herencia entre clases
# La herencia permite crear nuevas clases que heredan métodos y atributos de una clase base. Aquí te muestro cómo hacerlo:
# Clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método vacío (se sobreescribirá en las clases derivadas)

# Clase derivada 'Perro', que hereda de 'Animal'
class Perro(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} dice: ¡Guau!')

# Clase derivada 'Gato', que hereda de 'Animal'
class Gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} dice: ¡Miau!')

# Crear instancias (objetos) de las clases derivadas
perro = Perro('Rex')
gato = Gato('Felix')

# Llamar a los métodos de cada objeto
perro.hacer_sonido()  # Rex dice: ¡Guau!
gato.hacer_sonido()   # Felix dice: ¡Miau!


# 3. Atributos y métodos de clase
# Los atributos de clase son compartidos por todas las instancias de la clase. Mientras que los métodos de instancia trabajan sobre los atributos de un 
# objeto específico, los métodos de clase se aplican a la clase en sí.
class Coche:
    # Atributo de clase (compartido por todos los objetos)
    num_ruedas = 4

    def __init__(self, marca, modelo):
        # Atributos de instancia (únicos para cada objeto)
        self.marca = marca
        self.modelo = modelo

    # Método de instancia
    def mostrar_info(self):
        print(f'Coche: {self.marca} {self.modelo} con {Coche.num_ruedas} ruedas')

    # Método de clase
    @classmethod
    def cambiar_num_ruedas(cls, num):
        cls.num_ruedas = num

# Crear objetos de la clase Coche
coche1 = Coche('Toyota', 'Corolla')
coche2 = Coche('Ford', 'Focus')

# Mostrar información de los coches
coche1.mostrar_info()  # Coche: Toyota Corolla con 4 ruedas
coche2.mostrar_info()  # Coche: Ford Focus con 4 ruedas

# Cambiar el número de ruedas para todos los coches
Coche.cambiar_num_ruedas(6)

# Mostrar la nueva información después del cambio
coche1.mostrar_info()  # Coche: Toyota Corolla con 6 ruedas
coche2.mostrar_info()  # Coche: Ford Focus con 6 ruedas

# 4. Métodos estáticos
# Un método estático no recibe ni la instancia (self) ni la clase (cls) como primer argumento. Es simplemente una función que se agrupa dentro de la clase.
class Calculadora:
    # Método estático
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

# Llamar a los métodos estáticos sin necesidad de crear un objeto
resultado_suma = Calculadora.sumar(5, 3)
resultado_resta = Calculadora.restar(10, 4)

print(f'Suma: {resultado_suma}')  # Suma: 8
print(f'Resta: {resultado_resta}')  # Resta: 6

# 5. Encapsulamiento: atributos y métodos privados
# En Python, los atributos y métodos se pueden hacer privados utilizando un guion bajo (_) o doble guion bajo (__).
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre       # Atributo público
        self.__edad = edad         # Atributo privado (con doble guion bajo)

    # Método público
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Edad: {self.__edad}')

    # Método privado
    def __cumplir_anios(self):
        self.__edad += 1

    # Método para incrementar edad desde el exterior
    def envejecer(self):
        self.__cumplir_anios()

# Crear un objeto de la clase Persona
persona = Persona('Carlos', 30)

# Acceder al método público
persona.mostrar_info()  # Nombre: Carlos, Edad: 30

# Intentar acceder al atributo privado dará un error:
# print(persona.__edad)  # AttributeError

# Usar el método para incrementar la edad
persona.envejecer()
persona.mostrar_info()  # Nombre: Carlos, Edad: 31

# 6. Clases con propiedades (uso de @property)
# El decorador @property se usa para definir métodos que se comportan como atributos de solo lectura, y @setter para permitir la modificación controlada de esos atributos.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    # Definir el getter con @property
    @property
    def precio(self):
        return self._precio

    # Definir el setter para validar el precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError('El precio no puede ser negativo.')
        self._precio = nuevo_precio

# Crear un objeto Producto
producto = Producto('Laptop', 1200)

# Acceder al precio
print(producto.precio)  # 1200

# Modificar el precio
producto.precio = 1300
print(producto.precio)  # 1300

# Intentar establecer un precio negativo lanza un error
# producto.precio = -500  # ValueError: El precio no puede ser negativo.
