# Dia 15 - Programa un modelo de machine learning

## Índice
- [Dia 15 - Programa un modelo de machine learning](#dia-15---programa-un-modelo-de-machine-learning)
  - [Índice](#índice)
  - [5.1. - Bibliotecas](#51---bibliotecas)
  - [5.2. - Definiciones](#52---definiciones)
  - [5.3. - Cuadernos de trabajo en Colab de google drive](#53---cuadernos-de-trabajo-en-colab-de-google-drive)
  - [Ficheros y documentación](#ficheros-y-documentación)


## 5.1. - Bibliotecas

- **numpy**: es una biblioteca de Python para computación científica que se utiliza para realizar operaciones matemáticas en matrices y vectores. Es muy útil en aplicaciones de análisis de datos, aprendizaje automático, procesamiento de señales y otras áreas de la ciencia y la ingeniería. *Documentación*: https://numpy.org/devdocs/user/index.html 
- **pandas**: es una biblioteca de Python para análisis de datos que se utiliza para manipular y analizar datos estructurados. Proporciona estructuras de datos y funciones para la limpieza, manipulación y análisis de datos en tablas y series de tiempo. Se le conoce como el excel de python. *Documentación*: https://pandas.pydata.org/pandas-docs/stable/ 
- **matplotlib**: es una biblioteca de Python para visualización de datos que se utiliza para crear gráficos y visualizaciones en 2D y 3D. Proporciona una amplia gama de tipos de gráficos, como gráficos de línea, gráficos de barras, gráficos de dispersión y gráficos de torta, y es muy útil en aplicaciones de análisis de datos y ciencia de datos. *Documentación*: https://matplotlib.org/stable/index.html 
- **Seaborn**: es una biblioteca de visualización de datos en Python que se basa en matplotlib. Proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos y informativos. Seaborn simplifica la creación de visualizaciones complejas al proporcionar estilos preestablecidos y funciones optimizadas para representar relaciones estadísticas. Es especialmente útil en el análisis exploratorio de datos y la presentación visual de resultados.  *Documentación*: https://seaborn.pydata.org/
- **scikit-learn (sklearn)**: es una biblioteca de aprendizaje automático de código abierto para Python que proporciona una amplia gama de algoritmos y herramientas para el análisis de datos. Es ampliamente utilizado en ciencia de datos debido a su facilidad de uso y eficiencia computacional. *Documentación*: https://scikit-learn.org/stable/
- **DecisionTreeClassifier**: es un módulo de scikit-learn es una implementación de un clasificador de árbol de decisiones en Python. Permite construir modelos de clasificación basados en árboles de decisión, que son diagramas de flujo donde cada nodo interno representa una característica, cada rama representa una regla de decisión y cada hoja representa una clase o una predicción. *Documentación*: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html 
- **accuracy_score**: es un módulo de scikit-learn que proporciona funciones para evaluar y visualizar el rendimiento de los modelos de clasificación. En concreto, calcula la precisión del modelo. *Documentación*: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html 
- **confusion_matrix**: es un módulo de scikit-learn que proporciona funciones para evaluar y visualizar el rendimiento de los modelos de clasificación. En concreto, genera una matriz de confusión que muestra la cantidad de aciertos y errores de cada clase. traza una representación gráfica de la matriz de confusión. *Documentación*: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html 
- **plot_confusion_matrix**: es un módulo de scikit-learn que proporciona funciones para evaluar y visualizar el rendimiento de los modelos de clasificación. En concreto, traza una representación gráfica de la matriz de confusión. DEPRECATED. En su luega utilizo ConfusionMatrixDisplay.
- **ConfusionMatrixDisplay**: es una clase en scikit-learn que permite visualizar de forma gráfica una matriz de confusión. Proporciona una representación visual clara y legible de los resultados de la clasificación. La matriz de confusión es una tabla que muestra las predicciones de un modelo de clasificación en comparación con las etiquetas verdaderas. La visualización de la matriz de confusión proporcionada por ConfusionMatrixDisplay puede ayudar a evaluar el rendimiento del modelo al mostrar de manera intuitiva los aciertos y los errores de clasificación para cada clase.  *Documentación*: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html 
- **tree**: es un módulo de scikit-learn que proporciona herramientas para visualizar los árboles de decisión creados por los modelos entrenados, lo que ayuda a comprender mejor cómo se toman las decisiones dentro del modelo. *Documentación*: https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree 

## 5.2. - Definiciones
La **ciencia de datos** o data Science es un campo especial de la ciencia que aplica métodos científicos, procesos y sistemas para poder extraer conocimiento o un mejor entendimiento de los datos en sus diferentes formas.

**Machine Learning (ML) o Aprendizaje Automático** es una rama de la inteligencia artificial que permite a las máquinas aprender a partir de datos y realizar tareas sin ser específicamente programadas para hacerlo. El objetivo es que la máquina pueda generalizar el conocimiento aprendido a partir de un conjunto de datos y aplicarlo en nuevas situaciones. Se utiliza en una amplia variedad de aplicaciones, incluyendo la visión por computadora, el procesamiento del lenguaje natural, la detección de fraude, el reconocimiento de voz, la predicción y la toma de decisiones.

**Datasets** -  Conjunto de datos

Un **documento Colab** es un archivo de Jupyter Notebook que se ejecuta en la plataforma de Google Colaboratory, lo que permite acceder a recursos de hardware y herramientas de análisis de datos y bibliotecas de Python desde cualquier lugar con acceso a internet.
## 5.3. - Cuadernos de trabajo en Colab de google drive

- **Cuaderno de prácticas con Numpy**: https://colab.research.google.com/drive/1vp7zrchG_pJF3uzEgbCjfb_piu43mJXS?usp=sharing
- **Cuaderno de prácticas con Panda**: https://colab.research.google.com/drive/1-E33EMCehgPnmqgwm13-SZSnVYOHMpuQ?usp=sharing
- **Cuaderno de prácticas con Matplotlib**: https://colab.research.google.com/drive/1MX9ee5h_TTEc0HqZA6f6Ns6J4rwReHOH?usp=sharing 
- **Cuaderno de prácticas con Machine Learning**: https://colab.research.google.com/drive/1zRVPpLLmhMkmhX_kB9qrWUppHzRTJPFM?usp=sharing 

Podemos conectar nuestro cuaderno con:
```python
from google.colab import drive
drive.mount('/content/drive')
```

Página original con el reto «supervivientes del Titanic»: https://www.kaggle.com/c/titanic

## Ficheros y documentación

- [cuaderno_machine_learning.py](cuaderno_machine_learning.py)
- [cuaderno_matplotlib.py](cuaderno_matplotlib.py)
- [cuaderno_numpy.py](cuaderno_numpy.py)
- [cuaderno_panda.py](cuaderno_panda.py)
- [DataSet_Titanic.csv](DataSet_Titanic.csv)
- [ventas-autos.csv](ventas-autos.csv)

[Documentación del día](../doc_curso/15_machine_learning/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)
