"""
Vamos a ver ahora las funciones que no reciben ningún dato,
es decir ningún argumento,
pero que su algoritmo, retorna un dato.
El retorno puede ser un literal (string, int, bool) o una variable
"""

# Declaramos la funcion getNombre()
# que solicite al usuario su nombre y lo retorne 

# definicion de la función
def getNombre():
    nombreLocal = input("Ingrese su nombre desde la funcion local: ")
    return nombreLocal # retorno nombreLocal

# invocamos la función
# como la funcion getNombre() retorna un valor, este debe ser almacenado en una variable
nombreGlobal = getNombre()

# A fin de ver como se van sobrescribiendo las variables locales y globales
# invocamos a la función getNombre() dentro de un while

while True:
    # invocamos la funcion
    nombreGlobal = getNombre()
    print(f"NombreGlobal: {nombreGlobal}")
    if nombreGlobal == "fin":
        break

# -----------------------------------------------------------------------------------
# Modificamos ahora la función getNombre para que retorne nombre y edad
# la llamamos getCliente()
# veremos que retorna múltiples valores dentro de una tupla

# definicion de la funcion
def getCliente():
    nombreLocal = input("Ingrese su nombre desde la funcion local: ")
    edadLocal = input("Ingrese su edad desde la funcion local: ")
    return (nombreLocal, edadLocal) # retorna una tupla con nombreLocal y edadLocal

# invocamos la función getCliente()
# tener en cuenta que retorna dos valores, por ello debemos usar dos variables

nombreGlobal, edadGlobal = getCliente()
print (f"Nombre del cliente {nombreGlobal}, edad del cliente {edadGlobal}")


# -----------------------------------------------------------------------------------
# Ejercicio 1 (hicimos en clase)
# Generar una funcion que solicite (input) al usuario la base y la altura de un rectangulo
# calcule su area y lo retorne (return)
# Luego desde la función principal (o cuerpo principal) imprimir el valor en pantalla

# declaramos la funcion
def getArea():
    base = int(input("Ingrese valor de la base: ")) # solicito la base
    altura = int(input("Ingrese valor de la altura: ")) # solicito la altura
    # calculo el area
    area = base * altura
    return area # retorno el cálculo del área

# invocamos la funcion
# si la def de la funcion, tiene un return
# debo almacenar ese valor que devuelve en una variable

areaGlobal = getArea() # areaGlobal almacena el valor que retorna area
print(f"El area calculada por la funcion getArea() es: {areaGlobal}")


# Ejercicio 2 (tarea)
# agregar validación a la función getNombre()