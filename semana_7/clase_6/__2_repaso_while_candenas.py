"""
Bucle While:

Usos:
- permiten ejecutar un bloque de código un número desconocido de veces (mientras se cumpla la codición).
- esperar que el usuario ingrese un dato correcto (validación de datos)
- acumular valores (registro de ingresos en el ejemplo de clase 5)

Vimos además:
- concepto de contador y acumulador
- sentencias break y continue

"""

# Usamos el bucle while pare recorrer la cadena = "Python"
cadena = "Python"
indice = 0
longitud_cadena = len(cadena) # 6
while indice < longitud_cadena:
    print(f"El elemento {cadena[indice]} se encuentra en la posición {indice}")
    indice += 1 # indice = indice + 1


# Vemos break y continue con la validación del ingreso del nombre (semana 6 - after class - validar_ingresos.py)

while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre == "":
        print("No se admite vacio")
        continue
    else:
        break

while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre != "": # len(nombre)
        break
    else:
        print("No se admite vacio")



