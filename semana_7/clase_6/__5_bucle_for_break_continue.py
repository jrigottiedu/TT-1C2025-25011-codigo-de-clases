# Vemos el uso de las sentencias break y continue en el bucle For

# Ejemplo 1: Usamos break para buscar un elemento en la lista
# Declaramos la lista
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

# Pedimos al usuario que ingrese el valor a buscar:
buscar = input("Ingrese el valor a buscar: ").strip()
for producto in productos:
    if producto.lower() == buscar.lower(): # forzamos conversion a minúscula porque Python es case-sensitive
        print("Producto encontrado!")

# Una versión mejorada de búsqueda
estado_busqueda = False # declaro una variable Bool en False
buscar = input("Ingrese el valor a buscar: ").strip()
for producto in productos:
    if producto.lower() == buscar.lower(): # forzamos conversion a minúscula porque Python es case-sensitive
        estado_busqueda = True # Si se encuentra el producto, cambio el estado de la variable

# Al finalizar el bucle for, según sea el estado de la variable informo
if estado_busqueda: 
    print("Producto encontrado!")
else:
    print("Producto no encontrado")