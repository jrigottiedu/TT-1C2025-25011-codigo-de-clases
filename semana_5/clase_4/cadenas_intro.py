"""
Cadenas:

Las cadenas de texto, son una serie de caracteres
Cada caracter ocupa una posición dentro de la cadena
Esa posición que ocupa se llama índice
La cadena tiene una longitud
El primer índice es 0 y el último es longitud -1
Accedemos a cada caracter de la cadena usando el nombre de la variable y el índice entre []

"""
# variable con el nombre cadena que le asignamos un str o una serie de caracteres
cadena = "111codificar es crear"
print(cadena)

"""
Pensar...
1. el primer caracter es la c
2. el ultimo carcacter es la r
3. cual es el caracter que ocupa la posicion 5
"""

print(f"el primer caracter de la cadena es: {cadena[0]} ")
print(f"el segundo caracter de la cadena es: {cadena[1]} ")
print(f"la longitud de la cadena es: {len(cadena)} ")
print(f"el ultimo caracter de la cadena es: {cadena[len(cadena)-1]} ")
print(f"el ultimo caracter de la cadena es: {cadena[-1]} ")

for i in range(len(cadena)):
    print(f"Cadena [{i}] es {cadena[i]}")