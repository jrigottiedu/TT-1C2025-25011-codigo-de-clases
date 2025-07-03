"""
README:
En este archivo encontrarán el código modelo sugerido para la pre-entrega
Pero modularizado en funciones
Se ha creado una función para cada opción del menú, se sugiere seguir modularizando de manera
que las funciones sean lo más genéricas posibles.
"""

from bd_metodos import *

# Lista global de productos
# CREAR LA BASE DE DATOS EN SQLITE Y LA TABLA PRODUCTOS
# lista_productos = [
#     ["manzana roja", "fruta", 1500],
#     ["pera", "fruta", 2500],
#     ["manzana verde", "fruta", 2500],
# ]
bd_crear_tabla_productos()

# Declaración de la función alta de producto
"""
- Parámetros: ninguno
- Procesamiento: 
    1. se encarga de leer y validar nonbre, categoria y precio del producto
    2. los almacena en una lista temporal
    3. lo inserta en la variable global lista_productos
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
        descripcion = input("Ingrese la descripcion del producto: ").strip()
        if descripcion:
            break
        print("No se admite descripcion vacía, intente nuevamente.")

    while True:
        try:
            cantidad = input("Ingrese la cantidad del producto: ").strip()
            cantidad = float(cantidad)
            break
        except ValueError:
            print("Cantidad inválido, intente nuevamente.")

    # while True:
    #     try:
    #         precio = input("Ingrese el precio del producto: ").strip()
    #         precio = float(precio)
    #         break
    #     except ValueError:
    #         print("Precio inválido, intente nuevamente.")
    precio = input("Ingrese el precio: ")

    # producto = [nombre, categoria, precio] # variable temporal
    # lista_productos.append(producto) # insercion en la "BD"
    respuesta = bd_insertar_producto(nombre, categoria, descripcion, cantidad, precio)
    if respuesta["status"] == True:
        print("Producto agregado correctamente.")
    else:
        print(respuesta["error"])


# Declaración de la función mostrar productos
"""
- Parámetros: ninguno
- Procesamiento: 
    1. accede a la variable globar lista_productos
    2. la itera con for in
    3. muestra en pantalla cada elemento de la lista
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


# Declaración de la función buscar producto
"""
- Parámetros: ninguno
- Procesamiento: 
    1. se encarga de leer el nombre del producto a buscar
    2. itera la lista_productos y usa if in para evaluar coincidencias parciales
    3. muestra en consola cada coincidencia encontrada
    4. si no hay coincidencias, muestra producto no encontrado
- Retorno: ninguno
"""
def buscar_productos():
    buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()
    # Declaramos una bandera para saber si se encontro o no
    encontrado = False
    # Iteramos la lista producto, buscando coincidencia en el primer elemento de la sub-lista producto
    for producto in lista_productos:
        if buscar in producto[0].lower():
            # Si hay conincidencia, mostramos en pantalla y actualizamos la bandera
            print(
                f"Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}"
            )
            encontrado = True

    # Evaluamos el estado de la bandera e informamos si no se encontró
    if encontrado == False:
        print("Producto no encontrado")


# Declaración de la función eliminar producto
"""
- Parámetros: ninguno
- Procesamiento: 
    1. se encarga de leer y validar el índice del producto a buscar
    2. valida que el índice se encuentre dentro del rango de lista_productos
    3. usa el método pop() para remover el producto
- Retorno: ninguno
"""
def eliminar_producto():
    while True:
        indice_eliminar = input("Ingrese el índice del producto a eliminar: ").strip()
        if indice_eliminar.isdigit():
            indice_eliminar = int(indice_eliminar)
            break
        print("Índice no válido. Intente nuevamente.")

    if 0 <= indice_eliminar < len(lista_productos):
        producto_eliminado = lista_productos.pop(indice_eliminar)
        print(f"Producto '{producto_eliminado[0]}' eliminado exitosamente.")
    else:
        print("Índice fuera de rango.")


# Declaración de la función mostrar menú
"""
- Parámetros: ninguno
- Procesamiento: 
    1. imprime en pantalla todas las opciones del menú
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

# Declaración de la función principal
"""
- Parámetros: ninguno
- Procesamiento: 
    1. define un bucle while principal que se interrumpe con break solo cuando el usuario lo decide
    2. lee de la consola la opción elegida por el usuario
    3. usa el bloque match para evaluar la acción a partir de la opción elegida
    4. en cada "case" invoca a la función correspondiente
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
                buscar_productos()
            case "4":
                eliminar_producto()
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta. Intente nuevamente.")

    print("Gracias por usar mi App")


# Ejecución del programa principal
main()
