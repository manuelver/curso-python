# Clases y objetos

Documento original en inglés: [Classes and Objects](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md)

## Ejercicios

### Ejercicios: Nivel 1

1. Python tiene el módulo llamado estadísticas y podemos usar este módulo para realizar todos los cálculos estadísticos. Sin embargo, para aprender a crear funciones y reutilizar funciones, intentemos desarrollar un programa que calcule la medida de tendencia central de una muestra (media, mediana, moda) y la medida de variabilidad (rango, varianza, desviación estándar). Además de esas medidas, encuentra el mínimo, máximo, recuento, percentil y distribución de frecuencia de la muestra. Puedes crear una clase llamada Estadísticas y crear todas las funciones que realicen cálculos estadísticos como métodos para la clase Estadísticas. Mira la salida a continuación.

```python
edades = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Recuento:', data.count()) # 25
print('Suma: ', data.sum()) # 744
print('Mínimo: ', data.min()) # 24
print('Máximo: ', data.max()) # 38
print('Rango: ', data.range()) # 14
print('Media: ', data.mean()) # 30
print('Mediana: ', data.median()) # 29
print('Moda: ', data.mode()) # {'moda': 26, 'recuento': 5}
print('Desviación Estándar: ', data.std()) # 4.2
print('Varianza: ', data.var()) # 17.5
print('Distribución de Frecuencia: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
``` 

```python
# Tu resultado debería lucir de la siguiente manera
print(data.describe())
Recuento: 25
Suma:  744
Mínimo:  24
Máximo:  38
Rango:  14
Media:  30
Mediana:  29
Moda:  (26, 5)
Varianza:  17.5
Desviación Estándar:  4.2
Distribución de Frecuencia: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### Ejercicios: Nivel 2

1. Crea una clase llamada CuentaPersona. Tiene propiedades de nombre, apellido, ingresos, gastos y tiene métodos de total_ingreso, total_gasto, info_cuenta, agregar_ingreso, agregar_gasto y saldo_cuenta. Ingresos es un conjunto de ingresos y su descripción. Lo mismo ocurre con los gastos.

[<< Day 20](../20_Gestor_de_paquetes_de_Python/README.md) | [Day 22 >>](../22_Web_scraping/README.md)
