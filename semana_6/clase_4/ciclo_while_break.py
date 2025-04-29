"""
En este archivo vamos a ver el uso del While con un contador para control de flujo
Agregamos un acumulador para actualizar los ingresos
Si el usuario ingresa un valor negativo, el break finaliza la ejecución del ciclo while

"""

# declaramos el contador
contador = 0
# declaramos e inicializamos el acumulador
acumulador = 0

while contador < 3 :
    numero = int(input("Ingrese un numero para acumular: "))

    if numero < 0: # evaluo si el numero ingresado es negativo
        print("El ciclo while se interrumpió por ingresar un valor negativo")
        break
    else:  #si es positivo acumulo
        acumulador = acumulador + numero # actualizo el acumulador

    contador = contador + 1 # incremento el contador

print(f"El valor acumulado fue {acumulador}") # al finalizar, imprimo el valor acumulado

