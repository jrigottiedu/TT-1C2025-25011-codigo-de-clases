# Ejercicio de tarea 4

# A partir de la rutina / bloque de código de nuestro proyecto
# que busca en la lista_productos el nombre de un producto,
# convertirlo a una función con las siguientes características:
# 1. que use la variable global lista_productos
# 2. que reciba el nombre del producto a buscar
# 3. que retorne True si lo encuentra o False si no lo encuentra

# Variable global
lista_productos = [
    [
        "manzana roja",
        "fruta",
        1500,
    ],  # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
]

# Ingresamos el nombre del producto a buscar
buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()

# Declaramos una bandera para saber si se encontro o no
encontrado = False
# Iteramos la lista producto, buscando coincidencia en el primer elemento de la sub-lista producto
for producto in lista_productos:
    if buscar in producto[0].lower():
        # Si hay conincidencia, mostramos en pantalla y actualizamos la bandera
        print(f"Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}")
        encontrado = True

# Evaluamos el estado de la bandera e informamos si no se encontró
if encontrado == False:
    print("Producto no encontrado")


def buscarProducto(nombreProducto):
    # Iteramos la lista producto, buscando coincidencia en el primer elemento de la sub-lista producto
    for producto in lista_productos:
        if nombreProducto in producto[0].lower():
            return True
    return False


# Ingresamos el nombre del producto a buscar
buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()
resultadoBusqueda = buscarProducto(buscar)
if resultadoBusqueda:
    print("Encontrado")
else:
    print("No encontrado")
