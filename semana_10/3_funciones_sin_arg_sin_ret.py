# Funciones sin argumentos (sin parámetros) sin retorno

"""
Son funciones que no esperan ningún dato (parámetro o argumento) y no retornan ningún dato

Ejemplo: 
1. Una función que da un mensaje de bienvenida
"""
# Declaramos la funcion
def mensajeBinvenida():
    print("Hola, gracias por usar mi App")

# Llamamos o invocamos la funcion
mensajeBinvenida() 


# ------------------------------------------------
# Ejercicio de clase (3 minutos)
"""
Realizar una función que imprima un mensaje de bienvenida (sin parametros / sin argumentos / sin datos)
y muestre las primeras 2 opciones del menú:
1. Alta de producto
2. Mostrar productos
"""
# Resolución 

# Declaracion de la función
def saludarMenu():
    print(
        """
    Hola, como estas?
    Menú de opciones:
    1. Alta de producto
    2. Mostrar productos
    """
    )

# Llamando o invocando a la función
saludarMenu()


