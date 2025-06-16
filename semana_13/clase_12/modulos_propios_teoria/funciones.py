# declarar funciones / métodos
def getNombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("No se admite nombre vacío, intente nuevamente.")
    return nombre


def getCategoria():
    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        print("No se admite categoría vacía, intente nuevamente.")
    return categoria


def getPrecio():
    while True:
        precio = input("Ingrese el precio del producto: ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        print("Precio inválido, intente nuevamente.")
    return precio