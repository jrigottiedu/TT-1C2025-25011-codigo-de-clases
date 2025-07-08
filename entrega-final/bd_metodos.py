# importamos el módulo Sqlite3
import sqlite3

# importamos el módulo os
import os

# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)  # C:\Users\Talento\Documents\TT_1C2025_25011\Python\Codigo de clases\entrega-final

# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


# Funcion para crear la tabla productos
def bd_crear_tabla_productos():
    try:
        conexion = sqlite3.connect(bd_ruta)
        cursor = conexion.cursor()
        sql = """CREATE TABLE IF NOT EXISTS"productos" (
		"id"	INTEGER,
		"nombre"	TEXT NOT NULL,
		"categoria"	TEXT NOT NULL,
		"precio"	REAL NOT NULL,
		PRIMARY KEY("id" AUTOINCREMENT)
	);"""
        cursor.execute(sql)
        conexion.commit()
    except Exception as error:
        print(f"Error encontrado al crear la tabla: {error}")
    finally:
        conexion.close()


# Funcion para insertar datos en la tabla productos
def bd_insertar_producto(nombre, categoria, precio):
    conexion = sqlite3.connect(bd_ruta)
    cursor = conexion.cursor()
    # 4. preparar la consulta SQL
    sql = """INSERT INTO productos 
	("nombre","categoria","precio") 
	VALUES 
	(?,?,?)"""

    # 5. ejecutar la consulta
    cursor.execute(sql, (nombre, categoria, precio))

    # 6. confirmar el cambio
    conexion.commit()

    # 7. Cerramos la conexion a la base
    conexion.close()


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


# Funcion para buscar solo un producto segun su id de la tabla productos
def bd_leer_producto_por_id(id):
    # declaramos una variable local para retornar el resultado de la consulta en la tabla
    producto = None
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL parametrizada
        sql = """SELECT * FROM productos WHERE id = ?"""
        # ejecutamos la consulta con el parámetro id
        cursor.execute(sql, (id,))
        # volcamos en una variable local el dato que vienen de la base
        producto = cursor.fetchone()
    except Exception as error:
        # muestramos en pantalla si hubo error
        print(f"Error encontrado al leer el registro por id: {error}")
    finally:
        # cerramos la conexión
        conexion.close()
        # retornamos el resultado
        return producto


# Funcion para modificar el precio de un registro de la tabla productos según el id
def bd_actualizar_precio(id, precio):
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """UPDATE productos SET precio = ? WHERE id = ?"""  #
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


# Funcion para insertar datos en la tabla productos
def bd_eliminar_producto(id):
    conexion = sqlite3.connect(bd_ruta)
    cursor = conexion.cursor()
    # 4. preparar la consulta SQL
    sql = """DELETE FROM productos WHERE id = ?"""
    # 5. ejecutar la consulta
    cursor.execute(sql, (id,))
    # 6. confirmar el cambio
    conexion.commit()
    # 7. Cerramos la conexion a la base
    conexion.close()


# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_bajo_stock(stock):
    """
    argumento: stock
    retorna lista de productos con cantidad menor a stock
    """
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    # 4. preparar la consulta SQL
    sql = """SELECT * FROM productos WHERE cantidad < ?"""
    # 5. ejecutar la consulta
    cursor.execute(sql, (stock,))
    # 6. volcamos en una variable local los datos que vienen de la base
    lista_productos = cursor.fetchall()
    # print(lista_productos)
    # 7. Cerramos la conexion a la base
    conexion.close()
    return lista_productos
