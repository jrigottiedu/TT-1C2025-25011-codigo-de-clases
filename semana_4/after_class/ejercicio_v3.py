"""
Enunciado:

Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
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
# Bloque de validación / muestra en pantalla
print("\n" + "=" * 40)
print("        TARJETA DE PRESENTACIÓN")
print("=" * 40)

"""
Validamos todos los datos ingresados utilizando combinación de :
1. combinación de condiciones
2. operadores relacionales
3. operadores lógicos
"""

if nombre == "" or apellido == "" or edad == "" or int(edad) <= 18 or correo == "":
    print("ERROR")
else:
    print(f"Su nombre es: {nombre}")
    print(f"Su apellido es: {apellido}")
    print(f"Su edad es: {edad}")
    print(f"Su correo electronico es: {correo}")

print("=" * 40)
# **************************************************************
