import random

def lanzar_dados():
    # dado1 = 1 # variables locales
    # dado2 = 5
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    print(f"Lanzaste dado 1: {dado1} y dado 2: {dado2}. La suma es: {suma}")


while True:
    lanzar_dados() # invoca a la función
    continuar = input("\nLazar denuevo? s/n: ").strip().lower()
    if continuar == "n":
        break


