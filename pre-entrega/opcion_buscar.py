# Declaracion de variables (Globales)

# Declaramos la lista de productos, que va a almacenar los siguientes datos
# nombre, categoria, precio
# La inicializamos con algunos datos para poder testear la opcion 2 - Mostrar productos
lista_productos = [
    ["manzana roja", "fruta", 1500], # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
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
            # nombre, categoría, y precio
            # Nota: valiamos nombre, agregar validación en los otros campos
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
            producto = [nombre, categoria, precio]
            # Luego usamos el método append() para insertar la sub-lista productos en la lista principal lista_productos
            lista_productos.append(producto)

        case "2":
            # Aqui desarrollar código para mostrar productos
            for indice in range(len(lista_productos)):
                # Almaceno en una variable temporal cada sub-lista de la lista_productos
                producto=lista_productos[indice]
                print(
                    f"Indice: {indice}, Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: {producto[2]}"
                )  # Muestra en pantalla

        case "3":
            # Opcion Basica I
            # buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()
            # encontrado = False # si encuentro algo pongo True
            # for producto in lista_productos:
            #     if buscar == producto[0].lower():
            #         encontrado = True

            # if encontrado == True:
            #     print("Encotrnado")
            # else:
            #     print("No encontrado")

            # Opcion Basica Mejorada
            buscar = input("Ingresá el nombre del producto a buscar: ").strip().lower()
            listaEncontrados = [] # lista vacia
            for producto in lista_productos:
                if buscar in producto[0].lower():
                    listaEncontrados.append(producto)

            if len(listaEncontrados) > 0: # if listaEncontrados :
                for encontrado in listaEncontrados:
                    print(f"Producto encontrado: {encontrado}")
            else:
                print("No encontrado")


        case "4":
            # Aqui desarrollar código para eliminar productos
            # Pedimos al usuario que ingrese el indice producto a eliminar
            while True:
                indice_eliminar = input("Ingrese el indice del producto a eliminar: ")
                if indice_eliminar.isdigit():
                    indice_eliminar = int(indice_eliminar)
                    break
                else:
                    print("Indice no valido")
                    continue
            
            if indice_eliminar >= len(lista_productos):
                print("Indice invalido")
                continue
            else:
                lista_productos.pop(indice_eliminar)
            print("Producto eliminado exitosamente")

        case "5":
            print("Saliendo...")
            break  # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")
