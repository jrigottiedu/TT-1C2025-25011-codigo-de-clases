# Ejemplo 1: validar ingreso de dato tipo cadeno no vacio

nombre = ""
while nombre == "":
    nombre = input("Ingrese su nombre: ").strip()
    if nombre == "":
        print("Debe ingresar un nombre válido")
print(f"Nombre ingresado: {nombre}")


# Ejemplo 2: validar ingreso de dato tipo cadeno no vacio

while True:
    nombre = input("Ingrese su nombre:")
    if not nombre.strip():
        print("el nombre no puede estar vacio")
    else:
        break


# Ejemplo 3: validar ingreso de dato tipo cadeno no vacio

while True:
    nombre = input("Ingrese su nombre: ").strip()
    if nombre == "":
        print("No se admite vacio")
    else:
        break
print(f"Su nombre es: {nombre}")

# Ejemplo 4: validamos ingreso de datos numericos NO decimales
while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        edad = int(edad)
    else:
        print("Ingrese una edad válida")
        continue