"""
Intentar convertir la opción 2 del menú en una función que muestre los valores de lista_producto

La función puede o no recibir la lista_producto

La función debe iterar la lista_producto y formatear la salida

Apliquen colores de lo visto en el After Class de la semana 9
https://github.com/jrigottiedu/TT-1C2025-25011-codigo-de-clases/blob/master/semana_9/after_class/aplicando_colores_consola.py

"""

# declaracion de variables
# variable Global
lista_productos = [
    [
        "manzana roja",
        "fruta",
        1500,
    ],  # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
]


# declarar funcion
def mostrarListaProductos(listaGlobalProductos):
    # listaGlobalProductos es una variable local
    # print(f"iteramos la lista {listaGlobalProductos}")
    for indice in range(
        len(listaGlobalProductos)
    ):  # 0, 1, ... len(listaGlobalProductos)
        # Almaceno en una variable temporal cada sub-lista de la lista_productos
        producto = listaGlobalProductos[indice]
        # Mostramos en pantalla los campos por medio de los índices
        print(
            f"Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}"
        )  # Muestra en pantalla


# invocar funcion

mostrarListaProductos(lista_productos)  # lista_productos es la variable global
