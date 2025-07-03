productos = [
        ('Manzana roja', 'Manzana deliciosa colorada', 12, 'FRUTAS', 1200),
        ('Manzana verde', 'Manzana ácida verde', 19, 'FRUTAS', 1500),
        ('Harina Común', 'Harina común 000', 9, 'ALMACEN', 1800),
        ('Harina Leudante', 'Harina Leudante para repostería', 6, 'ALMACEN', 2000),
        ('Café', 'Café torrado suave', 20, 'ALMACEN', 5000),
        ('Café Instantáneo', 'Café soluble rápido', 30, 'ALMACEN', 8000),
        ('Cerezas', 'Fruta roja fresca', 23, 'FRUTAS',)]


#     # crea la tabla
# conexion = sqlite3.connect("inventario.db")
# # crear cursor
# cursor = conexion.cursor()
    
#     sql = """INSERT into productos
#       ("Nombre","Categoria","Precio")
#         VALUES (? , ?, ? )"""
#     item_nombre = input ("el nombre del articulo es:")
#     item_categoria = input ("la categoria articulo es:")
#     item_precio = int(input("el precio del articulo es:"))

    # ejecutar la consulta
    
    # cursor.execute (sql, (item_nom


def getCantidad():
  try:
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return (1,cantidad)
  except Exception as e:
    return (0,e)