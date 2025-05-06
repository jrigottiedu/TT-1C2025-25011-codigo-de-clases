# Vemos el uso de las sentencias break y continue en el bucle For

# Usamos break para buscar un elemento en la lista

productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

# Usamos continue para contar elementos str de nuestra lista

buscar = input("Ingrese el valor a buscar: ").strip()
for producto in productos:
    if producto.lower() == buscar.lower():
        print("Producto encontrado!")