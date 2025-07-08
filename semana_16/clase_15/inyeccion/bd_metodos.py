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
		PRIMARY KEY("id")
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
def bd_inicializar_tabla_productos(lista_productos):
    status = False
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # variable sql con la consulta en texto plano - los valores estan parametrizados
        sql = """INSERT INTO productos 
		("id","nombre","categoria","precio") 
		VALUES 
		(?,?,?,?)"""
        # ejecuta la consulta con los parametros en la lista
        cursor.executemany(sql, lista_productos)
        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount > 0:
            status = True
        # confirma los cambios
        conexion.commit()
    except Exception as error:
        # muestra en pantalla si hubo error
        print(f"Error encontrado al inicializar la tabla: {error}")
    finally:
        # cierra la conexión
        conexion.close()
        # retorna el estado de la transaccion
        return status


# Funcion para insertar datos en la tabla productos
def bd_insertar_producto(producto):
    status = False
    try:
        # establece la conexión a la base inventario.db con ruta relativa
        conexion = sqlite3.connect(bd_ruta)
        # cursor para ejecutar las consultas
        cursor = conexion.cursor()

        # sql parametrizados - SEGURA
        # sql = """INSERT INTO productos (id,nombre,categoria,precio) VALUES (?,?,?,?)"""
        # cursor.execute(sql, producto)

        # sql generica - VULNERABLE
        sql = f"INSERT INTO productos (id,nombre,categoria,precio) VALUES ({producto[0]},'{producto[1]}','{producto[2]}',{producto[3]})"
        print(sql)
        cursor.execute(sql)

        # confirma los cambios
        conexion.commit()

        # validamos que se haya actualizado el registro y actualizamos el estado para informar
        if cursor.rowcount == 1:
            status = True
    except Exception as error:
        # muestra en pantalla si hubo error
        print(f"Error encontrado insertar producto: {error}")
    finally:
        # cierra la conexión
        conexion.close()
        # retorna el estado de la transaccion
        return status


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

        # consulta sql parametrizada - SEGURA -
        # sql = """SELECT * FROM productos WHERE nombre LIKE ?"""
        # cursor.execute(sql, ("%" + nombre + "%",))

        # consulta sql generica - VULNERABLE -
        sql = f"SELECT * FROM productos WHERE nombre LIKE '%{nombre}%'"
        cursor.execute(sql)

        # volcamos en una variable local los datos que vienen de la base
        lista_productos = cursor.fetchall()
    except Exception as error:
        print(
            f"Error encontrado al leer la tabla: {error}"
        )  # muestramos en pantalla si hubo error
    finally:
        conexion.close()  # cerramos la conexión
    return lista_productos
