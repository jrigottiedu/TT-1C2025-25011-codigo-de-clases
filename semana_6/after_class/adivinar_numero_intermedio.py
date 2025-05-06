"""
Juego: "Guess the number"

Desarrollamos el código de una App en la que un jugador compite adivinando en número oculto en el código.
El número oculto se obtiene importando la librería random que genera un número aleatorio.

En esta versión intermedia:
1. Usamos la librería random para generar un número aleatorio entre 0 y 9
2. Validamos el ingreso del nombre del jugador
3. El jugador tiene un límite de 3 intentos para adivinar el número

"""

# importamos la libreria random
import random

# declaramos el número oculto en una constante
numero_oculto = random.randint(0, 9)

# declaramos la cantidad máxima de intentos
MAX_INTENTOS = 3

# declaramos e inicializamos el contador de intentos
contador_intentos = 0

print("*" * 40)
print("Bienvenido al Juego Guess the number!")
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
while contador_intentos < MAX_INTENTOS:
    # validamos el ingreso del numero a evaluar
    numero = input(f"{jugador_nombre}, ingresa un número entre 0 y 9: ")
    while True:
        if numero.isdigit():
            numero = int(numero)
            break
        else:
            print("Dato incorrecto! Por favor intenta nuevamente...")
            numero = input(f"Ingresa un número entre 0 y 9: ")

    # procesamos el numero ingresado para ver si hay acierto:

    if numero == numero_oculto:
        print("Felicitaciones! Ha acertado.")
        break
    else:
        print("Ops! Intenta nuevamente...")
        contador_intentos += 1 # Incrementamos el contador de intentos
    if contador_intentos == MAX_INTENTOS: # si el contador_intentos alcanza MAX_INTENTOS signifca que el jugador perdió
        print("Ops... alcanzaste la máxima cantidad e intentos..")
        print(f"El número oculto era: {numero_oculto}")