# Declaramos e inicializamos un diccionario para los datos del vehiculo
vehiculo_1 = {"marca": "Peugeot", "modelo": "208", "precio": 15000}
vehiculo_2 = {"marca": "Fiat", "modelo": "Cronos", "precio": 14000}

# Declarar la lista global e inicializarla
lista_vehiculos = [vehiculo_1, vehiculo_2] 
# en la segunda parte del curso
# esto se almacena en una Base de Datos

"""
Armamos el menú de opciones
"""
# print(
#     """
# Concesionaria de autos:

# Menú de opciones:
#     1. Alta de vehículo
#     2. Mostrar vehículos
#     3. Buscar vehículo por marca
#     4. Eliminar producto por índice
#     5. Salir
# """
# )

# Bucle principal
while True:

    print(
        """
Concesionaria de autos:

Menú de opciones:
    1. Alta de vehículo
    2. Mostrar vehículos
    3. Buscar vehículo por marca
    4. Eliminar producto por índice
    5. Salir 
"""
    )
    # Ingreso de opcion de menú
    opcion = input("Ingrese su opción: ")  # retorna un str

    match opcion:
        case "1":
            print("Procesando alta de productos...")
            # Validamos los ingresos:
            while True:
                marca = input("Ingrese la marca del vehículo: ")
                if marca != "":
                    break
                else:
                    print("Debe ingresar un valor!")

            while True:
                modelo = input("Ingrese el modelo: ")
                if modelo != "":
                    break
            
            while True:
                precio = input("Ingrese el precio: ")
                if precio != "": #if precio:
                    break


            # alternativamente armamos una lista temporal:
            # vehiculo_lista = [marca, modelo, precio]
            # armamos el diccionario temporal vehiculo
            vehiculo = {"marca": marca, "modelo": modelo, "precio": precio}
            # insertamos el diccionario en la lista_productos usando el método append()
            lista_vehiculos.append(vehiculo)
            print("Vehículo insertado exitosamente!")
            # print(lista_vehiculos)

        case "2":
            print("Procesando mostrando vehículos...")
            for vehiculo in lista_vehiculos:
                print(
                    f"Marca: {vehiculo["marca"]} - Modelo: {vehiculo['modelo']} - Precio: {vehiculo['precio']}"
                )

        case "3":
            print("Procesando Buscando vehículos...")
            # usuario ingresa la marca a buscar
            buscar = input("Ingrese la marca del vehículo a buscar: ").strip().lower()
            # pongo una bandera de resultado en False
            encontrado = False
            for vehiculo in lista_vehiculos:
                if buscar in vehiculo["marca"].lower():
                    # actualizo la bandera a True
                    encontrado = True
                    print(
                            f"Marca: {vehiculo["marca"]} - Modelo: {vehiculo['modelo']} - Precio: {vehiculo['precio']}"
                        )
            # cuando se termina el for evaluo la bandera:
            if encontrado == False:
                print("Marca no encontrada :(")    


        case "4":
            print("Procesando Eliminando vehículos...")
            # Mostrar indice y datos del vehículo
            for indice, vehiculo in enumerate(lista_vehiculos):
                print(
                    f"ID: {indice} - Marca: {vehiculo["marca"]} - Modelo: {vehiculo['modelo']} - Precio: {vehiculo['precio']}"
                )
            # Ingresar el ID del vehiculo a borrar:
            while True:
                # El usuario ingresa el ID del vehículo a eliminar
                id_borrar= input("Ingrese el ID del vehículo a borrar: ")
                if id_borrar.isdigit():
                    id_borrar = int(id_borrar)
                    # break
                else:
                    print("ID no valido, intente nuevamente...")
                    continue
                if id_borrar < len(lista_vehiculos):
                    break
                else:
                    print("ID fuera de rango, intente nuevamente...")
                    continue                    

            # usamos el método pop para eliminar
            lista_vehiculos.pop(id_borrar)
            print("Vehículo borrado exitosamente!")

        case "5":
            print("Saliendo...")
            break  # interrumpe el flujo del while
        case _:  # por defecto - si no hubo match
            print("Opción no válida")
