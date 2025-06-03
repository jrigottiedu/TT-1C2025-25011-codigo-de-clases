# Alcance local de las variables


# Declaracion de una funcion que imprime un saludo generico
def saludoGenerico():
    # Declaramos una variable local
    nombreGenerico = "Estudiante" # es local a la funcion
    print(f"Hola, {nombreGenerico} desde la funcion saludoGenerico")


# Invocamos a la funcion
saludoGenerico()
# print de la variable global
# print(f"\nHola, {nombreGenerico} desde la funcion principal") # NO se puede llamar a una variable local
