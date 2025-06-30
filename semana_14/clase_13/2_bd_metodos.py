# 1. importamos el módulo Sqlite3
import sqlite3

# Declaracion de funciones / métodos

# Funcion para crear la tabla productos
def bd_crear_tabla_productos():
    # 2. Creamos la conexion a la base de datos
	# si inventario.db no existe, se crea
	# si existe, no hace nada
	conexion = sqlite3.connect("inventario.db")
	# 3. Crear el cursor para ejecutar la consulta SQL
	cursor = conexion.cursor()

	# 4. preparar la consulta SQL
	sql = """CREATE TABLE "productos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"categoria"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);"""

	# 5. ejecutar la consulta
	cursor.execute(sql)

	# 6. confirmar el cambio
	conexion.commit()

	# 7. Cerramos la conexion a la base
	conexion.close()

# Funcion para crear la tabla productos
def bd_crear_tabla_productos_try():
	try:
		conexion = sqlite3.connect("inventario.db")
		cursor = conexion.cursor()
		sql = """CREATE TABLE "productos" (
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
def bd_insertar_producto():
	conexion = sqlite3.connect("inventario.db")
	cursor = conexion.cursor()

	# 4. preparar la consulta SQL
	sql = """INSERT INTO productos 
	("nombre","categoria","precio") 
	VALUES 
	(?,?,?)"""

	nombre_producto = "vacio"
	categoria_producto = "carnes"
	precio_producto = 10000
	# 5. ejecutar la consulta
	cursor.execute(sql, (nombre_producto, categoria_producto, precio_producto))

	# 6. confirmar el cambio
	conexion.commit()

	# 7. Cerramos la conexion a la base
	conexion.close()

# Funcion para leer TODOS los datos de la tabla productos
def bd_leer_productos():
	conexion = sqlite3.connect("inventario.db")
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






