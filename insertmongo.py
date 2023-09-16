import requests
from pymongo import MongoClient
import certifi
import pymongo
import ssl
import spacy

# MongoDB Setup
connection = 'mongodb+srv://jyee25:jyee@vthacks.lza3x1j.mongodb.net/'
client = MongoClient(connection, tlsCAFile=certifi.where())
db = client['users']
collection = db['login']

data = {"user" : "pm",
        "pass" : "pm"}

collection.insert_one(data)

client.close()
