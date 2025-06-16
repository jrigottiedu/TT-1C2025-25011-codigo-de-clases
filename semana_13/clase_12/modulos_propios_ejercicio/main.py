# **********************************************************************************************************
# VARIABLES GLOBALES

# Lista global de productos
lista_productos = [
    ["manzana roja", "fruta", 1500],
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
]

# **********************************************************************************************************
# FUNCIONES O METODOS
from funciones_validacion import *
# ------------------------------------------------------------------------------------
# Declaración de la función principal
"""
- Parámetros: ninguno
- Procesamiento: imprime menú, lee opción y procesa
- Retorno: ninguno
"""
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()

        match opcion:
            case "1":
                alta_producto()
            case "2":
                mostrar_productos()
            case "3":
                print("Procesando buscar productos")
            case "4":
                print("Procesando eliminar productos")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta. Intente nuevamente.")

    print("Gracias por usar mi App")

# ------------------------------------------------------------------------------------
# Declaración de la función mostrar menú
"""
- Parámetros: ninguno
- Procesamiento: imprime el menú en consola
- Retorno: ninguno
"""
def mostrar_menu():
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

# ------------------------------------------------------------------------------------
# Declaración de la función alta producto
"""
- Parámetros: ninguno
- Procesamiento: lee y valida nombre, categoria y precio. Inserta el producto en lista_productos
- Retorno: ninguno
"""
def alta_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("No se admite nombre vacío, intente nuevamente.")

    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        print("No se admite categoría vacía, intente nuevamente.")

    while True:
        precio = input("Ingrese el precio del producto: ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        print("Precio inválido, intente nuevamente.")

    producto = [nombre, categoria, precio]
    lista_productos.append(producto)
    print("Producto agregado correctamente.")


# ------------------------------------------------------------------------------------
# Declaración de la función mostrar productos
"""
- Parámetros: ninguno
- Procesamiento: itera lista_productos y muestra cada uno en consola
- Retorno: ninguno
"""
def mostrar_productos():
    if not lista_productos:
        print("No hay productos para mostrar.")
        return

    for indice, producto in enumerate(lista_productos):
        print(
            f"Indice: {indice}, Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}"
        )


# **********************************************************************************************************
# CUERPO PRINCIPAL DEL ARCHIVO
# Llamamos o invocamos a la funcion main
main()