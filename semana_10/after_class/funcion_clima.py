"""
2 parametros

1ero: temperatura:  0 y 30 grados
2do: cielo: soleado - nublado - llueve

primer caso: Dia lindo
temp 20 - 30
cielo: soleado

primer caso: Dia mas o menos
temp 10 - 20
cielo: nublado

tercer caso: Dia feo
temp 0 - 10
cielo: llueve
"""


# declaracion de la funcion
def evaluarClima(
    temperatura, cielo, humedad, presion_atmosferica=1013
):  # parametro temperatura = argumento varTemperatura
    # escribir mi funcion...
    if cielo == "soleado" and temperatura >= 20 and temperatura < 30:
        print("Dia lindo")
    elif cielo == "nublado" and temperatura >= 10 and temperatura < 20:
        print("Dia mas o menos")
    elif cielo == "llueve" and temperatura < 10:
        print("Dia feo")
    else:
        print("No fui entrenado para evaluar esas condiciones")


# declaramos las variables
varTemperatura = 25
varCielo = "llueve"
varHumedad=input("Ingrese la humedad")

# llamado o invocacion
evaluarClima(humedad = varHumedad, temperatura=varTemperatura, cielo=varCielo)
