from pymongo import MongoClient
from zad2_data import readers_data, books_data

client = MongoClient("mongodb://localhost:27017/")
db = client['library']

db.books.insert_many(books_data)
db.readers.insert_many(readers_data)

client.close()

