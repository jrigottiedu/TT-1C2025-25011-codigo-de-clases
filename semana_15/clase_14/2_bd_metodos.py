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
def bd_leer_producto_por_id():
	""""""

# Funcion para buscar solo un producto segun su nombre de la tabla productos
def bd_leer_producto_por_nombre():
	""""""

# Funcion para modificar un registro de la tabla productos
def bd_actualizar_precio():
	""""""

# Funcion para eliminar un registro de la tabla productos
def bd_eliminar_producto_por_id():
	""""""



# Invocar o llamar a las funciones
# bd_leer_productos()
# bd_leer_producto_por_id()
# bd_leer_producto_por_nombre()
# bd_actualizar_precio()
# bd_eliminar_producto_por_id()

while True:
	
	seguir = input("Seguir s/n: ").strip().lower()
	if seguir == "n":
		break





