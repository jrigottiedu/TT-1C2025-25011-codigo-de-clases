# 1. importamos el módulo Sqlite3
import sqlite3
import os 

# Carpeta donde está el script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos (por ejemplo, en una subcarpeta llamada 'data')
bd_ruta = os.path.join(BASE_DIR, "inventario.db")

# Declaracion de funciones / métodos
# Funcion para crear la tabla productos
def bd_crear_tabla_productos():
    try:
        conexion = sqlite3.connect(bd_ruta)
        cursor = conexion.cursor()
        sql = """CREATE TABLE IF NOT EXISTS "productos" (
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
def bd_insertar_producto(nombre, categoria, descripcion, cantidad, precio):
    respuesta = {"status": False, "data": None, "error": None}
    try:
        conexion = sqlite3.connect(bd_ruta)
        cursor = conexion.cursor()
        # 4. preparar la consulta SQL
        sql = """INSERT INTO productos 
        ("nombre","categoria","descripcion","cantidad","precio") 
        VALUES 
        (?,?,?,?,?)"""
        # 5. ejecutar la consulta
        cursor.execute(sql, (nombre, categoria, descripcion, cantidad, precio))
        # 6. confirmar el cambio
        conexion.commit()
        respuesta["status"] = True
    except Exception as e:
        respuesta["error"] = e
    finally:
        # 7. Cerramos la conexion a la base
        conexion.close()
        return respuesta


# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_productos():
    conexion = sqlite3.connect(bd_ruta)
    cursor = conexion.cursor()

    # 4. preparar la consulta SQL
    sql = """SELECT * FROM productos"""

    # 5. ejecutar la consulta
    cursor.execute(sql)

    # 6. volcamos en una variable local los datos que vienen de la base
    lista_productos = cursor.fetchall()

    print(lista_productos)

    # 7. Cerramos la conexion a la base
    conexion.close()


# Invocar o llamar a las funciones
# bd_crear_tabla_productos()
# bd_crear_tabla_productos_try()
# bd_insertar_producto()
# bd_leer_productos()
