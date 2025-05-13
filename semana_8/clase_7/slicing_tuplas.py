dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

# 1. Días laborales
print(dias[:5])
# ('lunes', 'martes', 'miércoles', 'jueves', 'viernes')


# 2. Fin de semana
print(dias[-2:])
# ('sábado', 'domingo')


# 3. Días alternos
print(dias[::2])
# ('lunes', 'miércoles', 'viernes', 'domingo')


# 4. Invertir el orden
print(dias[::-1])
# ('domingo', 'sábado', 'viernes', 'jueves', 'miércoles', 'martes', 'lunes')
