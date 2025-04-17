"""
Enunciado:

Solicite al cliente/a su nombre, apellido, edad y correo electrónico.
Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.
Muestre los datos por la terminal, en el orden que se ingresaron.
Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”

"""

# Solicitar los datos al usuario
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
correo = input("Por favor, ingrese su correo electrónico: ")

# **************************************************************
# Bloque de validación / muestramos en pantalla
print("\n" + "=" * 40)
print("        TARJETA DE PRESENTACIÓN")
print("=" * 40)

# Validamos los datos ingresados

# validacion del nombre
if nombre != "":  # condición nombre != ""
    # si ingreso un nombre No vacío imprimos el nombre
    print(f"Su nombre es {nombre}")
else:
    # si ingreso un nombre vacío imprimos ERROR
    print("Su nombre es: ERROR")

# validacion del apellido
if apellido != "":  # condición apellido != ""
    # si ingreso un apellido No vacío imprimos el apellido
    print(f"Su apellido es: {apellido}")
else:
    # si ingreso un apellido vacío imprimos ERROR
    print(f"Su apellido es: ERROR")

# Validación de la edad
# con la funcion int() convertimos el tipo de dato de str a int
edad = int(edad)
if edad >= 18:
    print(f"Su edad ingresada es: {edad}")
else:
    print("ERROR")

# Validacion del correo
if correo != "":  # condición correo != ""
    # si ingreso un correo No vacío imprimos el correo
    print(f"Su correo es: {correo}")
else:
    # si ingreso un correo vacío imprimos ERROR
    print(f"Su correo es: ERROR")


print("=" * 40)
# **************************************************************

