# 1. importamos el módulo Sqlite3
import sqlite3

# 2. Creamos la conexion a la base de datos
conexion = sqlite3.connect("inventario.db")

# 3. Crear el cursor para ejecutar la consulta SQL
cursor = conexion.cursor()

# 4. Cerramos la conexion a la base
conexion.close()

