"""
Juego: "Guess the number"

Desarrollamos el código de una App en la que un participante compite adivinando en número oculto autogenerado.
El número oculto se obtiene importando la librería random que genera un número aleatorio.

En esta versión avanzada:
1. Usamos la librería random para generar un número aleatorio entre 0 y 99
2. Validamos el ingreso del nombre del jugador
3. El jugador tiene un límite de 5 intentos para adivinar el número
4. Validamos que el número ingresado sea válido y que este entre los valores indicados, es decir entre 0 y 99
5. A través del uso de una lista mostramos al usuario los números ingresados en los intentos anteriores
6. Le damos una ayuda al jugador!
   si la diferencia entre el numero ingresado y el numero oculto es mayor a 50: Estas muy lejos!
   si la diferencia entre el numero ingresado y el numero oculto es mayor a 30 y menor o igual a 50: Estas lejos!
   si la diferencia entre el numero ingresado y el numero oculto es mayor a 10 y menor o igual a 30: Estas cerca!
   si la diferencia entre el numero ingresado y el numero oculto es menor o igual a 10: Estas muy cerca!
7. Si el jugador no acierta, puede repetir el juego

"""

# importamos la libreria random
import random

# inicalizamos el número oculto con el valor que retorna el método randint()
numero_oculto = random.randint(0, 99)

# declaramos la cantidad máxima de intentos
MAX_INTENTOS = 5

# declaramos e inicializamos el contador de intentos
contador_intentos = 0

# declaramos una lista que vamos a utilizar para almacenar y mostrar los intentos anteriores
lista_intentos = []

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

# Mostramos un mensaje de bienvenida personalizado
print(f"{jugador_nombre}, para comenzar ingresa un número entre 0 y 99: ")

# Bucle While que contiene el juego
while True:

    # este bloque se ejecuta solo a partir de la segunda iteración
    if contador_intentos > 0:
        print(f"Números ya ingresados: " + " - ".join(lista_intentos))
        print(f"Te quedan {MAX_INTENTOS-contador_intentos} intentos!\n")

    # solicitamos al jugador que ingrese su número
    numero = input(f"Ingresa un número entre 0 y 99: ")

    # Bucle while para validar el número ingresado
    while True:
        # validamos que el numero ingresado sea numerico natural positivo
        if not numero.isdigit():
            print("Dato incorrecto! Por favor intenta nuevamente...")
            numero = input(f"Ingresa un número entre 0 y 99: ")
            continue

        # como no se cumplió la condición del if anterior, podemos convertir de str a int
        numero = int(numero)

        # validamos que el número este dentro del rango menor a 99
        if numero > 99:
            print("Ha ingresado un número fuera de rango!")
            numero = input(f"Ingresa un número entre 0 y 99: ")
            continue
        break  # si llego a esta instancia es porque todo fue validado

    # procesamos el numero ingresado para ver si hay acierto:

    if numero == numero_oculto:
        print("Felicitaciones! Ha acertado =)")
        break

    else:
        contador_intentos += 1  # Incrementamos el contador de intentos
        lista_intentos.append(str(numero))  # agregamos a la lista el último numero intentado
        print(f"\nOps! Haz fallado :(")

        distancia_acierto = abs(numero - numero_oculto)
        match distancia_acierto:
            case distancia_acierto if distancia_acierto >= 50:
                print("Estas muy lejos!")
            case distancia_acierto if (
                distancia_acierto > 30 and distancia_acierto <= 50
            ):
                print("Estas lejos")
            case distancia_acierto if (
                distancia_acierto > 10 and distancia_acierto <= 30
            ):
                print("Estas cerca")
            case distancia_acierto if distancia_acierto <= 10:
                print("Estas muy cerca!")

    if (
        contador_intentos == MAX_INTENTOS
    ):  # si el contador_intentos alcanza MAX_INTENTOS signifca que el jugador perdió
        print("Ops... alcanzaste la máxima cantidad e intentos...")
        print(f"El número oculto era: {numero_oculto}")
        opcion = input("Deseas volver a jugar? presione s/n: ")
        if opcion.strip().lower() == "n":
            break
        elif opcion.strip().lower() == "s":
            # reinizializamos las variables
            contador_intentos = 0
            lista_intentos = []
            numero_oculto = random.randint(0, 99)
print("Gracias por tu participación!")
