import random

# Inicializamos el número oculto
numero_oculto = random.randint(0, 99)

MAX_INTENTOS = 5
contador_intentos = 0
lista_intentos = []

print("=" * 50)
print("🎯 BIENVENIDO AL JUEGO: GUESS THE NUMBER 🎯")
print("=" * 50)
print()

# Validamos el ingreso del nombre del jugador
jugador_nombre = input("🤖 Por favor, ingresa tu nombre para comenzar: ").strip()
while not jugador_nombre:
    print("❗ Nombre no válido. Intenta nuevamente...")
    jugador_nombre = input("🤖 Ingresa tu nombre: ").strip()

print(f"\n¡Hola {jugador_nombre}! Tienes {MAX_INTENTOS} intentos para adivinar el número secreto entre 0 y 99.")
print("💡 ¡Buena suerte!\n")

# Bucle principal del juego
while True:
    if contador_intentos > 0:
        print("-" * 50)
        print(f"📜 Intentos anteriores: {' | '.join(lista_intentos)}")
        print(f"🔁 Te quedan {MAX_INTENTOS - contador_intentos} intento(s)\n")

    numero = input("🔢 Ingresa un número entre 0 y 99: ")

    while True:
        if not numero.isdigit():
            print("⚠️ Entrada inválida. Solo se permiten números.")
            numero = input("🔢 Intenta nuevamente: ")
            continue

        numero = int(numero)

        if not (0 <= numero <= 99):
            print("🚫 Número fuera de rango (0 a 99).")
            numero = input("🔢 Intenta nuevamente: ")
            continue
        break

    if numero == numero_oculto:
        print("\n🎉 ¡Felicitaciones! Has acertado el número secreto 🎉\n")
        break
    else:
        contador_intentos += 1
        lista_intentos.append(str(numero))
        print("\n❌ Ups... número incorrecto.")

        distancia = abs(numero - numero_oculto)
        if distancia >= 50:
            print("📉 Estás MUY lejos...")
        elif 30 < distancia < 50:
            print("📏 Estás lejos.")
        elif 10 < distancia <= 30:
            print("📐 Estás cerca.")
        else:
            print("🔍 ¡Estás MUY cerca!")

    if contador_intentos == MAX_INTENTOS:
        print("\n💥 Has alcanzado el máximo de intentos.")
        print(f"🔒 El número oculto era: {numero_oculto}")
        opcion = input("🔁 ¿Quieres volver a jugar? (s/n): ").strip().lower()
        if opcion == "n":
            break
        elif opcion == "s":
            contador_intentos = 0
            lista_intentos = []
            numero_oculto = random.randint(0, 99)
            print("\n🔄 ¡Reiniciando juego!\n")

print("\n👋 Gracias por jugar. ¡Hasta la próxima!")
