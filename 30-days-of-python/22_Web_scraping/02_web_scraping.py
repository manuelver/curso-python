"""
01_web_scraping.py
"""
import requests
from bs4 import BeautifulSoup
import json

# 2. Extrae la tabla de esta URL
# (https://archive.ics.uci.edu/ml/datasets.php)
# y conviértela en un archivo JSON.

url = 'https://archive.ics.uci.edu/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = {}

for section in soup.find_all('section', class_='rounded-box'):

    section_name = section.h1.get_text().strip()
    section_data = {}

    for div in section.find_all('div', class_='rounded-box'):
        key = div.find('a', {'class': 'link-hover'}).get_text().strip()
        value = div.find('p', {'class': 'truncate'}).get_text().strip()
        section_data[key] = value

    data[section_name] = section_data


with open('uci_datasets.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Datos guardados en uci_datasets.json")
