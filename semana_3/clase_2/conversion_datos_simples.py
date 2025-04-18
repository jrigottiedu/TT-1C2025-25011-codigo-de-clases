"""
Conversión de tipo de datos

1. de int a float
2. de float a int
3. de int a str
4. de str a int
5. de bool a int
6. de int a bool

"""

# 1. int to float
numero_entero = int(input("Ingresa un número entero: "))
numero_decimal = float(numero_entero)
print(f"El número {numero_entero} convertido a float es: {numero_decimal}")


# 2. float to int
numero_float = float(input("Ingresa un número decimal: "))
numero_entero = int(numero_float)
print(f"El número {numero_float} convertido a entero es: {numero_entero}")


# 3. int to str
numero_como_cadena = str(42)
print("Número como cadena:", numero_como_cadena)
print("Tipo:", type(numero_como_cadena))

# 4. str to int
cadena = "123"
numero_desde_cadena = int(cadena)
print("Número desde cadena:", numero_desde_cadena)
print("Tipo:", type(numero_desde_cadena))

# 5. bool to int
valor_booleano = True
numero_desde_booleano = int(valor_booleano)
print("Número desde booleano:", numero_desde_booleano)

# 6. int to bool
numero = 0
valor_booleano_desde_entero = bool(numero)
print("Booleano desde entero (0):", valor_booleano_desde_entero)

numero = 7
valor_booleano_desde_entero = bool(numero)
print("Booleano desde entero (7):", valor_booleano_desde_entero)
