"""
Módulo datime
Primera parte

- Almacenar hora y fecha en variables
- Cálculos de tiempo
- Mostrar en diferentes formatos

"""
import datetime

# Guardar en una variable la hora
mi_hora = datetime.time(17, 35, 50, 1300)
# Imprimir tipo de formato
print(f'Formato de datetime: {type(mi_hora)}')
# Imprimir la hora establecida
print(mi_hora)
# Imprimir un elemento de la hora
print(mi_hora.minute)


print()
# Guardar en variable la fecha
mi_fecha = datetime.date(2025, 10, 23)
# Mostrar fecha
print(mi_fecha)
# Mostrar un elemento de fecha
print(mi_fecha.year)
# Cambiar el formato a la fecha
print(mi_fecha.ctime())
# Mostrar el día de hoy
print(mi_fecha.today())
