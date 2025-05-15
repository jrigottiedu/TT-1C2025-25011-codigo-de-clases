lista_productos = [
    ["manzana", "fruta", 1500], # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
    ["kiwi", "fruta", 2100],
    ["limon", "fruta", 1800],
    ["espinaca", "verdura", 800]
] 


print(f"Asi luce lista_productos:")
for indice in range(len(lista_productos)):
    producto = lista_productos[indice]
    print(f"indice: {indice}: {producto}")

# lista_productos con metodo pop() remueve el último elemento
print(f"\nlista_productos.pop() retorna: {lista_productos.pop()}")

print(f"\nAsi luce ahora lista_productos:")
for indice in range(len(lista_productos)):
    producto = lista_productos[indice]
    print(f"indice: {indice}: {producto}")

# lista_productos con metodo pop(1) remueve el elemento con índice 1
print(f"\nlista_productos.pop(1) retorna: {lista_productos.pop(1)}")

print(f"\nAsi luce lista_productos:")
for indice in range(len(lista_productos)):
    producto = lista_productos[indice]
    print(f"indice: {indice}: {producto}")

print("\n Notar que ahora el Kiwi tomo el indice 1 cuando antes tenía 2")