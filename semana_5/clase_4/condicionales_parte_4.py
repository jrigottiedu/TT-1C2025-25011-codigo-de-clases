"""
Clasificar la opción ingresada por el usuario:

Si la opción es 1, informar "Alta de productos"
Si la opción es 2, informar "Buscar productos"
Si la opción es cualquier otra, informar "Opción incorrecta"

Resolvemos primero con elif y luego con match
"""

# Ingreso de datos
opcion = input("Ingrese su opción: ")

if opcion == "1":
    print("Alta de productos")
elif opcion == "2":
    print("Buscar productos")
else:
    print("Opción incorrecta")

match opcion:
    case "1":
        print("Alta de productos")
    case "2":
        print("Buscar productos")
    case _:
        print("Opción incorrecta")
