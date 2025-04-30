# Enunciado

"""
Parte A:
Solicitar al usuario que ingrese:
nombre, apellido, correo y edad
Notas:
1. no se admiten valores en blanco o vacios
2. el correo debe contener 1 @ y al menos 1 punto
3. clasificar rango etario <15 niño/a, <18 adolescente, >=18 adulto

Parte B:
Registrar los ingresos mensuales de una cliente durante 6 meses.
Usá un bucle while para solicitar el ingreso de cada mes.

Validar que los ingresos sean números positivos.
Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.
Calcular el ingreso total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

"""

# declaracion de variables
cantidad_meses = 3  # declarar una constante
contador = 0
acumulador = 0  # inicializando el acumulador de sueldos mensuales
lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio"]

# operacion o procesamiento
while contador < cantidad_meses:

    sueldo = input(f"Ingrese el sueldo del mes {lista_meses[contador]}: ")

    # queremos validar que el ingreso no este vacio o en blanco
    if sueldo == "": 
        print("No se admite vacío, debe ingresar un valor.")
        continue
    else:
        sueldo = float(sueldo)

    if sueldo.isdigit():
        #True
        sueldo = int(sueldo)
    else:
        #False
        print("Ingreso inválido, intente nuevamente.")
        continue

    # try:
    #     sueldo = float(sueldo)
    # except ValueError:
    #     print("Ingreso inválido, intente nuevamente.")
    #     continue

    # validamos que el sueldo sea positivo (en realidad lo valida isdigit, se puede remover)
    if sueldo < 0: # preguntamos si el sueldo es negativo
        print("ERROR! No se admiten valores negativos.")
        continue
    # acumulador = acumulador + sueldo
    acumulador += sueldo
    contador = contador + 1  # contador += 1

print(f"El valor acumulado es de: {acumulador}")
