# Solicitamos el ingreso del nombre
edad = input("Ingrese su edad: ")

# Validamos que el dato se haya ingresado y que sea mayor o igual a 18
if edad != "" and int(edad) >= 18:
    print(edad)
else :
    print("ERROR")


"""
Analizamos la línea 5
if edad != "" and int(edad) >= 18:

1. 
recordar como funciona la operación AND
si algunas de las condiciones retorna False, el resultado es False
primero evalúa edad != "", si hay ingreso de dato retorna True,
si no hay ingreso de dato retorna False y se interrumpe el AND

2.
si damos vuelta el orden de las comparaciones de esta manera
if int(edad) >= 18 and edad != "" :
si algunas de las condiciones retorna False, el resultado es False
primero evalúa int(edad) >= 18, pero si no hay ingreso, van a notar
un error en la terminal, esto se debe a que int() no puede convertir un dato qu eno existe
"""


