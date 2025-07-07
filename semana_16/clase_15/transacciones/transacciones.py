from bd_metodos import *


def main():
    """"""
    while True:
        lista_productos = bd_leer_productos()
        if lista_productos:
            for producto in lista_productos:
                print(producto)

        print("\n*** Eliminar ***")
        delete_id = int(input("Ingrese el ID del producto a eliminar: "))

        print("\n*** Agregar ***")
        id = input("Ingrese el id del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        nuevo_producto = (id, nombre, categoria, precio)

        status = ejecutar_transaccion(delete_id, nuevo_producto)
        print("Cambio realizado con éxito!" if status else "ERROR!")

        continua = input("Continua? s/n: ").strip().lower()
        if continua == "n":
            break


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
