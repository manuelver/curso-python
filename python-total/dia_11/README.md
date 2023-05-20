**A partir de este tema la mayoría son ejercicios prácticos. Como has visto hasta ahora, el código está documentado y es una buena fuente de apuntes.**

# Día 11 - Programa un extracto de datos web

Web scraping = raspar internet
- Reglas del web scraping
- Limitaciones del web scraping

Se utilizarán tres bibliotecas: beautifulsoup4, lxml y requests. Se deben instalar:
```python
pip install beautifulsoup4
pip install requests
```

Enlace: https://escueladirecta-blog.blogspot.com/

## Índice
- [Día 11 - Programa un extracto de datos web](#día-11---programa-un-extracto-de-datos-web)
  - [Índice](#índice)
  - [11.1. - Extraer elementos de una clase](#111---extraer-elementos-de-una-clase)
  - [Ficheros y documentación](#ficheros-y-documentación)

## 11.1. - Extraer elementos de una clase

| Carácter  |           Sintaxis            | Resultados                                                                                       |
| :-------: | :---------------------------: | :----------------------------------------------------------------------------------------------- |
|     "     |     `soup.select('div')`      | Todos los elementos con la etiqueta 'div'                                                        |
|     #     |  `soup.select('#estilo_4')`   | Elementos que contengan id='estilo4'                                                             |
|     .     | `soup.select('.columna_der')` | Elementos que contengan class='columna der'                                                      |
| (ESPACIO) |   `soup.select('div span')`   | Cualquier elemento llamado 'span' dentro de un elemento 'div'                                    |
|     >     |   `soup.select('div>span')`   | Cualquier elemento llamado 'span' directamente dentro de un elemento 'div', sin nada en el medio |

Enlace: https://www.escueladirecta.com/courses

Enlace: https://toscrape.com/

## Ficheros y documentación
- [01_web_scraping_01.py](01_web_scraping_01.py)
- [02_web_scraping_02.py](02_web_scraping_02.py)
- [mi_imagen.jpg](mi_imagen.jpg)
- [programa_web_scraping.py](programa_web_scraping.py)

[Documentación del día](../doc_curso/11_web_scraping/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)
