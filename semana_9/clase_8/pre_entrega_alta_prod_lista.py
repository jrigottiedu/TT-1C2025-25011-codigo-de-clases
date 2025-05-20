"""
En esta versión desarrollamos las opciones 1 y 2 del menú de la pre-entrega empleando 
1. una sublista 'producto' para almacenar temporalmente los campos de cada producto
2. una lista global 'lista_productos' para almacenar las sublistas
"""


# Declaracion de variables globales
lista_productos = [
    ['pantalon', 'indu', '1500'],
    ['camisa', 'indu', '1300'],
    ['zapatos', 'indu', 800]
]


while True: # Condicion siempre True que maneja el flujo normal del menú

    print("""
Menú de opciones:
    1. Alta de producto
    2. Motrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
""")
    opcion = input("Ingrese su opción: ") # Solicito al usuario que ingresa su opción

    # Procesamiento de la opción ingresada
    match opcion :
        case "1": 
            # Aqui desarrollar código para el alta de productos
            nombre = input("Ingrese nombre ").strip()
            categoria = input("Ingrese categoria ")
            precio = input("Ingrese precio: ")
            producto = [nombre, categoria, precio] # lista temporal
            lista_productos.append(producto) # insertamos con append() el producto a la lista_productos

        case "2":
            # Aqui desarrollar código para mostrar productos
            # Iteramos lista_productos
            for producto in  lista_productos:
                print(f"Nombre: {producto[0]} Categoria: {producto[1]} Precio: {producto[2]}")

        case "3":
            # Aqui desarrollar código para buscar productos
            print("Procesando buscar productos...")
        case "4":
            # Aqui desarrollar código para eliminar productos
            print("Procesando eliminar productos...") 
        case "5":
            print("Saliendo...")
            break # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")
