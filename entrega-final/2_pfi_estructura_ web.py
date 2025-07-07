"""
README:
En este archivo se plantea la estructura de la nueva versión que vamos a armar para integrar con Sqlite3
Se reserva un espacio para declarar variables globales (si las hubiera)
Se declara la función principal y luego las funciones secundarias
Finalmente se invoca a la función principal (main)
"""

# -----------------------------------------------------------------
# Importar módulos
from bd_metodos_web import *

# -----------------------------------------------------------------
# Declarar variables (Globales) - si las hubiera


# -----------------------------------------------------------------
# Declarar funciones / métodos


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
                # actualizarPrecioProducto()  # Invocamos a la función que actualiza el precio
                actualizarProducto()
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
    precio = float(input("Ingrese el precio: "))
    return precio


def altaProducto():
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()
    # insertar en la tabla productos
    bd_insertar_producto(nombre, categoria, precio)


def mostrarProductos():
    lista_productos = bd_leer_productos()
    if len(lista_productos) > 0:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay registros para mostrar")


def getNombreBuscarProductos():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    return nombre


def buscarProductos():
    nombre = getNombreBuscarProductos()
    lista_productos = bd_leer_producto_por_nombre(nombre)
    if len(lista_productos) > 0:
        for producto in lista_productos:
            print(producto)
    else:
        print("No se han encontrado productos con ese nombre.")


def getIdProductoActualizar():
    mostrarProductos()
    id = int(input("Ingrese el ID del producto a actualizar: "))
    return id


def getPrecioProductoActualizar():
    precio = float(input("Ingrese el precio del producto a actualizar: "))
    return precio


def actualizarPrecioProducto():
    id = getIdProductoActualizar()
    precio = getPrecioProductoActualizar()
    status = bd_actualizar_precio(id, precio)
    if status:
        print("Producto actualizado exitosamente!")
    else:
        print("Error al actualizar el producto.")


def getProductoActualizar():
    mostrarProductos()
    while True:
        try:
            id = int(input("Ingrese el ID del producto a actualizar: "))
            break
        except ValueError:
            print("ID no válido. Intente nuevamente...")
    producto = bd_leer_producto_por_id(id)
    return producto


def actualizarProducto():
    producto = getProductoActualizar()
    if producto:
        # Desestructuramos la tupla en variables independientes
        id, nombre_actual, categoria_actual, precio_actual = producto
        # Mostramos y leemos los nuevos valores
        nuevo_nombre = input(f"Nombre actual [{nombre_actual}]: ").strip()
        nueva_categoria = input(f"Categoría actual [{categoria_actual}]: ").strip()
        nuevo_precio = input(f"Precio actual [{precio_actual}]: ").strip()
        # Preparamos las variables para llamar a la funcion
        nombre = nuevo_nombre if nuevo_nombre else nombre_actual
        categoria = nueva_categoria if nueva_categoria else categoria_actual
        try:
            precio = float(nuevo_precio) if nuevo_precio else precio_actual
        except ValueError:
            print("Precio inválido. Se mantiene el precio anterior.")
        # Invocamos a la función actualizar
        status = bd_actualizar_producto(id, nombre, categoria, precio)
        if status:
            print("Producto actualizado exitosamente!")
        else:
            print("Error al actualizar el producto.")


def getProductoEliminar():
    mostrarProductos()
    while True:
        try:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            break
        except ValueError:
            print("ID no válido. Intente nuevamente...")
    producto = bd_leer_producto_por_id(id)
    return producto


def eliminarProducto():
    producto = getProductoEliminar()
    if producto:
        # Pedir al usuario confirmación
        print("ATENCION!:\nEsta por eliminar este registro:")
        print(producto)
        confirma = input("s/n").strip().lower()
        if confirma == "s":
            status = bd_eliminar_producto(producto[0])
            if status:
                print("Producto eliminado exitosamente!")
            else:
                print("Error al eliniar el producto.")
        else:
            print("Operación cancelada.")
    else:
        print("No existe producto con ese id.")


def reporteBajoStock():
    stock = int(input("Ingrese el minimo stock: "))  # 50
    lista_bajo_stock = bd_leer_producto_bajo_stock(stock)  # 50
    print(lista_bajo_stock)


# -----------------------------------------------------------------
# Invocamos a la función princial y funciones complementarias
if __name__ == "__main__":
    bd_crear_tabla_productos()
    main()
