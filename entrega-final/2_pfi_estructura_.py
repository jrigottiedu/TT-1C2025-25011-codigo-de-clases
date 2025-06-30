"""
README:
En este archivo se plantea la estructura de la nueva versión que vamos a armar para integrar con Sqlite3
Se reserva un espacio para declarar variables globales (si las hubiera)
Se declara la función principal y luego las funciones secundarias
Finalmente se invoca a la función principal (main)
"""

# -----------------------------------------------------------------
# Importar módulos


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

            case "4": # Actualizar precio de productos
                actualizarPrecioProducto() # Invocamos a la función que actualiza el precio

            case "5":  # Eliminar producto
                eliminarProducto()  # Invocamos a la función que elimina prodcuto

            case "6":
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
    6. Salir
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
    precio = int(input("Ingrese el precio: "))
    return precio


def altaProducto():
    nombre = getNombre()
    categoria = getCategoria()
    precio = getPrecio()
    

def mostrarProductos():
    print("Función mostrarProductos")


def getNombreBuscarProductos():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    return nombre


def buscarProductos():
    print("Función buscarProducto")


def getIdProductoActualizar():
    mostrarProductos()
    id = int(input("Ingrese el ID del producto a actualizar: "))
    return id


def actualizarPrecioProducto():
    """"""

def getIdProductoEliminar():
    mostrarProductos()
    id = int(input("Ingrese el ID del producto a eliminar: "))
    return id


def eliminarProducto():
    print("Función eliminarProducto")


# -----------------------------------------------------------------
# Invocamos a la función princial
if __name__ == "__main__":
    main()
