from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['library']

res1 = db.books.find().sort({ "title": 1 }).skip(1).limit(2)
res2 = db.readers.find({ "borrowings.copy_id": "A102" })

#[print(res) for res in list(res1)]
[print(res) for res in list(res2)]