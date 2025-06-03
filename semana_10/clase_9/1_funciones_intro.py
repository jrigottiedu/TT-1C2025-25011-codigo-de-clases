# Declaracion de variables (Globales)

# Declaramos la lista de productos, que va a almacenar los siguientes datos
# nombre, categoria, precio
# La inicializamos con algunos datos para poder testear la opcion 2 - Mostrar productos
lista_productos = [
    ["manzana roja", "fruta", 1500], # nombre="manzana", categoria="fruta", precio="1500"
    ["pera", "fruta", 2500],
    ["manzana verde", "fruta", 2500],
] 

# -----------------------------------------------------------------
# Declaracion de funciones
def mostrarMenu():
    print("Función mostrar menú")

def getNombre():
    print("Función getNombre")

def getCategoria():
    print("Función getCategoriga")

def getPrecio():
    print("Función getPrecio")

def getBuscar():
    print("Función getBuscar")
    
def mostrarProductos(listaProductos):
    print("Función mostrarProductos")

def buscarProducto(producto):
    print("Función buscarProducto")

def getEliminar():
    print("Función getEliminar")

def eliminarProducto(producto):
    print("Función eliminarProducto")
# -----------------------------------------------------------------



# Cuerpo principal de nuestro código    
while True:  # Condicion siempre True que maneja el flujo normal del menú

# Imprimimos el menú de opciones
    mostrarMenu() # Nos imprime el menú en pantalla

    # El usuario ingresa su opción
    opcion = input("Ingrese su opción: ")  # Solicito al usuario que ingresa su opción

    # Procesamiento de la opción ingresada
    match opcion:
        case "1":
            # Adquisición de datos
            # nombre = input("Ingrese el nombre del producto") # Necesita validación!
            nombre = getNombre() # Solicita nombre y valida
            categoria = getCategoria() # Solicita categoría y valida
            precio = getPrecio() # Solicita precio y valida

            # Almacenamos los datos ingrsados en una sub-lista temporal llamada productos
            producto = [nombre, categoria, precio]
            # Luego usamos el método append() para insertar la sub-lista productos en la lista principal lista_productos
            lista_productos.append(producto)

        case "2":
            # Aqui desarrollar código para mostrar productos
            mostrarProductos(lista_productos)

        case "3":
            # Opcion Basica I - Sugerida
            # Ingresamos el nombre del producto a buscar
            buscar = getBuscar()

            encontrado = buscarProducto(buscar)

            if encontrado == False:
                print("Producto no encontrado")

        case "4":
            # Aqui desarrollar código para eliminar productos
            # Solicitamos al usuario que ingrese el indice producto a eliminar y validamos
            eliminar = getEliminar()
            resultado = eliminarProducto(eliminar)
            
        case "5":
            print("Saliendo...")
            break  # la sentencia break interrumpe el flujo normal del while
        case _:
            print("Opcion incorrecta")


print("Gracias por usar mi App")
