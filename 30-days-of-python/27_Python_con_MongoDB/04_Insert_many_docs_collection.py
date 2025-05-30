"""
Insertar varios documentos en una colección
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()
# variables .env
mongopass = os.getenv('mongopass')
mongouser = os.getenv('mongouser')
mongoname = os.getenv('mongoname')

uri = "mongodb+srv://" + \
    mongouser + ":" + \
    mongopass + "@" + \
    mongoname + ".m697hfm.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.pruebas_mongodb

students = [
    {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
    {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
    {'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25},
]

for student in students:
    db.students.insert_one(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
