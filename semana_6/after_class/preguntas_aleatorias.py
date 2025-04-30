import random

while True:
    numero_pregunta = random.randint(0, 3) # cadena.replace(" ", "*")
    lista_preguntas = ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4"]

    print(lista_preguntas[numero_pregunta])

    seguir = input("Seguimos? s/n")
    if seguir == "n":
        break
