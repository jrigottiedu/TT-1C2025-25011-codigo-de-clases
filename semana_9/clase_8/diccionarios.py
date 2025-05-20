# Sublistas de productos
producto_1 = ["pantanlon", 1500, 1]
producto_2 = ["camisa", 1200, 2]
producto_3 = ["zapatos", 800, 1]

# ['pantanlon', 1500, 1]
print(f"lista de producto_1 {producto_1}")
print(f"elemento pantalon de producto_1  {producto_1[0]}")

# lista principal
# lista_productos = [producto_1, producto_2, producto_3]
# print(f"la lista de productos es: {lista_productos}")
# print(f"Accedo a los elementos de la lista {lista_productos[0]}")

# # quiero acceder al producto pantalon
# print(lista_productos[0][0])

# Diccionarios
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

#{'nombre': 'pantanlon', 'precio': 1500, 'cantidad': 1}
print(f"diccionario de diccionario_1 {diccionario_1}")

# Accedemos a los elemetnos del diccionario
print(f"Elemento nombre del diccionario: {diccionario_1["nombre"]}")
print(f"Elemento precio del diccionario: {diccionario_1["precio"]}")

lista_productos_con_diccionarios = [diccionario_1, diccionario_2, diccionario_3]
print(lista_productos_con_diccionarios)

#accedemos al itemn en fila 0 y columna nombre
print(f"Pantalon esta en 0 - nombre {lista_productos_con_diccionarios[0]["nombre"]}")
print(f"1500 esta en 0 - precio {lista_productos_con_diccionarios[0]["precio"]}")