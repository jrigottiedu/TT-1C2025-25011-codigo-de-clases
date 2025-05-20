"""
En esta versión desarrollamos las opciones 1 y 2 del menú de la pre-entrega empleando 
1. un diccionario 'diccionario' para almacenar temporalmente los campos de cada producto
2. una lista global 'lista_productos' para almacenar las sublistas
"""


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
            lista_productos.append(diccionario) # insertamos con append() el diccionario a la lista_productos

        case "2":
            # Aqui desarrollar código para mostrar productos
            # Iteramos lista_productos y usamos las 'claves' para mostrar los valores
            for clave in  lista_productos.keys():
                print(f"Nombre: {diccionario["nombre"]} Categoria: {diccionario["categoria"]} Precio: {diccionario["precio"]}")
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
