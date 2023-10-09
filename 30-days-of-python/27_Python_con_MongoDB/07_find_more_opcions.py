"""
Buscar en la base de datos - más opciones
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

db.students.find().limit(3)

print("-"*30)

students = db.students.find().sort('name')
for student in students:
    print(student)

print("-"*30)

students = db.students.find().sort('name', -1)
for student in students:
    print(student)

print("-"*30)

students = db.students.find().sort('age')
for student in students:
    print(student)

print("-"*30)

students = db.students.find().sort('age', -1)
for student in students:
    print(student)

print("-"*30)

# New value

query = {'age': 40}
new_value = {'$set': {'age': 38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
