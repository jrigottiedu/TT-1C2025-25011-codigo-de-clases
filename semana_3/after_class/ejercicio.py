"""
Solicite a la clienta o cliente su nombre, apellido, edad y correo electrónico.
Almacene estos datos en variables.
Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
"""

# Solicitar los datos al usuario
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
correo = input("Por favor, ingrese su correo electrónico: ")


# Mostrar los datos en forma de tarjeta de presentación
print("\n" + "="*40)
print("        TARJETA DE PRESENTACIÓN")
print("="*40)
print(f"Nombre completo: {nombre} {apellido}")
print(f"Edad: {edad} años")
print(f"Correo electrónico: {correo}")
print("="*40)