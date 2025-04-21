"""
Los operadores lógicos se usan para:
1. evaluar múltiples condiciones a la vez
2. tomar decisiones más complejas: (ejemplo: si es mayor de edad y tiene licencia)
"""


# Operadores lógicos en Python

edad = 19 # int
tiene_licencia = True # bool

# AND: ambas condiciones deben ser verdaderas
print("¿Tiene más de 18 años y licencia? ->", edad > 18 and tiene_licencia)  # True

# OR: al menos una condición debe ser verdadera
print("¿Tiene más de 18 años o licencia? ->", edad > 18 or tiene_licencia)  # True

# NOT: invierte el valor lógico
es_menor = edad < 18 # 15 < 18 True
print("¿NO es menor de edad? ->", not es_menor)  # False

# Ejemplo práctico con condiciones combinadas
usuario = "admin"
password = "1234"

# Verificamos si usuario y contraseña coinciden
login_correcto = (usuario == "admin") and (password == "1234")
print("¿Login correcto? ->", login_correcto)  # True
