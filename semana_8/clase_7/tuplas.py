# 1. Tupla numérica
numeros = (10, 20, 30, 40, 50)
print(numeros[0])  # Accede al primer elemento: 10


# 2. Meses del año
meses = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)
print(meses[4])  # mayo


# 3. Días de la semana
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print(dias[-1])  # domingo


# 4. Tupla representativa: datos personales inmutables
persona = ("Juan", "Pérez", 35, "Argentina")
nombre, apellido, edad, pais = persona

print(f"{nombre} tiene {edad} años y vive en {pais}.")


"""
¿Por qué usar tuplas?

a. No se pueden modificar (inmutables)
b. Ocupan menos memoria que listas
c. Se pueden usar como claves en diccionarios
"""