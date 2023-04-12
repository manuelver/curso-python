"""
Módulo datime 
Segunda parte

"""
from datetime import datetime, timedelta, date

# Para los siguientes ejercicios
# se debe importar un objeto
# llamado datetime que se encuentra
# en el módulo datetime, el cuál crea conflicto
# con el anterior ejercicio import datetime

mi_dia = datetime(2025, 5, 15, 22, 10, 15, 2500)

print(mi_dia)

# Se puede reemplazar elementos
mi_dia = mi_dia.replace(month=11)

print(mi_dia)


print()
# Se pueden calcular tiempos
# se debe importar date

# Variables de nacimiento y de hoy
nacimiento = date(1983, 10, 30)
hoy = date.today()
# Se resta
tiempo_vida = hoy - nacimiento
# Se muestra en dias
print(tiempo_vida.days)

# También podemos calcular horas

despertar = datetime(2023, 3, 30, 6, 30)
dormir = datetime(2023, 3, 30, 23, 35)

tiempo_despierto = dormir - despertar

# Podemos verlo en segundos
print(tiempo_despierto.seconds)

print()
# Minutos ahora

hoys = datetime(2100, 10, 20, 10, 20).today().time().minute

print(hoys)


# Calcular el tiempo
# Extra. Importo timedelta para probarlo

hora_actual = datetime.now() + timedelta(hours=5, minutes=50)

print('{:%H:%M}'.format(hora_actual))
