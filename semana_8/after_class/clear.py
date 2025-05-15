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

# lista_productos[1] con metodo clear() limpia todo el contenido del elemento en posición 1
print(f"\nlista_productos.clear() retorna: {lista_productos[1].clear()}")

print(f"\nAsi luce ahora lista_productos:")
for indice in range(len(lista_productos)):
    producto = lista_productos[indice]
    print(f"indice: {indice}: {producto}")

print("\n Notar que se mantienen los índices")

print(f"\nAsi queremos acceder al contenido de la sublista, hay que validar antes que no sea una lista vacia:")
for indice in range(len(lista_productos)):
    producto = lista_productos[indice]
    if len(producto)==0:
        print(f"Indice: {indice}: *** Este elemento fue eliminado con clear() ***")
    else:
        print(f"Indice: {indice}: Nombre: {producto[0]}, categoría: {producto[1]}, precio: {producto[2]}")