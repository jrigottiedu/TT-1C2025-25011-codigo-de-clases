# Ejercicio de tarea 1

# modificar la función getNombre, para que su algoritmo
# no acepte nombres vacios
# debe retornar un nombre válido

def getNombreProducto():
    while True:
        nombreLocal = input("Ingrese el nombre del producto desde la funcion local: ").strip()
        if nombreLocal == "":
            print("No se acepta vacio")
            continue
        else:
            break
    return nombreLocal # retorno nombreLocal
    

# nombre = getNombreProducto()
# print(nombre)

# funcion para nombre producto y categoria
def getCadena(texto):
    # cadena = input("Ingrese el nombre del producto: ")
    cadena = input(texto)
    return cadena

nombreProducto = getCadena("Ingrese el nombre del producto: ")
print(nombreProducto)
categoriaProducto = getCadena("Ingrese la categoria del producto: ")
print(categoriaProducto)