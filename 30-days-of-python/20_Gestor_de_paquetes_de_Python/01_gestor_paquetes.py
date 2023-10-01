"""
01_gestor_paquetes.py
"""
import requests
from collections import Counter
import statistics
import pandas as pd
from bs4 import BeautifulSoup

# 1. Lee esta URL y encuentra las 10 palabras más frecuentes.
# Romeo y Julieta: 'http://www.gutenberg.org/files/1112/1112.txt'

url_romeo_julieta = 'http://www.gutenberg.org/files/1112/1112.txt'
response_romeo_julieta = requests.get(url_romeo_julieta)
words = response_romeo_julieta.text.split()
word_counts = Counter(words)
top_10_words = word_counts.most_common(10)

print("10 palabras más frecuentes:")
for word, count in top_10_words:
    print(word, "-", count)

print()

# 2. Lee la API de gatos y la URL:
# 'https://api.thecatapi.com/v1/breeds'
# y encuentra:

url_gatos = 'https://api.thecatapi.com/v1/breeds'
response_gatos = requests.get(url_gatos)
data_gatos = response_gatos.json()

# - El mínimo, máximo, promedio,
# mediana y desviación estándar
# del peso de los gatos en unidades métricas.

weights = [cat['weight']['metric'] for cat in data_gatos]
weights = [float(w.split()[0]) for w in weights]
min_weight = min(weights)
max_weight = max(weights)
avg_weight = statistics.mean(weights)
med_weight = statistics.median(weights)
std_weight = statistics.stdev(weights)

print("Peso de los gatos en unidades métricas:")
print("Mínimo:", min_weight)
print("Máximo:", max_weight)
print("Promedio:", avg_weight)
print("Mediana:", med_weight)
print("Desviación estándar:", std_weight)
print()

# - El mínimo, máximo, promedio,
# mediana y desviación estándar
# de la esperanza de vida
# de los gatos en años.

lifespans = [cat['life_span'] for cat in data_gatos]
lifespans = [int(l.split()[0]) for l in lifespans if l != '']
min_lifespan = min(lifespans)
max_lifespan = max(lifespans)
avg_lifespan = statistics.mean(lifespans)
med_lifespan = statistics.median(lifespans)
std_lifespan = statistics.stdev(lifespans)

print("Esperanza de vida de los gatos en años:")
print("Mínimo:", min_lifespan)
print("Máximo:", max_lifespan)
print("Promedio:", avg_lifespan)
print("Mediana:", med_lifespan)
print("Desviación estándar:", std_lifespan)
print()

# - Crea una tabla de frecuencias
# de países y razas de gatos.

country_counts = Counter([cat['origin']
                         for cat in data_gatos if cat['origin'] != ''])
breed_counts = Counter([cat['name'] for cat in data_gatos])

print("Tabla de frecuencias de países:")
print(pd.DataFrame.from_dict(country_counts, orient='index'))
print()

print("Tabla de frecuencias de razas:")
print(pd.DataFrame.from_dict(breed_counts, orient='index'))
print()

# 3. Lee la [API de países](https://restcountries.eu/rest/v2/all)
# y encuentra:

# El enlace está caído, uso otra versión
url_countries = 'https://restcountries.com/v3.1/all'
response_countries = requests.get(url_countries)
data_countries = response_countries.json()

# - Los 10 países más grandes.

df = pd.DataFrame(data_countries)
df['area'] = pd.to_numeric(df['area'])
largest_countries = df.nlargest(10, 'area')

print("Los 10 países más grandes:")
for country in largest_countries['name']:
    print(country['common'])
print()

# - Los 10 idiomas más hablados.

most_spoken_languages = df.explode('languages').groupby(
    'languages').size().nlargest(10)

print("Los 10 idiomas más hablados:")
print(most_spoken_languages)
print()

# - El número total de idiomas en la API de países.

total_languages = len(df.explode('languages')['languages'].unique())

print("Número total de idiomas en la API de países:", total_languages)
print()


# 4. La Universidad de California en Irvine (UCI)
# es uno de los lugares más comunes para obtener
# conjuntos de datos para ciencia de datos
# y aprendizaje automático.
# Lee el contenido de UCI
# (https://archive.ics.uci.edu/ml/datasets.php).
# Sin bibliotecas adicionales, puede ser difícil,
# por lo que puedes intentarlo con BeautifulSoup4.

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = [a['href'] for a in soup.find_all('a') if a.has_attr('href')]
