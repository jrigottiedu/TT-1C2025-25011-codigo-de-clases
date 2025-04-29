"""
Hacemos un resumen de ciclos while

En Python, un Bucle while se usa para repetir la ejecución de un bloque de código
mientras se cumpla una condición.

- repetir acciones un número desconocido de veces (hasta que pase algo).
- para esperar que el usuario ingrese un dato correcto.
- para contar o acumular valores.
"""

# Ejemplo_1:
"""
Escribimos un Bucle While que se ejecute 5 veces
"""

# contador = 5
# while contador > 0:
#     print(f"El valor del contador es: {contador}")
#     contador = contador - 1 # contador -= 1

# Ejemplo_2:
"""
Escribimos un Bucle While que se ejecute la cantidad de veces que indique el usuario
"""

# # iteraciones = int(input("Ingrese la cantidad de veces a iterar: "))
# iteraciones = input("Ingrese la cantidad de veces a iterar: ")
# # agregar un bloque validador y luego convertir

# while iteraciones > 0:
#     print(f"Ejecución o iteración número: {iteraciones}")
#     iteraciones -= 1


# Ejemplo 3:
"""
Validar el ingreso de datos, solicitar el nombre del usuario hasta que ingrese un dato válido
"""

# nombre = ""
# while nombre == "":
#     nombre = input("Ingrese su nombre: ")
#     if nombre == "":
#         print("Debe ingresar un nombre válido")
# print(f"Nombre ingresado: {nombre}")


# Ejemplo 4:
"""
Solicitar al usuario que ingrese su edad y validar usando el método isdigit()
"""

# cadena = "55"
# print(cadena.isdigit())

# while True: # nos obliga a usar break
#     edad = input("Ingrese su edad: ")
#     if edad.isdigit():
#         print(f"Edad ingresada: {edad}")
#         break
#     else:
#         print("Debe ingresar una edad válida, intente nuevamente.")


# Ejemplo 5:
"""
Validar ingreso de contaseña con un máximo de 3 intentos
"""

# intentos = 0
# max_intentos = 3
# contraseña_sistema = "admin"

# while intentos < max_intentos:
#     contraseña= input("Ingrese su contraseña: ")
#     if contraseña == contraseña_sistema:
#         print("Bienvenido!")
#         break
#     else:
#         print("Contraseña incorrecta, intente nuevamente.")
#         intentos += 1
#     if intentos == max_intentos:
#         print("Máxima cantidad de intentos posibles alcanzados.")


# Ejemplo 6:
"""
Acumular los ingresos de las ventas de los primeros 3 meses del año
Ignorar ingresos negativos (continue)
"""

# contador = 0
# cantidad_meses = 3
# acumulador = 0
# while contador < cantidad_meses:
#     ingreso = int(input(f"Ingrese el ingreso del mes número {contador + 1}: "))
#     if ingreso < 0:
#         print("Ingreso no válido, intente nuevamente")
#         continue
#     acumulador += ingreso
#     contador += 1
# print(f"Ingreso acumulado es: {acumulador}")


# Ejemplo 7
"""
Al ejemplo 6, validar que el número ingresado sea dígito antes de convertirlo
"""
# contador = 0
# cantidad_meses = 3
# acumulador = 0
# while contador < cantidad_meses:
#     ingreso = input(f"Ingrese el ingreso del mes número {contador + 1}: ")
#     if not ingreso.isdigit():
#         print("Ingreso no válido, intente nuevament")
#         continue
#     ingreso = int(ingreso)
#     if ingreso < 0:
#         print("Ingreso no válido, intente nuevamente")
#         continue
#     acumulador += ingreso
#     contador += 1
# print(f"Ingreso acumulado es: {acumulador}")


# Ejemplo de listas
"""
Generar una lista con los primeros 3 meses del año y modificar el ejemplo 6, para que muestre el mes:
"""
# meses = ["Enero" , "Febrero", "Marzo"]

# contador = 0
# cantidad_meses = 3
# acumulador = 0
# while contador < cantidad_meses:
#     ingreso = int(input(f"Ingrese el ingreso del mes {meses[contador]}: "))
#     if ingreso < 0:
#         print("Ingreso no válido, intente nuevamente")
#         continue
#     acumulador += ingreso
#     contador += 1
# print(f"Ingreso acumulado es: {acumulador}")