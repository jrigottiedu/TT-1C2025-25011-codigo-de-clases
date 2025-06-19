"""
README:
En este archivo se plantea la estructura de la nueva versión que vamos a armar para integrar con Sqlite3
Se reserva un espacio para declarar variables globales (si las hubiera)
Se declara la función principal y luego las funciones secundarias
Finalmente se invoca a la función principal (main)
"""

# -----------------------------------------------------------------
# Declaracion de variables (Globales) - si las hubiera



# -----------------------------------------------------------------
# Declaracion de funciones


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
                buscarProducto()  # Invocamos a la función que busca productos

            case "4":  # Eliminar producto
                eliminarProducto()  # Invocamos a la función que elimina prodcuto

            case "5":
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
    4. Eliminar productos
    5. Salir
"""
    )


def getOpcion():
    opcion = input("Ingrese su opción: ")
    return opcion


def getNombre():
    print("Función getNombre")


def getCategoria():
    print("Función getCategoriga")


def getPrecio():
    print("Función getPrecio")


def altaProducto():
    print("Procesando alta de producto")


def getBuscar():
    print("Función getBuscar")


def mostrarProductos():
    print("Función mostrarProductos")


def buscarProducto():
    print("Función buscarProducto")


def getEliminar():
    print("Función getEliminar")


def eliminarProducto():
    print("Función eliminarProducto")


# -----------------------------------------------------------------
# Invocamos a la función princial
if __name__ == "__main__":
    main()
