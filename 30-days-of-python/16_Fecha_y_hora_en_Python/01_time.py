"""
01_time.py
"""
from datetime import datetime
import locale

# 1. Obtener el día actual,
# mes, año, hora, minuto
#  y marca de tiempo actual
# desde el módulo datetime.
now = datetime.now()
print("Día actual:", now.day)
print("Mes actual:", now.month)
print("Año actual:", now.year)
print("Hora actual:", now.hour)
print("Minuto actual:", now.minute)
print("Marca de tiempo actual:", now)
print()

# 2. Formatear la fecha actual
# utilizando este formato:
# "%m/%d/%Y, %H:%M:%S".
formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Fecha formateada:", formatted_now)
print()

# 3. Cambiar la cadena de tiempo
# "5 de diciembre de 2019"
# a un objeto de tiempo.

# Establecer el idioma en español
# porque sino no funciona,
# el idioma por defecto es el inglés.
locale.setlocale(locale.LC_ALL, 'es_ES')

time_str = "05 de diciembre de 2019"
time_obj = datetime.strptime(time_str, "%d de %B de %Y")
print("Objeto de tiempo:", time_obj)
print()

# 4. Calcular la diferencia de tiempo entre ahora y el Año Nuevo.
new_year = datetime(2022, 1, 1)
time_diff = new_year - now
print("Diferencia de tiempo hasta el Año Nuevo:\n", time_diff)
print()

# 5. Calcular la diferencia de tiempo entre
# el 1 de enero de 1970 y ahora.
epoch = datetime(1970, 1, 1)
time_diff = now - epoch
print(
    "Diferencia de tiempo desde el 1 de enero de 1970 hasta ahora:\n",
    time_diff
)
print()

# 6. Ejemplos de uso del módulo datetime:
# - Análisis de series temporales.

# Lista de fechas
fechas = ["2023-09-01", "2023-09-15", "2023-09-30"]

# Convertir las fechas a objetos datetime
fechas_dt = [
    datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas
]
print()

# Calcular la diferencia entre fechas
diferencia = fechas_dt[-1] - fechas_dt[0]

print("Diferencia de tiempo:", diferencia)


# - Obtener una marca de tiempo de cualquier actividad en una aplicación.

# Registra la actividad
actividad = "Usuario inició sesión"
tiempo_actividad = datetime.now()

print(f"{actividad} a las {tiempo_actividad}")
print()


# - Publicar entradas en un blog.

# Contenido de la entrada del blog
contenido = "Hoy estoy publicando mi primera entrada en el blog."

# Fecha y hora de publicación
# Año, mes, día, hora, minuto
fecha_publicacion = datetime(2023, 9, 29, 15, 30)

# Publicar la entrada
print(f"Entrada publicada el {fecha_publicacion}:\n{contenido}")
print()
