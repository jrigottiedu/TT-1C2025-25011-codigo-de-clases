# Durante el After sugirieron el uso de la siguiente estructura
# que nos permite aplicar "color" a las impresione en consola!

# Inicializamos unas constantes con el código del color

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Al momento de imprimir, simplemente agregamos el color y el reset al final
print(f"{CYAN} --- MENÚ --- {RESET}")
print(f"{GREEN} Bienvenidos a mi App en Python {RESET}")
print()
print(f"{YELLOW} Este es un mensaje de alerta! {RESET}")
print()
print(f"{RED} Este es un mensaje de Error! {RESET}")
print()
print(f"{BLUE} Gracias por usar nuestra App {RESET}")