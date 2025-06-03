# Declaramos una funcion que solicita al usuario su nombre y 
# lo retorne

# definicion de la funcion
def getNombre():
    nombreLocal = input("Ingrese su nombre desde la funcion local: ")
    edadLocal = input("Ingrese su edad: ")
    # print(f"Su nombre es: {nombreLocal}")
    return (nombreLocal, edadLocal) # digo que devuelve o que retorna

# nombreGlobal = input("Ingrese su nombre desde la funcion principal: ")
# while True:
#     # invocamos la funcion
#     nombre, edad = getNombre()
#     print(f"NombreGlobal: {nombre}, Edad {edad}")
#     if nombre == "fin":
#         break


# Ejercicio 1
# Generar una funcion que solicite (input) al usuario la base y la altura de un rectangulo
# y calcule su area y lo retorne (return)
# Luego desde la función principal imprimir el valor en pantalla

# declaramos la funcion
def getArea():
    base = int(input("Ingrese valor de la base: ")) # solicito la base
    altura = int(input("Ingrese valor de la altura: ")) # solicito la altura
    # calculo el area
    area = base * altura
    return area

# invocamos la funcion
# si la def de la funcion, tiene un return
# debo almacenar ese valor que devuelve en una funcion

areaGlobal = getArea()
print(f"El area calculada por la funcion getArea() es: {areaGlobal}")




# Ejercicio 2
# agregar validación a la función getNombre()