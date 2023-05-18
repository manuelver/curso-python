# Curso de python
## [Manuel Vergara](https://vergaracarmona.es) – 2023


Este documento contiene los apuntes tomados en el curso «[Python total](https://www.udemy.com/course/python-total)» impartido por «Escuela Directa» en enero y febrero de 2023. El curso udemy consta de 30 horas aproximadamente de vídeo-tutoriales. Las prácticas aquí contenidas tuvieron una duración de alrededor de unas 150 horas.

Los apuntes no fueron pensados para compartirlos, por ello pueden tener lagunas de información o contenido adicional respecto al curso, ya que se redactaron para recordar procedimientos y conceptos que el autor creyó relevantes. Teniendo un documento, a mi parecer, tan completo y entendiendo que el conocimiento debe ser libre se decidió compartirlo. 

Si te parece útil este documento puedes agradecerlo a través de las vías de contacto de la web https://vergaracarmona.es 

Recuerda, 
>*"Quien se corta su propia leña se calienta dos veces"*

---
<br>

## Licencia

![](https://creativecommons.org/wp-content/themes/cc/images/cc.logo.white.svg)

Esta obra está bajo una Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional. Para ver una copia de esta licencia, visite https://creativecommons.org/licenses/by-sa/4.0/legalcode.es.

Usted es libre de:
- Compartir — copiar y redistribuir el material en cualquier medio o formato
- Adaptar — remezclar, transformar y crear a partir del material para cualquier finalidad, incluso comercial.

Bajo las condiciones siguientes:
- Reconocimiento — Debe reconocer adecuadamente la autoría, proporcionar un enlace a la licencia e indicar si se han realizado cambios. Puede hacerlo de cualquier manera razonable, pero no de una manera que sugiera que tiene el apoyo del licenciador o lo recibe por el uso que hace.
- Compartir Igual — Si remezcla, transforma o crea a partir del material, deberá difundir sus contribuciones bajo la misma licencia que el original.

![](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)

- No hay restricciones adicionales — No puede aplicar términos legales o medidas tecnológicas que legalmente restrinjan realizar aquello que la licencia permite.

Esta licencia está aceptada para Obras Culturales Libres.
El licenciador no puede revocar estas libertades mientras cumpla con los términos de la licencia.

---
<br>

##  Índice de las materias de los días

- [Día 1 - Programa un creador de nombres](dia_01/README.md)
  - 1.1. - print
  - 1.2. - strings
  - 1.3. - input
  - 1.4. - Proyecto del Día 1
- [Día 2 - Programa un calculador de comisiones](dia_02/README.md)
  - 2.1. - Tipos de datos
  - 2.2. - Variables
  - 2.3. - Nombres de variables
  - 2.4. - integers & floats
  - 2.5. - Conversiones
  - 2.6. - Formatear cadenas
  - 2.7. - Operadores matemáticos
  - 2.8. - Redondeo
  - 2.9. - Proyecto del Día 2
- [Día 3 - Programa un analizador de texto](dia_03/README.md)
  - 3.1. - Index( )
  - 3.2. - Substrings
  - 3.3. - Métodos para Strings
  - 3.4. - Strings: propiedades
  - 3.5. - Listas
  - 3.6. - Diccionarios
  - 3.7. - Tuples
  - 3.8. - sets
  - 3.9. - booleanos
  - 3.10. - Proyecto del Día 3
- [Día 4 - Programa el juego "adivina el número"](dia_04/README.md)
  - 4.1. - Operadores de comparación
  - 4.2. - Operadores lógicos
  - 4.3. - Control de flujo
  - 4.4. - loops while
  - 4.5. - range( )
  - 4.6. - enumerate( )
  - 4.7. - zip( )
  - 4.8. - min( ) & max( )
  - 4.9. - random
  - 4.10. - Comprensión de listas
  - 4.11. - match
  - 4.12. - Proyecto del Día 4
- [Día 5 - Programa el juego "El ahorcado"](dia_05/README.md)
  - 5.1. - Documentación
  - 5.2. - Funciones
  - 5.3. - return
  - 5.4. - Funciones dinámicas
  - 5.5. - Interacción entre funciones
  - 5.6. - *args
  - 5.7. - **kwargs
  - 5.8. - Ejercicios
  - 5.9. - Proyecto del Día 5
- [Día 6 - Programa un recetario](dia_06/README.md)
  - 6.1. - Abrir y leer archivos
  - 6.2. - Crear y escribir archivos
  - 6.3. - Directorios
  - 6.4. - pathlib
  - 6.5. - Path
  - 6.6. - Limpiar la consola
  - 6.7. - Archivos + funciones
  - 6.8. - Proyecto del Día 6
- [Día 7 - Programa una cuenta bancaria](dia_07/README.md)
  - 7.1. - Clases
  - 7.2. - Atributos
  - 7.3. - Métodos
  - 7.4. - Tipos de métodos
  - 7.5. - Herencia
  - 7.6. - Herencia extendida
  - 7.7. - Polimorfismo
  - 7.8. - Pilares de la Programación Orientada a Objetos
  - 7.9. - Métodos especiales
  - 7.10. - Proyecto del Día 7
- [Día 8 - Programa una consola de turnos](dia_08/README.md)
  - 8.1. - Instalar paquetes
  - 8.2. - Módulos y paquetes
  - 8.3. - Manejo de errores
  - 8.4. - pylint
  - 8.5. - unittest
  - 8.6. - Decoradores
  - 8.7. - Generadores
  - 8.8. - Proyecto del Día 8
- [Día 9 - Programa un buscador de números de serie](dia_09/README.md)
  - 9.1. - Módulo collections
  - 9.2. - Módulos shutil & os
  - 9.3. - Módulo datetime
  - 9.4. - Módulo para medir el tiempo
  - 9.5. - Módulo math
  - 9.6. - Expresiones regulares
  - 9.7. - Comprimir y descomprimir archivos
  - 9.8. - Proyecto del Día 9
- [Día 10 - Programa el juego "Invasión espacial"](dia_10/README.md)
  - 10.1. - Distancia entre dos puntos
  - 10.2. - Convertir el Juego en un Archivo Ejecutable (.exe)
- [Día 11 - Programa un extracto de datos web](dia_11/README.md)
  - 11.1. - Extraer elementos de una clase
- [Día 12 - Programa un gestor de restaurantes](dia_12/README.md)
- [Día 13 - Programa un asistente de voz](dia_13/README.md)
  - 13.1. - Librerias y módulos
  - 13.2. - Algunos problemas con las bibliotecas
  - 13.3. - Enlaces
- [Día 14 - Programa un controlador de asistencia](dia_14/README.md)
  - 14.1. - Bibliotecas
- [Día 15 - Programa un modelo de machine learning](dia_15/README.md)
  - 5.1. - Bibliotecas
  - 5.2. - Definiciones
  - 5.3. - Cuadernos de trabajo en Colab de google drive
- [Día 16 - Programa una aplicación web de tareas pendientes](dia_16/README.md)
  - 16.1. - Entornos Virtuales
  - 16.2. - Módulos
  - 16.3. - Preparación de estructura de trabajo
  - 16.4. - Configurar url
  - 16.5. - Crear tabla de tareas
  - 16.6. - Configurar la vista
  - 16.7. - Configurar la vista de Detalle
  - 16.8. - Crear Links a Detalle
  - 16.9. - Agregar nueva tarea
  - 16.10. - Formulario para nueva tarea
  - 16.11. - Editar tarea
  - 16.12. - Eliminar tarea
  - 16.13. - Crear la lógica de Logueo / Deslogueo
  - 16.14. - Formulario de Logueo / Deslogueo
  - 16.15. - Restringir acceso
  - 16.16. - Información específica de usuario
  - 16.17. - Registrar nuevo usuario
  - 16.18. - Barra de búsquedas
  - 16.19. - Un estilo para todas las vistas
  - 16.20. - Estilo general
  - 16.21. - Estilo de barra superiores
  - 16.22. - estilo de la lista
  - 16.23. - Estilo de la barra de cerca
  - 16.24. - Terminar el sitio
- [Día 17 - Extra bibliotecas para hacking ético](dia_17/README.md)
  - 17.1. - Bibliotecas
