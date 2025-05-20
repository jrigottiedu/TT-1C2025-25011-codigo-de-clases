# Sublistas de productos
producto_1 = ["pantanlon", 1500, 1]
producto_2 = ["camisa", 1200, 2]
producto_3 = ["zapatos", 800, 1]

# ['pantanlon', 1500, 1]
print(f"lista de producto_1 {producto_1}")
print(f"elemento pantalon de producto_1  {producto_1[0]}")

# Declaramos una variable tipo lista para almacenar las sublistas de productos
# y la incializamos con las variables anteriores
lista_productos = [producto_1, producto_2, producto_3]

# Imprimimos en pantalla a ver el resultado
print(f"la lista de productos es: {lista_productos}")

# A través del índice, accedemos a las sublistas de lista_productos
print(f"Accedo al primer elemento de la sublista {lista_productos[0]}")

# Podemos pensar la estructura como lista de listas o una matríz
# Si quiero acceder a pantalon, el primer elemento de la primer sublista, lo hago así
print(lista_productos[0][0])

# ***************************************************************************************
# Presentamos ahora los Diccionarios
# Los diccionarios al igual que las listas, son arreglos de elementos
# La principal diferencia de los diccionarios sobre las listas
# es que accedemos a sus elementos, a través de claves en lugar de índices

# Veamos la sintáxis de un diccionario

# diccionario_1 es el diccionario equivalente a la lista producto_1
diccionario_1 = {
    "nombre": "pantanlon", 
    "precio": 1500, 
    "cantidad": 1
    }

diccionario_2 = {
    "nombre": "camisas", 
    "precio": 1200, 
    "cantidad": 2
    }

diccionario_3 = {
    "nombre": "zapatos", 
    "precio": 800, 
    "cantidad": 1
    }

# Veamos la salida en pantalla del diccionario diccionario_1
print(f"diccionario de diccionario_1 {diccionario_1}")
#{'nombre': 'pantanlon', 'precio': 1500, 'cantidad': 1}

# A través de los corchetes y las claves, accedemos a los valores del diccionario
print(f"Elemento nombre del diccionario: {diccionario_1["nombre"]}")
print(f"Elemento precio del diccionario: {diccionario_1["precio"]}")

# A partir de los diccionarios, armamos entonces una lista de diccionarios:
lista_productos_con_diccionarios = [diccionario_1, diccionario_2, diccionario_3]
print(lista_productos_con_diccionarios)

# Ahora para acceder a pantalon, pasamos el índide del primer diccionario en la lista_productos
# Pero luego la clave "nombre". 
print(f"Pantalon esta en 0 - nombre {lista_productos_con_diccionarios[0]["nombre"]}")

# Analogamente, acceder al precio del pantalon lo hacemos con la clave precio
print(f"1500 esta en 0 - precio {lista_productos_con_diccionarios[0]["precio"]}")