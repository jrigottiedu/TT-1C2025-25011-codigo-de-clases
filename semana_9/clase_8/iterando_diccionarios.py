# En este archivo vemos las tres variantes para iterar un diccionario

# Comenzamos por declarar un diccionario
diccionario_1 = {
    "nombre": "pantalon",
    "cantidad": 100,
    "precio": 1500
}

# Usamos el método keys() que nos devuelve las claves del diccionario
# podemos compararlo con el for in + range cuando iteramos listas
print("\n Iteramos un diccionario usando el método keys()")
for clave in diccionario_1.keys():
    print(f"Accedemos al valor: '{diccionario_1[clave]}' usando la clave '{clave}'")

# Usamos el método values() que nos devuelves los valores
print("\n Iteramos un diccionario usando el método values()")
for valor in diccionario_1.values():
    print(f"Accedemos directamente al valor: '{valor}' sin clave")

# Usamos el método items() que retorna clave y valor
print("\n Iteramos un diccionario usando el método items()")
for clave, valor in diccionario_1.items():
    print(f"Accedemos al valor: '{valor}' sin usar la clave '{clave}'")
