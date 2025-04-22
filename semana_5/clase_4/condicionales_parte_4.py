"""
Clasificar la opción ingresada por el usuario:

Si la opción es 1, informar "Alta de productos"
Si la opción es 2, informar "Buscar productos"
Si la opción es 3, informar "Editar productos"

Si la opción es cualquier otra, informar "Opción incorrecta"

Resolvemos primero con luego con match
"""

# Ingreso de dato
opcion = input("Ingrese su opción: ")

# Procesamiento

match opcion :
    case "1": # implicitamente pregunta si opcion == 1
        print("Alta de producto")
    case "2":
        print("Buscar producto")
    case "3":
        print("Editar producto")
    case _:
        print("Opcion incorrecta")