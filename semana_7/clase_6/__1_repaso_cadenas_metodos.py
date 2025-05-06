# Repasar y completar cadenas y métodos

"""
Asumimos que ya se ha consolidado:
1. variables (espacios de memoria para almacenar datos temporarios) y tipos de datos (int, float, str, bool, list)
2. operadores aritméticos (+, -, *, /), relacionales (>, <, !=, ==) y lógicos (and, or, not)
4. condicionales if-elif-else
5. condicionales match
"""

# Declaración de una cadena
cadena = "  Python  "

# Longitud de una cadena
print(f"Longitud de la cadena {len(cadena)}")

# Elementos, posición e índices en las cadenas (clase 4 - cadenas_intro.py)
indice = 3
print(f"Elemento {cadena[indice]} esta en la posicion {indice}")

# Métodos de cadenas (clase 4 - cadenas_metodos.py)
# upper y lower
print(f"La cadena en mayuscula es {cadena.upper()}")
print(f"La cadena en lower es {cadena.lower()}")


# strip - fundamental para eliminar espacios en blanco al inicio y final de la cadena
print(f"La longitud de la cadena sin strip es {len(cadena)} y con strip es {len(cadena.strip())}")
print(f"La cadena con metodo strip es {cadena.strip()}")

# find - retorna la posición de un elemento en la cadena. Si no lo encuentra retorna -1
# nota: solo retorna la primer coincidencia
correo = "talento@gmail.com"
print(f"La posicion del @ en el correo es: {correo.find("@")}") # retorna 7

correo = "talento@gmail@.com"
print(f"La posicion del @ en el correo es: {correo.find("@")}") # retorna 7, aunque hay otro @ en la posición 12



# count - retorna la cantidad de elementos encontrados
correo = "talentogmail@.com"
print(f"La cantidad de @ es {correo.count("@")}") # retorna 1
correo = "talentogmail@.com@"
print(f"La cantidad de @ es {correo.count("@")}") # retorna 2


# isdigit (retorna True si corresponde a un número natural positivo)
numero = "22"
print(f"Evaluamos isdigit() en la variable numero {numero.isdigit()}")
# nota: para el valor "22,5", "-22", retorna falso

