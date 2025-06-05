"""
1.
¿Cuál de las siguientes opciones describe una función con un parámetro opcional?
"""
# def saludar(nombre, saludo="Hola"):
#     print(f"{saludo}, {nombre}!")

# # Ejemplos de uso
# saludar("Ana")              # Usa el saludo por defecto: "Hola"
# saludar("Ana", "Buenas")  # Usa el saludo personalizado: "Buenas"

"""
2.
¿Cuál de los siguientes beneficios se asocia con el uso de docstrings?"""
# def saludar(nombre, saludo="Hola"):
#     """
#     Imprime un saludo personalizado.

#     Parámetros:
#     nombre (str): El nombre de la persona a saludar. Obligatorio.
#     saludo (str): El saludo a utilizar. Opcional, por defecto es "Hola".

#     Ejemplos:
#     >>> saludar("Ana")
#     Hola, Ana!

#     >>> saludar("Juan", "Buenas tardes")
#     Buenas tardes, Juan!
#     """
#     print(f"{saludo}, {nombre}!")

# saludar()
# help(saludar)
"""
3. 
¿Cuál es la ventaja principal de devolver múltiples valores desde una función?
"""
# def calcular_area_perimetro_rectangulo(base, altura):
#     """
#     Calcula el área y el perímetro de un rectángulo.

#     Parámetros:
#     base (float): La base del rectángulo.
#     altura (float): La altura del rectángulo.

#     Retorna:
#     tuple: Una tupla con el área y el perímetro, en ese orden.

#     Ejemplo:
#     >>> area, perimetro = calcular_area_perimetro_rectangulo(5, 3)
#     >>> print(area)      # 15
#     >>> print(perimetro) # 16
#     """
    
#     area = base * altura
#     perimetro = 2 * (base + altura)
#     return area, perimetro, 1 # este retorno es una tupla

# area, perimetro, numero = calcular_area_perimetro_rectangulo(3, 5)
# print(area, perimetro, numero)
"""
6.
¿Qué se necesita para modificar una variable global dentro de una función?
"""
# contador = 0  # Variable global

# def incrementar():
#     global contador  # Indicamos que usaremos la variable global
#     contador += 1

# incrementar()
# print(contador)  # Resultado: 1

"""
7.
¿Qué sucede cuando una lista es pasada como parámetro a una función?
"""
# declaramos una lista global
# numeros = [1, 2, 3]

# # declaracion de la funcion
# def agregar_elemento(lista):
#     print(f"posicion de memoria de numeros dentro de la funcion {id(lista)}")
#     lista.append(100)  # Modifica la lista original

# # llamada
# print(f"posicion de memoria de numeros en el cuerpo principal {id(numeros)}")
# print(f"numeros antes de la llamada {numeros}")
# agregar_elemento(numeros)
# print(f"numeros despues de la llamada {numeros}")  # Resultado: [1, 2, 3, 100]

"""
8.
¿Qué sucede si llamás a una función que no tiene una sentencia return explícita?
"""
# def saludar():
#     print("Hola!")
#     # return "funciono"

# # saludar()
# resultado = saludar()
# print(resultado)  # Imprime: None

"""
9.
¿Qué tipo de dato es útil para devolver varios resultados relacionados de una función?
"""
# def calcular_medidas(rect_base, rect_altura):
#     """
#     Calcula el área y el perímetro de un rectángulo.
#     Devuelve ambos resultados en una tupla.
#     """
#     area = rect_base * rect_altura
#     perimetro = 2 * (rect_base + rect_altura)
#     resultado = {
#         "area": area,
#         "perimetro": perimetro
#     }
#     # return area, perimetro  # Se retorna una tupla
#     return resultado  # Se retorna un diccionario

# Uso de la función
# resultado = calcular_medidas(4, 3)
# print(resultado)           # Imprime: (12, 14)

# También podés desempaquetar o desestructurar
# a, p = calcular_medidas(4, 3)
# print(f"Área: {a}, Perímetro: {p}")

# Aqui usando diccionarios
# calculo = calcular_medidas(4,3)
# print(f"Área: {calculo.get("area")}, Perímetro: {calculo.get("perimetro")}")

"""
12.
En el siguiente código, ¿qué se imprime?
"""
# def suma(a, b):
#     # suma = a + b
#     # return suma
#     return a + b

# resultado = suma(3, 4)

# print(resultado)