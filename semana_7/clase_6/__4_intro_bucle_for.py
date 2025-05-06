"""
Bucle For:
- permite ejecutar un bloque de código un número definido de veces
- no se usan índices o contadores, por lo que simplifica el código
- hay una condición implícita
- ideal para iterar sobre cadenas, listas, (diccionarios) o rangos numéricos
"""

# Usamos el bucle For para recorrer los elementos de la cadena="Python"
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

for producto in productos:
    print(producto)

# usamos un bucle for para sumar los números del 1 al 5 usando un acumulador
acumulador = 1
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    acumulador = acumulador * numero

print(f"El acumulado es: {acumulador}")


# Usamos el bucle For para recorrer los elementos de la cadena="Python"
cadena = "Python"
for caracter in cadena:
    print(caracter)


# Introducimos la función range()
# ranger(5) retorna una lista de valores numericos: 1, 2, 3, 4, 5
# acepta hasta 3 argumentos: range( valor_inicial, valor_final, salto/incremento)
for numero in range(0, 5, 2): # valor inicial: 0, valor final: 5, incremento: 2
    print(numero)


# usamos range() para generar el índice y poder imprimir valor y posición
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

lngitud_lista = len(productos) # 5

for indice in range(lngitud_lista): 
    print(f"El elemento de la posicion {indice} es {productos[indice]}")