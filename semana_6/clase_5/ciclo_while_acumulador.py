"""
En este archivo vamos a ver el uso del While con un contador para control de flujo
y agregamos un acumulador para actualizar los ingresos
"""

# declaramos el contador
contador = 0
# declaramos e inicializamos el acumulador
acumulador = 0

# declaramos un ciclo while que se ejecuta mientras el contador es menor a 2
# como el contador se inicializa en 0 y se incrementa de 1 en 1
# entonces se ejecuta 2 veces
while contador < 2 :
    numero = int(input("Ingrese un numero para acumular: "))
    acumulador = acumulador + numero # actualizo el acumulador
    contador = contador + 1 # incremento el contador

print(f"El valor acumulado fue {acumulador}") # al finalizar, imprimo el valor acumulado
