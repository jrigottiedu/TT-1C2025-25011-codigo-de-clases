# importamos la libreria sqlite3
import os
import sqlite3

BASE_DIR = os.path.dirname(__file__)  # directorio donde está el script
db_path = os.path.join(BASE_DIR, "DB_browser", "inventario.db")


# Creamos la conexion a la bd usando el path relativo
def db_connection():
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as error:
        print(f"Error al conectar con la base de datos: {error}")
        return None

# Creamos la función que ejecuta la query "SELECT * FROM productos"
def db_get_productos():
    conexion = db_connection()
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall() 
    conexion.close()
    return lista_productos

# Llamamos a la función que nos retorna todos los productos de la tabla
# print(db_get_productos())