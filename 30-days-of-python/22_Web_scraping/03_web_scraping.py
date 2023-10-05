import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra la tabla por su clase
table = soup.find('table', {'class': 'wikitable'})

# Encuentra todas las filas en la tabla
rows = table.find_all('tr')

# Extrae los encabezados de la primera fila
headers = [header.get_text().strip()
           for header in rows[0].find_all(['th', 'td'])]

# Inicializa una lista para almacenar los datos
data = []

# Itera a través de las filas a partir de la segunda (índice 1)
for row in rows[1:]:
    # Encuentra todas las celdas en la fila
    cells = row.find_all(['th', 'td'])

    # Verifica que haya celdas suficientes en la fila
    if cells and len(cells) >= len(headers):
        president = {}
        for i, header in enumerate(headers):
            # Asigna el valor de la celda al encabezado correspondiente
            cell_data = cells[i].find(string=True) if cells[i].find(
                string=True) else cells[i].find('a')['title'].strip()
            president[header.lower()] = cell_data
        data.append(president)

# Guarda los datos como JSON
with open('us_presidents.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Datos guardados en us_presidents.json")
