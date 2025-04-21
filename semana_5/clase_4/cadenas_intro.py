"""
Cadenas:

Las cadenas de texto, son una serie de caracteres
Cada caracter ocupa una posición dentro de la cadena
Esa posición que ocupa se llama índice
La cadena tiene una longitud
El primer índice es 0 y el último es longitud -1
Accedemos a cada caracter de la cadena usando el nombre de la variable y el índice entre []

"""

# declaramos e inicializamos una variable
cadena = "codificar es crear"

print(f"El contenido de cadena es {cadena} y su longitud es {len(cadena)}")
# len(cadena) nos devuelve la longitud de la cadena

"""
Para pensar:
1. cual es el primer caracter de la cadena? c
2. cual es el último caracter de la cadena? r
3. cual es el caracter de la posición 5? f
"""

print(f"El primer caracter de cadena es {cadena[0]}")
print(f"El último caracter de cadena es {cadena[-1]}")
print(f"El caracter de la posición 5 es {cadena[4]}")

for i in range(len(cadena)):
    print(f"Cadena [{i}] es {cadena[i]}")


