productos = ["carne", "carbon", "ensaladas", "bebidas", "postre", "pan", "queso"]

# 1. Acceder a los 3 primeros elementos
print(productos[:3])
# ['carne', 'carbon', 'ensaladas']


# 2. Obtener los últimos 2 elementos
print(productos[-2:])
# ['pan', 'queso']


# 3. Obtener elementos desde la posición 2 a la 4 (sin incluir la 5)
print(productos[2:5])
# ['ensaladas', 'bebidas', 'postre']


# 4. Cada dos elementos
print(productos[::2])
# ['carne', 'ensaladas', 'postre', 'queso']

