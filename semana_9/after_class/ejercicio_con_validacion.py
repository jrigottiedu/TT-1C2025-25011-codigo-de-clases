# Como la versión anterior no validaba el ingreso de los datos,
# le pedimos a la IA que le agregue validación al código
# Analizamos el nuevo código y detectamos que no es la mejor solución
# Ya que si ingresamos el nombre pero no el precio
# Nos obliga a volver a ingresar el nombre

# Creamos el diccionario vacío
productos = {}

print("Bienvenido al registro de productos de TalentoLab")
print("Escribí 'salir' cuando quieras terminar.\n")

# Bucle principal
while True:
    # Pedimos el nombre del producto
    nombre = input("Ingresá el nombre del producto: ").strip()

    # Verificamos si quiere salir
    if nombre.lower() == "salir":
        break

    # Validamos que el nombre no esté en blanco
    if nombre == "":
        print("⚠️  El nombre no puede estar en blanco. Intentalo de nuevo.\n")
        continue

    # Pedimos el precio
    precio = input("Ingresá el precio de ese producto: ").strip()

    # Validamos que el precio no esté en blanco
    if precio == "":
        print("El precio no puede estar en blanco. Intentalo de nuevo.\n")
        continue

    # Intentamos convertir el precio a número
    try:
        precio = float(precio)
    except:
        print("El precio debe ser un número válido. Intentalo de nuevo.\n")
        continue

    # Guardamos en el diccionario
    productos[nombre] = precio

    # Mostramos los productos registrados hasta ahora
    print("\n📋 Productos registrados:")
    for prod, val in productos.items():
        print(f"- {prod}: ${val:.2f}")
    print("-" * 30)

# Mensaje final
print("\nGracias por usar el registro de productos.")
