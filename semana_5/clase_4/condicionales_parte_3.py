"""
Clasificar al usuario según la edad ingresada a partir de los siguientes parámetros:

Si la edad es menor a 12, el usuario se clasifica como "niño/a"
Si la edad es mayor o igual a 12 y menor a 18, el usuario se clasifica como "adolescente"
Si la edad es mayor o igual a 18, el usuario se clasifica como "adulto/a"
Si la edad es mayor o igual a 65, el usuario se clasifica como "adulto/a mayor"
Si la edad es mayor o igual a 90, el usuario se clasifica como "adulto/a super mayor"

Resolvemos con la estructura if-elif-else y luego con match
                                else + if

"""

# Ingreso de edad

edad = int(input("Ingrese su edad: "))

# Procesamiento de los datos

if edad < 0:
    print("Ingrese una edad válida")
elif edad <= 12:  # -5 es menor o igual a 12? => TRUE
    print("Usted es niño/a")
elif edad <= 18:
    print("Usted es adolescente")
elif edad <= 65:
    print("Usted es adulto/a")
else:
    print("Usted es adulto/a mayor")

"""
Aplicamos match a la resolucion de este ejercicio
"""

# en el match no van a ver ni else ni elif
match edad :
    case edad if edad <= 12:
        print("Usted es niño/a")
    case edad if edad <= 18:
        print("Usted es adolescente")
    case edad if edad <= 65:
        print("Usted es adulto/a")
    case _:
        print("Usted es adulto/a mayor")
