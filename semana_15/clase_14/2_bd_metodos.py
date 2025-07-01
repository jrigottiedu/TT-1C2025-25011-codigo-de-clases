# 1. importamos el módulo Sqlite3
import sqlite3

# Declaracion de funciones / métodos


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

# Funcion para leer solo un producto segun su id de la tabla productos
def bd_leer_producto_por_id(id): # parametro 1: id
	# id = 1
	conexion = sqlite3.connect("inventario.db")
	cursor = conexion.cursor()
	# 4. preparar la consulta SQL
	sql = """SELECT * FROM productos WHERE id = ?"""
	# 5. ejecutar la consulta
	cursor.execute(sql, (id,)) 
	# 6. volcamos en una variable local los datos que vienen de la base
	producto = cursor.fetchone()
	print(producto)
	# 7. Cerramos la conexion a la base
	conexion.close()

# Funcion para buscar solo un producto segun su nombre de la tabla productos
def bd_leer_producto_por_nombre(nombre):
	conexion = sqlite3.connect("inventario.db")
	cursor = conexion.cursor()
	# 4. preparar la consulta SQL
	sql = """SELECT * FROM productos WHERE nombre LIKE ?""" #campo nombre
	# 5. ejecutar la consulta
	cursor.execute(sql, ('%' + nombre + '%',)) 
	# 6. volcamos en una variable local los datos que vienen de la base
	lista_producto = cursor.fetchall()
	print(lista_producto)
	# 7. Cerramos la conexion a la base
	conexion.close()

# Funcion para modificar un registro de la tabla productos
def bd_actualizar_precio(id, precio):
	conexion = sqlite3.connect("inventario.db")
	cursor = conexion.cursor()
	# 4. preparar la consulta SQL
	sql = """UPDATE productos SET precio = :precio WHERE id = :id""" #
	# 5. ejecutar la consulta
	cursor.execute(sql, {"precio":precio, "id":id} ) 
	# 6. confirmar el cambio o actualizacion
	conexion.commit()
	# 7. Cerramos la conexion a la base
	conexion.close()

# Funcion para eliminar un registro de la tabla productos
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



# Invocar o llamar a las funciones
# bd_leer_productos()
# bd_leer_producto_por_id(5)
# bd_leer_producto_por_nombre()
# bd_actualizar_precio()
# bd_eliminar_producto_por_id()

while True:
	id = int(input("Ingrese el id del producto a actualizar: "))
	precio = float(input("Ingrese el nuevo precio: "))
	bd_actualizar_precio(id, precio)
	seguir = input("Seguir s/n: ").strip().lower()
	if seguir == "n":
		break





