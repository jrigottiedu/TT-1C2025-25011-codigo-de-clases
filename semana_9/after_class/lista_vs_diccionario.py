# Lista vs Diccionario

"""
Generamos una lista_productos y almacenamos los valores
índice 0: manzana (nombre)
índice 1: fruta (categoria) 
índice 2: 1500 (precio)

y luego un diccionario con los pares clave/valor
nombre: manzana
categoria: fruta
precio: 1500

Iteramos la lista con la función enumerate,
que retorna índice - elemento

Iteramos el diccionario con el método items(),
que retorna clave - valor

Y comparamos la ventaja de trabajar con diccionarios,
no tenemos que preocuparnos por la posición,
ya con los diccionarios, accedemos a los valores a través de la clave
"""

# Creamos la lista_producto con los siguientes valores según la posición
# 0: nombre - 1: categoria - 2: precio
lista_producto = ["manzana", "fruta", 1500]

# Iteramos la lista con la función enumerate() que retorna el par índice - elemento
for indice, elemento in enumerate(lista_producto):
    print(f"Indice {indice} - elemento {elemento}")

# Ahora creamos el diccionario con los mismos valores, pero para las claves indicadas
diccionario_producto = {
    "categoria": "fruta", 
    "nombre": "manzana", 
    "precio": 1500}

# Iteramos el diccionario con el método item() que retorna el par clave - valor
for clave, valor in diccionario_producto.items():
    print(f"Clave {clave} : Valor {valor}")

# Al usar listas, debemos preocuparnos por la posición del elemento
lista_producto[0]
# En cambio con diccionarios, no
diccionario_producto["nombre"]
