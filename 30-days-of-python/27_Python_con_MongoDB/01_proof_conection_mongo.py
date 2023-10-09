"""
Conection
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Se envió un ping a su deploy. ¡Se ha conectado correctamente a MongoDB!")
except Exception as e:
    print(e)
