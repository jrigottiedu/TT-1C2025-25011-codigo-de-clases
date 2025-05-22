# lista_productos = [
#     ["manzana", "fruta", 1500], # nombre="manzana", categoria="fruta", precio="1500"
#     ["pera", "fruta", 2500],
# ]

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