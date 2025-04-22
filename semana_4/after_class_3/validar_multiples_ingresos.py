nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# valido nombre y apellido usando el operador lógico and

if nombre != "" and apellido :
    print(f"Su nombre es: {nombre}")
    print(f"Su apellido es: {apellido}")
else:
    print("ERROR")

"""
Notar que en el caso del nombre usamos
la condición escrita de esta manera nombre != ""

Y en el caso del apellido
la condición escrita de esta otra manera apellido
"""
