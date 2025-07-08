"""
En este archivo encuentran código para hacer más robusta su aplicación

1. Establecer una ruta dinámica con el módulo os
2. Comparen las funciones bd_leer_productos() y bd_leer_productos_with,
    la segunda introduce with as, que se encarga de cerrar la conexión automaticamente
3. Al usar with, junto con un diccionario de retorno, se tiene un mejor control de los datos y los errores devueltos por la función
    armando, actualizando y retornando un diccionario de este tipo:
     respuesta = {"status": False, "data": [], "error": None}
"""

# importamos el módulo Sqlite3
import sqlite3

# importamos el módulo os
import os

# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_productos():
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # declaramos la variable sql con la consulta en texto plano
        sql = """SELECT * FROM productos"""
        # ejecutamos la consulta
        cursor.execute(sql)
        # volcamos en una variable local los datos que vienen de la base
        lista_productos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al crear la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_productos


# Funcion para leer TODOS los datos de la tabla productos usando with (me ahorro el conexion.close())
def bd_leer_productos_with():
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        with sqlite3.connect(bd_ruta) as conexion:
            # creamos el cursor para ejecutar la consulta
            cursor = conexion.cursor()
            # declaramos la variable sql con la consulta en texto plano
            sql = """SELECT * FROM productos"""
            # ejecutamos la consulta
            cursor.execute(sql)
            # volcamos en una variable local los datos que vienen de la base
            lista_productos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al crear la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        return lista_productos


# Funcion para leer TODOS los datos de la tabla productos usando with y un diccionario para retorno robusto
def bd_leer_productos_with():
    # declaramos una diccionario con los pares clave:valor a retornar
    respuesta = {"status": False, "data": [], "error": None}
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        with sqlite3.connect(bd_ruta) as conexion:
            # creamos el cursor para ejecutar la consulta
            cursor = conexion.cursor()
            # declaramos la variable sql con la consulta en texto plano
            sql = """SELECT * FROM productos"""
            # ejecutamos la consulta
            cursor.execute(sql)
            # volcamos en una variable local los datos que vienen de la base
            respuesta["data"] = cursor.fetchall()
            respuesta["status"] = True
    except Exception as error:
        respuesta["error"] = str(error)
    finally:
        return respuesta
