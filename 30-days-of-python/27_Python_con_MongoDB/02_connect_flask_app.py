"""
Conectar la aplicación flask a la base de datos MongoDB
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

print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
