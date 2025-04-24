"""
Formatee correctamente los textos ingresados en “apellido” y “nombre”,
 convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.

Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

Que clasifique a los y las clientes por rango etario basándose en su edad
(“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)
"""

# Declaración de variables
nombre = ""
apellido = ""
correo = ""
edad = ""

# ingreso de datos
"""
Aqui usamos el método strip() para eliminar espacios al inicio y fin de la cadena
Esto nos va a ahorrar potenciales errores luego
"""
nombre = input("ingrese fu nombre:").strip()
apellido = input("ingrese su apellido:").strip()
correo = input(" ingrese su correo:").strip()
edad = input("ingrese su edad:").strip()

print("\n" + "=" * 40)
print("        TARJETA DE PRESENTACIÓN")
print("=" * 40)


# poner en mayuscua a primer letra de nombre y el apellido y que no este vacio ninguno
"""
Usamos el método title() que convierte en mayúsculas el primer caracter de cada palabra
"""
if nombre != "" and apellido != "":
    print(f"su Nombre y Apellido: {nombre.title()} {apellido.title()}")
else:
    print("ingrese sus datos")

# Clasificamos la edad
"""
Agregamos un bloque de validacion con isdigit()
isdigit evalua que los caracteres de la cadena sean numericos,
en ese caso retorna True, de lo contrario retorna false.

Por ejemplo:
edad1 = "25"
edad1.isdigit() => retorna True

edad2 = "25años"
edad2.isdigit() => retorna False
"""
if edad.isdigit() == True:  # tambien se puede escribir if edad.isdigit():
    edad = int(edad)  # ahora que se que es dígito, lo convierto a int

    # definir rango etario y que la edad no este vacia
    if edad < 0:
        print("Ingrese una edad válida mayor a 0")
    elif edad <= 15:
        print(f"su edad es: {edad} años, niño/a")
    elif edad <= 18:
        print(f"su edad es: {edad} años, adolecente")
    else:
        print(f"su edad es: {edad} años, adulto/a")
else: 
    print("Debe ingresar una edad valida numerica")


# Vaidación del correo
"""
1. Validamos que el correo no este en blanco, usamos algunas de estas condiciones
if correo != "":
if correo:
if len(correo) > 0


2. Validamos que el correo contenga @, usamos algunas de estas condiciones
if "@" in correo
if correo.count("@") == 1 

3. Validamos que el correo no contenga espacio
como aplicamos strip() al momento de la asignación, sabemos que no hay espacios ni al inicio ni al final
pero puede haber espacios dentro de la cadena
por eso usamos count(" ") para contar los espacios interiores,
si no hay espacios interiore, retorna 0
Usamos la condición
if correo.count(" ") == 0
"""
if correo != "" and correo.count("@") == 1 and correo.count(" ") == 0:
    print(f"su correo es :{correo}")
else:
    print("error")

print("=" * 40)
