
"""
En TalentoLab necesitamos llevar un registro ordenado 
de los nombres de los nuevos y nuevas clientes que se van incorporando.

Tu tarea es escribir un programa en Python que haga lo siguiente:

1. Solicite los nombres de los y las clientes uno por uno, y valide que cada nombre no esté vacío. 
Si se deja el campo vacío, mostrar un mensaje de advertencia y pedir nuevamente el nombre.

2. Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

3. Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

4. Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista
 y mostrá la lista ordenada utilizando un bucle for.

ToolBox
- variables
- listas
- tuplas
- metodos
- condicionales
- bucle while
- bucle for

"""

# Declación de variables
clientes = [] # lista que almacena los clientes




while True:
    # Ingreso datos de clientes
    # while True:
    #     nombre = input("Ingrese su nombre: ").strip()
    #     if nombre == "":
    #         print("No se admite nombre vacío, intente nuevamente")
    #         continue
    #     break


    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre != "":
            print("Nombre aceptado!\n")
            break
        print("No se admite nombre vacío, intente nuevamente")


    if nombre.lower() == "fin":
        break


    # Agregamos el nombre en una lista
    clientes.append(nombre)
    print("Nombre agregado a la lista exitosamente!\n")


# Fin de bucle de ingreso de datos


# Ordenamos el arreglo o lista
clientes_ordenados = clientes.sort()


# Imprimimos el listado en pantalla
for cliente in clientes:
    print(cliente)
