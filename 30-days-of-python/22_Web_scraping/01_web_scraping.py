"""
01_web_scraping.py
"""
import requests
from bs4 import BeautifulSoup
import json


# 1. Realiza un raspado web del siguiente sitio web
# y guarda los datos en un archivo JSON
# (URL = 'http://www.bu.edu/president/boston-university-facts-stats/').


url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = {}
current_section = None

for section in soup.find_all('section', {'class': 'facts-categories'}):

    section_data = {}

    for item in section.find_all('div', {'class': 'facts-wrapper'}):
        section_name = section.find('h5').get_text().strip()
        for li in item.find_all('li'):
            key = li.find('p', {'class': 'text'}).get_text().strip()
            value = li.find('span', {'class': 'value'}).get_text().strip()
            section_data[key] = value

        data[section_name] = section_data

with open('bu_stats.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Datos guardados en bu_stats.json")

# 2. Extrae la tabla de esta URL
# (https://archive.ics.uci.edu/ml/datasets.php)
# y conviértela en un archivo JSON.

url = 'https://webcache.googleusercontent.com/search?q=cache:tT4BY9X5RxAJ:https://archive.ics.uci.edu/datasets&cd=8&hl=ca&ct=clnk&gl=es'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

datasets = []

for div in soup.find_all('div', class_='rounded-box'):
    dataset = {
        'name': div.find('h2').find('a').text.strip(),
        'description': div.find('p').text.strip(),
    }

    metadata_divs = div.find_all('div', class_='col-span-3')
    for metadata_div in metadata_divs:
        icon = metadata_div.find('div').find('svg')['viewBox']
        value = metadata_div.find('span').text.strip()
        dataset[icon] = value

    datasets.append(dataset)

with open('uci_datasets.json', 'w') as f:
    json.dump(datasets, f, indent=2)

print("Datos guardados en uci_datasets.json")


# 3. Realiza un raspado web de la tabla de presidentes
# y guarda los datos como JSON
# (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# La tabla no está muy estructurada
# y el proceso de raspado puede llevar mucho tiempo.


url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
headers = [header.get_text().strip() for header in table.find_all('th')]
rows = []

for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == len(headers):
        rows.append([cell.get_text().strip() for cell in cells])

data = []
for row in rows:
    president = {}
    for i, header in enumerate(headers):
        if i < len(row):  # Verificar si hay celdas suficientes en la fila
            if header == 'President':
                president['name'] = row[i]
            elif header == 'Party':
                president['party'] = row[i]
            elif header == 'State[a]':
                president['state'] = row[i]
            elif header == 'Took office':
                president['took_office'] = row[i]
            elif header == 'Left office':
                president['left_office'] = row[i]
    data.append(president)

with open('us_presidents.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Datos guardados en us_presidents.json")
