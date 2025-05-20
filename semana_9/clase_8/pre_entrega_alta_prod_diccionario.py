
# Declaracion de variables globales
lista_productos = []


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
            diccionario = {
                "nombre": nombre,
                "categoria": categoria,
                "precio": precio,
            }
            lista_productos.append(diccionario) # insertamos con append() el producto a la lista_productos

        case "2":
            # Aqui desarrollar código para buscar productos
            # Iteramos lista_productos
            for producto in  lista_productos:
                print(producto)
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
