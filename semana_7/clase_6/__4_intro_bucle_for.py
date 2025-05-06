"""
Bucle For:
- permite ejecutar un bloque de código un número definido de veces
- no se usan índices o contadores, por lo que simplifica el código
- hay una condición implícita
- ideal para iterar sobre cadenas, listas, (diccionarios) o rangos numéricos
"""

# Usamos el bucle For para recorrer los elementos de la cadena="Python"
# productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

# for producto in productos:
    # print(f"El elemento de la posicion {indice} es {productos[indice]}")

# acumulador = 1
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     acumulador = acumulador * numero

# print(f"El acumulado es: {acumulador}")

# Usamos el bucle For para recorrer los elementos de la cadena="Python"


# Introducimos la función range()
for numero in range(0, 5, 2): # range( valor_inicial, valor_final, salto/incremento)
    print(numero)


# usamos range() para generar el índice
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

lngitud_lista = len(productos) # 5

for indice in range(lngitud_lista):
    print(f"El elemento de la posicion {indice} es {productos[indice]}")