# APUNTES PYTHON Y CHATGPT

## Índice

## TEMA 1 - Introducción a ChatGPT y sus aplicaciones
### 1.1. - ¿Qué es ChatGPT?

ChatGPT es un modelo de lenguaje desarrollado por OpenAI, basado en la arquitectura GPT-3.5. GPT significa Generatice Pre-trained Tranformer (Transformador Generativo Pre-enternado). Es un sistema de procesamiento del lenguaje natural (NLP) capaz de generar respuestas coherentes y contextualmente relevantes a partir de las entradas de texto que recibe. Utiliza el aprendizaje automático y está entrenado en una amplia variedad de datos textuales para comprender y generar texto en lenguaje natural.

### 1.2. - ¿Cómo funciona?

El funcionamiento de ChatGPT se basa en un enfoque llamado "aprendizaje automático" o "aprendizaje profundo". El modelo GPT-3.5, en el que se basa ChatGPT, es una red neuronal profunda que ha sido entrenada en una enorme cantidad de datos textuales para aprender patrones y características del lenguaje humano.

Cuando se le proporciona una entrada de texto, como una pregunta o una declaración, ChatGPT descompone el texto en unidades más pequeñas, como palabras o tokens. Luego, analiza el contexto de las palabras y utiliza esa información para generar una respuesta relevante. El modelo se entrena para predecir la siguiente palabra o el siguiente token en una secuencia de texto, dada la secuencia anterior.

ChatGPT tiene una estructura en capas. Cada capa procesa y extrae información del texto de entrada de manera gradual y compleja. A medida que la información se mueve a través de las capas, se capturan representaciones cada vez más abstractas y significativas del texto.

Es importante tener en cuenta que ChatGPT se basa en la información con la que ha sido entrenado y no tiene conocimiento directo del mundo real fuera de los datos que se le han proporcionado durante su entrenamiento. Además, aunque ChatGPT puede generar respuestas coherentes y contextuales, también es posible que ocasionalmente genere respuestas incorrectas o no adecuadas, por lo que siempre se debe usar con cautela y verificar la información en caso de duda.

### 1.3. - Arquitectura

La arquitectura subyacente de ChatGPT se basa en la versión GPT-3.5 de OpenAI, que es una red neuronal de transformador. Un transformador es un tipo de arquitectura de aprendizaje profundo que ha demostrado excelentes resultados en tareas de procesamiento del lenguaje natural.

El transformador consta de múltiples capas de atención y alimentación hacia adelante. Cada capa tiene una estructura similar, que incluye una subcapa de atención multi-cabeza y una red de alimentación hacia adelante.

La subcapa de atención multi-cabeza se encarga de analizar la relación entre las diferentes palabras en la secuencia de entrada. Utiliza múltiples "cabezas de atención" para capturar diferentes aspectos de la dependencia entre palabras. Esto permite que el modelo entienda mejor las relaciones a largo plazo y el contexto en el texto.

La red de alimentación hacia adelante es una capa de redes neuronales completamente conectadas que procesa las representaciones de salida de la capa de atención. Ayuda a capturar relaciones no lineales en el texto y mejorar la calidad de las representaciones de las palabras.

En cuanto al funcionamiento, ChatGPT se entrena utilizando un proceso llamado "aprendizaje autodirigido". Durante el entrenamiento, se proporciona al modelo una gran cantidad de datos textuales de diferentes fuentes, como libros, artículos de noticias, páginas web, conversaciones y más. El modelo aprende a predecir la siguiente palabra en una secuencia de texto, dado el contexto anterior. El entrenamiento tiene dos fases:
- Pre-entrenamiento
- Ajuste fino 

[Paper ChatGPT](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 

![](img/python-chatgpt01.png)

### 1.4. - Casos de uso
- Chatbots y asistentes virtuales. Ejemplo https://my.replika.com/
- Generación de contenido. Ejemplo https://www.shortlyai.com/
- Resumen y parafraseo de textos. Ejemplo https://quillbot.com/
- Análisis de sentimiento. 
- Traducción automatica. DeepL utiliza IAs para sus resultados.

## TEMA 2 - Configuración y Autenticación con la API de OpenAI
### 2.1. - Pasos para autenticarse a ChatGPT


- Paso 1 – Registrarse en OpenAI https://platform.openai.com/ 
- Paso 2 – Obtener las credenciales API https://platform.openai.com/account/api-keys 
- Paso 3 – Almacenarlas de forma segura

Para guardar las contraseñas de manera segura nos bajamos la librería python-dotenv:
```shell
pip install python-dotenv
```

Para guardar la API creamos un fichero .env y ponemos una variable en mayúsculas con la API:
```python
OPENAI_API_KEY=sk-x5ejwlcnwvkcvME_ncjkwceLAcnoewejkINVENTOcnwjl
```

Luego, para llamar la api desde cualquier fichero python tenemos que llamar a la API mediante la librería python-dotenv. Ejemplo miPrograma.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
```

### 2.2. - Instalar y configurar las bibliotecas para OpenAI

- Paso 1 – Instalar la biblioteca de OpenAI
```pyhton
pip install openai
```

- Paso 2 – Importarla y configurar la API key
```python
import openai
```

Ahora vamos a configurar la biblioteca openai con la API

Debajo del código ponemos:
```python
openai.api_key = api_key
```

- Paso 3 – Verificar la conexión

Nos aseguramos de que está configurada la api llamando a los módelos a la biblioteca:
```python
modelos = openai.Model.list()
```

Nos devolverá todos los modelos disponibles. Para verlo en consola imprimimos la variable:
```python
print(modelos)
```

Ejecutando el programa podemos ver todos los modelos, para aislar los nombres se puede usar el comando jq:
```shell
python3 code/miPrograma.py | jq '.data[].id'
```

![](https://vergaracarmona.es/wp-content/uploads/2022/11/json_everywhere-1024x696.jpg)

## TEMA 3 - Interactuar con ChatGPT usando Python



## TEMA 4 - Aplicaciones Prácticas de Python + ChatGPT



## TEMA 5 - Otras consideraciones para la integración


