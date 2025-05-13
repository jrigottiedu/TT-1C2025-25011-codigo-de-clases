# C25011 - Pre-entrega PFI
# Fecha de publicación: Clase 8 - el lunes 19 de mayo
# Fecha de entrega: hasta el domingo 25 de mayo a la medianoche
# Modalidad de entrega: archivo py en un repositorio en la nube (Google Drive)

# Consigna: Ver debajo del código

# A continuación se presenta un bloque de código que pueden utilizar
# para la estructura inicial de su proyecto.
# La idea es luego, ir completando cada opción de menú con lo que aprendimos en clases

while True: # Condicion siempre True que maneja el flujo normal del menú

    print("""
Menú de opciones:
    1. Alta de producto
    2. Motrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
""")
    opcion = input("Ingrese su opción: ") # Solicito al usuario que ingresa su opción

    # Procesamiento de la opción ingresada
    match opcion :
        case "1": 
            # Aqui desarrollar código para el alta de productos
            print("Procesando alta de productos...")
        case "2":
            # Aqui desarrollar código para buscar productos
            print("Procesando mostrar productos...")
        case "3":
            # Aqui desarrollar código para buscar productos
            print("Procesando buscar productos...")
        case "4":
            # Aqui desarrollar código para eliminar productos
            print("Procesando eliminar productos...") 
        case "5":
            print("Saliendo...")
            break # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")


# Consigna
"""
1. Ingreso de datos de productos
El sistema debe permitir ingresar datos básicos de los productos: 
nombre, categoría, y precio (sin centavos). 
Estos datos deben almacenarse en una lista, donde cada producto sea representado
como una sublista de tres elementos (nombre, categoría, y precio).

Nota_JP: 
Menú de opciones: Alta de productos
Solicitar y validar ingresos: nombre (str), categoría (str o lista), precio (int)
Almacenar estos valores en una lista, y esta lista en otra lista general llamada lista_productos

----------------------------------------------------------------------------------------

2. Visualización de productos registrados
El programa debe incluir una funcionalidad para mostrar en pantalla
todos los productos ingresados. La información debe presentarse de manera ordenada y legible, 
con cada producto numerado.

Nota_JP: 
Menú de opciones: Mostrar productos
Iteramos lista_productos y mostramos cada elemento
Podemos usar el índice de la lista para obtener la numeración

----------------------------------------------------------------------------------------

3. Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. 
Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. 
Si no hay coincidencias, debe informar que no se encontraron resultados.

Nota_JP:
Menú de opciones: Buscar productos
Solicitar al usuario que ingrese el nombre del producto a mostrar
Iteramos lista_productos y buscamos coincidencia en cada iteración
A medida que haya coincidencia mostramos en pantalla

----------------------------------------------------------------------------------------

4. Eliminación de productos
El sistema debe permitir eliminar un producto de la lista, 
identificándolo por su posición (número) en la lista.

Nota_JP:
Menú de opciones: Eliminar productos
Solicitar al usuario que ingrese la posición que ocupa en la lista_productos para eliminar

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Requisitos

A. Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
B. Usar listas para almacenar y gestionar los datos. 
C. Presentar un menú que permita elegir entre las funcionalidades disponibles: 
agregar productos, visualizar productos, buscar productos y eliminar productos.
D. Incorporar bucles while y for según corresponda. 
E. Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
F. El programa debe continuar funcionando hasta que se elija una opción para salir.


Consejos

I. Usá lo aprendido sobre listas y bucles para gestionar los datos y recorrerlos.
II .Recordá validar las entradas utilizando condicionales.
III. Utilizá las herramientas vistas para organizar y presentar la información de manera clara.

"""