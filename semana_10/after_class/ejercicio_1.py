"""
Dada una lista sencilla de un producto

producto = ["manzana", "fruta", 1200]

Realizar una función que muestre en pantalla los 3 datos de nuestro producto
"""

# Declarar la variable
producto_1 = ["manzana", "fruta", 1200]
producto_2 = ["kiwi", "fruta", 1500]


# Declarar la funcion / metodo
def mostrarProducto(productoMostrar):  # parametro: productoMostrar
    print(
        f"Nombre: {productoMostrar[0]} Categoria: {productoMostrar[1]} Precio: {productoMostrar[2]}"
    )


# Invocar o llamar a la funcion
mostrarProducto(producto_2)  # argumento
