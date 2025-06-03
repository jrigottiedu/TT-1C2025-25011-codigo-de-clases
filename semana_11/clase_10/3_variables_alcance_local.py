# Alcance local de las variables


# Declaracion de una funcion que imprime un saludo generico
def saludoGenerico():
    # Declaramos una variable local
    nombreGenerico = "Estudiante" # es local a la funcion
    print(f"Hola, {nombreGenerico} desde la funcion saludoGenerico")


# Invocamos a la funcion
saludoGenerico()
# print de la variable local NO funciona, porque existe solo dentro de la funcion saludoGenerico
# print(f"\nHola, {nombreGenerico} desde la funcion principal") # daría error

"""
En este caso, la variable local nombreGenerico
ahora esta declarada dentro de la función saludoGenerico 
de manera que su valor solo se puede usar dentro de esa función
Por eso decimos que tiene alcance local
"""