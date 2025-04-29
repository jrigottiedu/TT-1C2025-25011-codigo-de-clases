"""
En este archivo vamos a ver el uso del While con un contador para control de flujo
Agregamos un acumulador para actualizar los ingresos
Si el usuario ingresa un valor negativo, usamos el continue para que no procese ese valor
El continue retorna la ejecución al inicio del While, donde está la condición
"""

# declaramos el contador
contador = 0
# declaramos e inicializamos el acumulador
acumulador = 0

while contador < 3 :
    # contador = contador + 1 # incremento el contador
    numero = int(input("Ingrese un numero para acumular: "))

    if numero < 0: # evaluo si el numero ingresado es negativo
        print("El ciclo while encontró un valor negativo")
        continue
    else:  #si es positivo acumulo
        acumulador = acumulador + numero # actualizo el acumulador

    contador = contador + 1 # incremento el contador

print(f"El valor acumulado fue {acumulador}") # al finalizar, imprimo el valor acumulado
