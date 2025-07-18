# importamos el módulo Sqlite3
import sqlite3

# importamos el módulo os
import os


# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


# Función para crear la tabla productos
def bd_crear_tabla_productos():
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano
        sql = """CREATE TABLE IF NOT EXISTS "productos" (
		"id"	INTEGER,
		"nombre"	TEXT NOT NULL,
		"categoria"	TEXT NOT NULL,
		"precio"	REAL NOT NULL,
        "descripcion" TEXT NOT NULL,
        "cantidad" INTEGER NOT NULL,
		PRIMARY KEY("id" AUTOINCREMENT)
	);"""
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


# Funcion para insertar datos en la tabla productos
def bd_insertar_producto(nombre, categoria, precio, descripcion, cantidad):
    status = False
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano - los valores estan parametrizados
        sql = """INSERT INTO productos 
		("nombre","categoria","precio", "descripcion", "cantidad") 
		VALUES 
		(?,?,?,?,?)"""
        # ejecuta la consulta con los parametros en la lista
        cursor.execute(sql, (nombre, categoria, precio, descripcion, cantidad))
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


# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_productos():
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_productos = []  # mejora seria armar un diccionario
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


# Funcion para buscar solo un producto segun su nombre de la tabla productos
def bd_leer_producto_por_nombre(nombre):
    # declaramos una lista local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """SELECT * FROM productos WHERE nombre LIKE ?"""
        # ejecutamos la consulta con el parámetro nombre
        cursor.execute(sql, ("%" + nombre + "%",))
        # volcamos en una variable local los datos que vienen de la base
        lista_productos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al crear la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_productos


# Funcion para eliminar un registro de la tabla productos segén el id
def bd_eliminar_producto(producto_id):
    # declaramos una variable local con el estado de la operacion
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """DELETE FROM productos WHERE id = ?"""
        # ejecutamos la consulta y pasamos como argumento la tupla con el id del registro a eliminar
        cursor.execute(sql, (producto_id,))
        # confirmamos el cambio
        conexion.commit()
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount > 0:
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


# Funcion para buscar los producto con bajo stock
def bd_leer_producto_bajo_stock(limite):
    # declaramos una variable local para retornar el resultado de la consulta en la tabla
    lista_productos = []
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """SELECT * FROM productos WHERE cantidad < ?"""
        # ejecutamos la consulta con el parámetro cantidad
        cursor.execute(sql, (limite,))
        # volcamos en una variable local el dato que vienen de la base
        lista_productos = cursor.fetchall()
    except Exception as error:
        # muestramos en pantalla si hubo error
        print(f"Error encontrado al leer el registro por id: {error}")
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el resultado
        return lista_productos
