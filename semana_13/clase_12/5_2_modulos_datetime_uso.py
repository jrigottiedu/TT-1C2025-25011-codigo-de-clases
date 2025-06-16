from datetime import datetime, date


# fecha_hoy = "16_06_2025"
# fecha_primavera = "21_09_2025"
fecha_hoy = datetime.now().date()
fecha_primavera = date(2025, 9, 21)
dias_primavera = fecha_primavera - fecha_hoy

print(f"Faltan {dias_primavera.days} días para la Primavera!!")