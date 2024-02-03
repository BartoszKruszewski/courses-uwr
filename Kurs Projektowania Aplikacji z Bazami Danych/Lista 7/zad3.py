from pymongo import MongoClient
from zad3_data import readers_validator, books_validator

client = MongoClient("mongodb://localhost:27017/")
db = client['library']

db.drop_collection('books')
db.drop_collection('readers')

db.create_collection('books', validator = books_validator)
db.create_collection('readers', validator = readers_validator)

client.close()

