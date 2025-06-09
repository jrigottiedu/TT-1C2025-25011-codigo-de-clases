# Evaluemos algunos ejemplos de errores

# value error 
try:
    precio = int(input("Ingrese el precio del producto: "))
# except Exception as error:
#     print(f"Error encontrado al ingresar el precio: {error}")
except ValueError:
    print(f"Debe ingresar un dato numerico")
except KeyboardInterrupt:
    print(f"ERROR: Interrumpido por el usuario")
else:
    print(f"El precio ingresado es: {precio}")

continua = input("Continua? s/n: ")
