# acumulador global
acumulador = 0

# declarar funcion
def sumar(nombre, numero1, numero2):  # (parametro1, parametro2)
    suma = numero1 + numero2
    # print(f"Hola {nombre}, la suma es {suma}")
    # acumulamos global
    global acumulador
    acumulador += suma
    return suma #35


nombre = input("Ingresa tu nombre: ")
try: #if
    num1 = float(input("Ingrese el primer número: "))  # variable local
    num2 = float(input("Ingrese el segundo número: ")) # 15R
    # invocar funcion
    resultado = sumar(numero1=num1, numero2=num2, nombre=nombre)  # argumentos por posicion
    print(f"Hola {nombre}, la suma es {resultado}")
except ValueError: #else
    print("El valor ingresado NO es numerico")


# sumar(numero1=num1, numero2=num2) # argumentos por nombre
# print(f"\n Acumulador actualizado: {acumulador}")
