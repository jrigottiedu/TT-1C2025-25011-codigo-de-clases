# 1. 
# ¿Cuál de las siguientes excepciones se produce al intentar dividir un número por cero en Python?

try:
    lista=[1,2]
    resultado = int("10") / lista[3]
    print(resultado)
except ValueError:
    print("Error al convertir numeros")
except ZeroDivisionError:
    print(f"Se produjo una excepción: No se puede dividir por cero")
except Exception as e:
    print(f"Se produjo una excepción: {e}")

# 4.
#¿Qué módulo estándar utilizarías para trabajar con números aleatorios?

import math

numero = 16
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")

# 6.
# ¿Qué ocurre si intentamos abrir un archivo inexistente en modo lectura sin manejar la excepción correspondiente?
try:
    archivo = open("dato.txt", "r")
except Exception as e:
    print(f"Se produjo una excepción: {type(e).__name__}")
    print(f"Se produjo una excepción: {e}")

# 7.
# ¿Qué método del módulo random permite seleccionar un elemento al azar de una lista?

import random

# a. random.randint(a, b)
# Devuelve un número entero aleatorio entre a y b (ambos inclusive).
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# random.sample(poblacion, k)
# Devuelve una lista de k elementos únicos elegidos aleatoriamente de la población dada.

colores = ["rojo", "verde", "azul", "amarillo"]
muestra = random.sample(colores, 2)
print(f"Muestra aleatoria de 2 colores: {muestra}")

# random.shuffle(lista)
# Reordena los elementos de la lista en el lugar (modifica la lista original).

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista mezclada: {numeros}")


# random.choice(lista)
# Devuelve un único elemento al azar de una lista.

frutas = ["manzana", "banana", "naranja", "kiwi"]
fruta = random.choice(frutas)
print(f"Fruta elegida: {fruta}")


# 10.
# ¿Qué significa el parámetro "w" al abrir un archivo en Python con la función open()?

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open("datos.txt", "w")
archivo.write("Hola, este es un archivo de prueba.\n")
archivo.write("Segunda línea del archivo.\n")
archivo.close()

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

"""
Hola
Este es un archivo de texto
Para estudiar como Python maneja archivos.

Exitos!
Talento Tech
"""

# 11.
# ¿Qué permite la instrucción from nombre_modulo import elemento en Python?
from datetime import date

mi_fecha = date(2025, 6, 16) # año, mes, dia
print("Fecha personalizada:", mi_fecha)

# 12.
# ¿Cuál es el propósito principal del módulo datetime en Python?
# Ver clase_12 5_1 y 5_2
