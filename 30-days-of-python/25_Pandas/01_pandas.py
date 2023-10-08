"""
01_pandas.py
"""

import pandas as pd

# 1. Lee el archivo hacker_news.csv del directorio de datos.
df = pd.read_csv('hacker_news.csv')

# 2. Obtén las primeras cinco filas.
print(df.head())
print()

# 3. Obtén las últimas cinco filas.
print(df.tail())
print()

# 4. Obtén la columna de títulos como una serie de pandas.
titles = df['title']
print(titles)
print()

# 5. Cuenta el número de filas y columnas.
print('Número de filas:', len(df))
print('Número de columnas:', len(df.columns))
print()

# Filtra los títulos que contengan "python".
python_titles = df[df['title'].str.contains('python', case=False)]
print(python_titles)
print()

# Filtra los títulos que contengan "JavaScript".
js_titles = df[df['title'].str.contains('JavaScript', case=False)]
print(js_titles)
print()

# Explora los datos y dales sentido.
# Puedes utilizar métodos como describe(), info(), value_counts(), etc. para explorar los datos y obtener estadísticas descriptivas.
print(df.describe())
print(df.info())
print(df['title'].value_counts())
print()
