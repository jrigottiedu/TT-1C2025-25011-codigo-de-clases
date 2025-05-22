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

# 0: nombre - 1: categoria - 2: precio
lista_producto = ["fruta", "manzana", 1500]

for indice, elemento in enumerate(lista_producto):
    print(f"Indice {indice} - elemento {elemento}")

diccionario_producto = {
    "categoria": "fruta", 
    "nombre": "manzana", 
    "precio": 1500}

for clave, valor in diccionario_producto.items():
    print(f"Clave {clave} : Valor {valor}")


lista_producto[0]
diccionario_producto["nombre"]

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
print(f"{CYAN} --- MENÚ --- {RESET}")
print("Linea siguiente")