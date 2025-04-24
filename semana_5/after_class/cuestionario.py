"""
Resolvemos el cuestionario 2 de la clase 4
"""

# Pregunta 
"""
Observá este programa. ¿Qué mostrará si se ingresa "Lunes"?
"""

dia = input("Ingresá un día de la semana: ")
match dia:
    case "Lunes":
        print("Inicio de semana.")
    case "Viernes":
        print("Fin de semana.")
    case _:
        print("Día intermedio.")

# Análisis
"""
Usamos la estructura match para evaluar la variable dia
Cada cade compara un valor específico, pero recuerden que Python es sensible a las mayúsculas
También debemos tener en cuenta los espacios

Una versión mejorada del código podría ser
match dia:
    case dia if dia.strip.lower() == "lunes":
        print("Inicio de semana.")
"""

# Pregunta
"""
Observá el siguiente código. 
¿Qué mensaje se imprime si el ingreso mensual es 60000 y la edad es 25?
"""
ingreso = 60000
edad = 25
if ingreso < 50000:
    print("Ingresos bajos.")
elif edad < 30:
    print("Joven con buenos ingresos.")
else:
    print("Adulto con buenos ingresos.")

# Análisis
"""
el primer if evalúa el ingreso, sin importar la edad
miestras que el segundo evalúa la edad, ya sabiendo que el ingreso es mayor a 50000
"""

# Pregunta
"""
¿Qué sucede si intentás modificar un carácter específico en una cadena en Python?
"""
texto = "Hola"
texto[0] = "J"

# Análisis
"""
En Python, las variables cadena o str son inmutables
Este concepto significa que no podemos modificar su valor,
por lo tanto no podemos cambiar el caracter de la posición 0
Este código da error

NOTA: no es lo mismo que esto:
texto = "Hola"
texto = "Chau"

en este caso, si bien el nombre de la variable es el mismo,
para Python la segunda variable texto apunta a otra posición de memoria,
esto si es posible.
Pero cuando hago 
texto[0]="J"
estoy intentando cambiar el caracter de la posición 0 de la misma posición de memoria
y eso no es posible, por el cocepto de inmutabilidad.

Para recordar:
cadenas => son inmutables, esto es, no soporta text[0]="J"
lista => son mutables, ya lo vamos a ver en breve
"""

# Pregunta
"""
Observá este código. ¿Cuál es el resultado?
"""

texto = "Python"
if "P" in texto and texto.endswith("on"):
    print("Condición cumplida.")
else:
    print("Condición no cumplida.")

# Análisis
"""
Esta es una estructura nueva:
if "P" in texto:

lo que hace es evaluar si la variable texto contiene un caracter "P" 

Tener en cuenta mayúsculas/minúsculas
Una versión mejorada podría ser:

if "p" in texto.lower() :
    print("Condición cumplida.")

Por otra parte, texto.endswith("on") es un método que retorna
True o False, si la cadena texto termina con "on"
"""

# Pregunta
"""
¿Cuál es la longitud de la siguiente cadena?
"""

texto = "¡Hola, Python!"
print(len(texto))

# Análisis
"""
Es importante diferenciar funciones de métodos

Los métodos son propiedades de algunos tipos de datos, por ejemplo
texto = "Python"
texto.lower()
texto.title()

Las funciones, reciben un argumento entre (), por ejemplo
numero = "25"
int(numero) => convierte 25 str a int

en este caso, len() es una función, que recibe una cadena y retorna la cantidad de caracteres que posee
cadena1 = "Python"
len(cadena1) => retorna 6

Nota: cuidado con los espacios
cadena2 = "  Python  "
len(cadena) => retorna 10
"""

# Pregunta
"""
¿Cuál es la salida del siguiente código?
"""

texto = "  Python  "
print(texto.strip().upper())

# Análisis
"""
En este caso, vemos 2 métodos anidados,
primero se aplica el método strip() que elimina los espacios al inicio y fin de la cadena
a ese resultado se le aplica el método upper() que convierte todos los caracteres a mayúscula
"""