# Segunda parte del código procesamiento_e_s.py

# Paso 1: Ingreso del núnero 1
"""
numero_1 es el nombre de la variable
= operador de asignacion (reemplaza la flecha)
voy a pedir al usuario que ingrese el número con la funcion input()
la funcion input() siempre devuelve un str / texto / cadena de caracteres
convertir el tipo de dato, de cadena (str) a entero (int)
"""
numero_1_str = input("Ingrese el número 1: ")
print("El tipo de dato de numero_1_str es: ", type(numero_1_str))
numero_1 = int(numero_1_str) # convertimos str a int
print("El tipo de dato de numero_1 es: ", type(numero_1))


# Paso 2: definimos la operación suma

# Paso 3: Ingreso del número 2
numero_2_str = input("Ingrese el número 2: ")
numero_2 = int(numero_2_str)

# Paso 4: Procesar la suma
"""
declaramos la variable suma, que almacena la suma de los números
usamos el operador aritmetico + para sumar
asignamos la suma a la variable suma
"""
suma = numero_1 + numero_2

# Paso 5: Mostrar resultado
"""
Uso la funcion print()
dentro del parentesis pongo la variable
"""
print("El resultado es: ", suma)
