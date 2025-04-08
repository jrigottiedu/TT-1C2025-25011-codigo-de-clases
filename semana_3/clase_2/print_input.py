# Función print() para mostrar información en la terminal

# 1. nueva línea \n
# Se usa para hacer un salto de línea dentro del texto.
print("Hola\nMundo")  # Salida:
                      # Hola
                      # Mundo

# 2. tabulación \t
# Se usa para agregar una tabulación (espacio similar al de una tecla TAB).
print("Nombre:\tJuan")  # Salida: Nombre:    Juan

# 3. uso del end
# El argumento end permite cambiar el carácter que se usa al final del print (por defecto es \n).
print("Hola", end=" ")  # No hace salto de línea
print("Mundo")          # Salida: Hola Mundo

# 4. format f""
# Se usa para insertar variables dentro de un texto de forma clara y legible.
nombre = "Ana"
edad = 25
print(f"{nombre} tiene {edad} años")  # Salida: Ana tiene 25 años

# ------------------------------------------------------------

# Función input() para ingreso de datos desde
