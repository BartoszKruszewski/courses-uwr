import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["mydatabase"]
collection = database["mycollection"]

# Insert a document into the collection
document_to_insert = {"name": "John Doe", "age": 30, "city": "New York"}
inserted_document = collection.insert_one(document_to_insert)
print(f"Document inserted with ID: {inserted_document.inserted_id}")

# Query the collection
query_result = collection.find({"city": "New York"})

print("Documents matching the query:")
for document in query_result:
    print(document)
