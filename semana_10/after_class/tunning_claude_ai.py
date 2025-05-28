from colorama import Fore, Back, Style, init

# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def mostrar_producto(producto):
    """
    Función que muestra en pantalla los 3 datos de un producto con colorama
    
    Args:
        producto (list): Lista con [nombre, categoría, precio] del producto
    """
    print(f"{Fore.GREEN}Nombre: {producto[0]}")
    print(f"{Fore.BLUE}Categoría: {producto[1]}")
    print(f"{Fore.YELLOW}Precio: ${producto[2]}")

def mostrar_producto_con_estilo(producto):
    """
    Versión con más estilos usando colorama
    """
    print(f"{Fore.GREEN + Style.BRIGHT}Nombre: {producto[0]}")
    print(f"{Fore.BLUE + Style.DIM}Categoría: {producto[1]}")
    print(f"{Fore.YELLOW + Back.BLACK}Precio: ${producto[2]}")

def mostrar_producto_colorido(producto):
    """
    Versión con diferentes combinaciones de colores
    """
    print(f"{Fore.MAGENTA}Nombre: {producto[0]}")
    print(f"{Fore.CYAN}Categoría: {producto[1]}")
    print(f"{Fore.RED + Style.BRIGHT}Precio: ${producto[2]}")

def mostrar_colores_disponibles():
    """
    Muestra todos los colores disponibles en colorama
    """
    print(f"{Fore.BLACK}BLACK")
    print(f"{Fore.RED}RED")
    print(f"{Fore.GREEN}GREEN")
    print(f"{Fore.YELLOW}YELLOW")
    print(f"{Fore.BLUE}BLUE")
    print(f"{Fore.MAGENTA}MAGENTA")
    print(f"{Fore.CYAN}CYAN")
    print(f"{Fore.WHITE}WHITE")
    print(f"{Style.BRIGHT}BRIGHT")
    print(f"{Style.DIM}DIM")
    print(f"{Style.NORMAL}NORMAL")

# Ejemplos de uso
producto = ["manzana", "fruta", 1200]

print("=== Versión básica ===")
mostrar_producto(producto)

print("\n=== Versión con estilos ===")
mostrar_producto_con_estilo(producto)

print("\n=== Versión colorida ===")
mostrar_producto_colorido(producto)

print("\n=== Colores disponibles ===")
mostrar_colores_disponibles()

print("\n" + "-"*30 + "\n")

# Otro ejemplo
otro_producto = ["laptop", "electrónica", 50000]
print("=== Otro producto ===")
mostrar_producto(otro_producto)