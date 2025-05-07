"""Tu tarea es la siguiente:

Crear una lista con los nombres de los y las clientes que vamos a procesar.
Algunos nombres pueden estar en blanco, y debemos detectarlo.

Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

Si encuentras a alguien cuyo nombre sea una cadena en blanco,
mostrar un mensaje de alerta indicando que ese dato no es válido.

Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(),
de modo que siempre tengan la primera letra en mayúscula y el resto en minúscula."""

# Lista de clientes con algunos nombres en blanco
lista_clientes = ["Juan", "ana maria", " ", "sonia ", "pablo", " "]
# indice_nombre = 0

for indice_nombre in range(len(lista_clientes)):  # range(6) => 0,1,2,3,4,5
    if len(lista_clientes[indice_nombre].strip()) == 0:
        print(f" ❌❌❌ El puesto {indice_nombre} esta vacio")
        continue

    print(f"cliente { indice_nombre}: {lista_clientes [indice_nombre].title()}")

# Enfoque con el while
indice = -1
while indice < len(lista_clientes) - 1:
    indice += 1
    if lista_clientes[indice].strip() == "":
        print(f"Atención: posición {indice} vacío")
        continue
    print(f"Cliente número: {indice}: {lista_clientes[indice].title()}")
