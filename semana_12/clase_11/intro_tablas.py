# Colores ANSI
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
VIOLETA = "\033[38;5;135m"
RESET = "\033[0m"  # Para volver al color normal

# Almacenando los productos

# ----------------------------------------------------------------------------------------
# Versión 1: usando lista de listas

# Lista global de productos
lista_productos = []

# Lista temporal producto_lista:
# producto_lista[0] => Nombre, producto_lista[1] => Categoría, producto_lista[2] => Precio
producto_lista = ["manzana", "fruta", 1500]
lista_productos.append(producto_lista)

producto_lista = ["pera", "fruta", 2500]
lista_productos.append(producto_lista)

producto_lista = ["kiwi", "fruta", 2000]
lista_productos.append(producto_lista)

print(f"{VIOLETA}Lista de listas \n{RESET}{AMARILLO}{lista_productos}{RESET}")

"""
Acceder a los elementos mediante índices puede ser engorroso
Por ejemplo, para acceder a manzana:
"""
# Prints con color
print(f"\n{VIOLETA}Accedemos al primer elemento de la lista_productos usando\n{RESET}{AMARILLO}lista_productos[0]: {lista_productos[0]}{RESET}")
print(f"\n{VIOLETA}Accedemos al primer elemento de la sublista producto_lista usando\n{RESET}{AMARILLO}lista_productos[0][0]: {lista_productos[0][0]}{RESET}")
print()


# ----------------------------------------------------------------------------------------
# Versión 2: usando lista de diccionarios

# Lista global de productos
lista_productos = []

# Diccionario temporal producto:
# producto["nombre"] => Nombre, producto["categoria"] => Categoría, producto["precio"] => Precio
producto_diccionario = {"nombre": "manzana", "categoria": "fruta", "precio": 1500}
lista_productos.append(producto_diccionario)
producto_diccionario = {"nombre": "pera", "categoria": "fruta", "precio": 2500}
lista_productos.append(producto_diccionario)
producto_diccionario = {"nombre": "kiwi", "categoria": "fruta", "precio": 2000}

print(f"{AZUL}Lista de diccionarios \n{RESET}{VERDE}{lista_productos}{RESET}")
print(f"\n{AZUL}Accedemos al primer elemento de la lista_productos usando\n{RESET}{VERDE}lista_productos[0]: {lista_productos[0]}{RESET}")
print(f"\n{AZUL}Accedemos al primer valor del diccionario producto_diccionario usando\n{RESET}{VERDE}lista_productos[0]['nombre']: {lista_productos[0]["nombre"]}{RESET}")
print()
