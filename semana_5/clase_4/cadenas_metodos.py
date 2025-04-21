
"""
Métodos de cadenas

Las cadenas en Python son objetos, y como se verá mas adelante, los objetos poseen (atributos y métodos)
Por ello es que las cadenas de texto poseen estos método o funciones que podemos usar
"""

# Cadena base con espacios
cadena = "  aprender python es divertido  "

# 1. .upper() → Convierte todo a MAYÚSCULAS
print(cadena.upper())  # "  APRENDER PYTHON ES DIVERTIDO  "

# 2. .lower() → Convierte todo a minúsculas
print(cadena.lower())  # "  aprender python es divertido  "

# 3. .title() → Pone la primera letra de cada palabra en mayúscula
print(cadena.title())  # "  Aprender Python Es Divertido  "

# 4. .capitalize() → Convierte solo la primera letra de la cadena en mayúscula, y el resto en minúsculas.
print(cadena.capitalize())  # "  Aprender python es divertido  "

# 5. .strip() → Elimina espacios en blanco al inicio y final
print(cadena.strip())  # "aprender python es divertido"

# 6. .replace() → Reemplaza partes de la cadena
print(cadena.replace("divertido", "fácil"))  # "  aprender python es fácil  "

# 7. .startswith() → ¿La cadena comienza con cierto texto?
print(cadena.strip().startswith("aprender"))  # True

# 8. .endswith() → ¿La cadena termina con cierto texto?
print(cadena.strip().endswith("divertido"))  # True

# 9. .find() → Devuelve la posición de un texto (o -1 si no lo encuentra)
print(cadena.find("python"))  # 11 (posición donde comienza "python")

# 10. .isdigit() → ¿La cadena contiene SOLO dígitos?
edad = "25"
print(edad.isdigit())  # True

texto = "25años"
print(texto.isdigit())  # False
