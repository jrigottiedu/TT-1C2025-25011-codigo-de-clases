""" Evaluemos algunos ejemplos de errores

Caso 1: ValueError
Supongamos el caso que ingresamos el precio del producto:

precio = int(input("Ingrese el precio del producto: "))

si convertimos a int una cadena no numérica, se va a generar una exception
del tipo ValueError. Corre el código y verifica que sucede si ingresas como precio 1r

--------------------------------------------------------------------------------------
Caso 1: IndexError

Supongamos este otro caso, tenemos la lista temporal producto con 3 elementos:

producto = ["manzana", "fruta", 1500]

donde:
producto[0] contiene "manzana"
producto[1] contiene "fruta"
producto[2] contiene 1500

Si intento imprimir la lista producto y le paso como índice 3
va a generar la exeption IndexError

print(producto[3])
Verificalo

--

Para evitar la interrupción abrupta del programa,
lo que hacemos es "encapsular" los bloques de código que,
por la dinámica del programa, podrían generar una exception

"""


# Caso 1: aplicamos try-except
try:
    precio = int(input("Ingrese el precio del producto: "))
except ValueError:
    print(f"Debe ingresar un dato numerico")
else:
    print(f"El precio ingresado es: {precio}")

"""
Explicación:
1. se ejecuta el código dentro de try
2. si se genera una exception del tipo ValueError,
    se ejecuta el código dentro de except ValueError
3. si no se genera ninguna exception, entonces se ejecuta el código dentro del else
"""

# Caso 2: IndexError

# declaro e inicializo la lista producto
producto = ["manzana", "fruta", 1500]

try:
    indice = int(input("Ingrese el índice del elemento a mostrar: "))
    print(producto[indice])
except IndexError:
    print("Indice fuera de rango")


# Caso 1 y 2 combinados:
"""
En el código del Caso 2, que sucede si ingresamos un número no válido como índice?
Verificalo.

Retorna un ValueError, cierto?
Veamos como resolverlo!!
"""

# Lo que hacemos es agregar otro bloque except:
try:
    indice = int(input("Ingrese el índice del elemento a mostrar: "))
    print(producto[indice])
except ValueError:
    print("Indice no válido!")
except IndexError:
    print("Indice fuera de rango")

"""
Explicación:
1. si ingreso 4 como índice imprime: Indice fuera de rango
2. si ingreso r como índice imprime: Indice no válido
"""

# Veamos una versión más completa:
while True:
    try:
        indice = int(input("Ingrese el índice del elemento a mostrar: "))
        print(producto[indice])
    except ValueError:
        print("Indice no válido!")
    except IndexError:
        print("Indice fuera de rango")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        continuar = input("Continúa probando? s/n:").strip().lower()
        if continuar == "s":
            continue
        else:
            break

"""
Explicación:
1. Ahora tenemos una estructura más robusta!
2. Capturamos ValueError e IndexError con sus correspondientes print
3. En caso que surja otra exception, 
    la capturamos con el bloque genérico except Exception as error:
4. Agregamos la sentencia finally, independientemente de lo que suceda 
    siempre se ejecuta, asi que lo aprovechamos para validar 
    si el bucle principal continúa o no.
"""