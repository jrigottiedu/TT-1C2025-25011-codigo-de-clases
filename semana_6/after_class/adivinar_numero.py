"""
Juego: "Guess the number"

Desarrollamos el código de una App en la que un participante compite adivinando en número oculto en el código.
El número oculto puede tener un valor entre 0 y 9

En esta primera versión:
1. Declaramos el número oculto como una constante con un valor fijo
2. Validamos el ingreso del nombre del jugador
3. El jugador no tiene límite de intentos para adivinar el número

"""

# declaramos el número oculto en una constante
NUMERO_OCULTO = 3

print("*" * 40)
print("Bienvenido al Juego Guess the number!")
print("Debes adivinar un número oculto entre 0 y 9")
print("*" * 40)
print()

# validamos el ingreso del nombre del jugador
jugador_nombre = input("Para comenzar ingresa tu nombre: ").strip()
while True:
    if len(jugador_nombre) == 0:
        print("Dato incorrecto! Por favor intente nuevamente...")
        jugador_nombre = input("Ingresa tu nombre: ").strip()
    else:
        break

# Definimos el Bucle Principal en el que el Jugador intenta adivinar el número
while True:
    # validamos el ingreso del numero a evaluar
    numero = input(f"{jugador_nombre}, ingresa tu número: ")
    while True:
        if numero.isdigit():
            numero = int(numero)
            break
        else:
            print("Dato incorrecto! Por favor intenta nuevamente...")
            numero = input(f"Ingrese su número: ")

    # procesamos el numero ingresado para ver si hay acierto:

    if numero == NUMERO_OCULTO:
        print("Felicitaciones! Ha acertado.")
        break
    else:
        print("Ops! Intenta nuevamente...")
