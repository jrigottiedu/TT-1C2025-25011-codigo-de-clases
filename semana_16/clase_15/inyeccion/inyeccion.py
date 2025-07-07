from bd_metodos import *


def main():
    """"""
    while True:

        opcion = input("Agregar [1] - Buscar [2] - Salir [3] ")

        match opcion:
            case "1":
                agregar_producto()
            case "2":
                buscar_producto()
            case "3":
                break
            case _:
                print("Opción incorrecta...")


def agregar_producto():
    id = input("Ingrese el id del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    nuevo_producto = (id, nombre, categoria, precio)
    status = bd_insertar_producto(nuevo_producto)
    print(
        "Producto agregado exitosamente" if status else "Error al insertar el producto"
    )


def buscar_producto():
    lista_productos = bd_leer_productos()
    if lista_productos:
        for producto in lista_productos:
            print(producto)

    print("\n*** Buscar por nombre ***")
    nombre = input("Ingrese el nombre del producto: ")
    lista_productos = bd_leer_producto_por_nombre(nombre)
    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No se han encontrado coincidencias.")


# Inicialización y llamada a función principal
bd_crear_tabla_productos()
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

main()

# Buscar
# "' OR 1=1 --"
# Insertar
# 'manzana', 'fruta', 1000); DROP TABLE productos; --
