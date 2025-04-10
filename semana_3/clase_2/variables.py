# VARIABLES EN PYTHON

# Las variables son contenedores, cajas, que almacenan datos temporales

"""
Tipos de datos simples
1. texto o cadena de caracteres => str o string
2. enteros => int integer
3. con coma decimal => float coma flotante
4. booleanos => bool (true/false)
"""

# Ejemplos de variables con distintos tipos de datos
nombre = 'Juan'        # string
edad = 30              # int
altura = 1.75          # float
es_mayor = True        # bool

# Tipado dinámico
# Python no necesita declarar el tipo de variable, lo detecta automáticamente
x = 10          # x es un entero
x = "diez"      # ahora x es un string

# Asignación simple
mensaje = "Hola mundo"
print(mensaje)

# Asignación múltiple
a = 1
b = 2
c = 3
a, b, c = 1, "2", True
print(a, b, c)   # Imprime: 1 2 3

# También se puede asignar el mismo valor a varias variables
x = y = z = 0
print(x, y, z)   # Imprime: 0 0 0

# Incrementar valor
contador = 5
contador = contador + 1   # tradicional
print(contador)           # Imprime: 6

contador += 1             # forma abreviada
print(contador)           # Imprime: 7

"""
Nombres de las variables:
1. letras, números y guiones bajos. Deben comenzar con letra o guion bajo
2. no se pueden usar palabras reservadas
3. sensible a mayúsculas

Buenas prácticas:
- camelCase: nombreDeVariable
- snake_case: nombre_de_variable  ✅ Recomendado en Python
"""

# Ejemplos válidos
_nombre = "Ana"
nombre1 = "Luis"
nombre_completo = "Ana García"

# Ejemplo inválido (no ejecutar):
# 1nombre = "Pedro"  ❌ comienza con número

# Ejemplo sensible a mayúsculas
edad = 25
Edad = 30
print(edad)   # 25
print(Edad)   # 30

"""
Función type para retornar el tipo de dato de una variable
"""
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hola"))    # <class 'str'>
print(type(True))      # <class 'bool'>
