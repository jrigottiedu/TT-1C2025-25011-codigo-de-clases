"""
Clasificar al usuario según la edad ingresada a partir de los siguientes parámetros:

Si la edad es menor a 12, el usuario se clasifica como "niño/a"
Si la edad es mayor o igual a 12 y menor a 18, el usuario se clasifica como "adolescente"
Si la edad es mayor o igual a 18, el usuario se clasifica como "adulto/a"

Resolvemos con la estructura if-elif-else y luego con match
"""

# Ingreso de datos
edad = int(input("Ingrese su edad: "))

# Procesamiento de datos
if edad < 12:
    print("Usted ha sido clasificado como niño/a")
else:
    if edad >= 12 and edad < 18:
        print("Usted ha sido clasificado como adolesncente")
    else:
        print("Usted ha sido clasificado como adulto/a")


match edad:
    case edad if edad < 12:
        print("Usted ha sido clasificado como niño/a")
    case edad if edad >= 12 and edad < 18:
        print("Usted ha sido clasificado como adolesncente")
    case _:
        print("Usted ha sido clasificado como adulto/a")
