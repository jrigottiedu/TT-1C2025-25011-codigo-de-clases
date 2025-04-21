"""
Los operadores relacionales en programación se usan para comparar valores. 
El resultado de esa comparación siempre es verdadero (true) o falso (false). 
Sirven principalmente para tomar decisiones dentro del código.
"""

# Operadores relacionales en Python

a = 10
b = 20

print("a =", a)
print("b =", b)

# Igualdad
print("¿a es igual a b? ->", a == b)  # False

# Desigualdad
print("¿a es distinto de b? ->", a != b)  # True

# Mayor que
print("¿a es mayor que b? ->", a > b)  # False

# Menor que
print("¿a es menor que b? ->", a < b)  # True

# Mayor o igual que
print("¿a es mayor o igual que b? ->", a >= b)  # False

# Menor o igual que
print("¿a es menor o igual que b? ->", a <= b)  # True

# Extra: comparación con strings
nombre1 = "Ana"
nombre2 = "Juan"
print("¿Ana es igual a Juan? ->", nombre1 == nombre2)  # False
print("¿Ana viene antes que Juan alfabéticamente? ->", nombre1 < nombre2)  # True
