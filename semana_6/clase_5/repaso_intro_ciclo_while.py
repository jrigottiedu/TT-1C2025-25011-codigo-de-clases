"""
Tomamos como referencia un condicional de la clase 4
Vemos la necesidad de introducir un ciclo o bucle de control de flujo

Luego analizar y comprender la estructura While que vimos en los archivos
ciclo_while_contador.py
ciclo_while_acumulador.py
ciclo_while_continue.py
ciclo_while_break.py

"""

contador = 0 # Inicializamos el contador

# Declaramos un ciclo while con la condición que siempre sea True
# Esto nos obliga a usar el break dentro del While para evitar loop infinito

while True: # Condicion siempre True
    # Aquí inicia el bloque de código que se ejecuta mientras las condición del while es verdadera

    print("""
Menú de opciones:
    1. Alta de producto
    2. Buscar productos
    3. Editar productos
    4. Salir
""")
    opcion = input("Ingrese su opción: ") # Usuario ingresa su opciónS

    # Procesamiento
    match opcion :
        case "1": # implicitamente pregunta si opcion == "1"
            print("Usted presionó opción 1")
            print("Alta de producto")
            # Agregar una lista con los productos que ingresa el usuario
        case "2":
            print("Buscar producto")
        case "3":
            print("Editar producto")
        case "4": # Si el usuario ingresa 4 el programa se termina
            print("Saliendo...")
            break # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")


