"""
Utiliza lo aprendido para:
1) Crear una base de datos SQLite llamada inventario.db

2) Definir una tabla llamada productos con los campos id 
(clave primaria autoincremental), nombre (texto, no nulo) y precio (real, no nulo). 
3) Diseñar un programa que permita: 

Registrar un producto ingresando su nombre, categoria y precio. 
Mostrar todos los productos almacenados en la base de datos. 
El sistema debe incluir validaciones básicas: 
El nombre no puede estar vacío. El precio debe ser un número mayor que cero.

"""
lista_productos = []
# 1. importamos el módulo Sqlite3
import sqlite3

# Declaramos la función principal
def main():
    # Cuerpo principal
    while True:
        # ingreso de datos
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = input("Ingrese el precio del producto: ")

        diccionario = {"nombre": nombre,
                        "categoria": categoria,
                         "precio": precio}
        # lista_productos.append(diccionario)
        db_insertar_producto(diccionario) # funcion o metodo que inserta el diccionario en la BD
        print("Producto insertado exitosamente!")
        bd_leer_productos()

        # preguntamos al usuario si continúa o no
        continuar = input("Continua cargando? s/n: ").strip().lower()
        if continuar == "n":
            print("Finalizando...")
            break

# declaramos las funciones secundarias
def db_insertar_producto(producto):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
	# 4. preparar la consulta SQL
    sql = """INSERT INTO productos 
	("nombre","categoria","precio") 
	VALUES 
	(?,?,?)"""
	# 5. ejecutar la consulta
    cursor.execute(sql, (producto["nombre"], producto["categoria"], producto["precio"]))
	# 6. confirmar el cambio
    conexion.commit()
	# 7. Cerramos la conexion a la base
    conexion.close()



# Funcion para crear la tabla productos
def bd_crear_tabla_productos():
    # 2. Creamos la conexion a la base de datos
	# si inventario.db no existe, se crea
	# si existe, no hace nada
	conexion = sqlite3.connect("inventario.db")
	# 3. Crear el cursor para ejecutar la consulta SQL
	cursor = conexion.cursor()

	# 4. preparar la consulta SQL
	sql = """CREATE TABLE IF NOT EXISTS "productos" (
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


# llamamos a la funcion que crea la tabla (creando la base si no existe)
bd_crear_tabla_productos()
# Invocamos a la función principal
main()


# cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (categoria_nombre,))
# result = cursor.fetchone()