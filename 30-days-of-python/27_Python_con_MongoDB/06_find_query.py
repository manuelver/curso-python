"""
Buscar en la base de datos con query
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

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

query = {
    "country": "Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


print("-"*30)

query = {
    "city": "Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


print("-"*30)

query = {
    "country": "Finland",
    "city": "Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


print("-"*30)

query = {"age": {"$gt": 30}}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
