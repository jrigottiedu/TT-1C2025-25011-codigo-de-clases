# Funciones con argumentos (con parámetros) sin retorno

"""
Son funciones que si esperan uno o más dato/s (parámetro/s o argumento/s) y no retornan ningún dato

Ejemplo:
1. Una función que da un mensaje de bienvenida personalizado
2. Una función que calula el área de un rectángulo, debe recibir la base y la altura
"""

# ***************************************************************
# Función que espera un solo dato (un argumento)
# de un mensaje personalizado


# Declaración de la función
def mensajePersonalizado(nombreEstudiante):
    print(f"Hola {nombreEstudiante}, bienvenido/a a mi App")


# Invocación o llamada de la función

# En este caso le pasamos el argumento literal "Cata"
mensajePersonalizado("Cata")

# En este caso le pasamos el argumento literal "Mariela"
mensajePersonalizado("Mariela")

# En este otro caso le pasamos a la función como argumento la variable nombre
nombre = "Nestor"
mensajePersonalizado(nombre)

# En este último caso, anidamos el input pero "DEBE" incluir la variable
nombre = input("Ingrese su nombre")
mensajePersonalizado(nombre = input("Ingrese su nombre"))


# ------------------------------------------------
# Ejercicio de clase (3 minutos)
"""
Generar una función que reciba un argumento, la edad de una persona 
y lo informe en pantalla
"""
# Resolución

# Declaración de la funcion
def edadPrint(edad):
    print(f"Su edad es:{edad}")

# Ingreso por consola el valor de la edad
ingresoEdad = input("Ingrese su edad:")

# Invocacion o llamado, paso como argumento la variable ingresoEdad
edadPrint(ingresoEdad)


# ***************************************************************
# Función que espera más de un dato (más de un argumento)
# del cálculo del área de un rectángulo (Tomado de la PPT clase 9)

# Declaramos la función que calcula el área de un rectángulo
# a partir de los datos "base" y "altura" (parámetros de la función)
# que recibe como argumentos

def areaRectangulo(base, altura): # parámetro 1: base, parámetro 2: altura
    area = base * altura
    print(f"El área es {area}")

# invocamos a la funcion

# En este caso pasamos los argumentos por posición
areaRectangulo(5, 2)
# tener el cuenta que el 5 corresponde a la base
# y el 2 a la altura, por el orden en que aparece en la función

# Y en este otro caso pasamos los argumentos nombrados
areaRectangulo(base=5, altura=2)
# aquí no importa el orden, porque se indica explicitamente a que parámetro corresponde cada valor


# ------------------------------------------------
# Ejercicio de clase (3 minutos)
"""
Generar una función que reciba dos argumentos, el nombre y la edad de una persona
y lo informe en pantalla
"""

# Resolución
def mostrarDatos(nombre, edad=20): # por default edad = 20
    print(f"Su nombre es: {nombre} y tiene {edad} años")

# Inicializamos las variables, o las inicializa el usuario con el input
varEdad = 25  # int(input("Ingrese su edad: "))
varNombre = "Ana"  # input("Ingrese su nombre: ")

# Invocamos a la función por posición:
mostrarDatos(varNombre,varEdad) # Argumento varNombre => parámetro nombre y argumento varEdad => parámetro edad

# Invocamos a la función por nombre:
mostrarDatos(nombre=varNombre, edad=varEdad)

# como en la función, edad tiene un valor por defecto, que es 20 puedo no pasarlo
mostrarDatos(nombre=varNombre)

# Cuidado, si invoco a la función, pero no paso el argumento nombre, da error!
mostrarDatos(edad=varEdad)


# Como referencia, recordemos la función range que usamos en el for

# Si le paso a range solo 1 argumento, ese corresponderá al valor final, por que los otros están por defecto
for i in range(10): # valor inicial=1 (default), valor final=10, incremento=1 (default)
    print(i)

# Si en cambio, le paso los 3 argumentos, ahora toman estos valores:    
for i in range(2,10,3): # valor inicial=2, valor final=10, incremento=3
    print(i)



# ------------------------------------------------
# Ejercicio de tarea
"""
Dada una lista sencilla de un producto

producto = ["manzana", "fruta", 1200]

Realizar una función que muestre en pantalla los 3 datos de nuestro producto

"""

# Resolución
"""
???
"""
