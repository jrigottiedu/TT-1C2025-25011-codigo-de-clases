# 1 ¿Cuál es el método utilizado para agregar un nuevo producto a la lista?
lista_productos = [
    ["manzana", "fruta", 1500],  # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
]
print(lista_productos)

# Usuario ingresa un producto nuevo
# lo almacenamos en una lista temporal
producto = ["yogurt", "lacteo", 800]
lista_productos.append(producto)
print(lista_productos)

# 2. ¿Cuál es el propósito de utilizar índices al mostrar la lista de productos?
print(f"Primer producto de la lista: {lista_productos[0]}")
print(
    f"Nombre {lista_productos[0][0]} - Categoria {lista_productos[0][1]} Precio {lista_productos[0][2]}"
)

# 3. ¿Cuál es el propósito de validar los datos ingresados antes de agregarlos a la lista de productos?
while True:
    precio = input("Ingrese el precio del prodcuto: ").strip()
    if not precio.isdigit():
        print("ERROR: Debe ser numerico")
        continue
    else:
        precio = int(precio)
        break

print(precio)

# 4. ¿Cuál es la estructura básica del menú principal del programa?
# Rsta: lo tienen en la sección pre-entrega

# 5.
producto = ["yogurt", "lacteo", 800]
print(producto[0])
producto[0] = "yogurt griego"
print(producto[0])

# 6 ¿Por qué se valida que el precio sea un número válido antes de agregar un producto?
# Rsta: lo vimos en la 4

# 7. ¿Qué debe verificar el programa al agregar un nuevo producto?
# Rsta: lo vimos arriba

# 8. ¿Qué estructura de datos debe utilizar en el programa para almacenar los productos?
# Usando lista
producto = ["yogurt", "lacteo", 800]

# Usando diccionario
producto = {"nombre": "yogurt", "categoria": "lacteo", "precio": 800}


# 9. ¿Qué método se usa para eliminar un producto de la lista?
print(f"Lista de productos: {lista_productos}")
lista_productos.pop(1)
print(f"Lista de productos liego de pop(0): {lista_productos}")

# 10. ¿Qué método se usa para eliminar un producto de la lista?
print(f"Lista de productos: {lista_productos}")
estadoEliminar = False
eliminarProducto = input("Ingrese el nombre del prodcuto a eliminar: ").strip().lower()


for indice, producto in enumerate(lista_productos):
    if producto[0].lower() == eliminarProducto:
        lista_productos.pop(indice)
        estadoEliminar = True

if estadoEliminar:
    print("Producto eliminado")
else:
    print("Producto no encontrado")
