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
                actualizarProducto()  # Invocamos a la función que actualiza el precio

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
    4. Actualizar producto
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

    # bd_leer_producto_por_nombre(nombre) retorna una lista con los productos encontrados
    lista_productos = bd_leer_producto_por_nombre(nombre)

    # Evaluamos el retorno e informamos
    if len(lista_productos) > 0:
        print(lista_productos)
    else:
        print("No se encontraron productos con ese nombre.")


# Actualizar el precio de un producto específico
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
    else:
        print("No existe producto con ese id.")


# Eliminar un producto específico
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
    lista_bajo_stock = bd_leer_bajo_stock(stock)  # 50
    print(lista_bajo_stock)


# -----------------------------------------------------------------
# Declarar funciones / métodos get/validar


def getOpcion():
    opcion = input("Ingrese su opción: ")
    return opcion


def getNombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre:
            break
        else:
            print("No se admite campo vacío")
    return nombre


def getCategoria():
    while True:
        categoria = input("Ingrese la categoria del producto: ")
        if categoria:
            break
        else:
            print("No se admite campo vacío")
    return categoria


def getPrecio():
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Precio no válido. Intente nuevamente.")
    return precio


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


def inicializarTablaProductos():
    lista_productos = bd_leer_productos()
    if len(lista_productos) == 0:
        productos = [
            (1, "Manzana", "Fruta", 1500),
            (2, "Pera", "Fruta", 1700),
            (3, "Kiwi", "Fruta", 2000),
        ]
        status = bd_inicializar_tabla_productos(productos)
        print(
            "Tabla inicializada!"
            if status
            else "No se ha podido inicializar la tabla productos."
        )


# -----------------------------------------------------------------
# Invocamos a la función princial y funciones complementarias
if __name__ == "__main__":
    bd_crear_tabla_productos()
    inicializarTablaProductos()
    main()
