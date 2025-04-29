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

# versión incrementado el contador
contador = 0
while contador < 5:
    print(f"El valor del contador es: {contador}")
    contador = contador + 1 # contador += 1

# versión decrementando el contador
contador = 5
while contador > 0:
    print(f"El valor del contador es: {contador}")
    contador = contador - 1 # contador -= 1

# Ejemplo_2:
"""
Escribimos un Bucle While que se ejecute la cantidad de veces que indique el usuario
"""

# Aquí también usamos el contador de forma decremental
iteraciones = int(input("Ingrese la cantidad de veces a iterar: "))

while iteraciones > 0:
    print(f"Ejecución o iteración número: {iteraciones}")
    iteraciones -= 1


# Ejemplo 3:
"""
Validar el ingreso de datos, solicitar el nombre del usuario hasta que ingrese un dato válido
"""

nombre = ""
while nombre == "":
    nombre = input("Ingrese su nombre: ")
    if nombre == "":
        print("Debe ingresar un nombre válido")
print(f"Nombre ingresado: {nombre}")


# Ejemplo 4:
"""
Solicitar al usuario que ingrese su edad y validar usando el método isdigit()
"""

# Recordamos el uso del método isdigit() con las cadenas
# cadena = "Python"
# print(cadena.isdigit()) # Imprime False
# cadena = "55"
# print(cadena.isdigit()) # Imprime True

while True: # nos obliga a usar break para evitar loops infinitos
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        print(f"Edad ingresada: {edad}")
        break # interrumple el flujo normal del while
    else:
        print("Debe ingresar una edad válida, intente nuevamente.")


# Ejemplo 5:
"""
Validar ingreso de contaseña con un máximo de 3 intentos
"""

intentos = 0 # contador de intentos de ingreso de contraseña
max_intentos = 3 # determino la cantidad de intentos permitidos
contraseña_sistema = "admin" # defino una contraseña de acceso

while intentos < max_intentos:
    contraseña= input("Ingrese su contraseña: ")
    if contraseña == contraseña_sistema:
        print("Bienvenido!")
        break # si la contraseña ingresa es correcta, el ciclo se interrumpe
    else:
        print("Contraseña incorrecta, intente nuevamente.")
        intentos += 1
    if intentos == max_intentos:
        print("Máxima cantidad de intentos posibles alcanzados.")

# Luego de 3 intentos fallidos de ingreso, el bucle while se termina por la condición
# Si se ingresa la contaseña correcta en algunos de esos 3 intentos, el bucle finaliza con break

# Ejemplo 6:
"""
Acumular los ingresos de las ventas de los primeros 3 meses del año
Ignorar ingresos negativos (continue)
"""

contador = 0
cantidad_meses = 3 # esta variable hace las veces de una constante
acumulador = 0
while contador < cantidad_meses:
    ingreso = int(input(f"Ingrese el ingreso del mes número {contador + 1}: "))
    if ingreso < 0:
        print("Ingreso no válido, intente nuevamente")
        continue # el continue omite el código que sigue y salta a la condición del while
    # si el ingreso es 0 o mayor que 0, continúa el flujo normal
    acumulador += ingreso
    contador += 1
print(f"Ingreso acumulado es: {acumulador}")


# Ejemplo 7
"""
Al ejemplo 6, validar que el número ingresado sea dígito antes de convertirlo
"""
contador = 0
cantidad_meses = 3
acumulador = 0
while contador < cantidad_meses:
    ingreso = input(f"Ingrese el ingreso del mes número {contador + 1}: ")
    
    # agregamos este condicional para validar que el str ingresado sea numerico
    if not ingreso.isdigit():
        print("Ingreso no válido, intente nuevament")
        continue

    # si es numerico, el programa sigue el flujo normal y conviernte a int
    ingreso = int(ingreso)
    
    # al igual que antes, valido si hay un ingreso negativo
    if ingreso < 0:
        print("Ingreso no válido, intente nuevamente")
        continue

    # si los ingresos fueron correcto, actualizo el acumulador e incremento el contador
    acumulador += ingreso
    contador += 1
print(f"Ingreso acumulado es: {acumulador}")


# Ejemplo de listas
"""
Generar una lista con los primeros 3 meses del año y modificar el ejemplo 6, para que muestre el mes:
"""
# declaramos e inicializamos una lista con los primeros 3 meses del año
meses = ["Enero" , "Febrero", "Marzo"]
# print(meses[0]) # retorna Enero
# print(meses[1]) # retorna Febrero

contador = 0
cantidad_meses = 3
acumulador = 0
while contador < cantidad_meses:
    # actualizamos esta linea, de manera de usar la lista y contador como índice
    ingreso = int(input(f"Ingrese el ingreso del mes {meses[contador]}: "))
    if ingreso < 0:
        print("Ingreso no válido, intente nuevamente")
        continue
    acumulador += ingreso
    contador += 1
print(f"Ingreso acumulado es: {acumulador}")