# importamos libreria y modulos
from datetime import datetime, date, time, timedelta



# obtener fecha y hora actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)
print("Solo la fecha:", ahora.date())
print("Solo la hora:", ahora.time())



# crear un objeto de fecha a partir de una cadena
mi_fecha = date(2025, 6, 16) # año, mes, dia
print("Fecha personalizada:", mi_fecha)



# crear un objeto de fecha a partir de una cadena
mi_hora = time(14, 30, 0)
print("Hora personalizada:", mi_hora)


# restar o sumar dias con timedelta
hoy = date.today()
ayer = hoy - timedelta(days=1)
anteayer = hoy - timedelta(days=2)
maniana = hoy + timedelta(days=1)

print("Ayer fue:", ayer)
print("Anteayer fue:", anteayer)
print("Mañana será:", maniana)



# calcular diferencia entre fechas
fecha1 = date(2025, 6, 1) # 1 de junio de 2025 YYYY-MM-DD
fecha2 = date(2025, 6, 16) # 16 de junio de 2025

diferencia = fecha2 - fecha1
print("Días entre fechas:", diferencia.days)



# convertir formatos de fechas: date a str
formato = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Formato legible:", formato)



# convertir formatos de fechas: str a date
fecha_str = "16/06/2025"
fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
print("Fecha convertida desde string:", fecha_obj.date())
