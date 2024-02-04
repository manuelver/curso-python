# Cursos de python 🐍 

Este repositorio contiene los apuntes tomados en diversos cursos de python reflejados en la siguiente tabla:

|                          Nombre del curso <br> y ubicación |   Nivel    | Duración <br> de vídeos | Duración <br> personal aprox. | Fuente original                                                                                         |
| ---------------------------------------------------------: | :--------: | :---------------------: | :---------------------------: | :------------------------------------------------------------------------------------------------------ |
|                         [HolaMundo](./HolaMundo/README.md) |    Bajo    |         5 horas         |           15 horas            | [Aprende python ahora!](https://www.youtube.com/watch?v=tQZy0U8s9LY&ab_channel=HolaMundo)               |
|                   [Python total](./python-total/README.md) | Intermedio |        30 horas         |           200 horas           | [Escuela Directa](https://www.udemy.com/course/python-total)                                            |
|             [Python y ChatGPT](./python-chatgpt/README.md) | Intermedio |         2 horas         |           15 horas            | [Escuela Directa](https://www.udemy.com/course/python-chatgpt/), [ChapGPT](https://www.chat.openai.com) |
|         [30 days of python](./30-days-of-python/README.md) | Intermedio |           ---           |           25 horas            | [Repo Asabeneh](https://github.com/Asabeneh/30-Days-Of-Python)                                          |
|                   [Cajón de sastre](./catch-all/README.md) | Intermedio |           ---           |           continua            | [Personal](https://vergaracarmona.es)                                                                   |
| [scripts-hacking-etico](./scripts-hacking-etico/README.md) |  Avanzado  |           ---           |            5 horas            | [ChapGPT](https://www.chat.openai.com), [Canal Telegram](https://t.me/seguridadinformatic4)             |
|             [Python ofensivo](./python-ofensivo/README.md) |  Avanzado  |        35 horas         |           100 horas           | [hack4u](https://hack4u.io)                                                                             |

Las prácticas y ejercicios aquí contenidos son los que hice mediante los cursos mencionados o por investigación propia, con mucho café para combatir el insomnio. Realmente, los apuntes no fueron pensados para compartirlos, por ello pueden tener lagunas de información o contenido adicional respecto al curso, ya que se redactaron para recordar procedimientos y conceptos que EMHO me parecieron relevantes. Teniendo estos documentos tan completos y entendiendo que el conocimiento debe ser libre, se decidió compartirlos. Si encuentras **cualquier error puedes abrir una issue o contactar conmigo**.

Si te parece útil este documento puedes agradecerlo a través de las vías de contacto de la [web](https://vergaracarmona.es) o [invítandome a un café ☕️](#invítame-a-un-café)

Recuerda, 

> *"Quien se corta su propia leña se calienta dos veces"* 

![](https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif)
---
<br>

## Información sobre python

<details>
<summary><strong> Qué es python según chatGPT 🤖</strong></summary>
Python es un lenguaje de programación interpretado y de alto nivel. Python se destaca por su sintaxis clara y legible, lo que lo hace muy accesible tanto para principiantes como para programadores experimentados.

Una de las características distintivas de Python es su enfoque en la legibilidad del código, lo que se conoce como el principio "bello es mejor que feo" (beautiful is better than ugly). Esto se logra mediante el uso de una sintaxis clara y estructurada que facilita la comprensión y el mantenimiento del código.

Python es un lenguaje multipropósito, lo que significa que se puede utilizar para una amplia variedad de aplicaciones, como desarrollo web, análisis de datos, inteligencia artificial, automatización de tareas, desarrollo de juegos y más. Tiene una amplia biblioteca estándar que proporciona módulos y funciones para realizar diversas tareas comunes, lo que facilita el desarrollo de aplicaciones sin tener que escribir todo desde cero.

Una de las razones por las que Python ha ganado popularidad es su comunidad activa y su ecosistema de paquetes. Existen numerosas bibliotecas y marcos de trabajo desarrollados por la comunidad que amplían las capacidades de Python en diferentes áreas, como Django para desarrollo web, NumPy y pandas para análisis de datos, TensorFlow y PyTorch para aprendizaje automático, entre otros.

Además, Python es conocido por ser un lenguaje fácil de aprender y utilizar. Su sintaxis intuitiva y legible permite a los programadores escribir código de manera más rápida y eficiente, lo que reduce el tiempo de desarrollo y facilita la colaboración en proyectos.

En resumen, Python es un lenguaje de programación de alto nivel, interpretado y fácil de aprender que se utiliza ampliamente en una variedad de aplicaciones, desde desarrollo web hasta análisis de datos e inteligencia artificial. Su enfoque en la legibilidad del código y su comunidad activa lo convierten en una elección popular entre los programadores.
</details>

<details>
<summary><strong>Historia de python 🏛️</strong></summary>
Python fue creado a finales de los años ochenta por [Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum) en Stichting Mathematisch Centrum (CWI), en los Países Bajos, como un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.

El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos [Monty Python](https://youtu.be/aQqhR26FOW8).

Guido van Rossum es el principal autor de Python, y su continuo rol central en decidir la dirección de Python es reconocido, refiriéndose a él como [Benevolente Dictador Vitalicio](https://es.wikipedia.org/wiki/Benevolent_Dictator_for_Life); sin embargo el 12 de julio de 2018 declinó de dicha situación de honor sin dejar un sucesor o sucesora y con una declaración altisonante:8

> *"Entonces, ¿qué van a hacer todos ustedes? ¿Crear una democracia? ¿Anarquía? ¿Una dictadura? ¿Una federación?"* 
> 
> Guido van Rossum

En 2019, Python fue el lenguaje de programación más popular en GitHub, superando a Java, el segundo lenguaje más popular, por más de 1 millón de repositorios.
</details>

<details>
<summary><strong>PEP 20 - Zen de Python 📄</strong></summary>
El Zen de Python es una colección de 20 principios de software que influyen en el diseño del Lenguaje de Programación Python, de los cuales 19 fueron escritos por Tim Peter en junio de 1999. El texto es distribuido como dominio público: 

```
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Espaciado es mejor que denso.
La legibilidad es importante.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Sin embargo la practicidad le gana a la pureza.
Los errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
A pesar de que eso no sea obvio al principio a menos que seas Holandés.
Ahora es mejor que nunca.
A pesar de que nunca es muchas veces mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea, ¡tengamos más de esos!
```
</details>

<details>
<summary><strong>Últimas versiones 🔄</strong></summary>
Python 2.7.x (última versión de la serie Python 2.x) fue oficialmente descontinuado el 1 de enero de 2020 (paso inicialmente planeado para 2015), por lo que ya no se publicarán parches de seguridad y otras mejoras para él. Con el final del ciclo de vida de Python 2, solo tienen soporte la rama Python 3.6.x y posteriores.

Con Python 3.5 llegaría el soporte incluido para entrada/salida asíncrona a través de la biblioteca asyncio, orientada a aplicaciones que requieren alto rendimiento de código concurrente, como servidores web, bibliotecas de conexión de bases de datos y colas de tareas distribuidas.

En la actualidad, Python se aplica en los campos de inteligencia artificial y machine learning.

</details>

<details>
<summary>Tabla de <strong>Usos de Python y sus Bibliotecas/módulos 📚</strong></summary>

|                                          Uso principal | Bibliotecas/módulos utilizados                                                |
| -----------------------------------------------------: | :---------------------------------------------------------------------------- |
|                                Acceso a bases de datos |                                                                               |
|                                                        | [SQLAlchemy](https://www.sqlalchemy.org/)                                     |
|                                                        | [psycopg2](https://www.psycopg.org/)                                          |
|                                                        | [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)    |
|                                                        | [pymongo](https://pymongo.readthedocs.io/)                                    |
|                                                        | [MongoDB](https://pymongo.readthedocs.io/)                                    |
|                                                        | [Redis](https://redis-py.readthedocs.io/)                                     |
|                                                        | [Cassandra](https://pypi.org/project/cassandra-driver/)                       |
|         Análisis y manipulación de datos geoespaciales |                                                                               |
|                                                        | [GeoPandas](https://geopandas.org/)                                           |
|                                                        | [Shapely](https://pypi.org/project/Shapely/)                                  |
|                                                        | [Folium](https://python-visualization.github.io/folium/)                      |
|                      Análisis y visualización de datos |                                                                               |
|                                                        | [Seaborn](https://seaborn.pydata.org/)                                        |
|                                                        | [Plotly](https://plotly.com/python/)                                          |
|                                                        | [Bokeh](https://bokeh.org/)                                                   |
|                                                        | [Dash](https://plotly.com/dash/)                                              |
|                                                        | [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)              |
| Análisis de texto y procesamiento del lenguaje natural |                                                                               |
|                                                        | [NLTK](https://www.nltk.org/)                                                 |
|                                                        | [spaCy](https://spacy.io/)                                                    |
|                                                        | [Gensim](https://radimrehurek.com/gensim/)                                    |
|                                                        | [TextBlob](https://textblob.readthedocs.io/)                                  |
|                                                        | [Transformers](https://huggingface.co/transformers/)                          |
|                             Aplicaciones de escritorio |                                                                               |
|                                                        | [PyQt](https://riverbankcomputing.com/software/pyqt/)                         |
|                                                        | [Tkinter](https://docs.python.org/3/library/tkinter.html)                     |
|                                                        | [wxPython](https://www.wxpython.org/)                                         |
|                                                        | [Kivy](https://kivy.org/)                                                     |
|                                 Aprendizaje automático |                                                                               |
|                                                        | [TensorFlow](https://www.tensorflow.org/)                                     |
|                                                        | [PyTorch](https://pytorch.org/)                                               |
|                                                        | [Keras](https://keras.io/)                                                    |
|                                                        | [scikit-learn](https://scikit-learn.org/)                                     |
|                                                        | [NLTK](https://www.nltk.org/)                                                 |
|                          Automatización de pruebas web |                                                                               |
|                                                        | [Selenium](https://www.selenium.dev/)                                         |
|                                                        | [Playwright](https://playwright.dev/python/)                                  |
|                                                        | [Splinter](https://splinter.readthedocs.io/)                                  |
|            Automatización de tareas de infraestructura |                                                                               |
|                                                        | [Ansible](https://docs.ansible.com/)                                          |
|                                                        | [Fabric](https://www.fabfile.org/)                                            |
|                                                        | [Paramiko](https://www.paramiko.org/)                                         |
|                                                        | [Boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)    |
|                    Automatización de tareas de sistema |                                                                               |
|                                                        | [Fabric](https://www.fabfile.org/)                                            |
|                                                        | [Invoke](https://www.pyinvoke.org/)                                           |
|                                                        | [PyAutoGUI](https://pyautogui.readthedocs.io/)                                |
|                                                        | [Selenium](https://www.selenium.dev/)                                         |
|                             Automatización y scripting |                                                                               |
|                                                        | [os](https://docs.python.org/3/library/os.html)                               |
|                                                        | [subprocess](https://docs.python.org/3/library/subprocess.html)               |
|                                                        | [shutil](https://docs.python.org/3/library/shutil.html)                       |
|                                                        | [pathlib](https://docs.python.org/3/library/pathlib.html)                     |
|                                                        | [argparse](https://docs.python.org/3/library/argparse.html)                   |
|                       Cálculos científicos y numéricos |                                                                               |
|                                                        | [NumPy](https://numpy.org/)                                                   |
|                                                        | [SciPy](https://www.scipy.org/)                                               |
|                                                        | [SymPy](https://www.sympy.org/)                                               |
|                                                        | [pandas](https://pandas.pydata.org/)                                          |
|                                       Ciencia de datos |                                                                               |
|                                                        | [NumPy](https://numpy.org/)                                                   |
|                                                        | [Pandas](https://pandas.pydata.org/)                                          |
|                                                        | [Matplotlib](https://matplotlib.org/)                                         |
|                                                        | [SciPy](https://www.scipy.org/)                                               |
|                                                        | [scikit-learn](https://scikit-learn.org/)                                     |
|             Creación de interfaces gráficas de usuario |                                                                               |
|                                                        | [PyQt](https://riverbankcomputing.com/software/pyqt/)                         |
|                                                        | [Tkinter](https://docs.python.org/3/library/tkinter.html)                     |
|                                                        | [wxPython](https://www.wxpython.org/)                                         |
|                                                        | [PySide](https://wiki.qt.io/PySide)                                           |
|       Desarrollo de aplicaciones de escritorio con GUI |                                                                               |
|                                                        | [PyQt](https://riverbankcomputing.com/software/pyqt/)                         |
|                                                        | [Tkinter](https://docs.python.org/3/library/tkinter.html)                     |
|                                                        | [wxPython](https://www.wxpython.org/)                                         |
|                                                        | [PySide](https://wiki.qt.io/PySide)                                           |
|                                                        | [Toga](https://toga.readthedocs.io/)                                          |
|                     Desarrollo de aplicaciones móviles |                                                                               |
|                                                        | [Kivy](https://kivy.org/)                                                     |
|                                                        | [PyQt](https://riverbankcomputing.com/software/pyqt/)                         |
|                                                        | [BeeWare](https://docs.beeware.org/)                                          |
|                                                        | [PySide](https://wiki.qt.io/PySide)                                           |
|                         Desarrollo de aplicaciones web |                                                                               |
|                                                        | [Django](https://www.djangoproject.com/)                                      |
|                                                        | [Flask](https://flask.palletsprojects.com/)                                   |
|                                                        | [Pyramid](https://trypyramid.com/)                                            |
|                                                        | [FastAPI](https://fastapi.tiangolo.com/)                                      |
|                                                        | [Requests](https://requests.readthedocs.io/)                                  |
|          Desarrollo de aplicaciones web con JavaScript |                                                                               |
|                                                        | [Flask](https://flask.palletsprojects.com/)                                   |
|                                                        | [Django](https://www.djangoproject.com/)                                      |
|                                                        | [Tornado](https://www.tornadoweb.org/)                                        |
|                                                        | [Bottle](https://bottlepy.org/)                                               |
|                                 Desarrollo de chatbots |                                                                               |
|                                                        | [NLTK](https://www.nltk.org/)                                                 |
|                                                        | [spaCy](https://spacy.io/)                                                    |
|                                                        | [Rasa](https://rasa.com/)                                                     |
|                                                        | [ChatterBot](https://chatterbot.readthedocs.io/)                              |
|                                   Desarrollo de juegos |                                                                               |
|                                                        | [Pygame](https://www.pygame.org/)                                             |
|                                                        | [Panda3D](https://www.panda3d.org/)                                           |
|                                                        | [Arcade](https://arcade.academy/)                                             |
|                                                        | [Pyglet](https://pyglet.readthedocs.io/)                                      |
|                   Integración con servicios en la nube |                                                                               |
|                                                        | [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)   |
|                                                        | [Google Cloud Client Library](https://cloud.google.com/python/docs/)          |
|                                                        | [Azure SDK for Python](https://docs.microsoft.com/python/api/overview/azure/) |
|                   Manipulación de datos en formato CSV |                                                                               |
|                                                        | [csv](https://docs.python.org/3/library/csv.html)                             |
|                                                        | [Pandas](https://pandas.pydata.org/)                                          |
|                                                        | [NumPy](https://numpy.org/)                                                   |
|                           Manipulación de archivos PDF |                                                                               |
|                                                        | [PyPDF2](https://pythonhosted.org/PyPDF2/)                                    |
|                                                        | [pdfminer](https://pypi.org/project/pdfminer/)                                |
|                                                        | [PyMuPDF](https://pymupdf.readthedocs.io/)                                    |
|                       Procesamiento de señales y audio |                                                                               |
|                                                        | [Librosa](https://librosa.org/)                                               |
|                                                        | [Soundfile](https://pysoundfile.readthedocs.io/)                              |
|                                                        | [PyDub](https://pydub.com/)                                                   |
|              Procesamiento de datos en grandes escalas |                                                                               |
|                                                        | [Dask](https://dask.org/)                                                     |
|                                                        | [Apache Spark](https://spark.apache.org/)                                     |
|                                                        | [Cython](https://cython.org/)                                                 |
|                                                        | [Numba](https://numba.pydata.org/)                                            |
|     Procesamiento de imágenes y visión por computadora |                                                                               |
|                                                        | [OpenCV](https://opencv.org/)                                                 |
|                                                        | [Pillow](https://python-pillow.org/)                                          |
|                                                        | [scikit-image](https://scikit-image.org/)                                     |
|    Procesamiento de lenguaje natural en idioma español |                                                                               |
|                                                        | [spaCy](https://spacy.io/)                                                    |
|                                                        | [Pattern](https://www.clips.uantwerpen.be/pattern)                            |
|                                                        | [Freeling](https://github.com/TALP-UPC/FreeLing)                              |
|                                    Pruebas de software |                                                                               |
|                                                        | [unittest](https://docs.python.org/3/library/unittest.html)                   |
|                                                        | [pytest](https://docs.pytest.org/)                                            |
|                                                        | [nose](https://nose.readthedocs.io/)                                          |
|                                                        | [Selenium](https://www.selenium.dev/)                                         |

</details>
<details>
<summary>Tabla de <strong>comparación con otros lenguajes de programación 🤔</strong></summary>

| Característica        | Python                                           | Java                                     | C++                                     | JavaScript                                |
| --------------------- | ------------------------------------------------ | ---------------------------------------- | --------------------------------------- | ----------------------------------------- |
| Paradigma             | Multiparadigma                                   | Orientado a objetos, estructurado        | Multiparadigma                          | Multiparadigma                            |
| Tipado                | Dinámico                                         | Estático                                 | Estático                                | Dinámico                                  |
| Sintaxis              | Concisa y legible                                | Verbosa                                  | Compleja                                | Flexible                                  |
| Uso principal         | Desarrollo web, ciencia de datos, automatización | Desarrollo de aplicaciones empresariales | Desarrollo de sistemas, videojuegos     | Desarrollo web, aplicaciones interactivas |
| Bibliotecas           | Amplia variedad                                  | Amplia variedad                          | Amplia variedad                         | Amplia variedad                           |
| Orientación a objetos | Sí                                               | Sí                                       | Sí                                      | Sí                                        |
| Rendimiento           | Moderado                                         | Alto                                     | Alto                                    | Moderado                                  |
| Comunidad y soporte   | Gran comunidad, abundante documentación          | Gran comunidad, abundante documentación  | Gran comunidad, abundante documentación | Gran comunidad, abundante documentación   |
| Curva de aprendizaje  | Baja                                             | Moderada                                 | Alta                                    | Baja                                      |

Esta tabla solo proporciona una comparación general entre los lenguajes y que cada uno tiene sus propias fortalezas y áreas de aplicación específicas.

</details>

---
<br>

# Licencia 📄

- [Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional](LICENSE) 

---

<br><br>

# Agradecimientos 🎁

Por supuesto, quiero agradecer a [Federico Garay](https://ar.linkedin.com/in/fedegaray), a [Nicolás Schürmann](https://www.linkedin.com/in/nicolasschurmann/) (¡Cuidao con el [teclado](https://youtu.be/y0T8UqBkawQ) que se gasta!) y a [Marcelo Vázquez](https://www.linkedin.com/in/s4vitar/) por los cursos en concreto que realice con ellos, fueron mi despegue. También mi más sincero agradecimiento a todos los contenidos libres de webs, canales de RRSS, repositorios de código, etc.

Y por último, a todos los compas que me han apoyado en este camino.

> [Solo no puedes, con amigos sí. 🤝](https://youtu.be/Ds7tje_Y0CM)


<br>

# Invítame a un café ☕️

<p>
<a href="https://www.buymeacoffee.com/manuelver"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="https://www.buymeacoffee.com/manuelver" /></a>
</p>

<br><br><br>
[Manu](https://vergaracarmona.es) 😊
