"""
Juego: "Guess the number"

Desarrollamos el código de una App en la que un participante compite adivinando en número oculto en el código, cuyos valores posibles van de 0 a 9.

Realizar una primera versión sin límite de intentos.
Luego mejorarlo con un máximo número de intentos de 3.
Finalmente investigar con IA cámo hacer que el número oculto se genere de manera random

"""
# numero = 2 # se genere de forma aleatoro (random)

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
numero = len(nombre) + edad 

guess = int(input("Ingrese su numero: "))
if guess == numero:
    print("Felicitaciones!!")
else:
    print("Intente nuevamente...")