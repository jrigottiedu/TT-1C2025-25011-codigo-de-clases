import sqlite3

# Funcion para crear la tabla productos
def bd_crear_tabla_productos():
	try:
		conexion = sqlite3.connect("inventario.db")
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
	conexion = sqlite3.connect("inventario.db")
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


# Funcion para insertar datos en la tabla productos
def bd_elimibar_producto(id):
	conexion = sqlite3.connect("inventario.db")
	cursor = conexion.cursor()
	# 4. preparar la consulta SQL
	sql = """DELETE FROM productos WHERE id = ?"""
    # 5. ejecutar la consulta
	cursor.execute(sql, (id,))
	# 6. confirmar el cambio
	conexion.commit()
	# 7. Cerramos la conexion a la base
	conexion.close()

