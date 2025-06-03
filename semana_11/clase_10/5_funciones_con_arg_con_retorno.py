"""
El cuarto caso, son aquellas funciones que reciben datos (argumentos)
que procesan esos datos,
y que retornan un valor o resultado
"""

# Declaramos una funcion que recibe la base y la altura de un rectangulo  
# y retorna su area.
# Esta funcion no solicita nada al usuario

# declaramos la funcion
def getArea(base, altura): # parámetro_1: base, parámetro_2: altura
    # calculo el area
    area = base * altura
    return area # retorno el área calculada


# invocamos la funcion
# si la def de la funcion tiene un return
# debo almacenar ese valor que devuelve en una variable

# opción_1 declarando las variables fijas
baseGlobal = 12
alturaGlobal = 5
# invoco a la getArea y le paso los argumentos baseGlobal y alturaGlobal
areaGlobal = getArea(baseGlobal, alturaGlobal)
print(f"El area calculada por la funcion getArea() es: {areaGlobal}")

# opción_2 el usuario ingresa los valores
baseGlobal = int(input("Ingrese la base del rectángulo: "))
alturaGlobal = int(input("Ingrese la altura del rectángulo: "))
# invoco a la getArea y le paso los argumentos baseGlobal y alturaGlobal
areaGlobal = getArea(baseGlobal, alturaGlobal)
print(f"El area calculada por la funcion getArea() es: {areaGlobal}")


# Ejercicio
# Generar una funciona que solicite al usuario el monto gastado en una compra y el impuesto IVA
# La funcion debe retorna el total a pagar, monto gastado con IVA
# Luego desde la funcion principal, indicar el monto a pagar









