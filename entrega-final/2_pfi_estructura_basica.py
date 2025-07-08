"""
README:
En este archivo se plantea la estructura de la nueva versión que vamos a armar para integrar con Sqlite3
Se reserva un espacio para declarar variables globales (si las hubiera)
Se declara la función principal y luego las funciones secundarias
Luego se agregan las funciones de ingreso y validación de datos
Finalmente se invoca a la función que crea la tabla productos y la función principal (main)
"""

# -----------------------------------------------------------------
# Importar módulos
# Importamos las funciones/métodos que manejan la base de datos
from bd_metodos import *

# -----------------------------------------------------------------
# Declarar variables (Globales) - si las hubiera


# -----------------------------------------------------------------
# Declarar función/método principal MAIN


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
                altaProducto()  # Invocamos a la función que procesa el alta de un nuevo producto

            case "2":  # Mostrar productos
                mostrarProductos()  # Invocamos a la función que muestra en consola

            case "3":  # Buscar productos
                buscarProductosPorNombre()  # Invocamos a la función que busca productos por nombre

            case "4":  # Actualizar precio de producto
                actualizarPrecioProducto()  # Invocamos a la función que actualiza el precio

            case "5":  # Eliminar producto
                eliminarProducto()  # Invocamos a la función que elimina prodcuto

            case "6":  # Reporte de bajo stock
                reporteBajoStock()  # invocamos a la función que genera reporte de bajo stock

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
    4. Actualizar precio de un producto
    5. Eliminar productos
    6. Bajo stock
    7. Salir
"""
    )


# Alta de un nuevo producto
def altaProducto():
    # El usuario ingresa los datos del producto
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()

    # Insertamos el producto en la tabla
    status = bd_insertar_producto(nombre, categoria, precio)

    # Evaluamos el retorno para informar al usuario
    if status:
        print("Producto insertado exitosamente!")
    else:
        print("Error al insertar el producto")


# Mostrar en consola todos los productos de la tabla
def mostrarProductos():
    # bd_leer_productos() retorna una lista con todos los productos de la tabla
    lista_productos = bd_leer_productos()

    # Evaluamos el retorno e informamos
    if len(lista_productos) > 0:
        for producto in lista_productos:
            print(producto)
    else:
        print("No se encontraron productos.")


# Mostrar productos que contengan el nombre ingresado
def buscarProductosPorNombre():
    # El usuario ingresa el nombre a buscar
    nombre = getNombre()

    # bd_leer_producto_por_nombre(nombre) retorna una lista con los productos encontrados para ese nombre
    lista_productos = bd_leer_producto_por_nombre(nombre)

    # Evaluamos el retorno e informamos
    if len(lista_productos) > 0:
        for producto in lista_productos:
            print(producto)
    else:
        print("No se encontraron productos con ese nombre.")


# Actualizar el precio de un producto específico
def actualizarPrecioProducto():
    # El usuario ingresa id del producto a modificar y nuevo precio
    id = getIdProductoActualizar()
    precio = getPrecio()

    # actulizamos el precio para ese id
    status = bd_actualizar_precio(id, precio)

    # evaluamos el retorno e informamos
    if status:
        print("Registro actualizado.")
    else:
        print("Error: algo fallo al actualizar.")


# Eliminar un producto específico
def eliminarProducto():
    # El usuario ingresa el id del producto a eliminar
    id = getIdProductoEliminar()

    # eliminamos el producto con ese id
    status = bd_eliminar_producto(id)

    # evaluamos el retorno e informamos
    if status:
        print("Registro eliminado.")
    else:
        print("Error: algo fallo al eliminar.")


# Mostrar reporte de bajo stock
# *** Código de referencia, no se puede implementar hasta actualizar la tabla con cantidad
def reporteBajoStock():
    # El usuario ingresa el umbral de mínimo stock
    stock = int(input("Ingrese el minimo stock: "))  # 50
    # bd_leer_bajo_stock(stock) retorna una lista con los productos cuya cantidad es menor al stock indicado
    lista_bajo_stock = bd_leer_bajo_stock(stock)  # 50
    print(lista_bajo_stock)


# -----------------------------------------------------------------
# Declarar funciones / métodos get/validar


# Captura la opción del menú
def getOpcion():
    opcion = input("Ingrese su opción: ")
    return opcion


# Captura el nombre del producto a ingresar
def getNombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre:
            break
        else:
            print("No se admite campo vacío")
    return nombre


# Captura la categoría del producto a ingresar
def getCategoria():
    while True:
        categoria = input("Ingrese la categoria del producto: ")
        if categoria:
            break
        else:
            print("No se admite campo vacío")
    return categoria


# Captura el precio del producto a ingresar
def getPrecio():
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Precio no válido. Intente nuevamente.")
    return precio


# Captura el id del producto a actualizar
def getIdProductoActualizar():
    mostrarProductos()
    while True:
        try:
            id = int(input("Ingrese el ID del producto a actualizar: "))
            break
        except ValueError:
            print("ID no válido. Intente nuevamente...")
    return id


# Captura el id del producto a eliminar
def getIdProductoEliminar():
    mostrarProductos()
    while True:
        try:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            break
        except ValueError:
            print("ID no válido, ingrese nuevamente")
    return id


# -----------------------------------------------------------------
# Invocamos a la función princial y funciones complementarias
if __name__ == "__main__":
    bd_crear_tabla_productos()
    main()
