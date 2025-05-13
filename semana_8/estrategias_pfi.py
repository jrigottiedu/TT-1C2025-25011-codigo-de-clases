productos = {
    1: {"nombre": " mouse ", "categoria": "periferico", "precio": 10000},
    2: {"nombre": "Disco SSD 520 GB", "categoria": "almacenamiento", "precio": 50000},
}

lista_productos = []

producto = {
    "codigo": 1,
    "nombre": " mouse ", 
    "categoria": "periferico", 
    "precio": 10000}

lista_productos.append(producto)

producto = {
    "codigo": 1,
    "nombre": "Disco SSD 520 GB", 
    "categoria": "periferico", 
    "precio": 50000}

lista_productos.append(producto)

for producto in lista_productos:
    for key, value in producto.items():
        print(key, value)