# Alcance global de las variables

# Declaramos una variable global (porque esta fuera de las funciones)
nombreGenerico = "Estudiante"

# Declaracion de una funcion que imprime un saludo generico
def saludoGenerico():
    print(f"Hola, {nombreGenerico} desde la funcion saludoGenerico")


# Invocamos a la funcion
saludoGenerico()
# print de la variable global
print(f"\nHola, {nombreGenerico} desde la funcion principal")