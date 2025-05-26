# categorias = {
#     "periferico": [["Mouse", 1000, 5], ["Teclado", 1500, 3], ["monitor 19", 55000, 3]],
#     "memoria": [["Ddr4 8GB", 6000, 4], ["Ddr3 4gb", 8000, 5], ["ddr4 kingston 16gb", 15000, 4]],
#     "procesador": [["Ryzen 5", 920000, 2], ["ryzen 7", 105000, 4], ["intel I7 12gen", 95000, 4]]
# }

# # for clave, valor in categorias.items():
# #     print(clave)
# #     print(valor)

# print(categorias["memoria"])
# producto = ["Ryzen 7", 9800, 2]
# categorias["memoria"].append(producto)
# print(categorias["memoria"])


# Diccionario de categorías con productos pre-cargados
categorias = {
    "periferico": [["Mouse", 1000, 5], ["Teclado", 1500, 3], ["monitor 19", 55000, 3]],
    "memoria": [["Ddr4 8GB", 6000, 4], ["Ddr3 4gb", 8000, 5], ["ddr4 kingston 16gb", 15000, 4]],
    "procesador": [["Ryzen 5", 920000, 2], ["ryzen 7", 105000, 4], ["intel I7 12gen", 95000, 4]]
}

intentos_max = 3
# menu inicial
while True:
    print(
        """
Menú de opciones:
    1. 💿 Alta de producto
    2. 🖥️  Mostrar productos
    3. 🔍 Buscar productos
    4. 🗑️  Eliminar productos
    5. Salir
"""
    )
    opcion = input("Ingrese su opción: ").strip()
#   prosesos del menu opcion uno alta de producto con creacion de categoria si no existe y volver al menu principal si
#     me equboque de opcion deceada 
    match opcion:
        case "1":
            print("\033[93mAlta de productos...\033[0m")

            for intento in range(intentos_max):
                cat = input("ingrese la categoría periferico, memoria, procesador (si no existe se creará) o \033[35mvolver:\033[0m ").strip().lower()
                if cat == "volver":
                    print("\033[94mAlta cancelada.\033[0m")
                    break
                if cat == "":
                    print("\033[91mCategoría no puede estar vacía.\033[0m")
                    continue

                nombre = input("Nombre del producto ").strip()
                
                if nombre == "":
                    print("\033[91mNombre no puede estar vacío.\033[0m")
                    continue

                precio_str = input("Precio sin centavos" ).strip()
                
                if not precio_str.isdigit():
                    print("\033[91mPrecio inválido.\033[0m")
                    continue

                cantidad_str = input("Cantidad:").strip()
               
                if not cantidad_str.isdigit():
                    print("\033[91mCantidad inválida.\033[0m")
                    continue

                precio = int(precio_str)
                cantidad = int(cantidad_str)
                producto = [nombre, precio, cantidad]

                if cat not in categorias:
                    categorias[cat] = []
                    print(f"\033[92mCategoría '{cat}' creada.\033[0m")

                categorias[cat].append(producto)
                print(f"\033[92mProducto '{nombre}' agregado en categoría '{cat}'.\033[0m")
                break
# proceso de menu mostrar productos
        case "2":
            print("\033[93mProductos registrados:\033[0m")
            if not any(categorias.values()):
                print("\033[91mNo hay productos registrados.\033[0m")
            else:
                for cat, productos in categorias.items():
                    print(f"\n--- {cat.capitalize()} ---")
                    if productos:
                        for i, p in enumerate(productos, start=1):
                            print(f"{i}. {p[0]} - ${p[1]} - Cantidad: {p[2]}")
                    else:
                        print("Sin productos.")
# buscar productos con opcion de volver al menu inicial 
        case "3":
            print("\033[93mBuscar productos...\033[0m")
            termino = input("Ingrese nombre a buscar (o \033[35mvolver:\033[0m): ").strip().lower()
            if termino == "volver":
                print("\033[94mBúsqueda cancelada.\033[0m")
                continue

            encontrado = False
            for cat, productos in categorias.items():
                for i, p in enumerate(productos, start=1):
                    if termino in p[0].lower():
                        print(f"{cat.capitalize()} - {i}. {p[0]} - ${p[1]} - Cantidad: {p[2]}")
                        encontrado = True

            if not encontrado:
                print("\033[91mNo se encontraron productos.\033[0m")
# eliminar productos por unidad o total de unidades o volver al menu inicial 
        case "4":
            print("\033[93mEliminar productos...\033[0m")
            print("Categorías disponibles:")
            for cat in categorias:
                print(f" - {cat}")

            cat_op = input("Ingrese categoría (o \033[35mvolver:\033[0m): ").strip().lower()
            if cat_op == "volver":
                print("\033[94mEliminación cancelada.\033[0m")
                continue
            if cat_op not in categorias:
                print("\033[91mCategoría no encontrada.\033[0m")
                continue

            productos = categorias[cat_op]
            if not productos:
                print("\033[91mNo hay productos en esta categoría.\033[0m")
                continue

            for i, p in enumerate(productos, start=1):
                print(f"{i}. {p[0]} - ${p[1]} - Cantidad: {p[2]}")

            pos_str = input("Ingrese el número del producto a reducir/eliminar (o \033[35mvolver:\033[0m): ").strip()
            if pos_str.lower() == "volver":
                print("\033[94mEliminación cancelada.\033[0m")
                continue
            if not pos_str.isdigit():
                print("\033[91mEntrada inválida.\033[0m")
                continue

            pos = int(pos_str)
            if 1 <= pos <= len(productos):
                producto = productos[pos - 1]
            print(f"\n¿Qué desea hacer con '{producto[0]}'?")
            print("1. Reducir una unidad")
            print("2. Eliminar todas las unidades")
            accion = input("Ingrese opción (1/2) o \033[35mvolver:\033[0m ").strip()

            if accion == "volver":
               print("\033[94mEliminación cancelada.\033[0m")
               continue
            elif accion == "1":
               if producto[2] > 1:
                  producto[2] -= 1
                  print(f"\033[92mCantidad de '{producto[0]}' ahora es {producto[2]}.\033[0m")
               else:
                  eliminado = productos.pop(pos - 1)
                  print(f"\033[91mProducto '{eliminado[0]}' eliminado (cantidad = 0).\033[0m")
            elif accion == "2":
                 eliminado = productos.pop(pos - 1)
                 print(f"\033[91mProducto '{eliminado[0]}' eliminado totalmente.\033[0m")
            else:
                 print("\033[91mOpción inválida.\033[0m")
# salir del programa con verificacion de elegir un menu 
#     
        case "5":
            print("\033[95mSaliendo del sistema...\033[0m")
            break

        case _:
            print("\033[91mOpción incorrecta. Intente nuevamente.\033[0m")
           
print("\n\033[96mGracias por usar la app.\033[0m")