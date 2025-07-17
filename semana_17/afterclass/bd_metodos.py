# importamos el módulo Sqlite3
import sqlite3

# importamos el módulo os
import os

# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


# Función para crear la tabla vehiculos
def bd_crear_tabla_vehiculos():
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano
        sql = """CREATE TABLE IF NOT EXISTS "vehiculos" (
	"id"	INTEGER,
	"marca"	TEXT NOT NULL,
	"modelo"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
        # ejecuta la consulta
        cursor.execute(sql)
        # confirma los cambios
        conexion.commit()
    except Exception as error:
        # muestra en pantalla si hubo error
        print(f"Error encontrado al crear la tabla: {error}")
    finally:
        # cierra la conexión
        conexion.close()


# Funcion para insertar datos en la tabla vehiculos
def bd_insertar_vehiculo(marca, modelo, precio, descripcion, cantidad):
    status = False
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano - los valores estan parametrizados
        sql = """INSERT INTO vehiculos 
		("marca","modelo","precio", "descripcion", "cantidad") 
		VALUES 
		(?,?,?,?,?)"""
        # ejecuta la consulta con los parametros en la lista
        cursor.execute(sql, (marca, modelo, precio, descripcion, cantidad))
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount == 1:
            status = True
        # confirma los cambios
        conexion.commit()
    except Exception as error:
        # muestra en pantalla si hubo error
        print(f"Error encontrado al crear la tabla: {error}")
    finally:
        # cierra la conexión
        conexion.close()
        # retorna el estado de la transaccion
        return status


# Funcion para leer TODOS los datos de la tabla vehiculos
def bd_leer_vehiculos():
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_vehiculos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # declaramos la variable sql con la consulta en texto plano
        sql = """SELECT * FROM vehiculos"""
        # ejecutamos la consulta
        cursor.execute(sql)
        # volcamos en una variable local los datos que vienen de la base
        lista_vehiculos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al leer los vehiculos: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_vehiculos


# Funcion para buscar vehiculos segun su marca en la tabla vehiculos
def bd_leer_vehiculo_por_marca(marca):
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_vehiculos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """SELECT * FROM vehiculos WHERE marca LIKE ?"""
        # ejecutamos la consulta con el parámetro nombre
        cursor.execute(sql, ("%" + marca + "%",))
        # volcamos en una variable local los datos que vienen de la base
        lista_vehiculos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al leer el vehiculo por marca: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_vehiculos


# Funcion para buscar vehiculos segun su id en la tabla vehiculos
def bd_leer_vehiculo_por_id(id):
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    vehiculo = None
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """SELECT * FROM vehiculos WHERE id = ?"""
        # ejecutamos la consulta con el parámetro nombre
        cursor.execute(sql, (id,))
        # volcamos en una variable local los datos que vienen de la base
        vehiculo = cursor.fetchone()
    except Exception as error:
        print(
            f"Error encontrado al leer el vehiculo por marca: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return vehiculo


# Funcion para eliminar un registro de la tabla vehiculos segén el id
def bd_eliminar_vehiculo(id):
    # declaramos una variable local con el estado de la operacion
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """DELETE FROM vehiculos WHERE id = ?"""
        # ejecutamos la consulta y pasamos como argumento la tupla con el id del registro a eliminar
        cursor.execute(sql, (id,))
        # confirmamos el cambio
        conexion.commit()
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount == 1:
            status = True
    except Exception as error:
        print(
            f"Error encontrado al eliminar el registro: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el estado de la operación
        return status


# Funcion para modificar el precio de un registro de la tabla vehiculos según el id
def bd_actualizar_precio(id, precio):
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """UPDATE vehiculos SET precio = ? WHERE id = ?"""
        # ejecutamos la consulta con los parámetros id y precio de forma nombrada
        cursor.execute(sql, (precio, id))
        # confirmamos el cambio
        conexion.commit()
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount > 0:
            status = True
    except Exception as error:
        print(
            f"Error encontrado al crear la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el estado de la operación
    return status


# Funcion para buscar los vehiculos con bajo stock
def bd_leer_vehiculos_bajo_stock(limite):
    # declaramos una variable local para retornar el resultado de la consulta en la tabla
    lista_vehiculos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """SELECT * FROM vehiculos WHERE cantidad < ?"""
        # ejecutamos la consulta con el parámetro cantidad
        cursor.execute(sql, (limite,))
        # volcamos en una variable local el dato que vienen de la base
        lista_vehiculos = cursor.fetchall()
    except Exception as error:
        # muestramos en pantalla si hubo error
        print(f"Error encontrado al leer minimo stock: {error}")
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el resultado
        return lista_vehiculos
