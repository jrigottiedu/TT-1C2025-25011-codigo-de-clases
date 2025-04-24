# Consulta 1 - uso del método isdigit

"""
isdigit() es un método de una variable tipo str, es decir de una cadena
isdigit() retorna True, si esa cadena es numerica o False si no lo es.

Ejemplo:
"""
numero1 = "25"
numero1.isdigit() #retorna True

numero2 = "25 años"
numero2.isdigit() # retorna False

"""
De esta manera podemos usar esta estructura condicional
"""
edad = input("Ingrese su edad")

if edad.isdigit():
    edad = int(edad) #ahora que se que es numerico, convierto str a int
else:
    print("Debe ingresar una edad numerica válida")


# Consulta 2 - uso de métodos

"""
Los metodos son equivalentes a las funciones
"""
cadena = "Python es divertido"
print(cadena.upper()) # PYTHON ES DIVERTIDO
print(cadena.lower()) # pthon es divertido
print(cadena.title()) # Python Es Divertido
print(cadena.capitalize()) # Python es divertido

# Consulta 3 - uso del operador lógico not
"""
Vimos 3 operados lógicos: and, or, not
not puede generar algunas dudas, pero básicamente niega el estado,
"""
estado = True
print(estado) # True
print(not estado) # False

"""
En este otro ejemplo vemos el impacto de combinarlo con operadores relacionales
Corran este código y vean la salida cuando ingresan texto y cuando no lo hacen
"""
nombre = input("Ingrese su nombre: ")

print(f'nombre == "" {nombre == ""}') 
print(f'not nombre == "" {not nombre == ""}')
print(f'nombre !=  "" {nombre != ""}')
print(f'not nombre !=  "" {not nombre != ""}')
