# Enunciado

"""
Parte A:
Solicitar al usuario que ingrese:
nombre, apellido, correo y edad
Notas:
1. no se admiten valores en blanco o vacios
2. el correo debe contener 1 @ y al menos 1 punto
3. clasificar rango etario <15 niño/a, <18 adolescente, >=18 adulto

Parte B:
Registrar los ingresos mensuales de una cliente durante 6 meses.
Usá un bucle while para solicitar el ingreso de cada mes.

Validar que los ingresos sean números positivos.
Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.
Calcular el ingreso total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

"""


# *****************
# Parte B - Registrar ingresos mensuales
# *****************

# declaración de variables
cantidad_meses = 6  # valor constante constante
contador = 0
acumulador = 0  # inicializando el acumulador de sueldos mensuales
# declaramos una variable tipo lista con los meses
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio"]

# operación o procesamiento
while contador < cantidad_meses:

    # Solicito al usuario que ingrese el sueldo del mes (usamos contador como índice de la lista)
    sueldo = input(f"Ingrese el sueldo del mes {lista_meses[contador]}: ")

    # validamos que sea digito natural positivo antes de convertirlo a int
    if sueldo.isdigit():
        sueldo = int(sueldo)
    else:
        print("Ingreso inválido, intente nuevamente.")
        continue

    # Código sugerido por IA para resolver validación de ingreso de datos float o decimal
    # try:
    #     sueldo = float(sueldo)
    # except ValueError:
    #     print("Ingreso inválido, intente nuevamente.")
    #     continue

    acumulador += sueldo  # equivalente a acumulador = acumulador + sueldo
    contador = contador + 1  # equivalente a contador += 1

print(f"El valor acumulado es de: {acumulador}")


# *****************
# Parte A - Solicitar ingreso de datos
# *****************
"""
Ver el archivo validar_ingresos.py con opciones de bloques de validación
"""

# Ingreso de nombre
while True:
    nombre = input("Ingrese su nombre: ").strip()
    if nombre == "":
        print("No se admite vacio")
    else:
        break
print(f"Su nombre es: {nombre}")

# Ingreso de apellido
while True:
    apellido = input("Ingrese su apellido: ").strip()
    if not apellido:
        print("el apellido no puede estar vacio")
    else:
        break

# Ingreso de la edad

while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():  # edad.isdigit() retorna True si el numerico
        edad = int(edad)  # convierto a int
        break
    else:
        print("Ingrese una edad válida")
        continue  # retorno a la condición del while

# Comentario: isdigit() valida que sea número natural y positivo


# Ingreso de correo electrónico
while True:
    correo = input("Ingres su email: ").strip()
    # correo.count("@") != 1: # count retorna la cantidad de coincidencias
    # correo.find(".") == -1: # find() retorna el índice del caracter y -1 si no lo encuentra

    if correo.count("@") != 1 or correo.find(".") == -1:
        print(
            "Correo inválido, debe contener un @ y al menos un punto. Intente nuevamente..."
        )
        continue
    else:
        break

# Ahora que los datos fueron validados mostramos en pantalla:
print(f"Nombre ingresado: {nombre}")
print(f"Apellido ingresado: {nombre}")
match edad:
    case edad if edad < 15:
        print(f"Edad ingresada: {edad } - Categoría: Niño/a")
    case edad if edad < 18:
        print(f"Edad ingresada: {edad } - Categoría: Adolescente")
    case _:
        print(f"Edad ingresada: {edad } - Categoría: Adulto/a")
print(f"Correo ingresado: {correo}")
