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


# strip
print(f"La longitud de la cadena sin strip es {len(cadena)} y con strip es {len(cadena.strip())}")
print(f"La cadena con metodo strip es {cadena.strip()}")

# find - count
correo = "talentogmail@.com"
print(f"La cantidad de @ es {correo.count("@")}")
print(f"La posicion del @ en el correo es: {correo.find("@")}")

# isdigit (retorna True si corresponde a un número natural positivo)
numero = "22"
print(f"Evaluamos isdigit() en la variable numero {numero.isdigit()}")

