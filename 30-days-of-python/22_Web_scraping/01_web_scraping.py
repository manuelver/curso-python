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

for item in soup.find_all('div', {'class': 'facts-wrapper'}):

    section_name = item.find('h5').get_text().strip()
    section_data = {}

    for li in item.find_all('li'):
        key = li.find('p', {'class': 'text'}).get_text().strip()
        value = li.find('span', {'class': 'value'}).get_text().strip()
        section_data[key] = value

    data[section_name] = section_data

with open('bu_stats.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Datos guardados en bu_stats.json")
