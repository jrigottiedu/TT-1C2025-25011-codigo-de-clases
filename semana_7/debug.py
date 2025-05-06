# Codigo de muestra para usar el Debug

# declaramos e inicializamos una lista con instrumentos musicales
instrumentos = ["guitarra", "piano", "flauta", "trompeta", "acordión"]

# declaramos e inicializamos un indice
indice = 0

# obtenemos la longitud de la lista instrumentos
longitud_instrumentos = len(instrumentos)

while indice < longitud_instrumentos:
    print(f"El elemento {instrumentos[indice]} se encuentra en la posición {indice}")
    indice += 1
