from funciones import *

# Lista global de productos
lista_productos = [
    ["manzana roja", "fruta", 1500],
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
]


# Cuerpo principal
while True:
    # ingreso de datos
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()

    # armamos la lista temporal
    producto = [nombre, categoria, precio]

    # insertamos el producto en la lista global
    lista_productos.append(producto)

    # mostramos en consola
    print(lista_productos)

    # preguntamos al usuario si continúa o no
    continuar = input("Continua cargando? s/n: ").strip().lower()
    if continuar == "n":
        print("Finalizando...")
        break
