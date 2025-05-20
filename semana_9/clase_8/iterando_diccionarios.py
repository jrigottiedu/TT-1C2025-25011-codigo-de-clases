producto_1 = {
    "nombre": "pantalon",
    "cantidad": 100,
    "precio": 1500
}

print("For con clave")
for clave in producto_1.keys():
    print(f"el valor desde la clave: {producto_1[clave]}")

print("For con valor")
for valor in producto_1.values():
    print(valor)

print("For con clave / valor")
for clave, valor in producto_1.items():
    print(clave, valor)
