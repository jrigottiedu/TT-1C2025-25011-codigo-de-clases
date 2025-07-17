from get_metodos import *
from bd_metodos import *

# creamos la bd inventario.db y la tabla vehiculos
bd_crear_tabla_vehiculos()

# Bucle principal
while True:

    print(
        """
Concesionaria de autos:

Menú de opciones:
    1. Alta de vehículo
    2. Mostrar vehículos
    3. Buscar vehículo por marca
    4. Eliminar vehículo por índice
    5. Actualizar precio
    6. Reporte de bajo stock
    7. Salir 
"""
    )
    # Ingreso de opcion de menú
    opcion = input("Ingrese su opción: ")  # retorna un str

    match opcion:
        case "1":
            marca = getMarca()
            modelo = getModelo()
            precio = getPrecio()
            descripcion = getDescripcion()
            cantidad = getCantidad()

            resultado = bd_insertar_vehiculo(
                marca, modelo, precio, descripcion, cantidad
            )
            if resultado:
                print("Vehiculo insertado OK")
            else:
                print("Ups, algo salió mal")

        case "2":
            print("Procesando mostrando vehículos...")
            lista_productos = bd_leer_vehiculos()
            if len(lista_productos) > 0:
                print(lista_productos)
            else:
                print("No hay registros que mostrar...")

        case "3":
            marca_buscar = getMarca()
            lista_productos = bd_leer_vehiculo_por_marca(marca_buscar)
            if len(lista_productos) > 0:
                print(lista_productos)
            else:
                print("No hay registros que mostrar...")

        case "4":
            print("Procesando Eliminando vehículos...")
            id = getIdVehiculo()
            vehiculo = bd_leer_vehiculo_por_id(id)
            if vehiculo:
                resultado = bd_eliminar_vehiculo(id)
                if resultado:
                    print("Vehiculo eliminado")
                else:
                    print("Ups, algo salió mal")
            else:
                print("No se encontro vehiculo con ese id")

        case "5":
            # actualizar
            id = getIdVehiculo()
            nuevo_precio = getPrecio()
            resultado = bd_actualizar_precio(id, nuevo_precio)
            if resultado:
                print("Actualizado OK")
            else:
                print("Ups...")

        case "6":
            # reporte de bajo stock
            limite = int(input("Ingrese el limite de stock"))
            lista_productos = bd_leer_vehiculos_bajo_stock(limite)
            if len(lista_productos) > 0:
                print(lista_productos)
            else:
                print("No hay registros que mostrar...")

        case "7":
            print("Saliendo...")
            break  # interrumpe el flujo del while
        case _:  # por defecto - si no hubo match
            print("Opción no válida")
