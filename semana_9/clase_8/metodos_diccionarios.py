diccionario_1 = {
    "nombre": "pantalon",
    "cantida": 100,
    "precio": 1500
}

# 1. get(): obtener el valor de una clave (devuelve None si no existe)
print(diccionario_1.get("precio"))      # 1500
print(diccionario_1.get("color"))       # None

# 2. keys(): devuelve todas las claves del diccionario
print(diccionario_1.keys())             # dict_keys(['nombre', 'cantida', 'precio'])

# 3. values(): devuelve todos los valores del diccionario
print(diccionario_1.values())           # dict_values(['pantalon', 100, 1500])

# 4. items(): devuelve pares clave-valor como tuplas
print(diccionario_1.items())            # dict_items([('nombre', 'pantalon'), ('cantida', 100), ('precio', 1500)])

# 5. pop(): elimina una clave y devuelve su valor
precio_eliminado = diccionario_1.pop("precio")
print(precio_eliminado)             # 1500
print(diccionario_1)                   # {'nombre': 'pantalon', 'cantida': 100}

# 6. popitem(): elimina y devuelve el último par clave-valor insertado
ultima_clave_valor = diccionario_1.popitem()
print(ultima_clave_valor)          # ('cantida', 100)
print(diccionario_1)                  # {'nombre': 'pantalon'}

# 7. update(): agrega o actualiza pares clave-valor
diccionario_1.update({"precio": 2000, "color": "azul"})
print(diccionario_1)                  # {'nombre': 'pantalon', 'precio': 2000, 'color': 'azul'}

# 8. clear(): elimina todos los elementos del diccionario
diccionario_1.clear()
print(diccionario_1)                  # {}
