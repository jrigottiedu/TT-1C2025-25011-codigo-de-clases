import sqlite3

# importamos el módulo os
import os


# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos
bd_ruta = os.path.join(BASE_DIR, "inventario.db")


def main():
    # print("Hola mundo")
    bd_insertar_producto("manzana", "fruta", 1500, "seleccionado", 500)


# Función para crear la tabla productos
def bd_crear_tabla_productos():
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano
        sql = """
CREATE TABLE IF NOT EXISTS "productos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"categoria"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
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
		("nombre","categoria","precio","descripcion","cantidad") 
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
def bd_leer_bajo_stock(stock):

    conexion = sqlite3.connect(bd_ruta)
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


# Funcion para modificar el precio de un registro de la tabla productos según el id
def bd_actualizar_cantidad(id, cantidad):
    status = False
    try:
        # establecemos la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # creamos el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        # preparamos la consulta SQL
        sql = """UPDATE productos SET cantidad = ? WHERE id = ?"""  #
        # ejecutamos la consulta con los parámetros id y precio de forma nombrada
        cursor.execute(sql, (cantidad, id))
        # confirmamos el cambio
        conexion.commit()
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if (
            cursor.rowcount > 0
        ):  # rowcount son la cantidad de filas afectadas/modificadas
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


bd_crear_tabla_productos()
main()
