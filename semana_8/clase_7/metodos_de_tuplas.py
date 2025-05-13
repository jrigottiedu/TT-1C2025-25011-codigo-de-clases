# 1. count(): cuenta cuántas veces aparece un elemento
colores = ("rojo", "azul", "verde", "rojo", "amarillo", "rojo")

cantidad_rojo = colores.count("rojo")
print(f"El color 'rojo' aparece {cantidad_rojo} veces.")
# Resultado: El color 'rojo' aparece 3 veces.


# 2. index(): devuelve el índice de la primera aparición de un elemento
frutas = ("manzana", "banana", "naranja", "banana")

posicion_banana = frutas.index("banana")
print(f"La primera 'banana' está en la posición {posicion_banana}.")
# Resultado: La primera 'banana' está en la posición 1


# 💡 Si el valor no está en la tupla, index() lanza un error, por lo que se puede usar con in para verificar antes:
if "pera" in frutas:
    print(frutas.index("pera"))
else:
    print("No se encontró 'pera' en la tupla.")
