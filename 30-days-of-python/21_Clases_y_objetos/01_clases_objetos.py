"""
01_clases_objetos.py
"""
import statistics


# 1. Python tiene el módulo llamado estadísticas
# y podemos usar este módulo para realizar todos
# los cálculos estadísticos. Sin embargo,
# para aprender a crear funciones y reutilizar funciones,
# intentemos desarrollar un programa
# que calcule la medida de tendencia central de una muestra
# (media, mediana, moda) y la medida de variabilidad
# (rango, varianza, desviación estándar).
# Además de esas medidas, encuentra el mínimo, máximo,
# recuento, percentil y distribución de frecuencia de la muestra.
# Puedes crear una clase llamada Estadísticas
# y crear todas las funciones que realicen cálculos estadísticos
# como métodos para la clase Estadísticas.

class Estadisticas:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        mode = statistics.mode(self.data)
        count = self.data.count(mode)
        return {'moda': mode, 'recuento': count}

    def std(self):
        return statistics.stdev(self.data)

    def var(self):
        return statistics.variance(self.data)

    def freq_dist(self):
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1
        freq_dist = [(freq[value], value) for value in freq]
        freq_dist.sort(reverse=True)
        return freq_dist


edades = [
    31, 26, 34, 37, 27,
    26, 32, 32, 26, 27,
    27, 24, 32, 33, 27,
    25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

estadisticas = Estadisticas(edades)

print('Recuento:', estadisticas.count())
print('Suma: ', estadisticas.sum())
print('Mínimo: ', estadisticas.min())
print('Máximo: ', estadisticas.max())
print('Rango: ', estadisticas.range())
print('Media: ', estadisticas.mean())
print('Mediana: ', estadisticas.median())
print('Moda:')
for key, value in estadisticas.mode().items():
    print(f'\t - {key}: {value}')
print('Desviación Estándar: ', estadisticas.std())
print('Varianza: ', estadisticas.var())
freq_dist = estadisticas.freq_dist()
print('Distribución de Frecuencia:')
for freq, value in freq_dist:
    print(f'\t - {freq}, {value}')
print()

# 2. Crea una clase llamada CuentaPersona.
# Tiene propiedades de nombre, apellido,
# ingresos, gastos y tiene métodos de total_ingreso,
# total_gasto, info_cuenta, agregar_ingreso,
# agregar_gasto y saldo_cuenta.
# Ingresos es un conjunto de ingresos y su descripción.
# Lo mismo ocurre con los gastos.


class CuentaPersona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.ingresos = {}
        self.gastos = {}

    def total_ingreso(self):
        return sum(self.ingresos.values())

    def total_gasto(self):
        return sum(self.gastos.values())

    def info_cuenta(self):
        print(f'Nombre: {self.nombre} {self.apellido}')
        print(f'Total de ingresos: {self.total_ingreso()}')
        print(f'Total de gastos: {self.total_gasto()}')
        print(f'Saldo de cuenta: {self.total_ingreso() - self.total_gasto()}')

    def agregar_ingreso(self, descripcion, monto):
        self.ingresos[descripcion] = monto

    def agregar_gasto(self, descripcion, monto):
        self.gastos[descripcion] = monto

    def saldo_cuenta(self):
        return self.total_ingreso() - self.total_gasto()


cuenta = CuentaPersona('Juan', 'Pérez')
cuenta.agregar_ingreso('Salario', 5000)
cuenta.agregar_ingreso('Venta de acciones', 2000)
cuenta.agregar_gasto('Alquiler', 1500)
cuenta.agregar_gasto('Comida', 500)
cuenta.info_cuenta()
