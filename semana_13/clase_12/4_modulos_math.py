import math

# Tenemos declarada la funcion area_circulo
# que calcula el área dada por: pi * radio^2

def area_circulo(radio):
    # area = 3.14 * radio*radio
    area = math.pi * math.pow(radio, 2)
    return area

# ingresamos el radio del círculo
radio = float(input("Ingresá el radio del círculo: "))
print(f"El área del círculo con radio {radio} es: {area_circulo(radio):.2f}")
