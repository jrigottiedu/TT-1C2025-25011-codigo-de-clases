# Alcance global de las variables

# Declaramos una variable global (es global cuando esta fuera de las funciones)
nombreGenerico = "Estudiante"

# Declaracion de una función que imprime un saludo generico
def saludoGenerico():
    print(f"Hola, {nombreGenerico} desde la funcion saludoGenerico")


# Invocamos a la funcion
saludoGenerico()
# print de la variable global funciona correctamente
print(f"\nHola, {nombreGenerico} desde la funcion principal")

"""
En este caso, la variable global nombreGenerico 
se puede usar en cualquier lado, 
en el cuerpo principal del archivo Python
o en cualquier función que definamos con def
Por eso decimos que tiene alcance global
"""