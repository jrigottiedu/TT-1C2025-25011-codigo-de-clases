# importamos los métodos de manejo de BD desde otro archivi
from bd_metodos import *


# Función principal
def main():
    while True:  # Condicion siempre True que maneja el flujo normal del menú

        # Invocamos a la función que muestra el menú principal
        mostrar_menu()

        # getOpcion() retorna la opción del menúelegida por el usuario
        opcion = getOpcion()

        # Procesamiento de la opción ingresada
        match opcion:
            case "1":
                # Llamamos a la función que captura los valores y los inserta en la BD
                main_insertar_producto()

            case "2":
                # la función bd_leer_productos() retorna una lista con todos los registros de la tabla
                lista_productos = bd_leer_productos()
                # invocamos a la función local y le pasamos la lista_productos para que los muestre en pantalla
                main_mostrar_lista_productos(lista_productos)

            case "3":
                # Buscar productos
                # Ingresamos el nombre del producto a buscar
                nombre = (
                    input("Ingresá el nombre del producto a buscar: ").strip().lower()
                )
                # la funcion bd_leer_producto_por_nombre(nombre) retorna todas la concidencias parciales para el nombre indicado
                lista_productos = bd_leer_producto_por_nombre(nombre)
                # mostrar productos
                main_mostrar_lista_productos(lista_productos)

            case "4":
                # llamamos a la función local que captura el índide del producto a eliminar
                indice_eliminar = getIndiceEliminar()
                # invocamos a la funcion y le pasamos el índice a eliminar
                resultado = bd_eliminar_producto(indice_eliminar)
                # evaluamos el resultado e informamos
                if resultado:
                    print("Producto eliminado exitosamente!")
                else:
                    print("Ups, algo salió mal...")

            case "5":
                # Reporte de bajo stock
                # capturamos el limite para la consulta
                limite = int(input("Ingrese el límite para el reporte de bajo stock: "))
                # la funcion bd_leer_prodcucto_bajo_stock(limite) nos retorna una lista con todos los productos cuyo campo cantidad es menor o igual a límite
                lista_productos = bd_leer_producto_bajo_stock(limite)
                # evaluamos e informamos
                if len(lista_productos) > 0:
                    main_mostrar_lista_productos(lista_productos)
                else:
                    print("No hay nada que mostrar")

            case "6":
                print("Saliendo...")
                break  # la sentencia break interrumpe el flujo normal del while
            case _:
                print("Opcion incorrecta")


def mostrar_menu():
    # Imprimimos el menú de opciones
    print(
        """
    Menú de opciones:
        1. Alta de producto
        2. Motrar productos
        3. Buscar productos
        4. Eliminar productos
        5. Informe de stock
        6. Salir
    """
    )


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


# Captura la descripcion del producto a ingresar
def getDescripcion():
    while True:
        descripcion = input("Ingrese la descripcion del producto: ")
        if descripcion:
            break
        else:
            print("No se admite campo vacío")
    return descripcion


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


# Captura la cantidad del producto a ingresar
def getCantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("cantidad no válido. Intente nuevamente.")
    return cantidad


# Captura el índice del producto a eliminar
def getIndiceEliminar():
    while True:
        try:
            indice = int(input("Ingrese el indice a eliminar: "))
            break
        except ValueError:
            print("indice no válido. Intente nuevamente.")
    return indice


# Función local que maneja el proceso de alta de producto
def main_insertar_producto():
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()
    descripcion = getDescripcion()
    cantidad = getCantidad()
    resultado = bd_insertar_producto(nombre, categoria, precio, descripcion, cantidad)
    if resultado:
        print("Registro insertado exitosamente!")
    else:
        print("Ups, algo salió mal...")


# Función local que maneja el proceso de iterar la lista y mostrar en consola con un estilo personalizado
def main_mostrar_lista_productos(lista_productos):
    # Aqui desarrollar código para mostrar productos
    for indice in range(len(lista_productos)):
        # Almaceno en una variable temporal cada sub-lista de la lista_productos
        producto = lista_productos[indice]
        # Mostramos en pantalla los campos por medio de los índices
        print(
            f"Indice: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}, Descripcion: {producto[4]}, Cantidad: {producto[5]}"
        )  # Muestra en pantalla


# Invocamos a la función que crea la tabla productos si no existe
bd_crear_tabla_productos()
# Invocamos a la función principal
main()
print("Gracias por usar mi App")
