"""
Slicing de cadena

En este archivo vemos 
"""

# Cadena base
cadena = "codificar es crear"
# Índices:   01234567890123456

# 1. Extraer los primeros 4 caracteres
print(cadena[0:2])  # "co" es una subcadena
print(cadena.replace("codi", "TODY"))

# 2. Extraer la palabra "es"
print(cadena[10:12])  # "es"

# 3. Extraer desde el índice 13 hasta el final
print(cadena[13:])  # "crear"

# 4. Extraer los últimos 6 caracteres
print(cadena[-6:])  # "crear"

# 5. Extraer la palabra "codificar"
print(cadena[0:9])  # "codificar"

# 6. Extraer desde el inicio hasta el espacio
print(cadena[:9])  # "codificar"

# 7. Extraer desde el espacio hasta el final
print(cadena[10:])  # "es crear"

# 8. Extraer cada 2 caracteres
print(cadena[::2])  # "cdfae ra"

# 9. Extraer la cadena al revés
print(cadena[::-1])  # "raerc se racifidoc"

# 10. Extraer la palabra "crear" al revés
print(cadena[-1:-6:-1])  # "raerc"
