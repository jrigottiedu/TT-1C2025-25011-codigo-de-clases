# Declarar funciones / métodos get/validar


def getOpcion():
    opcion = input("Ingrese su opción: ")
    return opcion


def getMarca():
    while True:
        marca = input("Ingrese la marca del vehiculo: ").strip()
        if marca:
            break
        else:
            print("No se admite campo vacío")
    return marca


def getModelo():
    while True:
        modelo = input("Ingrese el modelo del vehiculo: ")
        if modelo:
            break
        else:
            print("No se admite campo vacío")
    return modelo


def getPrecio():
    while True:
        try:
            precio = int(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Precio no válido. Intente nuevamente.")
    return precio


def getDescripcion():
    while True:
        descripcion = input("Ingrese la descripción del vehiculo: ")
        if descripcion:
            break
        else:
            print("No se admite campo vacío")
    return descripcion


def getCantidad():
    while True:
        try:
            cantidad = float(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Cantidad no válido. Intente nuevamente.")
    return cantidad


def getIdVehiculo():
    while True:
        try:
            id = int(input("Ingrese el ID del vehiculo: "))
            break
        except ValueError:
            print("ID no válido. Intente nuevamente...")
    return id
