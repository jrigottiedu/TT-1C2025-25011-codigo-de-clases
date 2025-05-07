"""
Tu tarea es la siguiente:

Crear una lista con los nombres de los y las clientes que vamos a procesar.
Algunos nombres pueden estar en blanco, y debemos detectarlo.

Recorrer la lista (bucle - while o for) y mostrar el nombre de cada cliente o clienta,
junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

Si encuentras a alguien cuyo nombre sea una cadena en blanco,
mostrar un mensaje de alerta indicando que ese dato no es válido.

Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(),
de modo que siempre tengan la primera letra en mayúscula y el resto en minúscula.

"""

# Declaramos e inicializamos la lista de nombres:
nombres = [
    "juan pablo",
    "  ",
    "maría jose",
    "ana belén",
    "  ",
    "luis miguel",
    "carlos alberto",
]

# Usamos un bucle while para iterar la lista

# Esta solución funciona
indice = 0
while indice < len(nombres):
    if nombres[indice].strip() == "":
        print(f"Atención: se ha encontrado un nombre vacío en la posición {indice}")
    else:
        print(f"Nombre del cliente {nombres[indice].title()} número: {indice + 1}")
    indice += 1

# Esta solución no funciona
# while indice < len(nombres):
#     indice += 1
#     if nombres[indice].strip() == "":
#         print(f"Atención: se ha encontrado un nombre vacío en la posición {indice}")
#         continue
#     print(f"Nombre del cliente {nombres[indice].title()} número: {indice + 1}")


# Usamos un bucle for para iterar la lista
for indice in range(len(nombres)):
    if nombres[indice].strip() == "":
        print(f"Atención: se ha encontrado un nombre vacío en la posición {indice}")
        continue
    print(f"Nombre: {nombres[indice].title()} - Posición: {indice}")