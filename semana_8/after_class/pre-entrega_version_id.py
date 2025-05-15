# Declaracion de variables (Globales)

# Declaramos la lista de productos, que va a almacenar los siguientes datos
# Id, nombre, categoria, precio
# La inicializamos con algunos datos para poder testear la opcion 2 - Mostrar productos
lista_productos = [
    [43, "manzana", "fruta", 1500], # Id = 43, nombre="manzana", categoria="fruta", precio="1500"
    [44, "pera", "fruta", 2500],
] 


while True:  # Condicion siempre True que maneja el flujo normal del menú

# Imprimimos el menú de opciones
    print(
        """
Menú de opciones:
    1. Alta de producto
    2. Motrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
"""
    )

    # El usuario ingresa su opción
    opcion = input("Ingrese su opción: ")  # Solicito al usuario que ingresa su opción

    # Procesamiento de la opción ingresada
    match opcion:
        case "1":
            # Aqui desarrollar código para el alta de productos
            # Ingreso de datos del producto
            # Id, nombre, categoría, y precio
            # Nota: valiamos nombre, agregar validación en los otros campos
            id= int(input("Ingrese el ID del producto: "))
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre == "":
                    print("No se admite vacío... intente nuevamente")
                    continue
                else:
                    break

            categoria = input("Ingrese la categoria del producto: ")
            precio = input("Ingrese el precio del producto: ")

            # Almacenamos los datos ingrsados en una sub-lista temporal llamada productos
            producto = [id, nombre, categoria, precio]
            # Luego usamos el método append() para insertar la sub-lista productos en la lista principal lista_productos
            lista_productos.append(producto)

        case "2":
            # Aqui desarrollar código para mostrar productos
            for producto in lista_productos:
                print(
                    f"ID: {producto[0]},  Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}"
                )  # Muestra en pantalla

        case "3":
            # Aqui desarrollar código para buscar productos
            print("Procesando buscar productos...")

        case "4":
            # Aqui desarrollar código para eliminar productos
            # Pedimos al usuario que ingrese el Id del producto a eliminar
            id_borrar = int(input("Ingrese el Id del producto a borrar: "))
            # Seteamos una bandera en False
            id_eliminado = False
            # Iteramos la lista_productos, buscando el índice de la sub-lista que contiene el Id a borrar
            for producto in lista_productos:
                if id_borrar in producto:
                    lista_productos.remove(producto)
                    id_eliminado = True
            if id_eliminado:
                print("Producto eliminado exitosamente!")
            else:
                print("Producto no encontrado")
        case "5":
            print("Saliendo...")
            break  # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")
