"""
En este código modelo valida ingresos de manera individual
"""

# Solicitamos el ingreso de los datos nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# En este módulo validamos el nombre con el operador != y el dato vacio asi ""

if nombre != "": # pregunta si el valor de nombre es distinto de ""
    # en caso que la condicion se cumpla
    print(f"Su nombre es: {nombre}")
else:
    # en caso que la condicion NO se cumpla
    print(f"Su nombre es: ERROR")

# En este módulo validamos el apellido sin operador (alternativa más avanzada)

if apellido : # pregunta si la variable apellido contiene algo
    #en caso que la condicion se cumpla
    print(f"Su nombre es: {apellido}")
else:
    #en caso que la condicion NO se cumpla
    print(f"Su nombre es: ERROR")