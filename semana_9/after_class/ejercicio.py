# Ejercicio Clase 8 resuelto con enfoque "Vibe Coding"

"""
Enunciado:

En TalentoLab nos han pedido desarrollar una aplicación que registre 
productos y sus precios utilizando diccionarios. 
Necesitamos que tu programa cumpla con estas instrucciones:

Crear un diccionario llamado productos 
donde las claves sean los nombres de los productos y los valores sean sus precios.

Permitir que se agreguen productos y sus precios hasta que se decida finalizar. 

Mostrar el contenido del diccionario después de cada operación.
"""

# Le pasamos el enunciado a una IA y le pedimos que genere el código en Python
# Luego analizamos y ajustamos el resultado

# Creamos el diccionario vacío
productos = {}

# Mostramos un mensaje de bienvenida
print("Bienvenido al registro de productos de TalentoLab")
print("Escribí 'salir' cuando quieras terminar.")

# Repetimos hasta que el usuario escriba 'salir'
while True:

    # Pedimos el nombre del producto
    # La versión de la IA no tenía validación, nosotros la agregamos
    while True:
        nombre = input("Ingresá el nombre del producto: ")
        if nombre == "":
            print("no se admite")
            continue
        else:
            break


    # Si el usuario quiere salir, cortamos el ciclo
    if nombre.lower() == "salir":
        break

    # Pedimos el precio del producto
    precio = input("Ingresá el precio de ese producto: ") 

    # # Convertimos el precio a número (float por si es con coma)
    # No necesitamos convertir a float en este proyecto
    # try:
    #     precio = float(precio)
    # except:
    #     print("El precio debe ser un número. Intentalo de nuevo.")
    #     continue

    # Agregamos al diccionario (notar que diccionario NO tiene método append())
    productos[nombre] = precio

    # Mostramos el contenido del diccionario hasta ahora
    print("\nProductos registrados hasta ahora:")
    for clave, valor in productos.items():
        print(f"{clave}: {valor}")

# Mensaje final
print("Gracias por usar el registro de productos.")

