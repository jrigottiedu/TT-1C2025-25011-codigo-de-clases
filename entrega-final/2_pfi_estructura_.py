"""
README:
En este archivo se plantea la estructura de la nueva versión que vamos a armar para integrar con Sqlite3
Se reserva un espacio para declarar variables globales (si las hubiera)
Se declara la función principal y luego las funciones secundarias
Finalmente se invoca a la función principal (main)
"""

# -----------------------------------------------------------------
# Importar módulos
from bd_metodos import *

# -----------------------------------------------------------------
# Declarar variables (Globales) - si las hubiera


# -----------------------------------------------------------------
# Declarar funció / método princial MAIN


def main():
    # Cuerpo principal de nuestro código
    while True:  # La rutina principal se repite hasta que el usuario lo indique

        # Imprimimos el menú de opciones
        mostrarMenu()  # Invocamos a la función que imprimer el menú

        # El usuario ingresa su opción
        opcion = getOpcion()  # Invocamos a la función que lee la opción del usuario

        # Procesamiento de la opción ingresada usando Match
        match opcion:
            case "1":  # Alta de producto
                altaProducto()  # Invocamos a la función que procesa el alta

            case "2":  # Mostrar productos
                mostrarProductos()  # Invocamos a la función que muestra en consola

            case "3":  # Buscar productos
                buscarProductos()  # Invocamos a la función que busca productos

            case "4":  # Actualizar precio de productos
                actualizarPrecioProducto()  # Invocamos a la función que actualiza el precio
                # actualizarProducto()  # Invocamos a la función que actualiza todos los campos

            case "5":  # Eliminar producto
                eliminarProducto()  # Invocamos a la función que elimina prodcuto

            case "6":
                reporteBajoStock()

            case "7":
                print("Saliendo...")
                break  # la sentencia break interrumpe el flujo normal del while
            case _:
                print("Opcion incorrecta")

    print("Gracias por usar mi App")


# -----------------------------------------------------------------
# Declarar funciones / métodos Secundarias


def mostrarMenu():
    print(
        """
Menú de opciones:
    1. Alta de producto
    2. Mostrar productos
    3. Buscar productos
    4. Actualizar productos
    5. Eliminar productos
    6. Bajo stock
    7. Salir
"""
    )


def altaProducto():
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()
    # insertar en la tabla productos
    bd_insertar_producto(nombre, categoria, precio)


def mostrarProductos():
    lista_productos = bd_leer_productos()
    if len(lista_productos) > 0:
        print(lista_productos)
    else:
        print("No se encontraron productos.")


def buscarProductos():
    nombre = getNombreBuscarProductos()
    lista_productos = bd_leer_producto_por_nombre(nombre)
    if len(lista_productos) > 0:
        print(lista_productos)
    else:
        print("No se encontraron productos con ese nombre.")


def actualizarPrecioProducto():
    id = getIdProductoActualizar()
    precio = getPrecio()

    producto = bd_leer_producto_por_id(id)
    if producto:
        status = bd_actualizar_precio(id, precio)
        if status:
            print("Registro actualizado.")
        else:
            print("Algo fallo al actualizar.")
    else:
        print("No se encontraron productos con ese id")


def actualizarProducto():
    """"""


def eliminarProducto():
    id = int(input("Ingrese el id del producto a eliminar: "))
    bd_eliminar_producto(id)


def reporteBajoStock():
    stock = int(input("Ingrese el minimo stock: "))  # 50
    lista_bajo_stock = bd_leer_bajo_stock(stock)  # 50
    print(lista_bajo_stock)


# -----------------------------------------------------------------
# Declarar funciones / métodos get/validar


def getOpcion():
    opcion = input("Ingrese su opción: ")
    return opcion


def getNombre():
    nombre = input("Ingrese el nombre del producto: ")
    return nombre


def getCategoria():
    categoria = input("Ingrese la categoria del producto: ")
    return categoria


def getPrecio():
    precio = int(input("Ingrese el precio: "))
    return precio


def getNombreBuscarProductos():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    return nombre


def getIdProductoActualizar():
    mostrarProductos()
    id = int(input("Ingrese el ID del producto a actualizar: "))
    return id


def getIdProductoEliminar():
    mostrarProductos()
    id = int(input("Ingrese el ID del producto a eliminar: "))
    return id


# -----------------------------------------------------------------
# Invocamos a la función princial y funciones complementarias
if __name__ == "__main__":
    bd_crear_tabla_productos()
    main()
