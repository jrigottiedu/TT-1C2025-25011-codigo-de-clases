"""
Solicite a la clienta o cliente su nombre, apellido, edad y correo electrónico.
Almacene estos datos en variables.
Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
"""

"""
Algoritmos: pasos lógicos (diagrama de flujo, pseudocódigo y codigo fuente)
Languages: Python (Java, C++, Ruby...)

DATOS => Variable: un contenedor o una caja o espacio en memoria 

30, 50, 677
Juan, Rigotti, juan@gmail.com
numerico (int, float), string (cadena de texto), bool (True -> 1 /False -> 0), 
"""

# declarar las variables
nombre = None
apellido = None
edad = None
email = None

# solicito ingreso de datos
nombre = input("Ingrese su nombre: ")  # siempre retorna una cadena
apellido = input("Ingrese su apellido: ")  # siempre retorna una cadena
edad = int(input("Ingrese su edad: "))  # siempre retorna una cadena
email = input("Ingrese su email: ")  # siempre retorna una cadena

# imprimir los datos ingresados en terminal / consola / pantalla
print("\n********************************")
print("Su nombre es: ", nombre, "Su apellido es: ", apellido)
print("Su nombre es: " + nombre + "Su apellido es: " + apellido)
print(f"Su nombre es: {nombre} \n su apellido es: {apellido}")
# print("Su apellido es: " + apellido)
# print("Su edad es: " + edad)
print(f"Su edad es: {edad} ")
print(f"Su correo es: {email}")
print("********************************")


# Falta el procesamiento
"Yo podria comparar la edad"
"Ingreso la fecha de nacimiento y computo la edad"
