"""
Enunciado:

Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
Validamos cada ingreso por separado:

Compruebe que el nombre no este vacío
Compruebe que el apellido no este vacío
Compruebe que la edad ingresada sea válidad (digitos) y que sea mayor de 18 años
Compruebe que el correo electrónico sea válido, que posea @ y .n.
Si alguno de los datos ingresados no cumple los requisitos, mostrar el texto “ERROR, + detalle”

"""

# Solicitar los datos al usuario
nombre = input("Por favor, ingrese su nombre: ").strip()
apellido = input("Por favor, ingrese su apellido: ").strip()
edad = input("Por favor, ingrese su edad: ").strip()
correo = input("Por favor, ingrese su correo electrónico: ").strip()

# **************************************************************
# Bloque de validación / muestra en pantalla
print("\n" + "=" * 40)
print("        TARJETA DE PRESENTACIÓN")
print("=" * 40)

"""
Validamos todos los datos ingresados utilizando combinación de :
1. combinación de condiciones
2. operadores relacionales
3. operadores lógicos

Introducimos mejoras a partir de o visto en clase
"""
if len(nombre) > 0:
    print(f"Su nombre es: {nombre.title()}")
else:
    print("ERROR, debe ingresar un nombre")

if len(apellido) > 0:
    print(f"Su apellido es: {apellido.title()}")
else:
    print("ERROR, debe ingresar un apellido")

if edad.isdigit():
    if int(edad) > 18:
        print(f"Su edad es: {edad}")
    else:
        print("ERROR, deber ser mayor de edad")
else:
    print("ERROR, debe ingresar una edad válida")

if len(correo) > 0 and correo.find("@") > 0 and correo.find(".") > 0:
    print(f"Su correo electronico es: {correo}")
else:
    print("ERROR, debe ingresar un correo válido")


print("=" * 40)
# **************************************************************
