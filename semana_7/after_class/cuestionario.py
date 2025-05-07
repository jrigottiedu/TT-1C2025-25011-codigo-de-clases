# Pregunta 1
# lista = ["a", "b", "c", "d", "e"]
# print(f"Longitud de la lista es {len(lista)} y el índice del último elemento es {lista.index("e")}")
# print(lista[4])
# print(lista[-1])
# print(lista[-2])

# Pregunta 2
# ingresos = [100, 150, 250, 300, 120]
# acumulador = 0
# for ingreso in ingresos:
#     acumulador += ingreso
# print(f"Ingreso acumulado: {acumulador}")


# Pregunta 3
# contador = 0
# while contador < 3:
#     print("Intento:", contador)
#     contador += 1

# Pregunta 4
# for i in range(2, 10, 2): # range(valor_inicial, valor_final(excluyente), incremento)
#     print(i)

# Pregunta 5
# palabra = "Python"
# for letra in palabra:
#     if letra == "o":
#         continue
#     print(letra)

# Pregunta 6
# while True:
#     nombre = input("Ingrese su nombre: ").strip()
#     if not nombre == "":
#         break
#     else:
#         print("No se admite vacío!")

# cadena = "Talento"
# for caracter in cadena:
#     print(caracter)

# Pregunta 7
# lista = ["A", "B", "C"]
# for i in range(len(lista)): # 0, 1, 2
#     print(f"Elemento {i}: {lista[i]}")

# Pregunta 8
# for i in range(5, 15, 3): # valores de i: 5, 8, 11, 14
#     print(i)

# Pregunta 9
# contador = 0
# while contador < 3:
#     print(contador)
#     contador += 1


# Pregunta 10
# lista = ["A", "B", "C", "D"]
# # print(lista[3])

# indice = 0
# while indice < len(lista):  # indice: 0, 1, 2, 3
#     print(f"Elemento {indice}: {lista[indice]}")
#     indice += 1

# Pregunta 11
numeros = [10, 20, -30, 40, -50]
suma = 0
for numero in numeros:
    if numero < 0:
        continue
    suma += numero

print(suma)

# Pregunta 12
# numeros = [10, -5, 20, 30]
# for numero in numeros:
#     if numero < 0:
#         break
#     print(numero)
