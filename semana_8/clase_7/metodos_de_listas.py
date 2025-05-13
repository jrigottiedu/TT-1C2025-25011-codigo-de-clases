# Recordamos nuestra lista de la clase 6
productos = ["carne", "carbon", "ensaladas", "bebidas", "postre"]

# 1. append(): agrega un elemento al final de la lista
productos.append("pan")
print(productos)
# Resultado: ['carne', 'carbon', 'ensaladas', 'bebidas', 'postre', 'pan']


# 2. remove(): elimina el primer elemento que coincida con el valor
productos.remove("carbon")
print(productos)
# Resultado: ['carne', 'ensaladas', 'bebidas', 'postre', 'pan']


# 3. pop(): elimina y devuelve un elemento (por defecto, el último)
producto_quitado = productos.pop()
print(producto_quitado)  # Resultado: 'pan'
print(productos)         # Resultado: ['carne', 'ensaladas', 'bebidas', 'postre']

# 3.1 tambien se puede usar el indice
producto_quitado = productos.pop(2)
print(producto_quitado)  # Resultado: 'bebidas'
print(productos)         # Resultado: ['carne', 'ensaladas', 'postre']


# 4. insert(): inserta un elemento en una posición específica
productos.insert(1, "verduras")
print(productos)
# Resultado: ['carne', 'verduras', 'ensaladas', 'postre']


# 5. extend(): agrega todos los elementos de otra lista al final
nuevos_productos = ["pan", "queso"]
productos.extend(nuevos_productos)
print(productos)
# Resultado: ['carne', 'carbon', 'ensaladas', 'bebidas', 'postre', 'pan', 'queso']


# 6. index(): devuelve la posición (índice) del primer elemento que coincida
posicion = productos.index("bebidas")
print(posicion)
# Resultado: 3


# 7. count(): cuenta cuántas veces aparece un elemento
productos.append("pan")  # Agregamos otro "pan"
cantidad = productos.count("pan")
print(cantidad)
# Resultado: 2


# 8. sort(): ordena la lista alfabéticamente (de forma permanente)
productos.sort()
print(productos)
# Resultado: ['bebidas', 'carbon', 'carne', 'ensaladas', 'pan', 'pan', 'postre', 'queso']


# 8.1 orden inverso
productos.sort(reverse=True)

