# Lista de listas

lista_productos = []  # Lista global

producto_1 = ["manzana", "fruta", 1500]  # Lista de producto
producto_2 = ["pera", "fruta", 2500]  # Lista de producto


lista_productos.append(producto_1)
lista_productos.append(producto_2)

# 

# --------------------------------------------
# ***** Lista de diccionarios *****
lista_productos = []  # Lista global
producto_1 = {
    "id_unico": 0,
    "nombre": "manzana",
    "categoria": "fruta",
    "precio": 1500,
    "stock": 10
}  # diccionario de producto

producto_2 = {
    "nombre": "pera",
    "categoria": "fruta",
    "precio": 1220,
}  # diccionario de producto

lista_productos.append(producto_1)
lista_productos.append(producto_2)
print(lista_productos)

# --------------------------------------------
# Diccionario de diccionarios
diccionario_productos = {} # Diccionario global
producto_1 = {
    "nombre": "manzana",
    "categoria": "fruta",
    "precio": 1500,
}  # diccionario de producto

producto_2 = {
    "nombre": "pera",
    "categoria": "fruta",
    "precio": 1220,
}  # diccionario de producto

diccionario_productos["producto_1"]= producto_1
diccionario_productos["producto_2"]= producto_2

diccionario_productos[0]= producto_1
diccionario_productos[1]= producto_2