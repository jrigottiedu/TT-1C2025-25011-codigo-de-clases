"""
Nuestro programa solicita y almacena en variable los siguientes datos:
<<< nombre, apellido, edad y correo electrónico >>>
Luego los muestra organizados en forma de una tarjeta de presentación en la pantalla.

Desafío planteado:
Supongamos ahora que estos datos se requieren para realizar un registro.

Como requerimiento se solicita que:
1. solo podemos registrar a personas mayores de edad
se entiende por mayor de edad si tiene al menos 18 años cumplidos

2. la persona sea estudiante de Talento Tech TT
"""

# declarar las variables
nombre = None
apellido = None
edad = None
email = None
estudiante_tt = True # asigno True a la variable estudiante_tt

# solicito ingreso de datos
nombre = input("Ingrese su nombre: ")  # siempre retorna una cadena
apellido = input("Ingrese su apellido: ")  # siempre retorna una cadena
edad_str = input("Ingrese su edad: ")  # siempre retorna una cadena
# edad mas alla de que ingrese 30, es un str No es int o float
email = input("Ingrese su email: ")  # siempre retorna una cadena
# estudiante_tt = input("Ingrese si es estudiante s/n")

# Falta el procesamiento
"Vamos a comparar la edad"

"""
PSEUDOCODIGO
si condicion (edad es mayor o igual a 18 ) entonces
    Salgo por el verdadero (True)
    imprimo Registro exitoso
sino
    salgo por el falso (False)
    imprimo Debe ser mayor de 18 - seguí participando

"""
# antes de comparar, debo convertir el tipo de dato de edad a int
edad = int(edad_str)  # int convierte str a int

if edad >= 18 and estudiante_tt == True :  # comparo edad (int) con 18 (int)
    # bloque de codigo si se cumple la condición => True
    print("\nRegistro exitoso")  # indentación
else:
    # bloque de codigo si NO se cumple la condición => False
    print("Seguí participando cuando seas mayor de edad")  # indentación

# imprimir los datos ingresados en terminal / consola / pantalla
"""
Vamos a imprimir si el registro es exitoso o hay algun problema
"""



