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

# declaramos la función
def buscarProducto(nombreProducto):
    # Iteramos la lista producto, buscando coincidencia en el primer elemento de la sub-lista producto
    for producto in lista_productos:
        if nombreProducto in producto[0].lower():
            return True
    return False


# Ingresamos el nombre del producto a buscar
buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()

# invocamos a la función y almacenamos el resultado
resultadoBusqueda = buscarProducto(buscar)

# en función del valor retornado, informamos en pantalla
if resultadoBusqueda:
    print("Encontrado")
else:
    print("No encontrado")
