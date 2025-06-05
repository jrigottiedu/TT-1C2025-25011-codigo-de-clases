# Ejercicio de tarea 2

# a partir de la función getNombre(), generar la función getPrecio()
# de manera que su algoritmo no acepte precios vacios, no numericos ni negativos
# debe retornar un precio válido


def getPrecio():
    while True:
        precioLocal = input("Ingrese el precio del producto: ").strip()
        print(f"id o posicion de precio dentro de getPrecio: {id(precioLocal)}")
        if precioLocal.isdigit():
            break
        else:
            print("Precio inválido, intente nuevamente.")
            continue
    return precioLocal # retorno nombreLocal

precio = getPrecio()
print(f"id o posicion de precio en el cuerpo principal con 55: {id(precio)}")
print(precio)
precio = 66
print(f"id o posicion de precio en el cuerpo principal con 66: {id(precio)}")