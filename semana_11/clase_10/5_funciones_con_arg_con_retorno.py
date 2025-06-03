# Declaramos una funcion que recibe la base y la altura de un rectangulo  
# y retorna su area.
# Esta funcion no solicita nada al usuario

# declaramos la funcion
def getArea(base, altura):
    # calculo el area
    area = base * altura
    return area


# invocamos la funcion
# si la def de la funcion, tiene un return
# debo almacenar ese valor que devuelve en una funcion

baseGlobal = 12
alturaGlobal = 5
areaGlobal = getArea(baseGlobal, alturaGlobal)
print(f"El area calculada por la funcion getArea() es: {areaGlobal}")


# Ejercicio
# Generar una funciona que solicite al usuario el monto gastado en una compra y el impuesto IVA
# La funcion debe retorna el total a pagar, monto gastado con IVA
# Luego desde la funcion principal, indicar el monto a pagar


# Ejercicio
# Como cambiarías las funciones para que retorne los datos que ingresa el usuario?







