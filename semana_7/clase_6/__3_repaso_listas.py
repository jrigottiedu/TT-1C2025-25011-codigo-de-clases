# Repaso de listas

"""
lista de productos:
carne
carbon
ensaladas
bebidas
postre
"""
# declaramos la lista
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]
print(f"La lista {productos} tiene una longitud de {len(productos)}")

# Elementos, posición e índices en las listas
indice = 0
print(f"El elemento de la posicion 0 es {productos[indice]}")
print(f"El elemento de la posicion 1 es {productos[indice + 1]}")


# Métodos de listas - append
productos.append("cafe")
print(productos)

# Usamos el bucle while para recorrer los elementos de la lista productos
indice = 0
longitud_lista = len(productos)
while indice < longitud_lista:
    print(f"El elemento de la posicion {indice} es {productos[indice]}")
    indice += 1
